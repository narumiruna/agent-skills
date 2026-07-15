from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path
from types import ModuleType

import yaml

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
        frontmatter = yaml.safe_load(skill_md.read_text().split("---", 2)[1])
        assert frontmatter.get("metadata", {}).get("internal") is True, skill_md


def test_openai_short_descriptions_fit_supported_ui_length() -> None:
    for metadata_path in sorted(SKILLS.glob("**/agents/openai.yaml")):
        metadata = yaml.safe_load(metadata_path.read_text())
        description = metadata["interface"]["short_description"]
        assert 25 <= len(description) <= 64, metadata_path


def test_bundled_script_commands_do_not_assume_source_checkout_layout() -> None:
    offenders: list[Path] = []
    for markdown_path in sorted(SKILLS.glob("**/*.md")):
        if "/assets/" in markdown_path.as_posix():
            continue
        if (
            "skills/" in markdown_path.read_text()
            and "/scripts/" in markdown_path.read_text()
        ):
            offenders.append(markdown_path)
    assert offenders == []


def test_marp_validator_rejects_unclosed_frontmatter(tmp_path: Path) -> None:
    deck = tmp_path / "invalid.md"
    deck.write_text("---\nmarp: true\n# Missing closing delimiter\n")

    result = subprocess.run(
        [
            "bash",
            str(SKILLS / "authoring-marp-slides/scripts/validate_marpit.sh"),
            str(deck),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "syntax valid" not in result.stdout


def test_contrast_checker_reports_failed_large_text(tmp_path: Path) -> None:
    del tmp_path
    result = subprocess.run(
        [
            "uv",
            "run",
            "--no-project",
            str(SKILLS / "designing-slide-colors/scripts/check_contrast.py"),
            "#999999",
            "#FFFFFF",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert "WCAG AA (large text):   ❌ Fail" in result.stdout


def test_generated_palette_contrast_is_calculated_from_colors() -> None:
    generator = load_module(
        SKILLS / "designing-slide-colors/scripts/generate_palette.py",
        "generate_palette_for_test",
    )
    checker = load_module(
        SKILLS / "designing-slide-colors/scripts/check_contrast.py",
        "check_contrast_for_test",
    )
    palette = generator.generate_preset_palette("accessibility")
    output = generator.format_palette_markdown(palette, "accessibility")
    expected = checker.contrast_ratio(palette["Primary"], palette["Background"])

    assert "All combinations meet WCAG AAA" not in output
    assert f"Primary/Background = {expected:.2f}:1" in output


def test_publish_examples_keep_tokens_out_of_argv() -> None:
    packaging = (SKILLS / "managing-python-with-uv/references/packaging.md").read_text()
    assert "--token" not in packaging
    assert "UV_PUBLISH_TOKEN" in packaging


def test_logging_context_has_a_default_for_unrelated_records() -> None:
    logging_reference = (
        SKILLS / "configuring-python-logging/references/logging.md"
    ).read_text()
    assert 'defaults={"user_id": "-"}' in logging_reference


def test_plan_archival_is_scoped_to_the_current_plan() -> None:
    plan_skill = (SKILLS / "writing-plans/SKILL.md").read_text()
    assert "inspect `./docs/plans/*.md`" not in plan_skill
    assert "current plan" in plan_skill


def test_generic_gourmet_ranking_is_not_hardcoded_to_okinawa() -> None:
    gourmet_skill = (SKILLS / "researching-gourmet-venues/SKILL.md").read_text()
    ranking_section = gourmet_skill.split("## Ranking Retrieval", 1)[1].split("## ", 1)[
        0
    ]
    assert "Okinawa" not in ranking_section
    assert "A4705" not in ranking_section


def test_slide_image_guidance_preserves_inline_images() -> None:
    slide_skill = (SKILLS / "creating-slide-decks/SKILL.md").read_text()
    assert "for all images" not in slide_skill
    assert "inline" in slide_skill
