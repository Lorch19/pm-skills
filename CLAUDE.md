# Operator Kit

Tools for building, shipping, and running products. PM frameworks, multi-agent workflows, executable scripts, document generation, analytics, and an always-on strategic advisor. Each pack includes a `NAVIGATOR.md` — start there to find the right skill.

---

## Quick Start — Top 15 Daily Drivers

| Task | Skill | Pack |
|------|-------|------|
| Write a PRD | `prd-partner` (personalized) or `pm-frameworks/prd-development` (generic) | Root / PM Frameworks |
| Competitive analysis | `domain-tools/competitive-teardown` | Domain Tools |
| Strategy session | `/pm:strategy` | PM Agents |
| Market sizing | `pm-frameworks/tam-sam-som-calculator` | PM Frameworks |
| Create a slide deck | `document-tools/pptx` | Document Tools |
| Build a spreadsheet model | `document-tools/xlsx` | Document Tools |
| A/B test analysis | `analytics-tools/ab-test-analysis` | Analytics Tools |
| Go-to-market entry | `gtm-tools/beachhead-segment` | GTM Tools |
| Growth flywheel design | `gtm-tools/growth-loops` | GTM Tools |
| Financial modeling | `domain-tools/financial-analyst` | Domain Tools |
| Discovery workflow | `pm-frameworks/discovery-process` | PM Frameworks |
| Multi-agent spec review | `/pm:review` | PM Agents |
| Create/optimize skills | `meta-tools/skill-creator` | Meta Tools |
| Plan an automation | `meta-tools/automation-planner` | Meta Tools |
| **Linx: any product work** | `linx-advisor` (always-on) | Linx Advisor |

---

## Installed Packs

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
- `/pm:lfg` — Full pipeline (discovery → spec → review)

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

### 4. Document Tools (`document-tools/`) — NEW
4 Anthropic official skills for creating real document files. Each includes scripts and production-grade templates.

**Skills:**
- `docx` — Create/read/edit Word documents (.docx) with formatting, tables, images
- `pptx` — Create/edit PowerPoint presentations with design guidance
- `xlsx` — Create/edit Excel spreadsheets with formulas, charts, financial formatting
- `pdf` — PDF manipulation: merge, split, forms, OCR, encryption

### 5. Analytics Tools (`analytics-tools/`) — NEW
Quantitative analysis skills for data-driven PM work. From Pawel Huryn's PM Skills collection.

**Skills:**
- `ab-test-analysis` — Statistical A/B test analysis (confidence intervals, chi-squared, MDE)
- `sql-queries` — Natural language → SQL query generation
- `cohort-analysis` — Retention and cohort pattern analysis

### 6. GTM Tools (`gtm-tools/`) — NEW
Go-to-market execution skills. From Pawel Huryn's PM Skills collection.

**Skills:**
- `beachhead-segment` — Market entry scoring (burning pain × willingness × winnable × referral)
- `competitive-battlecard` — Sales enablement battlecards (different from competitive-teardown analysis)
- `growth-loops` — Self-reinforcing flywheel and growth loop design

### 7. Meta Tools (`meta-tools/`) — NEW
Skills for building and optimizing your toolkit itself.

**Skills:**
- `skill-creator` — Create, test, evaluate, and benchmark Claude skills (Anthropic official)
- `web-artifacts-builder` — Build interactive React+shadcn HTML artifacts
- `adr-writer` — Write Architecture Decision Records with structured rationale
- `automation-planner` — Plan background automations with safety guards (timeouts, circuit breakers, monitoring)

### 8. Doc Coauthoring (`doc-coauthoring/`) — NEW
Structured co-authoring workflow with three phases: context gathering, section-by-section refinement, and fresh-eyes reader testing. Anthropic official skill.

### 9. PRD Partner (`prd-partner/`)
Personalized PRD creation skill. Discovery Mode (sharpen thinking) or PRD Mode (generate document). Three output modes: AI-Build, Dev-Team, Stakeholder.

### 10. Context Management (`context-management/`)
Context management system for AI coding agents (Claude Code, Cursor, etc.). Maintains project context across sessions with two lean files + on-demand docs.

**Key files:**
- `SKILL.md` — Full skill instructions and session workflow
- `assets/CLAUDE.template.md` — Template for agent instructions file
- `assets/STATE.template.md` — Template for project state file
- `assets/CONTEXT-PROTOCOL.md` — Context update protocol
- `references/GUIDE.md` — Human-readable quick guide

### 11. Linx Advisor (`linx-advisor/`) — Active Partner Mode

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

---

## Full Routing Table

| Task | Use this skill |
|------|---------------|
| **Documents & Files** | |
| Write a Word doc | `document-tools/docx` |
| Create a slide deck | `document-tools/pptx` |
| Build a spreadsheet | `document-tools/xlsx` |
| Manipulate PDFs | `document-tools/pdf` |
| Co-author a document | `doc-coauthoring` |
| **Product Management** | |
| Write a PRD | `prd-partner` or `pm-frameworks/prd-development` |
| Discovery workflow | `pm-frameworks/discovery-process` |
| JTBD analysis | `pm-frameworks/jobs-to-be-done` |
| Opportunity mapping | `pm-frameworks/opportunity-solution-tree` |
| Prioritization | `pm-frameworks/prioritization-advisor` |
| Roadmap | `pm-frameworks/roadmap-planning` |
| User stories | `pm-frameworks/user-story` |
| **Strategy & Research** | |
| Strategy session | `pm-agents` → `/pm:strategy` |
| Competitive analysis | `domain-tools/competitive-teardown` |
| Market sizing | `pm-frameworks/tam-sam-som-calculator` |
| Positioning | `pm-frameworks/positioning-workshop` |
| PESTEL analysis | `pm-frameworks/pestel-analysis` |
| Company research | `pm-frameworks/company-research` |
| Press release (Working Backwards) | `pm-frameworks/press-release` |
| **Analytics & Data** | |
| A/B test analysis | `analytics-tools/ab-test-analysis` |
| SQL query generation | `analytics-tools/sql-queries` |
| Cohort/retention analysis | `analytics-tools/cohort-analysis` |
| SaaS metrics | `pm-frameworks/saas-revenue-growth-metrics` |
| **Go-to-Market** | |
| Market entry (beachhead) | `gtm-tools/beachhead-segment` |
| Sales battlecard | `gtm-tools/competitive-battlecard` |
| Growth loops | `gtm-tools/growth-loops` |
| GTM strategy | `domain-tools/marketing-strategy-pmm` |
| Demand gen | `domain-tools/marketing-demand-acquisition` |
| **Financial** | |
| Financial modeling | `domain-tools/financial-analyst` |
| Revenue operations | `domain-tools/revenue-operations` |
| RICE prioritization | `domain-tools/product-manager-toolkit` |
| **Multi-Agent Workflows** | |
| Write + review spec | `/pm:spec` then `/pm:review` |
| Full pipeline | `/pm:lfg` |
| Brainstorm | `/pm:riff` |
| Simulate/stress-test | `/pm:simulate` |
| **Meta / Tooling** | |
| Create/optimize a skill | `meta-tools/skill-creator` |
| Build interactive artifact | `meta-tools/web-artifacts-builder` |
| Document a decision | `meta-tools/adr-writer` |
| Plan an automation | `meta-tools/automation-planner` |
| Context management | `context-management` |
| Career transition | `pm-frameworks/career-growth-advisor` |
| **Linx-Specific** | |
| Any Linx product work | `linx-advisor` (always-on) |
| Competitive question | `linx-advisor/knowledge/competitive-matrix.md` |
| Meeting prep | `linx-advisor` → Behavior 5 |
| Battle card | `linx-advisor/knowledge/battle-cards.md` |
