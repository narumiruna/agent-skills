---
name: resolving-pr-review-comments
description: Inspect all feedback on a pull request, assess whether each comment is valid against the current code, address reasonable findings, verify the changes, reply to and resolve eligible threads, commit, and push. Use only when the user explicitly invokes $resolving-pr-review-comments or names resolving-pr-review-comments; never auto-activate from ordinary requests about reviews, comments, pull requests, commits, or pushes.
---

# Resolving PR Review Comments

Use this skill only after explicit invocation. Treat review comments as claims to verify, not instructions to apply blindly. External actions covered by the invocation are review replies, thread resolution, commits, and a normal push to the current pull-request branch.

## Establish Scope

1. Inspect the worktree and current branch. Preserve unrelated staged, unstaged, and untracked changes; never blanket-stage them.
2. Resolve the pull request, repository, head branch, base branch, number, URL, and current state from the hosting provider. For GitHub, start with:

   ```bash
   gh pr view --json number,url,state,baseRefName,headRefName
   ```

3. Confirm that the checked-out branch is the pull request head. Stop rather than editing or pushing another branch accidentally.
4. Compare the pull request against the merge base of its reported base branch. Do not assume the base is `main`.

## Read All Feedback

Collect every feedback surface, not only the summary shown by `gh pr view`:

- top-level pull-request or issue comments
- submitted reviews and their bodies
- inline review comments
- review threads, including resolution and outdated state

On GitHub, use paginated REST endpoints for issue comments, reviews, and inline comments, plus the GraphQL `reviewThreads` connection for thread IDs, `isResolved`, `isOutdated`, and all thread comments. Paginate beyond the first page. Do not treat an empty top-level comment list as proof that no inline feedback exists.

Ignore non-actionable service messages such as quota notices, but do not silently omit substantive feedback. Re-query after pushing because comments can arrive while work is in progress.

## Assess Each Comment

Trace each concern against the current HEAD, pull-request intent, repository instructions, tests, and relevant callers.

Classify it as one of:

- **Reasonable and unresolved:** the issue reproduces or the current change violates a documented contract; fix it.
- **Already addressed or outdated:** current code resolves the concern; gather concrete file, commit, or test evidence.
- **Not reasonable:** the suggestion conflicts with requirements, relies on a false premise, or adds unjustified scope; prepare a concise evidence-based reply instead of changing code.
- **Ambiguous or disputed:** a behavior decision or external information is missing; ask one focused question or leave the thread open.

Do not implement preference-only suggestions as correctness fixes. Do not mark a thread resolved merely to clear the review queue.

## Address Reasonable Feedback

1. Add the smallest regression test or failing executable check before a non-trivial code fix when practical.
2. Fix the shared cause, then scan directly affected sibling paths for the same defect.
3. Keep changes bounded to accepted feedback. Preserve unrelated local work.
4. Run focused checks, then the repository's normal verification gate.
5. Inspect the final diff and verify that it contains only intended changes.

## Commit and Push

1. Group changes into coherent commit boundaries. If comments require unrelated fixes, use separate focused commits.
2. Stage only intended paths and write Conventional Commit messages grounded in each staged diff. Do not add attribution trailers.
3. If no file change is needed, do not create an empty commit.
4. Push the current pull-request branch to its configured upstream with a normal `git push`. Never force-push unless the user separately and explicitly requests it.

## Reply and Resolve

- Reply to each addressed thread with the commit ID, concise fix summary, and verification evidence.
- For already-addressed or declined feedback, reply with concrete evidence or rationale.
- Mark an inline thread resolved only after the fix is pushed or the concern is conclusively addressed. Leave ambiguous or genuinely disputed threads open.
- Top-level comments and review bodies may not have a resolvable thread; acknowledge them when a response is warranted.

Finally, re-query all feedback surfaces and verify:

- every reasonable comment is addressed
- every eligible thread is resolved
- intentionally open threads are reported with the reason
- local HEAD equals the pushed remote head
- the worktree contains no unintended changes

Report the pull-request URL, commits pushed, resolved and remaining thread counts, checks run, and any feedback deliberately not implemented.
