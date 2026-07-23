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
DEPRECATED = ROOT / "deprecated"


def all_skill_markdown() -> list[Path]:
    return sorted([*SKILLS.glob("*/*/SKILL.md"), *DEPRECATED.glob("*/SKILL.md")])


def load_module(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_deprecated_skills_are_hidden_from_standard_discovery() -> None:
    deprecated = sorted(DEPRECATED.glob("*/SKILL.md"))
    assert len(deprecated) == 6
    for skill_md in deprecated:
        frontmatter = skill_md.read_text().split("---", 2)[1]
        assert "\nmetadata:\n  internal: true\n" in f"\n{frontmatter}\n", skill_md


def test_every_skill_name_metadata_and_catalog_inventory_is_complete() -> None:
    skill_markdown = all_skill_markdown()
    assert len(skill_markdown) == 33
    readme = (ROOT / "README.md").read_text()

    for skill_md in skill_markdown:
        frontmatter = skill_md.read_text().split("---", 2)[1]
        name_line = next(
            line for line in frontmatter.splitlines() if line.startswith("name: ")
        )
        name = name_line.removeprefix("name: ")
        assert name == skill_md.parent.name, skill_md

        metadata_path = skill_md.parent / "agents/openai.yaml"
        metadata = metadata_path.read_text()
        assert f"${name}" in metadata, metadata_path
        assert f"| `{name}` |" in readme, skill_md


def test_naming_agent_skills_is_merged_into_creating_agent_skills() -> None:
    creating_dir = SKILLS / "workflow-repository/creating-agent-skills"
    active_naming_dir = SKILLS / "workflow-repository/naming-agent-skills"
    deprecated_naming_dir = DEPRECATED / "naming-agent-skills"

    assert not active_naming_dir.exists()
    assert deprecated_naming_dir.is_dir()

    creating = (creating_dir / "SKILL.md").read_text()
    metadata = (creating_dir / "agents/openai.yaml").read_text()
    deprecated = (deprecated_naming_dir / "SKILL.md").read_text()
    readme = (ROOT / "README.md").read_text()
    active_catalog, deprecated_catalog = readme.split("## 🗄️ Deprecated Skills", 1)
    rename_boundary = creating.split("A naming recommendation", 1)[1].split(
        "For naming-only output", 1
    )[0]
    metadata_fields = {
        line.split(":", 1)[0].strip(): json.loads(line.split(":", 1)[1].strip())
        for line in metadata.splitlines()
        if line.strip().startswith(
            ("display_name:", "short_description:", "default_prompt:")
        )
    }

    assert "Create, name, rename, revise, or review agent skills" in creating
    assert "Name the task and trigger the skill represents" in creating
    assert "lowercase kebab-case" in creating
    assert "original user intent" in creating
    assert "Compare a small candidate set" in creating
    assert "collision risk" in creating
    assert "recommendation does not authorize a repository rename" in creating
    assert "Do not edit files when the user asked only for names or review" in creating
    for rename_surface in (
        "directory",
        "frontmatter `name`",
        "UI metadata and default prompt",
        "catalog",
        "links",
        "examples",
        "tests",
        "other exact-name references",
        "compatibility note",
    ):
        assert rename_surface in rename_boundary
    assert "Naming" in metadata_fields["display_name"]
    assert "name, rename" in metadata_fields["short_description"]
    assert "$creating-agent-skills" in metadata_fields["default_prompt"]
    assert "name, rename" in metadata_fields["default_prompt"]
    assert "metadata:\n  internal: true" in deprecated
    assert "Creating, naming, renaming, optimizing, and reviewing" in active_catalog
    assert "| `naming-agent-skills` |" not in active_catalog
    assert "| `naming-agent-skills` |" in deprecated_catalog


def test_gourmet_research_is_deprecated() -> None:
    active_dir = SKILLS / "writing-research/researching-gourmet-venues"
    deprecated_dir = DEPRECATED / "researching-gourmet-venues"

    assert not active_dir.exists()
    assert deprecated_dir.is_dir()

    skill = (deprecated_dir / "SKILL.md").read_text()
    metadata = (deprecated_dir / "agents/openai.yaml").read_text()
    readme = (ROOT / "README.md").read_text()
    active_catalog, deprecated_catalog = readme.split("## 🗄️ Deprecated Skills", 1)

    assert "metadata:\n  internal: true" in skill
    assert "Deprecated" in metadata
    assert {
        path.name for path in (deprecated_dir / "assets/templates").glob("*.md")
    } == {
        "candidates.md",
        "excluded.md",
        "inbox.md",
        "notes.md",
        "overview.md",
        "top-places.md",
    }
    assert "| `researching-gourmet-venues` |" not in active_catalog
    assert "| `researching-gourmet-venues` |" in deprecated_catalog


def test_typer_skill_covers_current_framework_decisions() -> None:
    typer_dir = SKILLS / "python/building-typer-clis"
    skill = (typer_dir / "SKILL.md").read_text()
    metadata = (typer_dir / "agents/openai.yaml").read_text()
    references = {
        path.name: path.read_text()
        for path in sorted((typer_dir / "references").glob("*.md"))
    }
    readme = (ROOT / "README.md").read_text()

    assert set(references) == {
        "application-architecture.md",
        "packaging-and-completion.md",
        "parameters-and-runtime.md",
        "testing.md",
    }
    assert "Preserve the public invocation grammar" in skill
    assert "declared Typer version" in skill
    assert "`PROGRAM [ARGS]...`" in skill
    assert "`PROGRAM COMMAND [ARGS]...`" in skill
    assert "registering a sub-app with `app.add_typer(...)`" in skill
    assert "`typing.Annotated`" in skill
    assert "`typer.BadParameter`" in skill
    assert "`typer.Exit`" in skill
    assert "`typer.Abort`" in skill
    assert "`ctx.resilient_parsing`" in skill
    assert "## Minimal Pattern" not in skill

    architecture = references["application-architecture.md"]
    assert 'app.add_typer(users_app, name="users")' in architecture
    assert "Registering any sub-app also creates grouped grammar" in architecture
    assert "default missing-command error" in architecture
    assert "invoke_without_command=True" in architecture
    assert "ctx.invoked_subcommand is None" in architecture

    parameters = references["parameters-and-runtime.md"]
    assert "requiredness comes from the presence of a default" in parameters
    assert "absence of both a Python assignment and `default_factory=`" in parameters
    assert "Do not combine `default_factory=` with a Python assignment" in parameters
    assert "confirmation_prompt" in parameters
    assert "`autocompletion`" in parameters
    assert "`shell_complete`" in parameters

    testing = references["testing.md"]
    assert "sequentially" in testing
    assert "result.stdout" in testing and "result.stderr" in testing
    assert "`mix_stderr`" in testing
    assert "`isolated_filesystem()`" in testing

    packaging = references["packaging-and-completion.md"]
    assert "`uv add typer`" in packaging
    assert "`typer-slim`" in packaging and "`typer-cli`" in packaging
    assert "`[project.scripts]`" in packaging
    assert "Typer 0.26.0 vendors Click" in packaging
    assert "`python -m`" in packaging and "shell completion" in packaging

    assert all("https://typer.tiangolo.com/" in text for text in references.values())
    assert "command grammar" in metadata
    assert "Annotated" in metadata
    assert "Typer command grammar, typed parameters" in readme


def test_material_trigger_surfaces_are_semantically_aligned() -> None:
    readme = (ROOT / "README.md").read_text()
    svg_skill = (
        SKILLS / "slides-visuals/creating-svg-illustrations/SKILL.md"
    ).read_text()
    svg_metadata = (
        SKILLS / "slides-visuals/creating-svg-illustrations/agents/openai.yaml"
    ).read_text()
    ui_skill = (SKILLS / "ui-ux-design/designing-user-interfaces/SKILL.md").read_text()
    ui_metadata = (
        SKILLS / "ui-ux-design/designing-user-interfaces/agents/openai.yaml"
    ).read_text()

    assert "documents, and other static artifacts" in svg_skill
    assert "target artifact" in svg_metadata
    assert "SVG diagrams and illustrations for target artifacts" in readme
    assert "Apple-derived philosophy" in ui_skill
    assert "Apple-derived philosophy" in ui_metadata
    assert "Apple-derived, platform-adapted UI work" in readme


def test_skill_bodies_avoid_repeating_trigger_and_generic_cleanup_sections() -> None:
    redundant_headings = {
        "## Overview",
        "## Use When",
        "## When to Use",
        "## Common Mistakes",
        "## Common Failures",
        "## Red Flags",
    }

    for skill_md in all_skill_markdown():
        body = skill_md.read_text().split("---", 2)[2]
        headings = set(body.splitlines())
        assert redundant_headings.isdisjoint(headings), skill_md


def test_active_skills_are_grouped_one_category_deep() -> None:
    categorized = sorted(SKILLS.glob("*/*/SKILL.md"))
    assert categorized == sorted(SKILLS.glob("**/SKILL.md"))
    assert len(categorized) == 27
    assert len({skill_md.parent.name for skill_md in categorized}) == len(categorized)


def test_openai_short_descriptions_fit_supported_ui_length() -> None:
    metadata_paths = [
        skill_md.parent / "agents/openai.yaml" for skill_md in all_skill_markdown()
    ]
    for metadata_path in metadata_paths:
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


def test_marp_structure_check_rejects_unclosed_frontmatter(tmp_path: Path) -> None:
    deck = tmp_path / "invalid.md"
    deck.write_text("---\nmarp: true\n# Missing closing delimiter\n")

    result = subprocess.run(
        [
            "bash",
            str(
                SKILLS
                / "slides-visuals/authoring-marp-slides/scripts/check_marpit_structure.sh"
            ),
            str(deck),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "syntax valid" not in result.stdout


def test_marp_structure_check_requires_exactly_one_file(tmp_path: Path) -> None:
    deck = tmp_path / "valid.md"
    deck.write_text("---\nmarp: true\n---\n# Slide\n")

    result = subprocess.run(
        [
            "bash",
            str(
                SKILLS
                / "slides-visuals/authoring-marp-slides/scripts/check_marpit_structure.sh"
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


def test_marp_structure_check_accepts_relative_path_starting_with_dash(
    tmp_path: Path,
) -> None:
    deck = tmp_path / "--deck.md"
    deck.write_text("---\nmarp: true\n---\n# Slide\n")

    result = subprocess.run(
        [
            "bash",
            str(
                SKILLS
                / "slides-visuals/authoring-marp-slides/scripts/check_marpit_structure.sh"
            ),
            deck.name,
        ],
        cwd=tmp_path,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def test_marp_structure_check_accepts_crlf_and_yaml_comment(tmp_path: Path) -> None:
    deck = tmp_path / "windows.md"
    deck.write_bytes(
        b"---\r\nmarp: TRUE  # enable Marp\r\ntheme: default\r\n---\r\n# Slide\r\n"
    )

    result = subprocess.run(
        [
            "bash",
            str(
                SKILLS
                / "slides-visuals/authoring-marp-slides/scripts/check_marpit_structure.sh"
            ),
            str(deck),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout
    assert "Slides: 1" in result.stdout


def test_marp_structure_check_does_not_claim_to_parse_malformed_yaml(
    tmp_path: Path,
) -> None:
    deck = tmp_path / "malformed-yaml.md"
    deck.write_text("---\nmarp: true\ntheme: [\n---\n# Slide\n")

    result = subprocess.run(
        [
            "bash",
            str(
                SKILLS
                / "slides-visuals/authoring-marp-slides/scripts/check_marpit_structure.sh"
            ),
            str(deck),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Structural precheck passed" in result.stdout
    assert "syntax valid" not in result.stdout


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
    assert "Accessibility First" not in output
    assert "Accessibility requirements" not in output
    assert f"Primary/Background = {expected:.2f}:1" in output

    terminal_output = generator.format_palette_markdown(
        generator.generate_preset_palette("terminal-dark"), "terminal-dark"
    )
    data_viz_output = generator.format_palette_markdown(
        generator.generate_preset_palette("data-viz"), "data-viz"
    )
    assert "High contrast for projectors" not in terminal_output
    assert "colorblind-friendly" not in data_viz_output

    svg_output = generator.format_svg_palette("high-contrast")
    assert "High Contrast Candidate" in svg_output
    assert "Accessibility, large venue presentations" not in svg_output
    assert "AAA compliance" not in svg_output


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


def test_plan_archival_is_scoped_to_saved_current_plan() -> None:
    plan_skill = (SKILLS / "writing-research/writing-plans/SKILL.md").read_text()
    assert "inspect `./docs/plans/*.md`" not in plan_skill
    assert "current saved plan" in plan_skill
    assert "Do not create an archive file for a chat-only plan" in plan_skill
    assert "archive that plan under `docs/plans/archived/`" in plan_skill


def test_generic_gourmet_ranking_is_not_hardcoded_to_okinawa() -> None:
    gourmet_skill = (DEPRECATED / "researching-gourmet-venues/SKILL.md").read_text()
    ranking_section = gourmet_skill.split("## Ranking Retrieval", 1)[1].split("## ", 1)[
        0
    ]
    assert "Okinawa" not in ranking_section
    assert "A4705" not in ranking_section


def test_slide_image_guidance_preserves_inline_images() -> None:
    slide_skill = (SKILLS / "slides-visuals/creating-slide-decks/SKILL.md").read_text()
    assert "for all images" not in slide_skill
    assert "inline" in slide_skill


def test_worktree_default_storage_root_is_user_home() -> None:
    worktree_skill = (
        SKILLS / "workflow-repository/managing-git-worktrees/SKILL.md"
    ).read_text()

    assert "default the storage root to `$HOME/.worktrees`" in worktree_skill
    assert (
        "<root>/<main-name>-<branch-with-slashes-replaced-by-hyphens>" in worktree_skill
    )
    assert "default to a sibling" not in worktree_skill


def test_external_and_destructive_workflows_require_exact_authorization() -> None:
    uv_skill = (SKILLS / "python/managing-python-with-uv/SKILL.md").read_text()
    pr_skill = (
        SKILLS / "workflow-repository/resolving-pr-review-comments/SKILL.md"
    ).read_text()
    jira_skill = (SKILLS / "workflow-repository/using-jira-cli/SKILL.md").read_text()
    atuin_skill = (DEPRECATED / "cleaning-atuin-history/SKILL.md").read_text()

    assert "exact package/version, repository or index, and artifacts" in uv_skill
    assert "does not by itself authorize public replies" in pr_skill
    assert "push remote" in pr_skill and "reply text" in pr_skill
    assert "authorization for the exact operation, target, and content" in jira_skill
    assert "Supplying values for a draft does not authorize execution" in jira_skill
    assert "do not run interactive `jira init`" in jira_skill
    assert "approved candidate IDs" in atuin_skill
    assert "Do not invoke `cleanup-typos`" in atuin_skill
    assert "before every mutation" in atuin_skill
    assert "fixed cutoff" in atuin_skill
    assert "`atuin store push`" in atuin_skill and "`atuin sync`" in atuin_skill


def test_peewee_fixture_survives_sequential_connection_contexts() -> None:
    peewee = (SKILLS / "python/using-peewee-orm/SKILL.md").read_text()

    assert "def test_db(tmp_path):" in peewee
    assert 'tmp_path / "test.db"' in peewee
    assert 'SqliteDatabase(":memory:"' not in peewee
    assert "two sequential `connection_context()`" in peewee


def test_svg_embedding_preserves_host_level_accessibility() -> None:
    embedding = (
        SKILLS / "slides-visuals/creating-svg-illustrations/references/embedding.md"
    ).read_text()

    assert "descriptive host-level alt text" in embedding
    assert "adjacent semantic equivalent" in embedding
    assert "![System architecture w:800]" in embedding
    assert "![bg fit](assets/diagram.svg)" not in embedding


def test_marp_examples_pair_visuals_with_nonredundant_semantics() -> None:
    authoring = SKILLS / "slides-visuals/authoring-marp-slides"
    example = (authoring / "assets/examples/with-bg-syntax.md").read_text()
    template = (authoring / "assets/templates/with-bg-images.md").read_text()

    for markdown in (example, template):
        background_slides = [
            slide for slide in markdown.split("\n---\n") if "![bg" in slide
        ]
        assert background_slides
        for slide in background_slides:
            assert "**Diagram summary:**" in slide or "**Comparison summary:**" in slide

    assert 'alt="" aria-hidden="true"' in example


def test_atuin_disabled_automation_is_aligned_across_surfaces() -> None:
    atuin_dir = DEPRECATED / "cleaning-atuin-history"
    skill = (atuin_dir / "SKILL.md").read_text()
    reference = (atuin_dir / "references/atuin-cli.md").read_text()
    metadata = (atuin_dir / "agents/openai.yaml").read_text()

    for text in (skill, reference, metadata):
        assert "cleanup-typos" in text
        assert "disabled" in text
    assert "remote operations" not in metadata


def test_publication_and_research_boundaries_remain_explicit() -> None:
    telegraph = (
        SKILLS / "writing-research/creating-telegraph-pages/SKILL.md"
    ).read_text()
    gourmet = (DEPRECATED / "researching-gourmet-venues/SKILL.md").read_text()

    assert "explicit byline decision" in telegraph
    assert "--author-name '' --author-url ''" in telegraph
    assert "Require four independent source roles by default" in gourmet
    assert "three sources only" in gourmet
    assert "Do not score or publish a recommendation with fewer sources" in gourmet


def test_slide_color_checks_never_claim_unperformed_validation() -> None:
    output_template = (
        SKILLS
        / "slides-visuals/designing-slide-colors/references/color-design/output-template.md"
    ).read_text()

    assert "Mark all checklist items" not in output_template
    assert "Check an item only after performing it" in output_template
    assert "Do not describe a palette as projector-" in output_template


def test_visual_creation_does_not_imply_commit_authority() -> None:
    mermaid = (SKILLS / "slides-visuals/creating-mermaid-diagrams/SKILL.md").read_text()
    slide_decks = (SKILLS / "slides-visuals/creating-slide-decks/SKILL.md").read_text()

    assert "Commit source `.mmd`" not in mermaid
    assert "does not authorize a Git commit" in mermaid
    assert "does not authorize committing" in slide_decks


def test_logging_and_peewee_examples_preserve_runtime_semantics() -> None:
    loguru = (
        SKILLS / "python/configuring-python-logging/references/loguru.md"
    ).read_text()
    peewee = (SKILLS / "python/using-peewee-orm/SKILL.md").read_text()

    assert "@logger.catch(reraise=True)" in loguru
    assert "{extra}" in loguru
    assert "db_proxy.obj" not in peewee
    assert "MODELS = [User]" in peewee
    assert "with db.connection_context():\n    with db.atomic():" in peewee
    assert "finally:\n        with db.connection_context():" in peewee
    assert "            db.drop_tables(MODELS, safe=True)" in peewee


def test_relative_markdown_links_resolve() -> None:
    markdown_paths = [ROOT / "README.md"]
    for skill_md in all_skill_markdown():
        markdown_paths.extend(skill_md.parent.rglob("*.md"))

    for markdown_path in sorted(set(markdown_paths)):
        for target in re.findall(
            r"(?<!!)\[[^\]]*\]\(([^)]+)\)", markdown_path.read_text()
        ):
            relative_target = target.strip().split("#", 1)[0]
            if not relative_target or "://" in relative_target:
                continue
            assert (markdown_path.parent / relative_target).exists(), (
                markdown_path,
                relative_target,
            )
