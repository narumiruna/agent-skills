from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).with_name("google_genai_grounding.py")


def load_script():
    spec = importlib.util.spec_from_file_location("google_genai_grounding", SCRIPT)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FakeInteraction:
    output_text = "Grounded answer."

    def model_dump(self, **_kwargs):
        return {
            "id": "interaction-123",
            "steps": [
                {
                    "type": "google_search_call",
                    "queries": ["grounded test query"],
                    "signature": "opaque-and-large",
                },
                {
                    "type": "google_search_result",
                    "is_error": False,
                    "result": [{"search_suggestions": "large HTML payload"}],
                },
                {
                    "type": "thought",
                    "content": "not evidence",
                },
                {
                    "type": "model_output",
                    "content": [
                        {
                            "type": "text",
                            "text": "Grounded answer.",
                            "annotations": [
                                {
                                    "type": "url_citation",
                                    "title": "Primary source",
                                    "url": "https://example.com/source",
                                    "start_index": 0,
                                    "end_index": 16,
                                }
                            ],
                        }
                    ],
                },
            ],
            "usage": {"total_tokens": 42},
        }


def test_search_request_uses_required_default_model_and_is_stateless():
    grounding = load_script()

    request = grounding.build_interaction_request(
        mode="search",
        prompt="What changed today?",
    )

    assert grounding.DEFAULT_MODEL == "gemini-3.5-flash"
    assert request == {
        "model": "gemini-3.5-flash",
        "input": "What changed today?",
        "tools": [{"type": "google_search"}],
        "store": False,
    }


def test_maps_request_includes_location_only_when_both_coordinates_are_valid():
    grounding = load_script()

    request = grounding.build_interaction_request(
        mode="maps",
        prompt="Find a nearby coffee shop.",
        latitude=25.033,
        longitude=121.5654,
    )

    assert request["tools"] == [
        {
            "type": "google_maps",
            "latitude": 25.033,
            "longitude": 121.5654,
        }
    ]

    with pytest.raises(ValueError, match="together"):
        grounding.build_interaction_request(
            mode="maps",
            prompt="Find a nearby coffee shop.",
            latitude=25.033,
        )
    with pytest.raises(ValueError, match="latitude"):
        grounding.build_interaction_request(
            mode="maps",
            prompt="Find a nearby coffee shop.",
            latitude=91,
            longitude=121.5654,
        )


@pytest.mark.parametrize(
    "url",
    [
        "ftp://example.com/report",
        "https://localhost/report",
        "http://127.0.0.1/report",
        "https://user:secret@example.com/report",
        "https:///missing-host",
    ],
)
def test_url_context_rejects_unsupported_or_nonpublic_urls(url):
    grounding = load_script()

    with pytest.raises(ValueError, match="URL"):
        grounding.build_interaction_request(
            mode="url",
            prompt="Summarize this source.",
            urls=[url],
        )


def test_url_context_adds_validated_urls_to_the_prompt_and_caps_count():
    grounding = load_script()
    urls = ["https://example.com/one", "http://example.org/two"]

    request = grounding.build_interaction_request(
        mode="url",
        prompt="Compare the sources.",
        urls=urls,
    )

    assert request["tools"] == [{"type": "url_context"}]
    assert request["input"] == (
        "Compare the sources.\n\nURLs to retrieve:\n"
        "- https://example.com/one\n"
        "- http://example.org/two"
    )
    with pytest.raises(ValueError, match="20 URLs"):
        grounding.build_interaction_request(
            mode="url",
            prompt="Compare all sources.",
            urls=[f"https://example.com/{index}" for index in range(21)],
        )


def test_normalized_output_preserves_citations_and_tool_evidence_only():
    grounding = load_script()

    result = grounding.normalize_interaction(
        FakeInteraction(),
        mode="search",
        model="gemini-3.5-flash",
    )

    assert result == {
        "interaction_id": "interaction-123",
        "mode": "search",
        "model": "gemini-3.5-flash",
        "text": "Grounded answer.",
        "citations": [
            {
                "type": "url_citation",
                "title": "Primary source",
                "url": "https://example.com/source",
                "start_index": 0,
                "end_index": 16,
            }
        ],
        "tool_steps": [
            {
                "type": "google_search_call",
                "queries": ["grounded test query"],
            },
            {
                "type": "google_search_result",
                "is_error": False,
            },
        ],
        "usage": {"total_tokens": 42},
    }
