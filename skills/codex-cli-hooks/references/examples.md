# Minimal Examples

Use these as starting points. Expand only after the minimal contract works.

## SessionStart: add context on startup or resume

`hooks.json`

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 ~/.codex/hooks/session_start.py",
            "statusMessage": "Loading session notes"
          }
        ]
      }
    ]
  }
}
```

`session_start.py`

```python
#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)
print(
    json.dumps(
        {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": f"Session started from {payload['source']}."
            }
        }
    )
)
```

## PreToolUse: deny destructive Bash commands

`hooks.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ]
  }
}
```

`pre_tool_use.py`

```python
#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)
command = payload["tool_input"]["command"]

if "rm -rf" in command:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": "Blocked destructive command."
                }
            }
        )
    )
```

## PostToolUse: replace raw tool result with feedback

```python
#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)
command = payload["tool_input"]["command"]

if command.startswith("git add "):
    print(
        json.dumps(
            {
                "decision": "block",
                "reason": "Review staged paths before continuing.",
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": "Confirm staging scope is intentional."
                }
            }
        )
    )
```

## UserPromptSubmit: ask for safer framing

```python
#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)

if "production database" in payload["prompt"].lower():
    print(json.dumps({"decision": "block", "reason": "Ask for explicit confirmation first."}))
```

## Stop: force one more pass

```python
#!/usr/bin/env python3
import json
import sys

json.load(sys.stdin)
print(json.dumps({"decision": "block", "reason": "Run one more pass over failing checks."}))
```

## Practical Notes

- Start with one event per file until behavior is proven.
- Prefer repo-local paths resolved from `git rev-parse --show-toplevel`.
- Keep hook output machine-readable; ad hoc logs often make the event look broken.
