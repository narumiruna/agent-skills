---
name: jira-cli
description: Use when interacting with Jira through ankitpokhrel/jira-cli (`jira`), including setup, authentication, issue queries, issue creation or edits, transitions, comments, worklogs, epics, sprints, releases, projects, boards, and script-friendly output.
---

# Jira CLI

## Overview

Use `jira` for Jira work from the terminal. Prefer read-only discovery first, script-friendly output for agents, and explicit confirmation before changing Jira state.

## Safety Rules

- Do not print or store Jira tokens. Use `JIRA_API_TOKEN`, `.netrc`, keychain, or the user's existing shell setup.
- Check the installed command help when flags matter: `jira --help`, then `jira <resource> <command> --help`.
- Prefer non-interactive output in agent runs: `--plain`, `--raw`, `--csv`, `--no-headers`, and `--columns`.
- Prefer `--no-input` only when all required write parameters are known.
- Before create/edit/move/assign/delete/comment/worklog/link operations, show the exact command and ask for confirmation unless the user already authorized that exact mutation.
- Always confirm before `jira issue delete`, even if the user asked generally.

## Setup Check

```sh
command -v jira
jira version
jira me
```

If `jira` is not installed, tell the user to install JiraCLI first and point them to https://github.com/ankitpokhrel/jira-cli/wiki/Installation.

If `jira` is installed but not configured:

```sh
export JIRA_API_TOKEN=...     # never echo the value
jira init                     # Cloud or Local setup
```

For on-prem Personal Access Token auth, set:

```sh
export JIRA_AUTH_TYPE=bearer
export JIRA_API_TOKEN=...
```

For multiple Jira configs, use one of:

```sh
JIRA_CONFIG_FILE=./jira-config.yaml jira issue list --plain
jira issue list -c ./jira-config.yaml --plain
```

## Read Workflow

1. Identify context with read-only commands:
   ```sh
   jira project list --plain
   jira board list --plain
   jira me
   ```
2. Search issues with filters or JQL:
   ```sh
   jira issue list --plain --columns key,status,assignee,summary --no-headers
   jira issue list -a$(jira me) -s"In Progress" --plain
   jira issue list -q "summary ~ cli" --plain
   jira issue list --raw
   ```
3. Inspect the ticket before proposing changes:
   ```sh
   jira issue view ISSUE-1
   jira issue view ISSUE-1 --comments 5
   ```

## Write Workflow

Use explicit issue keys and quote values with spaces.

```sh
# Create
jira issue create -tTask -s"Summary" -b"Description" --no-input
jira issue create -tStory -s"Story summary" -PEPIC-42 --no-input

# Edit
jira issue edit ISSUE-1 -s"New summary" --no-input
jira issue edit ISSUE-1 --label -old-label --label new-label --no-input

# Assign / unassign
jira issue assign ISSUE-1 $(jira me)
jira issue assign ISSUE-1 x

# Transition
jira issue move ISSUE-1 "In Progress"
jira issue move ISSUE-1 Done -RFixed -a$(jira me)

# Comments and worklogs
jira issue comment add ISSUE-1 "Comment body"
echo "Long comment" | jira issue comment add ISSUE-1
jira issue worklog add ISSUE-1 "2h" --comment "What changed" --no-input
```

Use templates or stdin for longer descriptions/comments:

```sh
jira issue create --template /path/to/template.md
jira issue comment add ISSUE-1 --template - < comment.md
```

## Planning / Agile Commands

```sh
# Epics
jira epic list --table --plain
jira epic list EPIC-1 --plain
jira epic create -n"Epic name" -s"Epic summary" --no-input
jira epic add EPIC-1 ISSUE-1 ISSUE-2
jira epic remove ISSUE-1 ISSUE-2

# Sprints
jira sprint list --table --plain
jira sprint list --current --plain
jira sprint list SPRINT_ID -a$(jira me) --plain
jira sprint add SPRINT_ID ISSUE-1 ISSUE-2

# Releases, projects, boards
jira release list --plain
jira release list --project KEY --plain
jira project list --plain
jira board list --plain
```

## Output Patterns For Scripts

```sh
# Stable tabular extraction
jira issue list --plain --columns key,status,assignee,summary --no-headers

# Machine-readable extraction
jira issue list --raw
jira issue list --csv

# Count examples
jira issue list --created month --plain --columns created --no-headers
jira sprint list --table --plain --columns id,name --no-headers
```

## Common Mistakes

- Letting `jira issue list` open the interactive UI during an automated agent run.
- Mutating the wrong Jira instance because `JIRA_CONFIG_FILE` or `-c` was omitted.
- Assuming status, resolution, priority, issue type, or custom field names; discover them with `jira ... --help`, existing tickets, or Jira config first.
- Using unquoted shell arguments for statuses or summaries with spaces.
- Adding token values to chat, logs, shell history, or repository files.
