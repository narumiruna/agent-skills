---
name: building-codex-hooks
description: Use when designing, implementing, reviewing, or debugging Codex CLI hooks, including `hooks.json`, `.codex/hooks.json`, feature-flag setup, matcher behavior, event-specific stdin/stdout payloads, and hook scripts for `SessionStart`, `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, or `Stop`.
metadata:
  internal: true
---

# Codex CLI Hooks

## Overview

Design Codex hooks from the current workspace outward: enable the feature flag, choose the right config layer, then implement the smallest hook that proves the event contract before adding policy logic.

Treat hooks as workflow guardrails, not absolute enforcement. Current runtime support is intentionally partial, especially for shell interception.

## Workflow

1. Confirm hooks are actually available.
   Check `config.toml` for:
   ```toml
   [features]
   codex_hooks = true
   ```
   Remember hooks are currently disabled on Windows.
2. Choose the config layer.
   Prefer `~/.codex/hooks.json` for personal defaults and `<repo>/.codex/hooks.json` for repo-specific behavior. Matching hooks from multiple files all run; higher-precedence config does not replace lower-precedence hooks.
3. Choose the event before writing code.
   Use `SessionStart` for startup or resume context, `PreToolUse` for pre-Bash checks, `PostToolUse` for post-Bash review, `UserPromptSubmit` for prompt gating or augmentation, and `Stop` for continue-or-stop logic at the end of a turn.
4. Start with a minimal handler.
   First make the hook emit a tiny valid response for the chosen event. Only after that should you add regex matchers, policy checks, file I/O, or transcript parsing.
5. Resolve repo-local commands from the git root.
   Prefer commands like:
   ```bash
   /usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use.py"
   ```
   Do not assume Codex started from the repo root.
6. Choose between a custom script and `codhc`.
   Write a custom hook script when the hook must inspect payload fields, branch on runtime state, or emit event-specific JSON. Prefer `uvx codhc <command...>` when the hook only needs to run an existing CLI check and map its exit status into a Codex-compatible response, especially for `Stop`.

## Event Selection

- `SessionStart`: inject startup or resume context.
- `PreToolUse`: inspect an upcoming Bash command and optionally deny it.
- `PostToolUse`: review Bash output after the command already ran.
- `UserPromptSubmit`: inspect or block the prompt before it is sent.
- `Stop`: stop the turn or force one more continuation pass.

Read `references/events.md` before implementing event-specific stdout formats or blocker behavior.

## Matcher Rules

- Use `matcher` only where runtime honors it.
- For `PreToolUse` and `PostToolUse`, current `tool_name` is only `Bash`.
- For `SessionStart`, matcher applies to `startup` or `resume`.
- For `UserPromptSubmit` and `Stop`, matcher is currently ignored.
- Use `"*"`, `""`, or omit `matcher` to match everything supported by that event.

## Implementation Rules

- Keep `hooks.json` small and explicit. Favor one matcher group per intent.
- Expect concurrent execution when multiple command hooks match the same event.
- Assume every hook receives one JSON object on `stdin`.
- Validate stdout shape per event. Some events accept plain text, some ignore it, and `Stop` requires JSON.
- Use `uvx codhc <command...>` for simple `Stop`-hook validation commands such as `ruff`, `pytest`, or project-specific check scripts.
- Write a custom hook script instead of `codhc` when the hook must read payload fields, compute custom continuation reasons, or produce non-`Stop` event shapes.
- Pass `codhc` commands as argv, not a single shell string. Use `uvx codhc ruff check --fix`, not `uvx codhc "ruff check --fix"`.
- Prefer `systemMessage` or hook-specific structured output over ad hoc print debugging.
- Treat unsupported fields as fail-open. Parsed does not mean enforced.

## Known Runtime Limits

- `PreToolUse` and `PostToolUse` currently only support Bash payloads.
- Shell interception is incomplete for richer execution paths.
- Hooks do not currently intercept MCP, Write, WebSearch, or other non-shell tools.
- `PostToolUse` cannot undo side effects from a command that already ran.
- `PreToolUse` is useful for policy guardrails, not a hard security boundary.
- `codhc` is a thin command wrapper, not a general hook framework or policy engine.
- `codhc` is most useful for `Stop` hooks that wrap an existing command; do not treat it as the default solution for every hook event.

## Debugging Checklist

- Verify the feature flag is enabled.
- Verify the hook file is in an active config layer.
- Verify the event supports the matcher you wrote.
- Verify the matcher can match current runtime values.
- Verify the command path is stable from the session `cwd`.
- Verify stdout matches the event contract exactly.
- Verify you are not depending on unsupported fields such as fail-open updates.
- Verify behavior still makes sense when multiple matching hooks run together.

## References

- `references/events.md`: event matrix, supported fields, and fail-open notes.
- `references/examples.md`: minimal `hooks.json` and hook script output examples.
