import hashlib
import importlib.util
import json
from pathlib import Path

import pytest


SCRIPT = (
    Path(__file__).parents[1] / "scripts" / "download_human_interface_guidelines.py"
)
SPEC = importlib.util.spec_from_file_location("download_hig", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_collect_hig_paths_uses_the_complete_navigation_tree():
    index = {
        "interfaceLanguages": {
            "swift": [
                {
                    "path": "/design/human-interface-guidelines",
                    "children": [
                        {
                            "path": "/design/human-interface-guidelines/accessibility",
                            "children": [
                                {
                                    "path": "/design/human-interface-guidelines/color",
                                }
                            ],
                        },
                        {"path": "/documentation/not-hig"},
                        {
                            "path": "/design/human-interface-guidelines/accessibility#vision"
                        },
                    ],
                }
            ]
        }
    }

    assert MODULE.collect_hig_paths(index) == [
        "/design/human-interface-guidelines",
        "/design/human-interface-guidelines/accessibility",
        "/design/human-interface-guidelines/color",
    ]


def test_collect_asset_urls_only_archives_resource_references():
    page = {
        "references": {
            "hero.png": {
                "type": "image",
                "variants": [
                    {"url": "https://docs-assets.example/hero.png"},
                    {"url": "https://docs-assets.example/hero-dark.png"},
                ],
            },
            "demo.mp4": {
                "type": "video",
                "variants": [{"url": "https://media.example/demo.mp4"}],
            },
            "article": {
                "type": "topic",
                "url": "https://example.com/an-external-article",
                "images": ["hero.png"],
            },
        },
        "legalNotices": {"termsOfUse": "https://example.com/terms"},
    }

    assert MODULE.collect_asset_urls(page) == [
        "https://docs-assets.example/hero-dark.png",
        "https://docs-assets.example/hero.png",
        "https://media.example/demo.mp4",
    ]


def test_local_path_for_url_is_stable_and_query_safe():
    plain = MODULE.local_path_for_url(
        "https://assets.example/published/icon%402x.png", Path("assets")
    )
    queried = MODULE.local_path_for_url(
        "https://assets.example/download/file.pdf?platform=ios", Path("assets")
    )

    assert plain == Path("assets/assets.example/published/icon%402x.png")
    assert queried.parent == Path("assets/assets.example/download")
    assert queried.name.startswith("file--")
    assert queried.suffix == ".pdf"


@pytest.mark.parametrize(
    "path, expected",
    [
        (
            "/design/human-interface-guidelines",
            Path("data/design/human-interface-guidelines.json"),
        ),
        (
            "/design/human-interface-guidelines/accessibility",
            Path("data/design/human-interface-guidelines/accessibility.json"),
        ),
    ],
)
def test_page_data_path_mirrors_apple_endpoint(path, expected):
    assert MODULE.page_data_path(path) == expected


def test_verify_manifest_detects_corruption(tmp_path):
    artifact = tmp_path / "data/page.json"
    artifact.parent.mkdir(parents=True)
    artifact.write_bytes(b"complete")
    manifest = {
        "artifacts": [
            {
                "path": "data/page.json",
                "size": 8,
                "sha256": hashlib.sha256(b"complete").hexdigest(),
            }
        ]
    }
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps(manifest))

    assert MODULE.verify_archive(tmp_path) == []

    artifact.write_bytes(b"broken")
    errors = MODULE.verify_archive(tmp_path)
    assert any("data/page.json" in error and "size" in error for error in errors)
