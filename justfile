sync_flags := "--restow -v"
clean_flags := "--delete -v"
target := env('HOME') + "/.codex/skills"

[default]
sync:
    stow {{ sync_flags }} -t {{ target }} skills

clean:
    stow {{ clean_flags }} -t {{ target }} skills
