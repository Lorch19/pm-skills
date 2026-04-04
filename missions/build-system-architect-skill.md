# Mission: Build System Architect Skill

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
Create a System Architect skill for operator-kit that does what BMAD Winston agent does — but with full domain context from Omri existing skills baked in.

## Background & Trigger
During the portfolio-dashboard build session (April 2026), Omri used BMAD Method architect agent (Winston) to design the architecture for a React/FastAPI monitoring dashboard for his autonomous investment system. Winston structured workflow added clear value that operator-kit could not replicate:

1. **Codebase exploration** — Winston read the actual portfolio-system repo, found both SQLite DBs (portfolio.db with 28 tables, michael_supervisor.db with 5 tables), identified existing patterns (DataBridge ?mode=ro, ReportAssembler, CLI --json output) and used them to inform architectural decisions.
2. **Requirements-to-schema mapping** — Winston mapped every PRD tab to specific DB tables and columns (e.g., scout_candidates, sim_positions, arena_decisions, rejection_log).
3. **Gap detection** — Winston found 4 gaps where PRD requirements had no DB backing (VPS metrics, agent logs, Strangler Fig status, VPS cost) and proposed concrete resolutions before implementation started.
4. **Implementation patterns doc** — Winston produced naming conventions, boundary rules, anti-patterns, and enforcement guidelines that every downstream Claude Code session must follow for consistency.

## BMAD Reference
- Framework: BMAD Method v6.2.2 (https://github.com/bmad-code-org/BMAD-METHOD)
- Agent: Winston (Architect) — bmad-agent-architect, trigger CA
- Workflow: bmad-create-architecture
- What to study/adapt: The architecture workflow forces: (1) project scan, (2) starter evaluation with web research, (3) decision-by-decision walkthrough with explicit options + trade-offs, (4) coherence validation against real codebase, (5) gap identification with resolutions
- What BMAD does better: The structured sequential workflow ensures the validation step always happens.
- What operator-kit should do better: BMAD Winston has zero domain knowledge. The operator-kit architect skill should be aware of Omri tech stack preferences, infrastructure, and side project patterns.

## Skill Design Requirements
The skill should:
1. **Trigger** on requests to design architecture for a new project or major feature
2. **Start** by reading the target codebase (or asking for the path) to understand existing patterns, schemas, and data models
3. **Map** every PRD/requirements item to a concrete technical answer (table, API, file, config)
4. **Flag gaps** where no backing exists and propose resolutions before proceeding
5. **Produce** two artifacts:
   - architecture.md — stack decisions, component structure, data flow, deployment model
   - project-context.md — naming conventions, boundary rules, anti-patterns, enforcement guidelines for Claude Code
6. **Enforce** Omri known preferences unless explicitly overridden:
   - Backend: Python/FastAPI, raw sqlite3, no ORMs, uv for package management
   - Frontend: React/TypeScript, Vite, Tailwind v4, shadcn/ui, TanStack Router + Query
   - Deployment: Vercel (frontend) + Hetzner VPS (backend), systemd + nginx
   - Patterns: parameterized SQL, read-only DB connections, no global state managers

## Open Decisions

### Decisions:

- **[OPEN] Skill location**: Where does this skill live in operator-kit?
  - Option A: `meta-tools/system-architect/SKILL.md` — consistent with other meta-tools
  - Option B: Top-level `system-architect/SKILL.md` — parallel to prd-partner (which is also top-level)
  - Option C: `pm-frameworks/system-architect/SKILL.md` — alongside other PM workflow tools
  - Resolution: _[TBD]_

- **[OPEN] Overlap with project-context-generator**: Both this skill and the project-context-generator produce project-context.md. How do they coexist?
  - Option A: Architect skill always produces project-context.md as part of its output (generator skill is redundant for architect users)
  - Option B: Architect skill produces architecture.md only, then explicitly calls the generator skill for project-context.md
  - Option C: Architect skill produces a "raw" context section, generator skill formats it into the standard project-context.md
  - Resolution: _[TBD]_

- **[OPEN] Codebase access model**: How does the skill read the target codebase when running in claude.ai vs Claude Code?
  - Option A: Require Claude Code only — skill uses filesystem tools to read the codebase directly
  - Option B: Accept a pasted codebase summary — works in claude.ai but loses depth
  - Option C: Two-mode design — deep mode (Claude Code with filesystem) and light mode (claude.ai with pasted context)
  - Resolution: _[TBD]_

- **[OPEN] Gap resolution authority**: When the skill finds a gap (requirement with no data backing), who decides the resolution?
  - Option A: Skill proposes resolution, Omri must approve each one before the architecture doc is finalized
  - Option B: Skill proposes and auto-accepts resolutions that match established patterns (e.g., "add config constant"), only escalates novel gaps
  - Option C: Skill lists all gaps but does NOT propose resolutions — human fills them in
  - Resolution: _[TBD]_

- **[OPEN] Architecture doc format**: What structure should architecture.md follow?
  - Option A: BMAD format (mirrors Winston's output structure for consistency with existing portfolio-dashboard docs)
  - Option B: Custom operator-kit format (optimized for Omri's workflow, may differ from BMAD)
  - Option C: C4 model-inspired (Context, Containers, Components, Code — industry standard)
  - Resolution: _[TBD]_

## Acceptance Criteria
- Skill file exists in operator-kit with correct routing in NAVIGATOR.md
- Given a PRD and a codebase path, produces architecture.md and project-context.md
- Catches at least the category of gaps Winston found (requirements with no data source)
- Incorporates Omri stack preferences as defaults
- Works in both claude.ai (planning) and Claude Code (implementation support) contexts

## Out of Scope
- NOT a BMAD installation or wrapper — standalone skill that borrows workflow patterns only
- Does NOT generate PRDs (that is prd-partner job) — consumes them as input
- Does NOT produce implementation stories or epics — stops at architecture + project-context
- Does NOT manage deployment infrastructure — documents deployment model only
- Does NOT replace the project-context-generator skill — produces project-context.md as a byproduct of architecture, while the generator skill is a focused standalone tool

## Verification
- Run against portfolio-system repo with the portfolio-dashboard PRD
- Verify architecture.md contains: stack decisions, component structure, data flow, deployment model
- Verify gap detection catches at least 3 of the 4 gaps Winston found (VPS metrics, agent logs, Strangler Fig status, VPS cost)
- Verify project-context.md output matches the project-context-generator skill expected sections
- Verify Omri stack defaults (FastAPI, raw sqlite3, React/Vite/Tailwind, Vercel+Hetzner) appear as defaults

## Reference Implementation
- `prd-partner/SKILL.md` — multi-phase structured workflow with pre-populated defaults and decision points
- BMAD bmad-agent-architect workflow for the sequential validation pattern (scan, evaluate, decide, validate, gaps)
- Deviation: heavier than most skills — needs codebase reading + gap detection phases that prd-partner does not have

## Effort: L
