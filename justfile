target := env('HOME') + "/.codex/skills"

# Default behavior: show available recipes instead of mutating state.
[default]
list:
    @just --list

# Install all local skills into ~/.codex/skills by copying directories.
install-all:
    mkdir -p {{ target }}
    for dir in skills/*; do [ -d "$dir" ] || continue; name=${dir##*/}; rm -rf "{{ target }}/$name"; cp -R "$dir" "{{ target }}/$name"; done

# Install a single local skill into ~/.codex/skills/<skill> by copying it.
install skill:
    test -d skills/{{ skill }}
    mkdir -p {{ target }}
    rm -rf "{{ target }}/{{ skill }}"
    cp -R "skills/{{ skill }}" "{{ target }}/{{ skill }}"

# Clean all local skill copies managed by this repo when target exists.
clean-all:
    if [ -d {{ target }} ]; then for dir in skills/*; do [ -d "$dir" ] || continue; name=${dir##*/}; if [ -e "{{ target }}/$name" ] || [ -L "{{ target }}/$name" ]; then rm -rf "{{ target }}/$name"; else echo "skip clean: {{ target }}/$name does not exist"; fi; done; else echo "skip clean: {{ target }} does not exist"; fi

# Clean a single local skill copy only when its target exists.
clean skill:
    test -d skills/{{ skill }}
    if [ -e "{{ target }}/{{ skill }}" ] || [ -L "{{ target }}/{{ skill }}" ]; then rm -rf "{{ target }}/{{ skill }}"; else echo "skip clean: {{ target }}/{{ skill }} does not exist"; fi

# Create the next semantic version tag from the latest major.minor.patch tag.
bump-version bump="patch":
    scripts/bump-version.sh {{ bump }}
