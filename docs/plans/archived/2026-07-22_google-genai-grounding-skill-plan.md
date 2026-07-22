# Google GenAI Grounding Skill Plan

## Goal

Create a discoverable, executable skill for one-shot Google GenAI research with Google Search, Google Maps, and URL Context grounding, defaulting to `gemini-3.5-flash` and preserving citation evidence.

## Assumptions

- Place the skill under `skills/writing-research/` because all three workflows retrieve evidence for grounded answers.
- Use the generally available Interactions API and a standalone PEP 723 script run with `uv run --script`.
- Keep requests stateless with `store=false`; accept `GEMINI_API_KEY` only from the environment.

## Plan

- [x] Scaffold `grounding-with-google-genai` with the official initializer; verified the generated skill and metadata paths exist.
- [x] Add focused failing pytest coverage for the default model, tool routing, Maps coordinates, URL validation, stateless requests, and normalized evidence output; captured 9 expected failures before implementation and one serializer regression failure during refinement.
- [x] Implement the standalone CLI and concise skill instructions; focused tests pass and `uv run --script ... --help` executes successfully.
- [x] Update `README.md` and repository inventory expectations; the full repository suite passes with 85 tests.
- [x] Run live Search, Maps, and URL Context requests with the local `.env` key without exposing it; Search and Maps returned citations, and URL Context returned a successful retrieval plus citation after one source-specific retry.
- [x] Run `quick_validate.py`, `prek run -a`, and a clean diff review; all checks pass.
- [x] Forward-test realistic skill usage in a fresh agent thread; the agent selected URL Context, verified the retrieval, cited Python.org, and made no repository edits.

## Risks

- Grounded requests can incur API charges and may be unavailable by region or quota; keep live checks minimal and bounded to one call per mode.
- Google Maps grounding currently supports English prompts and responses only; state that limitation in the skill.
- SDK response step schemas can evolve; normalize through Pydantic serialization and retain tool-step metadata rather than depending on undocumented object internals.

## Completion Checklist

- [x] Skill frontmatter, UI metadata, README catalog, CLI defaults, and tests agree on scope and model.
- [x] All three grounding modes are exercised without leaking the API key.
- [x] Focused tests, full pytest, validator, and lint gate pass.
- [x] Completed plan is archived under `docs/plans/archived/`.
