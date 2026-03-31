---
name: debug
description: Structured debugging session — reproduce, isolate, diagnose, and fix. TRIGGER with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected.
argument-hint: "<error message or problem description>"
---

# /debug

Run a structured debugging session to find and fix issues systematically.

## Workflow

1. **REPRODUCE** — Understand expected vs. actual behavior, exact repro steps, scope
2. **ISOLATE** — Narrow down component/service/code path, check recent changes, review logs
3. **DIAGNOSE** — Form hypotheses, trace code path, identify root cause (not symptoms)
4. **FIX** — Propose fix, consider side effects, suggest regression tests

## What I Need

- Error message or stack trace
- Steps to reproduce
- What changed recently
- Expected vs. actual behavior

## Output

```markdown
## Debug Report: [Issue Summary]

### Reproduction
- **Expected**: [What should happen]
- **Actual**: [What happens instead]
- **Steps**: [How to reproduce]

### Root Cause
[Why the bug occurs]

### Fix
[Code changes or configuration fixes]

### Prevention
- [Test to add]
- [Guard to put in place]
```

## Tips

1. **Share error messages exactly** — Don't paraphrase
2. **Mention what changed** — Recent deploys, dependency updates, config changes
3. **Include context** — "Only affects large payloads" narrows things fast
