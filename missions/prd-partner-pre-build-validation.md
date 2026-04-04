# Mission: Add Pre-Build Validation Phase to PRD Partner Skill

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
Add a mandatory validation phase at the end of PRD Partner that checks every requirement against known technical constraints and flags gaps before implementation starts.

## Background & Trigger
During the portfolio-dashboard BMAD session (April 2026), BMAD architect agent (Winston) ran a coherence validation step that caught 4 gaps between PRD requirements and available data:
1. VPS metrics (CPU/memory) — no DB table existed, needed psutil
2. Agent logs — in systemd journal files, not SQLite
3. Strangler Fig migration status — no DB table, needed static config
4. VPS running cost — not in any DB, needed config constant

These gaps were caught before implementation started — which is the right time to find them. If they had been discovered during story implementation, they would have caused rework or scope changes mid-build.

Omri PRD Partner skill currently stops at requirements — it produces a good PRD but has no step that validates technical feasibility or catches gaps. This is a structural advantage BMAD workflow has over operator-kit current flow.

## BMAD Reference
- Framework: BMAD Method v6.2.2 (https://github.com/bmad-code-org/BMAD-METHOD)
- Agent: Winston (Architect) — bmad-check-implementation-readiness workflow
- What BMAD does: after PRD + architecture + epics, runs an implementation readiness check that validates cohesion across all docs. Catches misalignments before dev starts.
- What we are adapting: a lighter version that happens right after PRD completion, before architecture — checks requirements against stated technical constraints and known data sources
- BMAD version is a separate workflow. Ours should be a phase within PRD Partner to keep operator-kit simpler flow.

## Design Requirements
Add a Validation Gate phase to PRD Partner that triggers after PRD is marked complete:

**Phase triggers when:** PRD has functional requirements, data sources, and tech stack are mentioned or inferable

**What it checks:**
1. For each functional requirement: does a data source/API/table exist that can serve it?
2. For each NFR: is there a concrete technical answer in the stack choices?
3. Are there requirements that assume capabilities not yet built?
4. Are there dependencies on external systems (APIs, DBs, services) that are not confirmed available?

**Output format:**
- [Requirement] -> [Data source / technical answer] (pass)
- [Requirement] -> Gap: [what is missing] -> Proposed resolution: [X] (warning)
- [Requirement] -> Blocker: [no viable path found] (fail)

**Behavior:**
- If all pass -> PRD is implementation-ready
- If warnings -> Present gaps with proposed resolutions, ask Omri to accept or override each
- If fails -> Flag as blocker, do not proceed until resolved
- Resolutions get appended to PRD as a Gap Resolutions section

## Open Decisions

### Decisions:

- **[OPEN] Trigger mechanism**: How does the validation phase start?
  - Option A: Auto-trigger — PRD Partner detects "PRD complete" and immediately runs validation (no user action needed)
  - Option B: Explicit command — user types `/validate` or similar after PRD is done
  - Option C: Prompted transition — PRD Partner asks "PRD looks complete. Run validation gate?" and waits for yes/no
  - Resolution: _[TBD]_

- **[OPEN] Data source knowledge**: Where does the validator get its knowledge of available data sources?
  - Option A: From the PRD itself — only checks requirements against data sources explicitly mentioned in the PRD
  - Option B: From the PRD + a project-context.md or architecture.md if available — deeper validation
  - Option C: Asks the user to list available data sources/APIs before running validation
  - Resolution: _[TBD]_

- **[OPEN] Gap resolution authoring**: Who writes the proposed resolutions for warnings?
  - Option A: The skill proposes resolutions based on patterns it knows (e.g., "add config constant", "add psutil call")
  - Option B: The skill only identifies gaps — Omri writes all resolutions
  - Option C: Skill proposes, Omri can accept/modify/reject each one individually
  - Resolution: _[TBD]_

- **[OPEN] Blocker escalation path**: When a true blocker is found (no viable path), what happens to the PRD workflow?
  - Option A: PRD Partner halts and refuses to finalize — user must resolve blocker or remove the requirement
  - Option B: PRD Partner flags it but allows finalization with a visible "UNRESOLVED BLOCKER" warning
  - Option C: Blocker gets auto-added to a "Known Risks" section in the PRD — acknowledged but not blocking
  - Resolution: _[TBD]_

- **[OPEN] Validation persistence**: Where do validation results live after the phase completes?
  - Option A: Appended to the PRD as a "## Validation Results" section — co-located with requirements
  - Option B: Separate file (e.g., `validation-results.md`) — keeps PRD clean
  - Option C: Inline annotations on each requirement in the PRD — most granular but changes PRD structure
  - Resolution: _[TBD]_

## Acceptance Criteria
- PRD Partner SKILL.md updated with validation phase documentation
- Phase activates automatically after PRD completion (not as optional step)
- Output format matches the pass/warning/fail structure above
- Gap resolutions are written back into PRD as a named section
- Works for both technical projects (check DB/API backing) and product features (check dependency on unbuilt systems)
- Tested against portfolio-dashboard PRD — should catch the same 4 gaps Winston found

## Out of Scope
- NOT a full architecture review — lightweight validation only (architecture is system-architect job)
- Does NOT generate implementation plans or stories from gaps — stops at resolution proposals
- Does NOT require codebase access — validates against stated tech stack and data sources in the PRD
- Does NOT replace BMAD implementation readiness check — lighter, PRD-scoped version only
- Does NOT validate NFRs against benchmarks (e.g., < 200ms response time) — checks existence of technical answer only

## Verification
- Run against portfolio-dashboard PRD with its stated tech stack (React/FastAPI, SQLite with portfolio.db + michael_supervisor.db)
- Verify output catches at least 3 of 4 known gaps: VPS metrics (no DB table), agent logs (in journal not SQLite), Strangler Fig status (no DB table), VPS cost (not in any DB)
- Verify pass items include at least 5 requirements that DO have data backing (e.g., portfolio positions to portfolio.db tables)
- Verify gap resolutions section is appended to PRD output
- Verify phase triggers automatically — no manual invocation needed after PRD completion

## Reference Implementation
- `prd-partner/SKILL.md` — the skill being modified; new phase integrates into existing workflow
- BMAD bmad-check-implementation-readiness workflow — for validation pattern inspiration

## Effort: M
