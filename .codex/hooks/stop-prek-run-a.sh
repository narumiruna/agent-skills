#!/usr/bin/env bash
set -euo pipefail

input="$(cat)"
stop_hook_active=false
if printf '%s' "$input" | rg -q '"stop_hook_active"[[:space:]]*:[[:space:]]*true'; then
  stop_hook_active=true
fi

repo_root="$(CDPATH= cd -- "$(dirname "$0")/../.." && pwd)"
cache_root="${XDG_CACHE_HOME:-/tmp/codex-prek-cache}"
export XDG_CACHE_HOME="$cache_root"
export PREK_CACHE_DIR="${PREK_CACHE_DIR:-$cache_root/prek}"
export PREK_LOG_FILE="${PREK_LOG_FILE:-$cache_root/prek.log}"
mkdir -p "$PREK_CACHE_DIR"
mkdir -p "$(dirname "$PREK_LOG_FILE")"

if ! output="$(cd "$repo_root" && prek run -a 2>&1)"; then
  if [ -n "$output" ]; then
    printf '%s\n' "$output" >&2
  fi

  if [ "$stop_hook_active" = true ]; then
    printf '%s\n' '{"continue":false,"systemMessage":"`prek run -a` failed after the Stop continuation pass."}'
    exit 0
  fi

  printf '%s\n' '{"decision":"block","reason":"`prek run -a` failed. Inspect the pre-commit output, fix the issues, then stop again."}'
  exit 0
fi

printf '%s\n' '{"continue":false,"systemMessage":"`prek run -a` passed."}'
