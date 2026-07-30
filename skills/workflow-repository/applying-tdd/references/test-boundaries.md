# Test Boundaries

These are explicit policy defaults for this skill, not claims that every project in an ecosystem uses the same layout. More-specific repository instructions may replace a row. Otherwise, apply a listed row exactly; do not substitute another production root because the project uses a different layout.

A work unit enters TDD only when:

1. its production path matches the ecosystem row
2. it passes the behavior gate in `SKILL.md`
3. its test uses only the permitted test-owned inputs

For an unlisted ecosystem, use the general behavior gate until an explicit row is added.

## Boundary List

| Ecosystem | Project boundary | Production behavior eligible for TDD | Test placement and owned inputs |
| --- | --- | --- | --- |
| Python | Nearest ancestor containing `pyproject.toml`, `setup.cfg`, or `setup.py` | Behavior and packaged runtime resources under `src/`; exclude generated and vendored code | Tests under `tests/`; inline builders, `tests/fixtures/`, temporary paths, mocks, and fakes |
| Rust | Nearest ancestor whose `Cargo.toml` defines a package; evaluate each workspace member separately | Behavior and packaged runtime resources under `src/`; exclude generated and vendored code | Unit and documentation tests attached to `src/`; integration tests and fixtures under `tests/`; temporary paths, mocks, and fakes |
| Go | Nearest ancestor containing `go.mod`; evaluate each workspace module separately | Non-test, non-generated `.go` files in packages selected by `go list ./...`; exclude `vendor/` and `testdata/` | Colocated `*_test.go`; the target package's `testdata/`, `t.TempDir()`, mocks, fakes, and local in-process test servers |
| TypeScript | Nearest ancestor containing `package.json`; evaluate each monorepo member separately | Runtime source under `src/` using `.ts`, `.tsx`, `.mts`, or `.cts`; exclude declarations, generated code, tests, fixtures, and mocks | Files discovered by the configured runner; conservative fallback: `tests/**/*.test.{ts,tsx,mts,cts}`; test-owned fixtures, temporary paths, mocks, and fakes |
| JavaScript | Nearest ancestor containing `package.json`; evaluate each monorepo member separately | Runtime source under `src/` using `.js`, `.jsx`, `.mjs`, or `.cjs`; exclude generated code, tests, fixtures, and mocks | Files discovered by the configured runner; conservative fallback: `tests/**/*.test.{js,jsx,mjs,cjs}`; test-owned fixtures, temporary paths, mocks, and fakes |

## Isolation Rules

- Test only behavior provided by the eligible production path. Helpers and fixtures are support code, not the subject under test.
- Exercise a stable interface; do not inspect source text or repeat static source or config values in assertions.
- If eligible behavior normally reads data from outside its production path, recreate the smallest representative input in a permitted fixture location or per-test temporary workspace, then pass or inject it.
- Tests may import ordinary dependencies, but replace external side effects with controlled test doubles or local in-process substitutes.
- Test code must not open or assert against real manifests, lockfiles, tool configuration, scripts, migrations, examples, benchmarks, build output, user files, host environment values, network services, or databases. Build and test tools may still read their own configuration to compile and discover tests.
- A production change outside the listed path is outside TDD. Tests may still be added in the listed test location for eligible production behavior.

## Ecosystem-Specific Rules

### Python

Test `src/package/config.py` with data under `tests/fixtures/` or generated in a temporary directory. Do not read the project's real `pyproject.toml` as test data.

### Rust

Keep focused unit tests in `#[cfg(test)]` modules beside the behavior. Use `tests/` for public integration behavior and documentation tests for documented public examples. Treat `build.rs`, `examples/`, `benches/`, manifests, lockfiles, and `target/` as outside TDD.

### Go

Use the package name when private access is necessary and its `_test` variant when testing only the exported contract. Keep static samples in that package's `testdata/`; the Go tool excludes this directory from normal package discovery. Use `t.TempDir()` for mutable files and `httptest` for HTTP behavior.

### TypeScript and JavaScript

Determine the runner from package scripts and runner configuration before choosing the test filename. Configuration controls discovery, but it is not test data.

- If the runner defines `include`, `testMatch`, or an equivalent matcher, the test must match it.
- Without a custom matcher, Vitest discovers `*.test.*` and `*.spec.*`; Jest discovers those suffixes and supported files under `__tests__/`.
- For another or unknown runner, use the conservative `tests/<behavior>.test.<extension>` fallback and invoke that file explicitly when supported.
- Store static data under a fixture or mock directory owned by the discovered test location; otherwise generate it in a per-test temporary directory.
- TypeScript declaration-only changes such as `.d.ts` are outside TDD; validate them with the configured type checker or type-test tooling.
- Treat package manifests, lockfiles, `tsconfig`, runner and bundler configuration, scripts, distribution output, coverage output, and real browser profiles as outside TDD.

## Outside-TDD Validation

Always run relevant existing tests or a focused smoke check plus the repository gate when available. Add the cheapest ecosystem-specific checks that cover the change:

| Ecosystem | Typical checks |
| --- | --- |
| Python | Parser or schema validation, lint, formatting, type checking, packaging, or build checks |
| Rust | `cargo fmt --check`, `cargo check`, Clippy, or package and workspace builds |
| Go | `gofmt`, `go vet`, package and module builds, migration checks, or generation checks |
| TypeScript | Configuration parsing, lint, formatting, type checking, or package builds |
| JavaScript | Configuration parsing, lint, formatting, package or bundle builds |

## Convention Basis

The `src/` restrictions for Python, TypeScript, and JavaScript are deliberate skill policy defaults. Python's `src` layout is documented but not universal; JavaScript and TypeScript have no single mandatory source layout. Rust and Go locations follow their toolchains more directly. Test discovery must still be verified against the active runner.

- [Python `src` layout versus flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [Cargo package layout](https://doc.rust-lang.org/cargo/guide/project-layout.html)
- [Cargo tests](https://doc.rust-lang.org/cargo/guide/tests.html)
- [Go test packages](https://pkg.go.dev/cmd/go#hdr-Test_packages)
- [Vitest test inclusion](https://vitest.dev/config/include)
- [Jest `testMatch`](https://jestjs.io/docs/configuration#testmatch-arraystring)
- [Node.js test runner](https://nodejs.org/api/test.html#running-tests-from-the-command-line)

Add another ecosystem only when its production scope, test discovery, permitted inputs, and outside-boundary validation can all be defined explicitly.
