---
name: managing-git-worktrees
description: Create, inspect, attach, repair, remove, prune, and clean up local Git worktrees safely. Use when Codex needs to manage a repository's worktree lifecycle, including creating a branch-backed worktree under worktrees/, attaching an existing local branch, repairing moved worktrees, diagnosing stale metadata, preserving detached commits and local-only files during removal, or optionally deleting a merged branch.
---

# Manage Git Worktrees

Inspect repository state before changing worktrees. Keep worktree operations separate from commit and push workflows.

Treat every branch, ref, and path as untrusted data. Prefer an argv-capable command interface; when using a shell, quote every dynamic value and never concatenate it into a command string. The variables in examples below stand for already validated values.

## Inspect State

1. Before changing directories, capture the invoking worktree root, symbolic branch, and HEAD object. Treat `refs/heads/<invoking-branch>` as the default start-point.
2. If `git symbolic-ref --quiet --short HEAD` fails during creation because the invoking HEAD is detached, stop and ask for an explicit start-point.
3. Parse `git worktree list --porcelain -z`; use its first record as the main worktree. Do not substitute `git rev-parse --show-toplevel`, which returns the invoking linked worktree.
4. If the first record is bare rather than a main worktree, ask for an explicit storage root instead of inventing one. If its path is stale, repair it before deriving a worktree path.
5. Resolve the requested branch, path, and start-point before mutating anything. Never assume the default branch is named `main`.

## Choose the Path

- Default to `<main-worktree-root>/worktrees/<path-name>`.
- Derive `<path-name>` from the branch by replacing every `/` with `-`; for example, map `feat/login` to `worktrees/feat-login`.
- Check that the resolved path does not already exist and does not collide with another branch after normalization. Stop and report a collision instead of inventing another name.
- Keep `worktrees/` local by ensuring an exact `/worktrees/` line appears in the common Git directory's `info/exclude`. Resolve the file with `git rev-parse --path-format=absolute --git-path info/exclude`, preserve all existing patterns, and append only when the exact line is absent. Do not overwrite the file or modify the tracked `.gitignore`.

## Create or Attach

1. Validate and normalize the branch with `git check-ref-format --branch "$branch"`; use its output as the branch value and stop on failure.
2. Resolve the start-point to one commit with `git rev-parse --verify --end-of-options "${start_point}^{commit}"`; stop if it is missing or ambiguous.
3. Check for the local branch with `git show-ref --verify --quiet "refs/heads/$branch"`.
4. Parse `git worktree list --porcelain -z` to determine branch occupancy. Do not use substring matching.
5. If the branch does not exist, create it from the resolved start object with:

   ```bash
   git worktree add -b "$branch" "$worktree_path" "$start_oid"
   ```

6. If the branch exists and is not present in another worktree record, attach it with:

   ```bash
   git worktree add "$worktree_path" "$branch"
   ```

7. If the branch is already checked out elsewhere, stop and report that worktree's path. Do not use `--force` to bypass branch occupancy.
8. Verify the exact path and branch with `git worktree list --porcelain -z` and `git -C "$worktree_path" status --short --branch`.

## Remove Safely

1. Parse `git worktree list --porcelain -z`. Confirm that the exact target path is registered and is not the first, main-worktree record.
2. Inventory tracked, untracked, ignored, and submodule state with:

   ```bash
   git -C "$worktree_path" status --porcelain=v1 --untracked-files=all --ignored=matching --ignore-submodules=none
   ```

3. Treat every output line, including `??` and `!!`, as data that removal can discard. Expand directory entries when needed to make the loss concrete. If initialized submodules exist, inspect each recursively with the same status options. Stop and show the complete inventory before any destructive approval.
4. Read the target's porcelain record. If it is detached, record its HEAD object and run `git for-each-ref --format='%(refname)' --contains="$head_oid" refs/heads refs/tags refs/remotes`. If no shared durable ref contains it, stop and preserve it with a user-named branch or tag before removal.
5. If the target is locked, report its reason and stop. Unlock it only after the user explicitly confirms that the lock is no longer needed; do not bypass a lock with repeated `--force`.
6. If the inventory is empty and detached-commit reachability is safe, run `git worktree remove "$worktree_path"` and verify that its exact record disappeared.
7. If any local-only data exists, require explicit approval that names what will be lost. Use `--force` only when Git requires it and the user has approved the displayed loss; ignored files may be deleted even when Git does not require `--force`.
8. Preserve the branch by default.

## Delete a Branch When Explicitly Requested

1. Remove the worktree first, then validate the branch name and resolve both the branch and user-chosen comparison ref to commit objects with `git rev-parse --verify --end-of-options`.
2. Do not silently choose a merge target. Verify ancestry with `git merge-base --is-ancestor "$branch_oid" "$comparison_oid"`.
3. If ancestry fails, stop. Use `git branch -D "$branch"` only after a separate, explicit request that acknowledges commits not contained in the comparison ref.
4. If ancestry succeeds, verify immediately that `refs/heads/$branch` still points to `$branch_oid`, then try `git branch -d "$branch"`. This command checks the branch's configured upstream, or current `HEAD` when no upstream exists, rather than the chosen comparison ref.
5. If `-d` refuses solely because those merge targets differ, report the mismatch. Use `git branch -D "$branch"` only after separate explicit approval to bypass Git's built-in check and after re-verifying that the branch still points to `$branch_oid` and remains an ancestor of `$comparison_oid`.

## Repair or Prune Metadata

- Do not prune during routine creation or removal.
- Treat a missing registered path as a diagnosis, not proof of deletion. Run `git worktree repair` inside a moved main or linked worktree; when repairing multiple moved linked worktrees from another worktree, pass each quoted new path to `git worktree repair`. Verify every repaired porcelain record.
- Prune only when the working directory is genuinely gone and the user does not want it recovered. Before pruning a detached record, run the same `git for-each-ref --contains` check and preserve any HEAD object not contained by a shared durable ref.
- Preview with `git worktree prune --dry-run --verbose`. Show the exact preview before running `git worktree prune --verbose` with the same expiry options.
- Do not conflate pruning administrative metadata with deleting a worktree directory or branch.

## Safety Rules

- Prefer porcelain output for reliable worktree and branch occupancy checks.
- Avoid interactive Git commands and pagers.
- Do not delete directories directly as a substitute for `git worktree remove`.
- Never treat an empty default `git status` as proof that removal is lossless.
- Do not perform commits, pushes, rebases, or unrelated branch changes unless the user separately requests that workflow.
