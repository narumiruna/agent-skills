# Conventional Commits Reference

## Core Format

Use this structure:

```text
<type>[optional scope][!]: <description>

[optional body]

[optional footer(s)]
```

Rules:

- Start with a lowercase type such as `feat`, `fix`, `docs`, or `refactor`.
- Add an optional scope in parentheses when it clarifies which area changed.
- Place `!` immediately before `:` to mark a breaking change in the title.
- Put the description immediately after `: `.
- Separate the body from the title with one blank line.
- Separate footers from the body with one blank line.

## Type Selection

- `feat`: add a new feature or capability
- `fix`: patch a bug or incorrect behavior
- `docs`: change documentation only
- `refactor`: restructure code without intended behavior change
- `perf`: improve performance
- `test`: add or update tests
- `build`: change build tooling or packaging
- `ci`: change CI configuration or automation
- `style`: change formatting without behavior impact
- `chore`: maintenance work that does not fit the above
- `revert`: revert an earlier change

If one change honestly fits several types, prefer splitting it into multiple commits.

## Scope Guidance

Use a short noun-like scope only when it adds signal:

- `feat(api): add webhook retry configuration`
- `fix(parser): reject trailing commas in strict mode`

Avoid broad or unstable scopes such as `misc`, `stuff`, or full file paths unless the repo already standardizes on them.

## Body Guidance

Use the body for context the title cannot carry:

- why the change was needed
- what constraint or edge case shaped the implementation
- what tradeoff or follow-up the reader should know

Multi-paragraph bodies are valid when the extra detail matters.

## Footer Guidance

Footers follow git-trailer style. Common examples:

- `Refs: #123`
- `Reviewed-by: Z`
- `Co-authored-by: Name <email@example.com>`

`BREAKING CHANGE:` is a special footer token and must be uppercase.

## Breaking Changes

Mark a breaking change with either:

- `!` in the title, such as `feat(api)!: remove v1 session endpoint`
- a footer, such as `BREAKING CHANGE: session tokens now expire after 15 minutes`
- or both

Use a `BREAKING CHANGE:` footer when the impact or migration path needs more than the title can say.

## SemVer Mapping

- `fix` maps to a patch release
- `feat` maps to a minor release
- any commit with a breaking change maps to a major release

Other types do not imply a version bump unless they include a breaking change.

## Examples

```text
docs: correct spelling of changelog
```

```text
feat(lang): add Polish language
```

```text
fix: prevent racing of requests

Introduce a request id and track the latest request so stale responses
can be ignored safely.

Refs: #123
```

```text
feat!: drop support for Node 6

BREAKING CHANGE: use JavaScript features not available in Node 6.
```
