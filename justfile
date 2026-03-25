sync_flags := "--restow -v"
clean_flags := "--delete -v"
target := env('HOME') + "/.agents/skills"

# Default behavior: show available recipes instead of mutating state.
[default]
list:
    @just --list

# Install (symlink) local skills into ~/.agents/skills.
install:
    mkdir -p {{ target }}
    stow {{ sync_flags }} -t {{ target }} skills

# Clean only when target exists to avoid noisy first-run errors.
clean:
    if [ -d {{ target }} ]; then stow {{ clean_flags }} -t {{ target }} skills; else echo "skip clean: {{ target }} does not exist"; fi
