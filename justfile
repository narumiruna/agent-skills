sync_flags := "--restow -v"
clean_flags := "--delete -v"
target := env('HOME') + "/.codex/skills"

# Default behavior: show available recipes instead of mutating state.
[default]
list:
    @just --list

# Install (symlink) all local skills into ~/.codex/skills.
install-all:
    mkdir -p {{ target }}
    stow {{ sync_flags }} -t {{ target }} skills

# Install (symlink) a single local skill into ~/.codex/skills/<skill>.
install skill:
    test -d skills/{{ skill }}
    mkdir -p {{ target }}/{{ skill }}
    stow {{ sync_flags }} -d skills -t {{ target }}/{{ skill }} {{ skill }}

# Clean all local skill symlinks only when target exists.
clean-all:
    if [ -d {{ target }} ]; then stow {{ clean_flags }} -t {{ target }} skills; else echo "skip clean: {{ target }} does not exist"; fi

# Clean a single local skill symlink only when its target exists.
clean skill:
    test -d skills/{{ skill }}
    if [ -d {{ target }}/{{ skill }} ]; then stow {{ clean_flags }} -d skills -t {{ target }}/{{ skill }} {{ skill }}; else echo "skip clean: {{ target }}/{{ skill }} does not exist"; fi
