#!/usr/bin/env python3
"""Create Telegraph accounts and publish Telegraph pages with the standard library."""

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_ROOT = "https://api.telegra.ph"
ALLOWED_TAGS = {
    "a",
    "aside",
    "b",
    "blockquote",
    "br",
    "code",
    "em",
    "figcaption",
    "figure",
    "h3",
    "h4",
    "hr",
    "i",
    "iframe",
    "img",
    "li",
    "ol",
    "p",
    "pre",
    "s",
    "strong",
    "u",
    "ul",
    "video",
}
ALLOWED_ATTRIBUTES = {"href", "src"}
MAX_CONTENT_BYTES = 64 * 1024


def validate_content(content):
    if not isinstance(content, list):
        raise ValueError("Content must be a JSON array of Telegraph nodes")

    def validate_node(node):
        if isinstance(node, str):
            return
        if not isinstance(node, dict):
            raise ValueError("Each node must be a string or object")
        tag = node.get("tag")
        if tag not in ALLOWED_TAGS:
            raise ValueError(f"Unsupported tag: {tag}")
        for attribute in node.get("attrs", {}):
            if attribute not in ALLOWED_ATTRIBUTES:
                raise ValueError(f"Unsupported attribute: {attribute}")
        children = node.get("children", [])
        if not isinstance(children, list):
            raise ValueError("Node children must be an array")
        for child in children:
            validate_node(child)

    for item in content:
        validate_node(item)
    encoded = json.dumps(content, ensure_ascii=False, separators=(",", ":"))
    if len(encoded.encode("utf-8")) > MAX_CONTENT_BYTES:
        raise ValueError("Content exceeds Telegraph's 64 KB limit")
    return encoded


def _post(method, fields):
    request = Request(
        f"{API_ROOT}/{method}",
        data=urlencode(fields).encode("utf-8"),
        headers={"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"},
        method="POST",
    )
    with urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if not payload.get("ok"):
        raise RuntimeError(
            f"Telegraph API error: {payload.get('error', 'UNKNOWN_ERROR')}"
        )
    return payload["result"]


def create_account(short_name, author_name=None, author_url=None):
    if not 1 <= len(short_name) <= 32:
        raise ValueError("short_name must contain 1 to 32 characters")
    fields = {"short_name": short_name}
    if author_name is not None:
        fields["author_name"] = author_name
    if author_url is not None:
        fields["author_url"] = author_url
    return _post("createAccount", fields)


def create_account_with_token_file(
    short_name, token_file, author_name=None, author_url=None
):
    token_file = Path(token_file)
    fd = os.open(token_file, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    keep_file = False
    try:
        account = create_account(short_name, author_name, author_url)
        if not isinstance(account, dict):
            raise RuntimeError("Telegraph API returned an invalid account")
        access_token = account.get("access_token")
        if not isinstance(access_token, str) or not access_token:
            raise RuntimeError("Telegraph API response did not include an access token")

        with os.fdopen(fd, "w", encoding="utf-8") as secret_file:
            fd = None
            secret_file.write(access_token)
        keep_file = True
    finally:
        if fd is not None:
            os.close(fd)
        if not keep_file:
            token_file.unlink(missing_ok=True)

    public_account = {
        key: account[key]
        for key in ("short_name", "author_name", "author_url")
        if key in account
    }
    public_account["token_file"] = str(token_file)
    return public_account


def create_page(access_token, title, content, author_name=None, author_url=None):
    if not 1 <= len(title) <= 256:
        raise ValueError("title must contain 1 to 256 characters")
    fields = {
        "access_token": access_token,
        "title": title,
        "content": validate_content(content),
        "return_content": "false",
    }
    if author_name is not None:
        fields["author_name"] = author_name
    if author_url is not None:
        fields["author_url"] = author_url
    return _post("createPage", fields)


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    account = commands.add_parser("create-account", help="Create a Telegraph account")
    account.add_argument("--short-name", required=True)
    account.add_argument("--author-name")
    account.add_argument("--author-url")
    account.add_argument(
        "--token-file",
        required=True,
        type=Path,
        help="New owner-readable file in which to store the access token",
    )

    page = commands.add_parser("create-page", help="Publish a Telegraph page")
    page.add_argument("content", type=Path, help="JSON file containing Telegraph nodes")
    page.add_argument("--title", required=True)
    page.add_argument("--author-name")
    page.add_argument("--author-url")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.command == "create-account":
        result = create_account_with_token_file(
            args.short_name, args.token_file, args.author_name, args.author_url
        )
    else:
        token = os.environ.get("TELEGRAPH_ACCESS_TOKEN")
        if not token:
            raise SystemExit("TELEGRAPH_ACCESS_TOKEN is required for create-page")
        with args.content.open(encoding="utf-8") as content_file:
            content = json.load(content_file)
        result = create_page(
            token, args.title, content, args.author_name, args.author_url
        )
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
