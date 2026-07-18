target := env('HOME') + "/.codex/skills"
active_skills := "find skills -mindepth 3 -maxdepth 3 -type f -name SKILL.md -printf '%h\\n' | sort"

# Default behavior: show available recipes instead of mutating state.
[default]
list:
    @just --list

# Install all local skills into ~/.codex/skills by copying directories.
install-all:
    mkdir -p {{ target }}
    {{ active_skills }} | while read -r dir; do name=${dir##*/}; rm -rf "{{ target }}/$name"; cp -R "$dir" "{{ target }}/$name"; done

# Install a single categorized skill into ~/.codex/skills/<skill> by copying it.
install skill:
    set -- skills/*/{{ skill }}; test "$#" -eq 1; dir=$1; test -f "$dir/SKILL.md"; mkdir -p {{ target }}; rm -rf "{{ target }}/{{ skill }}"; cp -R "$dir" "{{ target }}/{{ skill }}"

# Clean all local skill copies managed by this repo when target exists.
clean-all:
    if [ -d {{ target }} ]; then {{ active_skills }} | while read -r dir; do name=${dir##*/}; if [ -e "{{ target }}/$name" ] || [ -L "{{ target }}/$name" ]; then rm -rf "{{ target }}/$name"; else echo "skip clean: {{ target }}/$name does not exist"; fi; done; else echo "skip clean: {{ target }} does not exist"; fi

# Clean a single local skill copy only when its source and target exist.
clean skill:
    set -- skills/*/{{ skill }}; test "$#" -eq 1; test -f "$1/SKILL.md"; if [ -e "{{ target }}/{{ skill }}" ] || [ -L "{{ target }}/{{ skill }}" ]; then rm -rf "{{ target }}/{{ skill }}"; else echo "skip clean: {{ target }}/{{ skill }} does not exist"; fi

# Create the next semantic version tag from the latest major.minor.patch tag.
bump-version bump="patch":
    scripts/bump-version.sh {{ bump }}
