## GOTCHA

- Symptom: recursively downloading Apple HIG HTML misses the navigator and article source. Cause: the site is a DocC SPA whose complete tree and content live under `/tutorials/data/`. Fix: enumerate `/tutorials/data/index/design--human-interface-guidelines`, then download each indexed page JSON and its resource references.
- Symptom: one-off `uv run --with ...` validation fails while initializing `~/.cache/uv` or resolving an uncached dependency. Cause: the sandbox may make that cache read-only, and uv may need network access for a cache miss. Fix: set `UV_CACHE_DIR=/tmp/uv-cache` and request temporary network access only when resolution still fails.

## TASTE

- Prefer applying Apple-derived design philosophy across platforms while translating platform-specific metrics and controls to target conventions; minimize cognitive load without sacrificing functional completeness, keep critical actions and state visible, and use predictable progressive disclosure for secondary complexity.
- Prefer preserving a skill's original user intent when naming or renaming skills; do not force `<verb-ing>-<object>` if it changes the meaning.
- Prefer retaining explicit-invocation skills that act as useful mode shortcuts even when the model can infer the behavior; specifically keep `explaining-step-by-step` for requesting progressive explanations.

## CONVENTIONS
