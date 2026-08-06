---
name: using-codebase-memory-cli
description: Index and explore codebases with the `codebase-memory-mcp` command-line interface for graph-first symbol search, call and data-flow tracing, source snippets, architecture, Cypher queries, and change impact. Use proactively for non-trivial code discovery, architecture exploration, relationship tracing, or change-impact analysis whenever the CLI is installed, and whenever the user or repository requests codebase-memory; never start or use an MCP server.
---

# Using Codebase Memory CLI

Use codebase-memory proactively as the default discovery path for unfamiliar or non-trivial code. Prefer its graph over grep, globbing, or broad file reads for symbols, relationships, architecture, and impact analysis, even when the user does not name the tool. Skip it for a known small file, a literal or configuration search, or when `command -v codebase-memory-mcp` shows that the CLI is unavailable.

Do not start the MCP server, call MCP graph tools, or configure an agent to use them. Every graph operation must have the form `codebase-memory-mcp cli <tool> ...`; never run bare `codebase-memory-mcp`, because that starts the stdio server.

## Establish the Index

1. Run `command -v codebase-memory-mcp`, `codebase-memory-mcp --version`, and the narrowest relevant help: `codebase-memory-mcp cli <tool> --help`.
2. Run `codebase-memory-mcp cli list_projects` and match the target by `root_path`, not only by project name.
3. Run `index_status` for an existing project. Compare its root and Git HEAD with the target repository; re-index when it is absent or stale. If semantic search is required and the existing index mode is unknown, re-index with an explicit semantic-capable mode.
4. Use `index_repository` with an explicit repository path. Prefer `fast` for ordinary structural discovery, `moderate` when semantic search is needed with filtered files, and `full` only when excluded files or complete semantic coverage justify the extra work. Do not enable persistence unless a repository artifact was requested.

Read [references/commands.md](references/commands.md) when choosing flags, structured input, index modes, or a less common tool.

## Discover Graph-First

Use this order, stopping when the required evidence is sufficient:

1. `search_graph` to locate functions, methods, classes, interfaces, routes, channels, or other symbols. Start with `--query`; use `--name-pattern` or `--qn-pattern` for regex-like identifier matching. Do not combine `--query` with `--name-pattern`, because the query takes precedence.
2. `trace_path` to find inbound callers, outbound callees, parameter data flow, or cross-service paths. Resolve ambiguous short names with search results before trusting a trace.
3. `get_code_snippet` with the returned `qualified_name` to inspect exact source and optional immediate neighbors.
4. `query_graph` only for relationships or aggregations the focused tools cannot express. Run `get_graph_schema` first and build Cypher from the reported labels, properties, and edge types.
5. `get_architecture` for a high-level or path-scoped view, not as a substitute for focused symbol evidence.

Use `search_graph` pagination while `has_more` is true when completeness matters. Semantic queries require a `moderate` or `full` index and an array of keywords.

Treat graph results as discovery evidence rather than infallible source truth. For critical behavior, verify the reported file, lines, snippet, and relevant tests or runtime evidence. Report unresolved ambiguity, filtered paths, stale index state, or missing edges instead of filling gaps by inference.

## Fallback and Change Impact

- Use CLI `search_code` for literals, error text, regexes, and exact source patterns that are a poor fit for symbol search.
- Fall back to repository `rg`, `find`, or file reads for non-code files, generated or excluded paths, or when graph results remain insufficient. State why the fallback was needed.
- Use `detect_changes` to identify symbols affected by the working tree or a requested Git range. Re-index before relying on subsequent graph exploration if source has changed since the index was built.

## CLI and Safety Boundaries

Prefer flags for simple values and piped JSON or `--args-file` for arrays and complex values. Positional raw JSON is deprecated. Parse stdout as JSON; initialization logs may appear on stderr. Inspect installed help rather than assuming remembered flags or schemas.

Indexing without persistence is an expected local operation for an authorized discovery task. `delete_project`, persisted indexing, ADR updates, and trace ingestion are state-changing or potentially sensitive operations: perform them only when explicitly requested, after checking their installed help and exact target. Do not run `install`, agent integration setup, or server configuration as part of this workflow.

Conclude with the project and index mode used, the relevant symbols and file/line evidence, any fallback performed, and material coverage limits. Do not leave a temporary test index behind unless the user wants to reuse it.
