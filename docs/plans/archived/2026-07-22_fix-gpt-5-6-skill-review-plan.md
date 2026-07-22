## Goal

Resolve every confirmed finding from the review of PR #95 with regression evidence, then prepare a new stacked pull request targeting `agent/optimize-skills-for-gpt-5-6` so merging it updates the original PR.

## Assumptions

- “New PR” means a focused stacked fix PR rather than a duplicate replacement PR against `main`.
- Local edits, tests, branching, and commits are authorized; pushing the branch and creating the public PR require approval of the exact ref, title, and body.

## Plan

- [x] Add focused failing checks for the Peewee connection lifecycle, Marp structural-check claims, SVG host accessibility, palette candidate language, Jira authorization, Atuin disabled automation/fixed cutoffs, Telegraph byline defaults, gourmet source minimum, and chat-only plan archival; verified 12 focused repository assertions and the Atuin fixed-cutoff test failed for the reviewed reasons, while the Telegraph request-field test proved empty author fields are already transmitted.
- [x] Fix Peewee and Marp guidance/scripts at their lifecycle and validation boundaries; verified a file-backed two-context Peewee example passed, the renamed structural precheck accepted malformed YAML without claiming syntax validity, and focused repository tests passed.
- [x] Fix SVG accessibility and palette output claims; verified host-level alt/adjacent semantic alternatives are documented and representative terminal, data-viz, high-contrast, and accessibility generator output uses candidate/verification language.
- [x] Fix Jira, Atuin, and Telegraph authorization/destructive/publication boundaries; verified exact-operation authorization text, disabled transactional cleanup across all prompt surfaces, fixed dedup command cutoffs, and explicit empty author fields in Telegraph request data.
- [x] Restore gourmet evidence minimum and scope plan archival to saved plans; verified targeted repository assertions in `tests/test_skill_repository.py`.
- [x] Run skill validation, focused tests, the full repository suite, representative scripts, `prek run -a`, and final diff review; verified `just`, 32/32 skill validation, 76/76 tests, live Peewee/Marp/palette checks, all `prek` hooks, `git diff --check`, zero broken links, and an independent nine-finding re-review.
- [x] Create a focused local commit and prepare the exact stacked push/PR payload for user approval; verified `agent/fix-gpt-5-6-skill-review` is clean and one commit ahead of `agent/optimize-skills-for-gpt-5-6`, with the exact base, head, title, body, and push ref prepared.

## Risks

- Mitigated: deprecated Atuin automation is removed from the CLI parser, disabled on every prompt surface, and covered by no-mutation and fixed-cutoff tests.
- Mitigated: the Marp structural checker rename has no stale references, all relative links resolve, and malformed-YAML behavior is tested without a false syntax claim.
- Controlled: the new PR payload targets the PR #95 branch, not `main`, so it will contain only the focused fixes.

## Completion Checklist

- [x] All nine reviewed issue groups are resolved, verified by targeted regressions and an independent PASS re-review.
- [x] No destructive or public action can be inferred from supplied content alone, verified by Jira, Atuin, and Telegraph boundary tests.
- [x] All affected skill trigger, metadata, reference, script, and README surfaces remain aligned, verified by skill validation, searches, and link checks.
- [x] All repository gates pass on the final files, verified by 76 tests and all `prek` hooks.
- [x] The completed plan is archived and the exact external PR action is ready for explicit approval.
