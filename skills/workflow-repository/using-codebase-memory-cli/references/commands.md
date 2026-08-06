# Codebase Memory CLI Command Shapes

These shapes were verified with `codebase-memory-mcp 0.9.0`. Check `codebase-memory-mcp cli <tool> --help` because flags and output schemas may change.

## Invocation and Input

```sh
codebase-memory-mcp --version
codebase-memory-mcp --help
codebase-memory-mcp cli <tool> --help
codebase-memory-mcp cli <tool> --flag value
codebase-memory-mcp cli <tool> --args-file /tmp/codebase-memory-args.json
printf '%s\n' '{"project":"my-project"}' | codebase-memory-mcp cli index_status
```

Do not use the deprecated positional raw-JSON form. Normal tool output is JSON on stdout; informational initialization logs are written to stderr. Bare `codebase-memory-mcp` starts the MCP stdio server and is forbidden by this skill.

## Projects and Indexing

```sh
codebase-memory-mcp cli list_projects
codebase-memory-mcp cli index_status --project my-project
codebase-memory-mcp cli index_repository \
  --repo-path /absolute/path/to/repository \
  --mode fast \
  --name my-project
```

`--name` is optional; use it to avoid collisions or make worktree identity explicit.

Index modes from installed help:

- `fast`: filtered files, type-aware LSP call/usage resolution, no similarity or semantic edges.
- `moderate`: filtered files plus similarity and semantic edges.
- `full`: all files plus similarity and semantic edges.
- `cross-repo-intelligence`: match routes and channels across projects; pass `--target-projects` as an array.

All modes perform per-file and cross-file type-aware LSP resolution. `--persistence true` writes `.codebase-memory/graph.db.zst` into the target repository; omit it unless that artifact is explicitly wanted.

## Focused Discovery

Keyword or natural-language BM25 search:

```sh
codebase-memory-mcp cli search_graph \
  --project my-project \
  --query 'extension loader' \
  --limit 20 \
  --offset 0
```

Identifier or structural search:

```sh
codebase-memory-mcp cli search_graph \
  --project my-project \
  --name-pattern '.*OrderHandler.*' \
  --label Function \
  --include-connected true \
  --limit 20
```

A supplied `--query` ignores `--name-pattern`. Responses include `total` and `has_more`; increase `offset` by `limit` until complete when exhaustive coverage is required.

Semantic search needs a `moderate` or `full` index. Use structured input so `semantic_query` remains an array:

```sh
printf '%s\n' '{
  "project": "my-project",
  "semantic_query": ["send", "pubsub", "publish"],
  "limit": 20
}' | codebase-memory-mcp cli search_graph
```

Each semantic keyword is scored independently, and semantic matches appear separately under `semantic_results`.

## Tracing and Source

```sh
codebase-memory-mcp cli trace_path \
  --project my-project \
  --function-name OrderHandler \
  --direction inbound \
  --depth 3 \
  --mode calls \
  --risk-labels true \
  --include-tests false

codebase-memory-mcp cli trace_path \
  --project my-project \
  --function-name OrderHandler \
  --direction outbound \
  --depth 3 \
  --mode data_flow \
  --parameter-name order

codebase-memory-mcp cli get_code_snippet \
  --project my-project \
  --qualified-name my-project.pkg.orders.OrderHandler \
  --include-neighbors true
```

Trace modes are `calls`, `data_flow`, and `cross_service`. Cross-service mode follows HTTP, async, data-flow, and available cross-repository edges. When test callers matter, set `--include-tests true` explicitly.

## Schema, Cypher, and Architecture

Inspect the actual graph before writing Cypher:

```sh
codebase-memory-mcp cli get_graph_schema --project my-project

codebase-memory-mcp cli query_graph \
  --project my-project \
  --query "MATCH (n:Function) WHERE n.name = 'OrderHandler' RETURN n.name, n.qualified_name, n.file_path LIMIT 20" \
  --max-rows 20

codebase-memory-mcp cli get_architecture \
  --project my-project \
  --aspects overview

codebase-memory-mcp cli get_architecture \
  --project my-project \
  --path packages/orders \
  --aspects all
```

`query_graph` has no offset pagination; constrain Cypher and `--max-rows`. `search_graph` is the better choice for paginated browsing.

## Literal Search and Change Impact

```sh
codebase-memory-mcp cli search_code \
  --project my-project \
  --pattern 'ORDER_NOT_FOUND' \
  --file-pattern '*.ts' \
  --mode compact \
  --context 2 \
  --limit 20

codebase-memory-mcp cli detect_changes \
  --project my-project \
  --scope all \
  --depth 2

codebase-memory-mcp cli detect_changes \
  --project my-project \
  --since HEAD~5 \
  --depth 2
```

`search_code` modes are `compact`, `full`, and `files`. It reports grep and enriched-result totals but has no offset; narrow the path or file pattern, or raise the limit.

## Non-Discovery Tools

The CLI also exposes `delete_project`, `manage_adr`, and `ingest_traces`. These mutate stored state or may ingest sensitive runtime data. Do not use them during ordinary discovery. If explicitly requested, inspect the installed tool help, confirm the exact project and payload, execute only the approved operation, and verify the resulting state.
