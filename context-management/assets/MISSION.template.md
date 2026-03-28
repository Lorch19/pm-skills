# Mission: [Title]

<!-- WHEN DOES A TASK BECOME A MISSION? -->
<!-- - Touches 3+ files → mission -->
<!-- - Has architectural implications → mission -->
<!-- - Requires multi-step verification → mission -->
<!-- - Could break existing behavior → mission -->
<!-- - Simple single-file change → stays in BACKLOG.md only -->

## Goal
[1-2 sentences: what success looks like]

## Context
[Why this matters. What triggered this work. Link to relevant backlog item.]

## Impact Assessment
- **Files to modify:** [list]
- **Files to create:** [list]
- **Risk level:** [low/medium/high — what could break?]
- **Dependencies:** [other tasks, libraries, approvals needed]

## Steps
1. [Step with enough detail to execute without guessing]
2. [Step]
3. [Step]

## Acceptance Criteria
- [ ] [Specific, testable criterion]
- [ ] [Criterion]
- [ ] All existing tests pass
- [ ] Changes documented in STATE.md if significant

## Review Plan
- **Domain logic involved?** [yes/no — if yes, adversarial review required before shipping]
- **Adversarial questions:** [What are 2-3 ways this change could break or produce wrong results?]
- **Pre/post diff needed?** [yes/no — does this change system outputs that should be compared?]
- **LESSONS.md checked for:** [which prior burns are relevant to this mission?]

## Notes
- [Implementation decisions, constraints, references to existing patterns]
