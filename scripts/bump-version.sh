#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/bump-version.sh <major|minor|patch>

Reads the latest git tag matching major.minor.patch, bumps the requested
segment, and creates a new lightweight git tag named <major.minor.patch>.

If no matching tag exists, starts from 0.0.0.
USAGE
}

if [[ $# -ne 1 ]]; then
  usage >&2
  exit 2
fi

bump="$1"

case "${bump}" in
  major | minor | patch) ;;
  *)
    echo "Unsupported bump: ${bump}" >&2
    usage >&2
    exit 2
    ;;
esac

git fetch --tags --force

latest_version="$({
  git tag --list '[0-9]*.[0-9]*.[0-9]*' --sort=v:refname \
    | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' \
    | tail -n 1
} || true)"

if [[ -z "${latest_version}" ]]; then
  latest_version="0.0.0"
fi

IFS=. read -r major minor patch <<< "${latest_version}"

case "${bump}" in
  major)
    major=$((major + 1))
    minor=0
    patch=0
    ;;
  minor)
    minor=$((minor + 1))
    patch=0
    ;;
  patch)
    patch=$((patch + 1))
    ;;
esac

next_version="${major}.${minor}.${patch}"

if git rev-parse -q --verify "refs/tags/${next_version}" >/dev/null; then
  echo "Tag ${next_version} already exists" >&2
  exit 1
fi

git tag "${next_version}"

echo "latest_version=${latest_version}"
echo "next_version=${next_version}"

if [[ -n "${GITHUB_OUTPUT:-}" ]]; then
  {
    echo "latest_version=${latest_version}"
    echo "next_version=${next_version}"
  } >> "${GITHUB_OUTPUT}"
fi
