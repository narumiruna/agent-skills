---
name: checking-cli-help
description: Decide when to check command help before running shell or CLI commands. Use when Codex is about to execute a command and must judge whether it already understands the exact command form, flags, subcommands, or help path well enough to proceed, or should first consult `--help`, built-in `help`, `man`, or shell `help`.
---

# Help Me

## Overview

Decide whether you know the exact command form well enough to run it. Keep the rule simple: if you can explain it clearly, run it; if you cannot, check help first.

## Decision Tree

1. Ask whether you are familiar with the exact command form you are about to run, not only the base command name.
2. Treat it as familiar only if you can explain:
   - what it will do
   - what target, path, or object it will touch
   - what the important flags or subcommands change
3. Run it directly if you can answer those questions clearly.
4. Check help first if you cannot.
5. Use this order:
   - `<cmd> --help`
   - `<cmd> <subcommand> --help`
   - the tool's built-in `help` form
   - `man <cmd>`
   - `type <cmd>` or `command -v <cmd>` when the help path is unclear; if it is a shell builtin, use shell `help`

Do not use a hard whitelist. Judge familiarity on the exact command you are about to run.

## Examples

- Run directly when familiar: `pwd`, `ls src`, `git status`
- Check first when unfamiliar: `find ... -exec ...`, `git rebase --rebase-merges`, `docker run ... --filter ...`
- Resolve builtins explicitly: if unsure about `cd` or `export`, run `type cd` and then `help cd`
