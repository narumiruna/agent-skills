import json
import os
import sys
from unittest.mock import patch
from urllib.parse import parse_qs

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
        if isinstance(self.payload, bytes):
            return self.payload
        return json.dumps(self.payload).encode()


def test_create_page_posts_validated_content_and_returns_page():
    content = [{"tag": "p", "children": ["Hello"]}]
    response = FakeResponse(
        {"ok": True, "result": {"url": "https://telegra.ph/Hello-01-01"}}
    )

    with patch("telegraph.urlopen", return_value=response) as urlopen:
        page = telegraph.create_page("token", "Hello", content, "Author", "")

    request = urlopen.call_args.args[0]
    form = request.data.decode()
    assert page["url"] == "https://telegra.ph/Hello-01-01"
    assert "access_token=token" in form
    assert "title=Hello" in form
    assert "content=%5B" in form


def test_create_page_cli_can_clear_account_author_defaults(tmp_path):
    content_file = tmp_path / "content.json"
    content_file.write_text('["Text"]')
    response = FakeResponse(
        {"ok": True, "result": {"url": "https://telegra.ph/Anonymous-01-01"}}
    )

    with (
        patch.dict(os.environ, {"TELEGRAPH_ACCESS_TOKEN": "token"}, clear=True),
        patch("telegraph.urlopen", return_value=response) as urlopen,
    ):
        telegraph.main(
            [
                "create-page",
                "--title",
                "Anonymous",
                "--author-name",
                "",
                "--author-url",
                "",
                str(content_file),
            ]
        )

    request = urlopen.call_args.args[0]
    form = parse_qs(request.data.decode(), keep_blank_values=True)
    assert form["author_name"] == [""]
    assert form["author_url"] == [""]


def test_create_page_cli_requires_explicit_byline_fields():
    with pytest.raises(SystemExit):
        telegraph.build_parser().parse_args(
            ["create-page", "--title", "Hello", "content.json"]
        )


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


@pytest.mark.parametrize(
    ("node", "message"),
    [
        ({"tag": [], "children": []}, "Node tag must be a string"),
        ({"tag": "a", "attrs": None}, "Node attrs must be an object"),
        ({"tag": "a", "attrs": ["href"]}, "Node attrs must be an object"),
        (
            {"tag": "a", "attrs": {"href": None}},
            "Attribute values must be strings",
        ),
        (
            {"tag": "p", "childen": ["lost text"]},
            "Unsupported node field: childen",
        ),
    ],
)
def test_rejects_malformed_node_shapes(node, message):
    with pytest.raises(ValueError, match=message):
        telegraph.validate_content([node])


def test_rejects_content_with_excessive_nesting():
    node = "text"
    for _ in range(sys.getrecursionlimit() + 10):
        node = {"tag": "p", "children": [node]}

    with pytest.raises(ValueError, match="nesting is too deep"):
        telegraph.validate_content([node])


def test_rejects_invalid_scalar_fields_before_request():
    with patch("telegraph.urlopen") as urlopen:
        with pytest.raises(ValueError, match="author_name.*128"):
            telegraph.create_account("Writer", author_name="a" * 129)
        with pytest.raises(ValueError, match="author_url.*512"):
            telegraph.create_page(
                "token", "Hello", ["text"], author_url="https://" + "a" * 505
            )
        with pytest.raises(ValueError, match="access_token.*non-empty"):
            telegraph.create_page("", "Hello", ["text"])

    urlopen.assert_not_called()


def test_api_error_is_reported_without_exposing_token():
    response = FakeResponse(
        {"ok": False, "error": "ACCESS_TOKEN_INVALID: secret-token"}
    )

    with patch("telegraph.urlopen", return_value=response):
        with pytest.raises(RuntimeError, match="ACCESS_TOKEN_INVALID") as raised:
            telegraph.create_page("secret-token", "Hello", ["text"])

    assert "secret-token" not in str(raised.value)


@pytest.mark.parametrize(
    ("response", "message"),
    [
        (FakeResponse([]), "invalid response"),
        (FakeResponse(b"not JSON"), "invalid JSON"),
    ],
)
def test_malformed_api_response_is_reported_cleanly(response, message):
    with patch("telegraph.urlopen", return_value=response):
        with pytest.raises(RuntimeError, match=message):
            telegraph.create_page("token", "Hello", ["text"])


def test_create_page_rejects_malformed_result():
    response = FakeResponse({"ok": True, "result": []})

    with patch("telegraph.urlopen", return_value=response):
        with pytest.raises(RuntimeError, match="invalid page"):
            telegraph.create_page("token", "Hello", ["text"])


@pytest.mark.parametrize(
    "url",
    [
        "",
        "http://telegra.ph/Hello-01-01",
        "https://example.com/Hello-01-01",
        "https://telegra.ph/",
    ],
)
def test_create_page_rejects_invalid_public_url(url):
    response = FakeResponse({"ok": True, "result": {"url": url}})

    with patch("telegraph.urlopen", return_value=response):
        with pytest.raises(RuntimeError, match="invalid page"):
            telegraph.create_page("token", "Hello", ["text"])


def test_create_page_redacts_reflected_token_from_success_response():
    response = FakeResponse(
        {
            "ok": True,
            "result": {
                "url": "https://telegra.ph/Hello-01-01",
                "description": "unexpected secret-token reflection",
            },
        }
    )

    with patch("telegraph.urlopen", return_value=response):
        page = telegraph.create_page("secret-token", "Hello", ["text"])

    assert "secret-token" not in json.dumps(page)
    assert "[REDACTED]" in page["description"]


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


def test_cli_rejects_deeply_nested_json_before_request(tmp_path):
    depth = sys.getrecursionlimit() + 10
    content_file = tmp_path / "content.json"
    content_file.write_text(
        "[" + '{"tag":"p","children":[' * depth + '"text"' + "]}" * depth + "]"
    )

    with (
        patch.dict(os.environ, {"TELEGRAPH_ACCESS_TOKEN": "token"}, clear=True),
        patch("telegraph.urlopen") as urlopen,
        pytest.raises(ValueError, match="nesting is too deep"),
    ):
        telegraph.main(
            [
                "create-page",
                "--title",
                "Hello",
                "--author-name",
                "",
                "--author-url",
                "",
                str(content_file),
            ]
        )

    urlopen.assert_not_called()


def test_cli_requires_token_from_environment():
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(SystemExit, match="TELEGRAPH_ACCESS_TOKEN"):
            telegraph.main(
                [
                    "create-page",
                    "--title",
                    "Hello",
                    "--author-name",
                    "",
                    "--author-url",
                    "",
                    "content.json",
                ]
            )
