# Default behavior: show available recipes instead of mutating state.
[default]
list:
    @just --list

# Create the next semantic version tag from the latest major.minor.patch tag.
bump-version bump="patch":
    scripts/bump-version.sh {{ bump }}
