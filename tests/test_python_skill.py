from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = REPO_ROOT / "skills" / "python" / "SKILL.md"
QUALITY_REFERENCE_PATH = REPO_ROOT / "skills" / "python" / "references" / "quality.md"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_new_project_baseline_requires_default_dev_toolchain() -> None:
    skill_text = read_text(SKILL_PATH)
    quality_text = read_text(QUALITY_REFERENCE_PATH)

    expected_command = "uv add --dev ruff ty pytest pytest-cov"

    assert expected_command in skill_text
    assert expected_command in quality_text
    assert "brand-new Python project" in skill_text


def test_new_projects_default_to_pytest_best_practices() -> None:
    skill_text = read_text(SKILL_PATH)
    quality_text = read_text(QUALITY_REFERENCE_PATH)

    assert "`pytest` is the default test framework for new projects." in quality_text
    assert "function-based `tests/test_*.py` files" in skill_text
    assert "plain `assert`" in skill_text
    assert "@pytest.mark.parametrize" in skill_text
    assert "fixtures" in quality_text


def test_python_skill_rejects_unittest_as_the_new_project_default() -> None:
    skill_text = read_text(SKILL_PATH)
    quality_text = read_text(QUALITY_REFERENCE_PATH)

    assert "`unittest.TestCase`" in skill_text
    assert "`unittest.TestCase`" in quality_text
    assert "Do not start with `unittest`" in skill_text


def test_existing_repositories_keep_their_current_test_stack() -> None:
    skill_text = read_text(SKILL_PATH)
    quality_text = read_text(QUALITY_REFERENCE_PATH)

    expected_policy = (
        "follow the established test stack unless the user explicitly asks to migrate frameworks"
    )

    assert expected_policy in skill_text
    assert "follow the established test stack unless the user explicitly requests a migration" in quality_text
