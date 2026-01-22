STOW       := stow
SYNC_FLAGS := --restow -v
CLEAN_FLAGS := --delete -v
TARGET     := ~/.codex/skills

sync:
	@$(STOW) $(SYNC_FLAGS) -t $(TARGET) skills

clean:
	@$(STOW) $(CLEAN_FLAGS) -t $(TARGET) skills

.PHONY: sync clean
