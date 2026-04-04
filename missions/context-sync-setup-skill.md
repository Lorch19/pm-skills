# Mission: Create context-sync-setup Skill

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

## Goal
Parametrized skill that generates a scheduled context-sync task for any project, following the established pattern.

## Problem
Three projects have context-sync tasks (portfolio-system, linx-advisor, shopagent) but each was created manually with copy-paste-modify. WatchTogether and first-bloom had to wait for this audit to get theirs. New projects should get auto-sync as part of bootstrap.

## Pattern to codify
Source: `~/.claude/scheduled-tasks/portfolio-context-sync/SKILL.md`

All context-sync tasks follow identical structure:
1. Read git log + STATE.md + BACKLOG.md
2. Check external health (optional — VPS, Railway, etc.)
3. Update STATE.md if changed
4. Update BACKLOG.md if changed
5. Skip if nothing changed
6. Rules: read before write, size limits, do not touch CLAUDE.md

### Inputs
- Project name and path
- Optional: health check command (SSH, curl, etc.)
- Cron schedule (default: every 2 days at a staggered minute)
- Notify on completion? (default: false)

### Output
A scheduled task created via mcp scheduled-tasks create_scheduled_task with a complete SKILL.md prompt.

### Skill location
operator-kit/meta-tools/context-sync-setup/SKILL.md

## Open Decisions

### Decisions:

- **[OPEN] Stagger strategy**: How to pick non-colliding cron minutes for new tasks?
  - Option A: Inspect existing tasks at skill runtime, find the next available 15-minute slot
  - Option B: Use a deterministic hash of the project name to assign a minute (no inspection needed)
  - Option C: Let user specify the minute, but warn if it collides with an existing task
  - Resolution: _[TBD]_

- **[OPEN] Idempotency on re-run**: What happens if the skill is run for a project that already has a context-sync task?
  - Option A: Refuse — error out with "task already exists"
  - Option B: Update the existing task with new parameters (destructive overwrite)
  - Option C: Prompt user to confirm overwrite or skip
  - Resolution: _[TBD]_

- **[OPEN] STATE.md size guard**: Existing context-sync tasks have implicit size limits. Should the generated task enforce an explicit max line count for STATE.md?
  - Option A: Hard cap (e.g., 80 lines) — truncate oldest entries if exceeded
  - Option B: Soft warning — flag if STATE.md exceeds threshold but do not truncate
  - Option C: No guard — trust the sync logic to be concise (current behavior)
  - Resolution: _[TBD]_

- **[OPEN] Health check failure behavior**: When the optional health check fails during a sync run, what should happen?
  - Option A: Log the failure in STATE.md and continue with the rest of the sync
  - Option B: Abort the entire sync — do not update STATE.md or BACKLOG.md
  - Option C: Update STATE.md with the health failure as the top item, skip BACKLOG.md update
  - Resolution: _[TBD]_

## Acceptance Criteria
- Generates a working context-sync scheduled task for any project path
- Stagger schedule minutes to avoid concurrent runs (inspect existing tasks first)
- Health check step is optional and parameterized
- Output task follows the exact pattern of existing context-sync tasks

## Out of Scope
- Does NOT run the sync itself — only creates the scheduled task definition
- Does NOT modify CLAUDE.md, STATE.md, or BACKLOG.md directly — the generated task does that
- Does NOT handle project bootstrap (that is the project-bootstrap skill)
- Does NOT monitor task success/failure (that is health-check-monitor job)

## Verification
- Run the skill with a test project path (e.g., first-bloom)
- Verify a scheduled task is created via the scheduled-tasks MCP tool
- Verify the generated SKILL.md prompt contains: git log read, STATE.md read/write, BACKLOG.md read/write, skip-if-unchanged logic
- Diff the generated prompt against portfolio-context-sync/SKILL.md — structure should match
- Verify cron minute is staggered (not colliding with existing tasks)

## Reference Implementation
- `meta-tools/context-sync-setup/SKILL.md` — the skill itself (if already built; validate against this mission requirements)
- Source pattern: `~/.claude/scheduled-tasks/portfolio-context-sync/SKILL.md`

## Effort: S (1 hour)
