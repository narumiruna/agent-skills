---
name: using-codebase-memory-cli
description: Use `codebase-memory-mcp` in CLI-only mode for graph-first codebase indexing, symbol search, call and data-flow tracing, source snippets, architecture, Cypher, and change impact. Use proactively for unfamiliar or non-trivial code discovery, relationship tracing, architecture analysis, or impact work when the CLI is installed, and whenever the user or repository requests codebase-memory; use ordinary repository tools for known-file, literal/config-only, or unsupported-path searches. Never start or configure the MCP server.
---

# Using Codebase Memory CLI

Use the graph to locate structure and relationships before broad file search or reading. It is discovery evidence, not a replacement for source, tests, history, or runtime evidence.

Run graph tools only as `codebase-memory-mcp cli <tool> ...`. `codebase-memory-mcp` with no arguments starts the stdio server; never run it. Do not call MCP graph tools or configure an agent to use them.

Read [the command reference](references/commands.md) only when selecting index modes, constructing structured input, or using a less common tool.

## Establish a Trustworthy Index

1. Check `command -v codebase-memory-mcp`, `codebase-memory-mcp --version`, and `codebase-memory-mcp cli <tool> --help`. If the binary is missing, continue with repository tools and report the lost graph coverage; do not block ordinary discovery on installation.
2. Run `list_projects`. Select a project by its exact `root_path`; for worktrees also verify the reported canonical root, worktree root, branch, and HEAD rather than trusting the derived name.
3. For a match, run `index_status` and compare its root and indexed HEAD with the target repository. Re-index before relying on graph evidence when the root or HEAD differs, when uncommitted source being explored is newer than the index, or when the required index mode cannot be established. In v0.9.0, status does not report the mode or prove working-tree freshness.
4. For a new or stale project, run `index_repository` with an absolute path and an unambiguous name. Default to `fast`; use `moderate` only for semantic/similarity search, `full` only when relevant files filtered by ordinary modes must be included, and `cross-repo-intelligence` only for repositories within the requested scope.
5. Inspect the indexing result. Treat `degraded`, skipped files, exclusions, a mismatched root, or an unexpected node count as coverage limits, not a successful complete index. Omit `--persistence` unless a repository artifact was explicitly requested.

## Query from Narrow to Broad

Stop when evidence is sufficient:

- For a diff or Git range, use `detect_changes` to identify changed files and candidate impacted symbols, then inspect the important paths.
- Use `search_graph --query` for BM25 keyword discovery. Use `--name-pattern` or `--qn-pattern` for identifier matching, with label and file filters where useful; do not combine `--query` with `--name-pattern`, because the query wins. Paginate until `has_more` is false when completeness matters.
- Use semantic search only on a known `moderate` or `full` index. Pass `semantic_query` as an array and evaluate `semantic_results`; ordinary `results` and `total` are separate and can be broad when no structural filter was supplied.
- Use `trace_path` for inbound callers, outbound callees, parameter data flow, or cross-service traversal. Resolve a short or duplicated name through `search_graph`, then pass the returned `qualified_name`; include tests explicitly when they matter.
- Use `get_code_snippet` with that qualified name to inspect the symbol's source and optional neighbors.
- Use `query_graph` only when focused tools cannot express the relationship or aggregation. Run `get_graph_schema` first and constrain the read-only Cypher result.
- Use path-scoped `get_architecture` for a compact overview after focused evidence, not instead of it.

Verify critical claims in the reported source lines and relevant tests or runtime behavior. Missing edges do not prove that no relationship exists. Re-index when later traversal must reflect source changes, and report stale index state, ambiguity, exclusions, skipped files, or unresolved edges instead of inferring through them.

## Fallback and Boundaries

Use CLI `search_code` for exact text or regex within indexed files. Use `rg`, `find`, and targeted reads for non-code, generated, ignored, excluded, changed-but-unindexed, or unsupported files, or when graph results are insufficient. State the material fallback and why it was needed.

Ordinary discovery authorizes an index in the tool's local cache without `--persistence`; it does not authorize repository artifacts or unrelated repositories. `--persistence` additionally writes into the repository. Existing-index deletion, ADR mutation, trace ingestion, cross-repository expansion, native `install`/`update`/`config`, agent integration, and server/UI setup require explicit scope or authorization. A uniquely named temporary index created during the current task may be deleted during cleanup; never delete a pre-existing or reused index without exact approval.

Installation expands scope. Only with explicit approval to download and execute the upstream script, use its binary-only mode because the default configures detected agents:

```sh
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash -s -- --skip-config
```

Verify the installed path and version afterward; do not start the server.

Prefer flags for scalar values and stdin JSON or `--args-file` for arrays and complex input. Positional raw JSON is deprecated. Parse stdout as JSON; initialization and progress logs can appear on stderr. Trust installed help over remembered flags or this version-qualified reference.

Conclude with the matched root/project, known index mode and freshness, decisive symbols and file/line evidence, relevant impact paths, material fallbacks, and coverage limits. Do not claim an unknown reused-index mode or complete coverage.
