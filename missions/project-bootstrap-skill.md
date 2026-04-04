# Mission: Create project-bootstrap Skill

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
Build a reusable skill that scaffolds the full context management structure for any new or existing project, eliminating manual setup.

## Problem
Omri has 7 active repos. 5 use the identical CLAUDE.md + STATE.md + BACKLOG.md + docs/ pattern. Setting this up manually each time is error-prone and inconsistent. lorchprotfoliotracker was actively developed for 101 commits before getting context files.

## Scope

### Inputs (parameterized)
- Project name and path
- Tech stack (Python/React/etc.)
- Role description (co-founder CTO, contributor, etc.)
- Database type (SQLite/Supabase/Postgres)
- Deployment target (VPS/Railway/Vercel/none)
- Dev server command and port (for launch.json)

### Outputs
1. CLAUDE.md — from template, with stack-specific sections filled in
2. STATE.md — initial state from git log analysis
3. BACKLOG.md — empty structured template with tiers
4. docs/LESSONS.md — empty template
5. docs/CONTEXT-PROTOCOL.md — standard protocol (reusable across all projects)
6. .claude/launch.json — if dev server provided
7. Optionally: a context-sync scheduled task (uses context-sync-setup skill)

### Templates to extract from
- portfolio-system/CLAUDE.md — gold standard for co-founder persona, session discipline, backlog discipline, lessons loop, context management sections
- lorchprotfoliotracker/CLAUDE.md — freshly created, good example of a simpler project
- context-management/assets/ — existing templates (CLAUDE.template.md, STATE.template.md)

### Skill location
operator-kit/meta-tools/project-bootstrap/SKILL.md

## Open Decisions

### Decisions:

- **[OPEN] CLAUDE.md persona section**: The "co-founder CTO" persona is baked into portfolio-system's CLAUDE.md. Should bootstrap always include it?
  - Option A: Always include the co-founder persona — it is Omri's standard working relationship with Claude
  - Option B: Parametrize the persona — role description input controls which persona template is used
  - Option C: Include a minimal persona by default, let user customize after generation
  - Resolution: _[TBD]_

- **[OPEN] .cursorrules migration strategy**: When retrofitting a project with existing .cursorrules, how to handle conflicts?
  - Option A: Merge .cursorrules content into CLAUDE.md automatically, delete .cursorrules
  - Option B: Merge into CLAUDE.md but keep .cursorrules as a backup (rename to .cursorrules.bak)
  - Option C: Import .cursorrules content into a "Legacy Rules" section in CLAUDE.md, flag for manual review
  - Resolution: _[TBD]_

- **[OPEN] STATE.md initial population depth**: How much git history to analyze for the initial STATE.md?
  - Option A: Last 20 commits — quick, gives recent context
  - Option B: Full history summary — slower, but gives complete project narrative
  - Option C: Adaptive — analyze last N commits where N depends on repo age and commit frequency
  - Resolution: _[TBD]_

- **[OPEN] Template source of truth**: Where do the templates live that bootstrap uses?
  - Option A: Inline in the SKILL.md itself — self-contained but harder to maintain
  - Option B: Reference `context-management/assets/*.template.md` — DRY but creates a dependency
  - Option C: Copy templates into `meta-tools/project-bootstrap/templates/` — independent copy, may drift
  - Resolution: _[TBD]_

- **[OPEN] Context-sync auto-setup**: Should bootstrap automatically create a context-sync scheduled task?
  - Option A: Always create it — every project benefits from auto-sync
  - Option B: Ask during bootstrap — "Set up auto-sync? (y/n)"
  - Option C: Never auto-create — user runs context-sync-setup skill separately if they want it
  - Resolution: _[TBD]_

## Acceptance Criteria
- Running the skill on a bare repo creates all 6-7 files
- Running on a repo with existing .cursorrules migrates content into CLAUDE.md
- The shared boilerplate (co-founder persona, session discipline) is consistent across all projects
- The skill handles both greenfield (new project) and retrofit (existing project with history)

## Out of Scope
- Does NOT create the git repo itself — assumes repo already exists (even if empty)
- Does NOT set up CI/CD, deployment, or infrastructure — only context management files
- Does NOT install dependencies or configure dev environment
- Does NOT create scheduled tasks directly — optionally calls context-sync-setup skill
- Does NOT customize CLAUDE.md content beyond template parameters — deeper customization is manual

## Verification
- Run on a bare temp directory with git init — verify all 7 files created (CLAUDE.md, STATE.md, BACKLOG.md, docs/LESSONS.md, docs/CONTEXT-PROTOCOL.md, .claude/launch.json, optionally context-sync task)
- Verify CLAUDE.md contains stack-specific sections matching input parameters (e.g., Python to uv/FastAPI sections)
- Verify STATE.md is populated from git log if repo has history (test on a repo with 10+ commits)
- Verify BACKLOG.md has correct tier structure (Urgent, High, Priority, Strategic, Non-priority)
- Run on a repo with existing .cursorrules — verify content is migrated into CLAUDE.md and .cursorrules is noted for removal
- Diff generated CLAUDE.md boilerplate against portfolio-system CLAUDE.md — shared sections (co-founder persona, session discipline) should match

## Reference Implementation
- `meta-tools/project-bootstrap/SKILL.md` — the skill itself (if already built; validate against this mission requirements)
- `context-management/SKILL.md` — the context management system this skill bootstraps
- Templates: context-management/assets/CLAUDE.template.md, context-management/assets/STATE.template.md

## Effort: M (2-3 hours)
