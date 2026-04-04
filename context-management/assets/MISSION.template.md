# Mission: [Title]

## Status: DRAFT

<!--
Status rules:
- DRAFT: Has [OPEN] decisions. Cannot be executed.
- READY: All decisions [RESOLVED]. Can be picked up by an agent.
- IN_PROGRESS: Agent is executing.
- DONE: Verification passed.

EXECUTION GATE: If status is DRAFT, the executing agent MUST refuse to start
and instead list the unresolved decisions.
-->

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

## Open Decisions

<!-- REQUIRED: The creating agent must populate this section using the forcing questions below. -->
<!-- Each decision must be tagged [OPEN] or [RESOLVED]. -->
<!-- The executing agent MUST refuse to start if any [OPEN] decisions remain. -->

### Forcing Questions (run these against the mission scope):

1. **Integration boundaries**: What does this skill touch that it doesn't own?
   - Other skills, external systems, crons, APIs, file paths, config files
   - Each boundary = potential decision about ownership, format, or contract

2. **Conflict scenarios**: What happens when two things disagree?
   - Two versions of a file, stale cache, partial failure, race conditions
   - Each conflict needs an explicit resolution policy

3. **Trigger & lifecycle**: What starts this? What stops it? What if it fails mid-run?
   - Manual vs automated, frequency, retry policy, idempotency
   - If the mission doesn't specify, the agent WILL guess wrong

4. **Opinionated defaults**: Where would two competent engineers make different choices?
   - File format, naming convention, directory structure, verbosity level
   - If reasonable people disagree, it's a decision — not an implementation detail

5. **Blast radius**: What breaks if this skill does the wrong thing?
   - Overwrites, data loss, service disruption, security implications
   - Higher blast radius = decision MUST be resolved before execution

### Decisions:

- **[OPEN/RESOLVED] Decision title**: Description of the choice to make.
  - Option A: ...
  - Option B: ...
  - Resolution: _[filled by human]_

## Acceptance Criteria
- [ ] [Specific, testable criterion]
- [ ] [Criterion]
- [ ] All existing tests pass
- [ ] Changes documented in STATE.md if significant

## Out of Scope
- [What this mission explicitly does NOT cover]
- [Adjacent work that should be a separate mission]
- [Technology or approach explicitly NOT being used]

## Verification
- [Concrete command, comparison, or test the agent runs to confirm the skill works]
- [Expected output or diff to validate against]
- Must be executable without human judgment — binary pass/fail

## Reference Implementation
- [Path to an existing skill in operator-kit to use as structural template]
- [Any deviations from the reference to note]

## Effort: [S / M / L]

## Review Plan
- **Domain logic involved?** [yes/no — if yes, adversarial review required before shipping]
- **Adversarial questions:** [What are 2-3 ways this change could break or produce wrong results?]
- **Pre/post diff needed?** [yes/no — does this change system outputs that should be compared?]
- **LESSONS.md checked for:** [which prior burns are relevant to this mission?]

## Notes
- [Implementation decisions, constraints, references to existing patterns]
