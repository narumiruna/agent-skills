from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path
from types import ModuleType

import pytest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def load_module(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_deprecated_skills_are_hidden_from_standard_discovery() -> None:
    for skill_md in sorted((SKILLS / "deprecated").glob("*/SKILL.md")):
        frontmatter = skill_md.read_text().split("---", 2)[1]
        assert "\nmetadata:\n  internal: true\n" in f"\n{frontmatter}\n", skill_md


def test_active_skills_are_grouped_one_category_deep() -> None:
    categorized = sorted(SKILLS.glob("*/*/SKILL.md"))
    assert categorized == sorted(SKILLS.glob("**/SKILL.md"))
    assert len({skill_md.parent.name for skill_md in categorized}) == len(categorized)


def test_openai_short_descriptions_fit_supported_ui_length() -> None:
    for metadata_path in sorted(SKILLS.glob("**/agents/openai.yaml")):
        description_line = next(
            line
            for line in metadata_path.read_text().splitlines()
            if line.lstrip().startswith("short_description:")
        )
        description = json.loads(description_line.split(":", 1)[1].strip())
        assert isinstance(description, str), metadata_path
        assert 25 <= len(description) <= 64, metadata_path


def test_bundled_script_commands_do_not_assume_source_checkout_layout() -> None:
    checkout_script = re.compile(r"(?<![\w/])skills/[^\s`\"']+/scripts/")
    offenders: list[Path] = []
    for markdown_path in sorted(SKILLS.glob("**/*.md")):
        if "/assets/" in markdown_path.as_posix():
            continue
        if checkout_script.search(markdown_path.read_text()):
            offenders.append(markdown_path)
    assert offenders == []


def test_marp_validator_rejects_unclosed_frontmatter(tmp_path: Path) -> None:
    deck = tmp_path / "invalid.md"
    deck.write_text("---\nmarp: true\n# Missing closing delimiter\n")

    result = subprocess.run(
        [
            "bash",
            str(
                SKILLS
                / "slides-visuals/authoring-marp-slides/scripts/validate_marpit.sh"
            ),
            str(deck),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "syntax valid" not in result.stdout


def test_marp_validator_requires_exactly_one_file(tmp_path: Path) -> None:
    deck = tmp_path / "valid.md"
    deck.write_text("---\nmarp: true\n---\n# Slide\n")

    result = subprocess.run(
        [
            "bash",
            str(
                SKILLS
                / "slides-visuals/authoring-marp-slides/scripts/validate_marpit.sh"
            ),
            str(deck),
            "unexpected.md",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "Usage:" in result.stdout


def test_marp_validator_accepts_relative_path_starting_with_dash(
    tmp_path: Path,
) -> None:
    deck = tmp_path / "--deck.md"
    deck.write_text("---\nmarp: true\n---\n# Slide\n")

    result = subprocess.run(
        [
            "bash",
            str(
                SKILLS
                / "slides-visuals/authoring-marp-slides/scripts/validate_marpit.sh"
            ),
            deck.name,
        ],
        cwd=tmp_path,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def test_marp_validator_accepts_crlf_and_yaml_comment(tmp_path: Path) -> None:
    deck = tmp_path / "windows.md"
    deck.write_bytes(
        b"---\r\nmarp: TRUE  # enable Marp\r\ntheme: default\r\n---\r\n# Slide\r\n"
    )

    result = subprocess.run(
        [
            "bash",
            str(
                SKILLS
                / "slides-visuals/authoring-marp-slides/scripts/validate_marpit.sh"
            ),
            str(deck),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout
    assert "Slides: 1" in result.stdout


def test_contrast_checker_reports_failed_large_text() -> None:
    result = subprocess.run(
        [
            sys.executable,
            str(
                SKILLS
                / "slides-visuals/designing-slide-colors/scripts/check_contrast.py"
            ),
            "#999999",
            "#FFFFFF",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert "WCAG AA (large text):   ❌ Fail" in result.stdout


def test_color_parsers_reject_malformed_six_character_values() -> None:
    generator = load_module(
        SKILLS / "slides-visuals/designing-slide-colors/scripts/generate_palette.py",
        "generate_palette_invalid_color_test",
    )
    checker = load_module(
        SKILLS / "slides-visuals/designing-slide-colors/scripts/check_contrast.py",
        "check_contrast_invalid_color_test",
    )

    for module in (generator, checker):
        with pytest.raises(ValueError, match="Invalid hex color"):
            module.hex_to_rgb("-12345")


def test_brand_palette_normalizes_color_and_rejects_unknown_style() -> None:
    generator = load_module(
        SKILLS / "slides-visuals/designing-slide-colors/scripts/generate_palette.py",
        "generate_palette_brand_test",
    )

    palette = generator.generate_palette_from_brand("2e75b6", "light")

    assert palette["Primary"] == "#2E75B6"
    with pytest.raises(ValueError, match="Style must be 'light' or 'dark'"):
        generator.generate_palette_from_brand("#2E75B6", "sepia")


def test_generated_palette_contrast_is_calculated_from_colors() -> None:
    generator = load_module(
        SKILLS / "slides-visuals/designing-slide-colors/scripts/generate_palette.py",
        "generate_palette_for_test",
    )
    checker = load_module(
        SKILLS / "slides-visuals/designing-slide-colors/scripts/check_contrast.py",
        "check_contrast_for_test",
    )
    palette = generator.generate_preset_palette("accessibility")
    output = generator.format_palette_markdown(palette, "accessibility")
    expected = checker.contrast_ratio(palette["Primary"], palette["Background"])

    assert "All combinations meet WCAG AAA" not in output
    assert f"Primary/Background = {expected:.2f}:1" in output


def test_publish_examples_keep_tokens_out_of_argv() -> None:
    packaging = (
        SKILLS / "python/managing-python-with-uv/references/packaging.md"
    ).read_text()
    assert "--token" not in packaging
    assert "UV_PUBLISH_TOKEN" in packaging


def test_logging_context_has_a_default_for_unrelated_records() -> None:
    logging_reference = (
        SKILLS / "python/configuring-python-logging/references/logging.md"
    ).read_text()
    assert 'defaults={"user_id": "-"}' in logging_reference


def test_plan_archival_is_scoped_to_the_current_plan() -> None:
    plan_skill = (SKILLS / "writing-research/writing-plans/SKILL.md").read_text()
    assert "inspect `./docs/plans/*.md`" not in plan_skill
    assert "current plan" in plan_skill


def test_generic_gourmet_ranking_is_not_hardcoded_to_okinawa() -> None:
    gourmet_skill = (
        SKILLS / "writing-research/researching-gourmet-venues/SKILL.md"
    ).read_text()
    ranking_section = gourmet_skill.split("## Ranking Retrieval", 1)[1].split("## ", 1)[
        0
    ]
    assert "Okinawa" not in ranking_section
    assert "A4705" not in ranking_section


def test_slide_image_guidance_preserves_inline_images() -> None:
    slide_skill = (SKILLS / "slides-visuals/creating-slide-decks/SKILL.md").read_text()
    assert "for all images" not in slide_skill
    assert "inline" in slide_skill
