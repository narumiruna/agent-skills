import json
import os
from unittest.mock import patch

import pytest

import telegraph


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self):
        return json.dumps(self.payload).encode()


def test_create_page_posts_validated_content_and_returns_page():
    content = [{"tag": "p", "children": ["Hello"]}]
    response = FakeResponse(
        {"ok": True, "result": {"url": "https://telegra.ph/Hello-01-01"}}
    )

    with patch("telegraph.urlopen", return_value=response) as urlopen:
        page = telegraph.create_page("token", "Hello", content, "Author", None)

    request = urlopen.call_args.args[0]
    form = request.data.decode()
    assert page["url"] == "https://telegra.ph/Hello-01-01"
    assert "access_token=token" in form
    assert "title=Hello" in form
    assert "content=%5B" in form


def test_rejects_unsupported_tags_before_request():
    with patch("telegraph.urlopen") as urlopen:
        with pytest.raises(ValueError, match="Unsupported tag: script"):
            telegraph.create_page(
                "token", "Unsafe", [{"tag": "script", "children": ["x"]}]
            )

    urlopen.assert_not_called()


def test_rejects_unsupported_attributes():
    content = [{"tag": "a", "attrs": {"onclick": "x"}, "children": ["link"]}]

    with pytest.raises(ValueError, match="Unsupported attribute: onclick"):
        telegraph.validate_content(content)


def test_api_error_is_reported_without_exposing_token():
    response = FakeResponse({"ok": False, "error": "ACCESS_TOKEN_INVALID"})

    with patch("telegraph.urlopen", return_value=response):
        with pytest.raises(RuntimeError, match="ACCESS_TOKEN_INVALID") as raised:
            telegraph.create_page("secret-token", "Hello", ["text"])

    assert "secret-token" not in str(raised.value)


def test_create_account_stores_token_without_printing_secrets(tmp_path, capsys):
    token_file = tmp_path / "telegraph-token"
    account = {
        "short_name": "Writer",
        "author_name": "Author",
        "access_token": "secret-token",
        "auth_url": "https://edit.telegra.ph/auth/secret",
    }

    with patch("telegraph.create_account", return_value=account):
        telegraph.main(
            [
                "create-account",
                "--short-name",
                "Writer",
                "--token-file",
                str(token_file),
            ]
        )

    output_text = capsys.readouterr().out
    output = json.loads(output_text)
    assert token_file.read_text() == "secret-token"
    assert token_file.stat().st_mode & 0o777 == 0o600
    assert output == {
        "short_name": "Writer",
        "author_name": "Author",
        "token_file": str(token_file),
    }
    assert "secret-token" not in output_text
    assert account["auth_url"] not in output_text


def test_create_account_refuses_existing_token_file_before_request(tmp_path):
    token_file = tmp_path / "telegraph-token"
    token_file.write_text("existing-token")

    with patch("telegraph.create_account") as create_account:
        with pytest.raises(FileExistsError):
            telegraph.main(
                [
                    "create-account",
                    "--short-name",
                    "Writer",
                    "--token-file",
                    str(token_file),
                ]
            )

    create_account.assert_not_called()
    assert token_file.read_text() == "existing-token"


def test_create_account_failure_removes_reserved_token_file(tmp_path):
    token_file = tmp_path / "telegraph-token"

    with patch("telegraph.create_account", side_effect=RuntimeError("API unavailable")):
        with pytest.raises(RuntimeError, match="API unavailable"):
            telegraph.main(
                [
                    "create-account",
                    "--short-name",
                    "Writer",
                    "--token-file",
                    str(token_file),
                ]
            )

    assert not token_file.exists()


def test_cli_requires_token_from_environment():
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(SystemExit, match="TELEGRAPH_ACCESS_TOKEN"):
            telegraph.main(["create-page", "--title", "Hello", "content.json"])
