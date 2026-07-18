---
name: syncing-main-branch
description: Switch a clean Git worktree to the local main branch and fast-forward it from its configured upstream. Use only when the user explicitly invokes $syncing-main-branch or names syncing-main-branch; never auto-activate from ordinary requests to switch branches, return after a merge, pull, update, or sync a repository.
---

# Syncing Main Branch

Use this skill only after explicit invocation. Switch to `main`, update it without creating a merge commit, and preserve the branch, commits, and local files being left.

## Workflow

1. Inspect before mutating:

   ```bash
   git status --porcelain=v1 --untracked-files=all
   git status --short --branch
   git symbolic-ref --quiet --short HEAD
   ```

   Stop if tracked or untracked changes exist. Report them; do not stash, commit, discard, or carry them onto `main` automatically.

   If the symbolic-ref check fails, record `git rev-parse HEAD` and inspect containing refs with `git for-each-ref --format='%(refname)' --contains=HEAD refs/heads refs/tags refs/remotes`, then stop. Do not leave a detached commit reachable only through reflog; ask whether to preserve it with a branch or tag before switching.

2. Resolve `main`.
   - If `refs/heads/main` exists locally, use it.
   - If local `main` is absent and exactly one intended remote-tracking `main` is clear from repository context, create it with `git switch --no-overwrite-ignore --track -c main <remote>/main`.
   - If the remote is ambiguous, `main` does not exist, or another worktree already has it checked out, stop and report the specific blocker. Do not substitute `master`, bypass worktree protection, or invent a remote.

3. Switch when not already on `main`, protecting ignored local files from branch collisions:

   ```bash
   git switch --no-overwrite-ignore main
   ```

4. Verify that `main` tracks the intended `<remote>/main`. Fetch that remote without updating the worktree, then fast-forward with ignored-file overwrite protection:

   ```bash
   upstream_remote=$(git config --get branch.main.remote)
   git rev-parse --abbrev-ref 'main@{upstream}'
   git fetch "$upstream_remote"
   git merge --ff-only --no-overwrite-ignore 'main@{upstream}'
   ```

   If the branch has diverged, the upstream is missing or unexpected, authentication fails, an ignored path would be overwritten, or the update cannot fast-forward, stop. Do not rebase, reset, force, delete ignored files, or change upstream configuration without a separate request.

5. Verify and report:

   ```bash
   git status --short --branch
   git log -1 --oneline --decorate
   ```

   Confirm the active branch, whether it advanced, and whether it matches its upstream. Do not delete the previous feature branch.

## Safety Rules

- Operate on the current repository only.
- Require tracked and untracked state to be clean; leave ignored files untouched and use overwrite-protected switch and merge commands.
- Never use interactive Git commands or a pager.
- Never use `--force`, automatic stashing, hard reset, or branch deletion.
- If the protected fast-forward reports no changes, treat that as success and do not create a commit.
