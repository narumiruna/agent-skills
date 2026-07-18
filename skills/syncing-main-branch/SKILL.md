---
name: syncing-main-branch
description: Switch a clean Git worktree to the local main branch and fast-forward it from its configured upstream. Use only when the user explicitly invokes $syncing-main-branch or names syncing-main-branch; never auto-activate from ordinary requests to switch branches, return after a merge, pull, update, or sync a repository.
---

# Syncing Main Branch

Use this skill only after explicit invocation. Switch to `main`, update it without creating a merge commit, and preserve the branch and worktree being left.

## Workflow

1. Inspect before mutating:

   ```bash
   git status --porcelain=v1 --untracked-files=all
   git status --short --branch
   git branch --show-current
   ```

   Stop if tracked or untracked changes exist. Report them; do not stash, commit, discard, or carry them onto `main` automatically.

2. Resolve `main`.
   - If `refs/heads/main` exists locally, use it.
   - If local `main` is absent and exactly one intended remote-tracking `main` is clear from repository context, create the tracking branch with `git switch --track -c main <remote>/main`.
   - If the remote is ambiguous, `main` does not exist, or another worktree already has it checked out, stop and report the specific blocker. Do not substitute `master`, bypass worktree protection, or invent a remote.

3. Switch when not already on `main`:

   ```bash
   git switch main
   ```

4. Verify that `main` has a configured upstream, then update without an implicit merge commit:

   ```bash
   git rev-parse --abbrev-ref 'main@{upstream}'
   git pull --ff-only
   ```

   If the branch has diverged, the upstream is missing, authentication fails, or the pull cannot fast-forward, stop. Do not rebase, reset, force, or change upstream configuration without a separate request.

5. Verify and report:

   ```bash
   git status --short --branch
   git log -1 --oneline --decorate
   ```

   Confirm the active branch, whether it advanced, and whether it matches its upstream. Do not delete the previous feature branch.

## Safety Rules

- Operate on the current repository only.
- Keep the worktree clean throughout the switch and pull.
- Never use interactive Git commands or a pager.
- Never use `--force`, automatic stashing, hard reset, or branch deletion.
- If `git pull --ff-only` reports no changes, treat that as success and do not create a commit.
