---
name: incident-response
description: Run an incident response workflow — triage, communicate, and write postmortem. TRIGGER with "we have an incident", "production is down", an alert needing severity assessment, a status update mid-incident, or when writing a blameless postmortem.
argument-hint: "<incident description or alert>"
---

# /incident-response

Manage an incident from detection through postmortem.

## Phases

1. **TRIAGE** — Assess severity (SEV1-4), identify affected systems, assign roles
2. **COMMUNICATE** — Internal status update, customer comms, war room cadence
3. **MITIGATE** — Document steps taken, track timeline, confirm resolution
4. **POSTMORTEM** — Blameless postmortem, 5 whys, action items

## Severity Classification

| Level | Criteria | Response Time |
|-------|----------|---------------|
| SEV1 | Service down, all users affected | Immediate |
| SEV2 | Major feature degraded | Within 15 min |
| SEV3 | Minor feature issue | Within 1 hour |
| SEV4 | Cosmetic or low-impact | Next business day |

## Output — Status Update

```markdown
## Incident Update: [Title]
**Severity:** SEV[1-4] | **Status:** Investigating | Identified | Monitoring | Resolved

### Current Status
[What we know now]

### Actions Taken
- [Action 1]

### Next Steps
- [What's happening next and ETA]
```

## Output — Postmortem

```markdown
## Postmortem: [Title]
**Date:** [Date] | **Duration:** [X hours] | **Severity:** SEV[X]

### Summary
[2-3 sentence plain-language summary]

### Impact
- [Users affected, duration, business impact]

### Timeline
| Time (UTC) | Event |
|------------|-------|

### Root Cause
[Detailed explanation]

### 5 Whys
1. Why? → Because...
[Continue to root cause]

### Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
```

## Tips

1. **Start writing immediately** — Update as you learn more
2. **Keep updates factual** — What we know, what we've done, what's next
3. **Postmortems are blameless** — Systems and processes, not individuals
