---
name: security-guidance
description: Security reminder hook that warns about potential security issues when editing files, including command injection, XSS, eval, pickle, SQL injection, and unsafe code patterns. Install as a PreToolUse hook to get automatic security warnings during development.
---

# Security Guidance Hook

A PreToolUse hook that monitors file edits for 9 common security anti-patterns and blocks with warnings.

## Patterns Detected

| Pattern | Risk | Safe Alternative |
|---------|------|-----------------|
| `child_process.exec()` | Command injection | Use `execFile()` with argument arrays |
| `new Function()` | Code injection | Alternative design patterns |
| `eval()` | Arbitrary code execution | `JSON.parse()` or alternatives |
| `dangerouslySetInnerHTML` | XSS | Sanitize with DOMPurify |
| `document.write()` | XSS | `createElement()` + `appendChild()` |
| `.innerHTML =` | XSS | `textContent` or DOMPurify |
| `pickle` | Arbitrary code execution | JSON serialization |
| `os.system` | Command injection | Static arguments only |
| SQL string interpolation | SQL injection | Parameterized queries |

## Installation

Add to your `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /path/to/operator-kit/meta-tools/security-guidance/hooks/security_reminder_hook.py"
          }
        ]
      }
    ]
  }
}
```

## How It Works

- Fires on every Edit, Write, or MultiEdit tool call
- Checks file content against 9 security patterns
- Exit code 0 = allow (no pattern found)
- Exit code 2 = block and warn Claude (pattern found)
- Disable with `ENABLE_SECURITY_REMINDER=0` environment variable
