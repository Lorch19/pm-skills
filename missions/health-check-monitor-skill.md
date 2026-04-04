# Mission: Create health-check-monitor Skill

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
Unified cross-project health monitoring that sends a single digest instead of scattered per-project alerts.

## Problem
Currently health is checked ad-hoc or per-project:
- portfolio-system: manual run_health_check.py, VPS pipeline health in context-sync
- WatchTogether: Railway health endpoint /api/health
- Scheduled tasks: no visibility into success/failure rates
- No unified view — issues can go unnoticed, especially since portfolio-system handles real money

## What the skill should do

### Checks (all optional, configured per-project)
1. **VPS pipeline health** — SSH to VPS, check latest log, count open positions, verify cron is running
2. **Railway deployment** — curl health endpoint, check response
3. **Scheduled task health** — list tasks, flag any that have not run when expected
4. **Supabase health** — check edge function response (for first-bloom, lorchprotfoliotracker)
5. **Git freshness** — flag repos with uncommitted changes older than 3 days

### Output
Single Telegram message with:
- Green/red status per project
- Any issues requiring attention
- Time since last successful check

### Implementation
Could be a scheduled task running daily at ~09:00 IST, or an on-demand skill triggered manually.

### Skill location
operator-kit/meta-tools/health-check-monitor/SKILL.md

## Open Decisions

### Decisions:

- **[OPEN] Execution model**: How does this run?
  - Option A: Scheduled task only — runs daily via `mcp__scheduled-tasks`, sends Telegram digest automatically
  - Option B: On-demand skill only — Omri invokes it manually when he wants a health check
  - Option C: Both — scheduled task for daily digest + on-demand invocation for ad-hoc checks
  - Resolution: _[TBD]_

- **[OPEN] Project config location**: Where is the per-project check configuration stored?
  - Option A: Hardcoded in the SKILL.md itself — simple but requires skill edits to add/remove projects
  - Option B: Separate config file (e.g., `health-checks.json` in operator-kit) — decoupled, easy to maintain
  - Option C: Derived from STATE.md/CLAUDE.md of each registered project — auto-discovers but fragile
  - Resolution: _[TBD]_

- **[OPEN] Telegram bot reuse**: Which Telegram bot/chat sends the digest?
  - Option A: Reuse portfolio-system's existing Telegram bot and chat ID
  - Option B: Create a dedicated "ops-monitor" bot for health checks (separation of concerns)
  - Option C: Use the same bot but a different chat/channel for ops vs portfolio alerts
  - Resolution: _[TBD]_

- **[OPEN] Partial failure handling**: What if some checks succeed and others fail (e.g., SSH timeout to VPS but Railway is fine)?
  - Option A: Send digest with whatever succeeded + explicit "UNREACHABLE" for failed checks
  - Option B: Retry failed checks once after 30s, then report
  - Option C: Send partial digest immediately, retry failures separately, send follow-up if status changes
  - Resolution: _[TBD]_

- **[OPEN] "Last successful check" tracking**: The output includes "time since last successful check" — where is this state stored?
  - Option A: No persistent state — each run is stateless, "last check" means "this run"
  - Option B: Write last-check timestamps to a file on VPS (e.g., `/home/ubuntu/.health-check-state.json`)
  - Option C: Track in operator-kit STATE.md — visible but adds noise to project state
  - Resolution: _[TBD]_

## Acceptance Criteria
- Checks are modular — each project configures which checks apply
- Single Telegram digest (not one message per project)
- Clear green/red status with actionable next steps for red items
- Runs in under 60 seconds

## Out of Scope
- NOT a real-time alerting system — batch digest only (daily or on-demand)
- Does NOT remediate issues — reports only, human decides next steps
- Does NOT monitor application-level metrics (response times, error rates) — infrastructure health only
- Does NOT replace per-project health checks — aggregates and unifies them
- Does NOT store historical health data — each run is stateless

## Verification
- Run against portfolio-system (VPS with known-good state) — verify green status appears
- Run with a deliberately failing check (e.g., wrong SSH host) — verify red status with actionable message
- Verify Telegram digest format: single message, green/red per project, timestamp
- Verify total execution time < 60 seconds with 3+ projects configured
- Verify modular config: adding/removing a project check does not require code changes

## Reference Implementation
- `meta-tools/health-check-monitor/SKILL.md` — the skill itself (if already built; validate against this mission requirements)
- `meta-tools/automation-planner/SKILL.md` — for safety guard patterns (timeouts, circuit breakers)

## Effort: M (2-3 hours)
