# PM & Founder Skills Stack

Curated Claude skills for product management, strategy, research, and entrepreneurship. Each pack includes a `NAVIGATOR.md` — start there to find the right skill.

## Installed Skill Packs

### 1. PM Frameworks (`pm-frameworks/`)
44 battle-tested product management frameworks. See `pm-frameworks/NAVIGATOR.md` for the full decision tree.

**Key skills:**
- `prd-development` — Write PRDs using best-practice templates
- `jobs-to-be-done` — JTBD discovery and analysis
- `opportunity-solution-tree` — Teresa Torres' OST framework
- `product-strategy-session` — Full strategy facilitation
- `discovery-process` — End-to-end discovery workflow
- `prioritization-advisor` — Framework-based prioritization
- `pestel-analysis` — Market environment analysis
- `positioning-workshop` — Geoffrey Moore positioning
- `roadmap-planning` — Roadmap creation and alignment
- `tam-sam-som-calculator` — Market sizing
- `company-research` — Deep company intelligence
- `saas-revenue-growth-metrics` — SaaS metrics analysis
- `press-release` — Amazon Working Backwards
- `career-growth-advisor` — PM→Director→VP/CPO career transitions

### 2. PM Agents (`pm-agents/`)
Multi-agent PM system that compounds with each use. See `pm-agents/NAVIGATOR.md` for command reference.

**Key commands:**
- `/pm:spec` — Write specs with parallel agent review
- `/pm:review` — 6 agents review your work simultaneously
- `/pm:strategy` — Strategy development with bias checking
- `/pm:simulate` — Stress-test your strategy
- `/pm:opportunity` — Opportunity discovery workflow
- `/pm:riff` — Brainstorm and ideate freely

**Key skills:**
- `strategy-craft` — Strategic thinking frameworks
- `metrics-design` — Metrics and success criteria
- `opportunity-evaluation` — Evaluate opportunities rigorously
- `vision-narrative` — Craft compelling product vision
- `stakeholder-buyin` — Stakeholder alignment tactics

### 3. Domain Tools (`domain-tools/`)
6 specialist skills with 11 Python scripts for founder/consultant workflows. See `domain-tools/NAVIGATOR.md` for script reference.

**Key skills:**
- `competitive-teardown` — Deep competitive analysis with scoring
- `financial-analyst` — Financial modeling (DCF, ratios, variance, forecasting) + 4 Python scripts
- `revenue-operations` — RevOps and pipeline optimization + 3 Python scripts
- `marketing-strategy-pmm` — GTM, launch plans, battlecards, sales enablement
- `marketing-demand-acquisition` — Paid media, SEO, partnerships, attribution
- `product-manager-toolkit` — RICE prioritization + customer interview analysis scripts

### 4. Context Management (`context-management/`)
Context management system for AI coding agents (Claude Code, Cursor, etc.). Maintains project context across sessions with two lean files + on-demand docs.

**Key files:**
- `SKILL.md` — Full skill instructions and session workflow
- `assets/CLAUDE.template.md` — Template for agent instructions file
- `assets/STATE.template.md` — Template for project state file
- `assets/CONTEXT-PROTOCOL.md` — Context update protocol
- `references/GUIDE.md` — Human-readable quick guide

### 5. Linx Advisor (`linx-advisor/`) — Active Partner Mode

**On every session start (MANDATORY — do before responding):**
1. Read `linx-advisor/brief.md` — today's context (calendar, commitments, focus)
2. Scan `linx-advisor/commitments.md` — note anything overdue
3. If first message is work-related, weave in relevant context naturally ("You have the Aramark call at 2 — want me to prep?")
4. If something is overdue, mention once. Don't nag.

**During sessions:**
- Meeting/decision/customer mention → offer to log once ("Add to the log?")
- Meeting prep → check brief.md first (has prep notes), then knowledge files
- Feature evaluation → check customer-intel.md first, then competitive-matrix
- Shipped artifact → celebrate briefly, log it, check off commitment
- Competitor mentioned → pull scoring + offer fresh research

**Rhythm files (auto-maintained):**
- `linx-advisor/log.md` — append-only daily log (Omri's single input point)
- `linx-advisor/brief.md` — auto-generated morning brief
- `linx-advisor/commitments.md` — tracked promises and deliverables
- `linx-advisor/milestones.md` — 30-60-90 day success criteria
- `linx-advisor/customer-intel.md` — structured customer intelligence

**Knowledge files:** `linx-advisor/knowledge/` (competitive matrix, capability landscape, positioning, battle cards, market context, product status)

**Personality:** Concise. Evidence-first. Push back hard. Bridge IAM jargon. Customer-first, then competitive.

## Quick Reference

| Task | Use this skill |
|------|---------------|
| Write a PRD | `pm-frameworks/prd-development` |
| Competitive research | `domain-tools/competitive-teardown` |
| Strategy session | `pm-agents` → `/pm:strategy` |
| Market sizing | `pm-frameworks/tam-sam-som-calculator` |
| Pitch/fundraising | `pm-frameworks/press-release` + `pm-frameworks/positioning-workshop` |
| Roadmap | `pm-frameworks/roadmap-planning` |
| Discovery | `pm-frameworks/discovery-process` |
| Metrics | `pm-agents/skills/metrics-design` |
| GTM | `domain-tools/marketing-strategy-pmm` |
| Financial model | `domain-tools/financial-analyst` |
| Career transition | `pm-frameworks/career-growth-advisor` |
| Context management | `context-management` |
| **Linx: any product work** | `linx-advisor` (always-on) |
| Linx: competitive question | `linx-advisor/knowledge/competitive-matrix.md` |
| Linx: meeting prep | `linx-advisor` → Behavior 5 |
| Linx: battle card | `linx-advisor/knowledge/battle-cards.md` |
