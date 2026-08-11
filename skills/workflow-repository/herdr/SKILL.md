---
name: herdr
description: Control Herdr panes, tabs, workspaces, commands, and coding agents when the user explicitly mentions Herdr or asks to use it. Requires HERDR_ENV=1 and must not trigger merely because parallel or background work could help.
---

# Herdr

Use the `herdr` CLI to inspect or control the current Herdr session.

## Verify the session

Run this check before any Herdr control command:

```bash
test "${HERDR_ENV:-}" = 1
```

If it fails, say that this agent is not running inside Herdr and stop.
Do not inspect or control a focused Herdr session from outside Herdr.

## Confirm command syntax

Treat the installed binary as authoritative.
Run `herdr --help`, then run the relevant group without a subcommand, such as `herdr agent` or `herdr pane`.
Never run bare `herdr` for discovery because it launches or attaches the TUI.
Never probe a potentially mutating nested command by omitting arguments because commands such as `herdr workspace create` execute with defaults.

Use these groups when needed:

```bash
herdr agent
herdr pane
herdr workspace
herdr tab
herdr worktree
herdr terminal
herdr notification
herdr integration
herdr session
```

## Choose the right control surface

Use workspace, tab, and pane commands for terminal layout and ordinary processes.
Use agent commands for a recognized coding agent and its `idle`, `working`, `blocked`, `done`, or `unknown` state.
`unknown` does not prove completion.

Agent targets are a unique live agent name or the pane ID hosting that agent.
They are not terminal IDs or bare agent-kind labels.
Agent names must match `[a-z][a-z0-9_-]{0,31}` and be unique among live agents.

Prefer `--current`, an explicit pane ID, or a unique agent name.
Do not omit a target when another client's focused pane could be selected.
Parse opaque IDs and state from command JSON rather than predicting them.

Inspect live context with only the commands needed for the task:

```bash
herdr pane current --current
herdr pane list --workspace "$HERDR_WORKSPACE_ID"
herdr agent list
```

## Create background layout

Default to a sibling pane in the current tab with `--cwd "$PWD"`.
Do not create a workspace, tab, worktree, or different working directory unless the user requests that topology or location.
Use `--no-focus` for background work unless the user asks to switch context.

Honor a requested split direction.
Otherwise inspect `herdr pane layout --pane "$HERDR_PANE_ID"`, split a wide pane right, and split a narrow or tall pane down.
Avoid layouts with unusably narrow columns or short rows.

```bash
herdr pane split --current --direction right --cwd "$PWD" --no-focus
```

Read the new pane ID from `.result.pane.pane_id`.
After moving a pane, continue with `.result.move_result.pane.pane_id` or its live agent name rather than the old pane ID.

## Start and coordinate an agent

Start an agent only in an existing shell pane that is idle at its interactive prompt:

```bash
herdr agent start reviewer --kind codex --pane <pane-id>
```

Use the agent kind requested by the user and inspect `herdr agent` for supported kinds and current options.
Pass native agent arguments only after `--`.

Prompt through the agent surface and wait for a settled state:

```bash
herdr agent prompt reviewer "Review the current diff and report only actionable findings." --wait --timeout 120000
```

For ordinary work, `--wait` already waits for `idle`, `done`, or `blocked`, so do not restate those defaults with `--until`.
Use `--until` only for a state-specific workflow:

```bash
herdr agent wait reviewer --until blocked --timeout 120000
```

If a prompt stalls, a wait fails, or the agent becomes `blocked`, inspect state and output before sending more input:

```bash
herdr agent get reviewer
herdr agent read reviewer --source recent-unwrapped --lines 120
```

Use `herdr agent send-keys` with validated logical keys such as `esc` or `ctrl+c` for interactive agent controls.
Use pane commands instead only when raw terminal control is intentional.

## Run an ordinary command

Run non-agent processes through the pane surface:

```bash
herdr pane run <pane-id> "just test"
herdr pane wait-output <pane-id> --match "test result" --timeout 120000
herdr pane read <pane-id> --source recent-unwrapped --lines 120
```

Use `--match` for a literal substring or `--regex` for a Rust regular expression.
Prefer `recent-unwrapped` for logs and transcripts, `visible` for the viewport, `recent` when soft wraps matter, and `detection` for the agent-detection snapshot.
Use `--format ansi` only when terminal styling is evidence.

If more `--lines` cannot recover a completed agent response from the alternate screen, ask the agent to write the full response as Markdown in a temporary directory and return only its path.
Use that file fallback only after a failed read.

## Keep control safe

- Do not close workspaces, tabs, panes, or sessions you did not create unless the user explicitly asks.
- Never run `herdr server stop` from an active session unless the user explicitly intends to stop the server and its pane processes.
- Never kill the main Herdr process.
- Use named test sessions for experiments that require an isolated server.
- Treat CLI server errors as JSON on stderr with exit status 1 and syntax errors as exit status 2.

Stop when the requested inspection or control action is complete, and report the relevant result or blocker.
