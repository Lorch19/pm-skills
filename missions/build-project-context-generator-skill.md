# Mission: Build Project Context Generator Skill

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
Create a skill that produces a `project-context.md` file — the implementation consistency doc that makes AI-generated code coherent across Claude Code sessions.

## Background & Trigger
During the portfolio-dashboard BMAD session (April 2026), Winston (BMAD architect agent) produced a detailed implementation patterns section as part of the architecture workflow. This doc covered:
- Naming conventions (snake_case API keys, PascalCase components, camelCase hooks)
- Boundary rules (SQL only in db/, HTTP only in api/, no leaking between layers)
- Anti-patterns (no camelCase transform layer, no envelope wrappers, no ORM, no Redux)
- Enforcement guidelines (8 explicit rules all AI agents MUST follow)

This doc is what makes every story implementation consistent — when Claude Code picks up a new story, it reads project-context.md and knows exactly how to write code that matches everything else. Without it, each session drifts.

Omri currently has no skill or workflow that produces this artifact. It is a critical gap for his Claude Code-based side project builds.

## BMAD Reference
- Framework: BMAD Method v6.2.2 (https://github.com/bmad-code-org/BMAD-METHOD)
- Agent: Winston (Architect) + `bmad-generate-project-context` workflow
- The BMAD project-context.md lives at `_bmad-output/project-context.md`
- BMAD version covers: technical preferences, implementation rules, conventions, constraints
- What BMAD does: generates project-context after architecture is complete, feeds it to every downstream dev agent session
- What operator-kit should do better: BMAD project-context is generic. Ours should start with Omri known defaults pre-populated and only ask for project-specific overrides.

## Skill Design Requirements
The skill should:
1. **Trigger** after architecture decisions are made (or after PRD for smaller projects)
2. **Accept** the architecture doc and PRD as input (or ask for them)
3. **Pre-populate** with Omri known stack defaults:
   - Python: snake_case, raw SQL, parameterized queries, no ORM, uv, FastAPI, uvicorn
   - TypeScript/React: PascalCase components, camelCase hooks/utils, TanStack Router + Query
   - Testing: co-located frontend tests, separate api/tests/ directory
   - Dates: ISO 8601 everywhere
   - Errors: inline per component, no global toast for data errors
   - DB: always ?mode=ro, dependency injection pattern
4. **Ask** only for project-specific overrides (not re-ask what is already known)
5. **Produce** a single `project-context.md` with:
   - Stack summary
   - Naming conventions (with examples)
   - File/folder structure rules
   - Boundary rules (what lives where, what never crosses)
   - Anti-patterns list
   - Enforcement guidelines (numbered, imperative)
6. **Format** for Claude Code consumption — concise, scannable, no prose fluff

## Open Decisions

### Decisions:

- **[OPEN] Output file location**: Where does project-context.md get written?
  - Option A: Project root (e.g., `./project-context.md`) — simple, discoverable
  - Option B: Inside docs/ (e.g., `./docs/project-context.md`) — keeps root clean
  - Option C: Inside `.claude/` — co-located with other Claude Code config
  - Resolution: _[TBD]_

- **[OPEN] Relationship to CLAUDE.md**: project-context.md overlaps with CLAUDE.md (both tell agents how to code). What's the boundary?
  - Option A: project-context.md is standalone — agents read it directly, no duplication in CLAUDE.md
  - Option B: project-context.md content gets merged INTO CLAUDE.md as a section — single source of truth
  - Option C: CLAUDE.md references project-context.md via include/pointer — separation but linked
  - Resolution: _[TBD]_

- **[OPEN] Handling unknown stacks**: What if the project uses a stack Omri has no defaults for (e.g., Go, Rust, Swift)?
  - Option A: Skill refuses — only works for known stacks (Python, TypeScript/React)
  - Option B: Skill falls back to asking all questions from scratch (no pre-population)
  - Option C: Skill provides generic defaults and asks for everything stack-specific
  - Resolution: _[TBD]_

- **[OPEN] Override persistence**: When Omri overrides a default for a specific project, where does that override live?
  - Option A: Only in the generated project-context.md — no memory across projects
  - Option B: Overrides get written back to a defaults file in operator-kit — learned preferences
  - Option C: Overrides tracked in the project's CLAUDE.md — per-project memory
  - Resolution: _[TBD]_

- **[OPEN] Partial regeneration**: If the project evolves and conventions change, can the skill update an existing project-context.md without losing manual edits?
  - Option A: Full regeneration only — manual edits get overwritten (simple, predictable)
  - Option B: Diff-aware update — detects manually added sections and preserves them
  - Option C: No update support — generate once, then hand-edit forever
  - Resolution: _[TBD]_

## Acceptance Criteria
- Skill exists in operator-kit with correct routing
- Given architecture.md + PRD, produces project-context.md in under 2 exchanges
- Output is immediately usable as Claude Code project context (drop-in)
- Omri known defaults are pre-populated, not asked again
- Works standalone (no BMAD installation required)

## Out of Scope
- NOT a full BMAD installation or dependency — standalone skill only
- NOT an architecture design tool (that is the system-architect mission)
- Does NOT generate CLAUDE.md or STATE.md — only project-context.md (context-management handles the rest)
- Does NOT auto-detect stack from codebase — takes architecture doc as input

## Verification
- Run the skill against the portfolio-dashboard architecture.md + PRD
- Verify output contains all required sections: stack summary, naming conventions, file/folder rules, boundary rules, anti-patterns, enforcement guidelines
- Verify Omri defaults (snake_case Python, PascalCase React, raw SQL, no ORM) appear without being asked
- Diff output against BMAD _bmad-output/project-context.md — should cover the same categories with less generic prose

## Reference Implementation
- `prd-partner/SKILL.md` — structured doc generation from inputs, multi-mode output, pre-populated defaults
- Deviation: simpler than PRD Partner — single output mode, fewer exchanges needed

## Effort: M
