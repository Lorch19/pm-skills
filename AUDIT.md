# Operator Kit — Skill Audit

**Date:** 2026-04-16
**Scope:** All 124 skills across 14 packs
**Purpose:** Identify genuinely weak skills worth improving. High bar for archival — dormant skills cost near-zero tokens since Claude Code loads SKILL.md bodies on demand, not at startup.

---

## Bucket 1: Keep As-Is (100 skills)

These skills range from solid scaffolds to excellent structured tools. No action needed.

### Tier A — Excellent (well-structured, 200+ lines, strong output quality)

| Pack | Skill | Lines | Notes |
|------|-------|-------|-------|
| prd-partner | prd-partner | 428 | Mode detection, scope creep checks, 3 output formats |
| doc-coauthoring | doc-coauthoring | 227 | Three-stage workflow with reader testing — innovative |
| pm-frameworks | discovery-process | 505 | 6-phase workflow with decision gates |
| pm-frameworks | prd-development | 656 | Comprehensive PRD guide (overlaps prd-partner — see notes) |
| pm-frameworks | roadmap-planning | 506 | Full strategic roadmap creation |
| pm-frameworks | opportunity-solution-tree | 421 | Teresa Torres' OST, well-implemented |
| pm-frameworks | prioritization-advisor | 441 | Multi-framework selector with guidance |
| pm-frameworks | positioning-workshop | 417 | Geoffrey Moore framework, deep |
| pm-frameworks | customer-journey-map | 347 | Comprehensive touchpoint mapping |
| pm-frameworks | customer-journey-mapping-workshop | 516 | Interactive workshop variant |
| pm-frameworks | discovery-interview-prep | 411 | Interview prep with Mom Test |
| pm-frameworks | product-strategy-session | 427 | Full strategy facilitation |
| pm-frameworks | jobs-to-be-done | 371 | JTBD framework, well-structured |
| pm-frameworks | pestel-analysis | 377 | Macro-environmental analysis |
| pm-frameworks | tam-sam-som-calculator | 393 | Market sizing with Python script |
| pm-frameworks | company-research | 386 | Deep company intelligence |
| pm-frameworks | saas-revenue-growth-metrics | 631 | Comprehensive SaaS metrics |
| pm-frameworks | saas-economics-efficiency-metrics | 687 | Unit economics deep dive |
| pm-frameworks | business-health-diagnostic | 784 | SaaS business health audit |
| pm-frameworks | ai-shaped-readiness-advisor | 924 | AI-first product assessment |
| pm-frameworks | acquisition-channel-advisor | 636 | Channel evaluation with unit economics |
| pm-frameworks | feature-investment-advisor | 632 | Feature ROI analysis |
| pm-frameworks | finance-based-pricing-advisor | 756 | Pricing impact analysis |
| pm-frameworks | epic-breakdown-advisor | 658 | Richard Lawrence methodology |
| pm-frameworks | lean-ux-canvas | 554 | Jeff Gothelf's Lean UX Canvas v2 |
| pm-frameworks | user-story-mapping-workshop | 478 | Interactive story mapping |
| pm-frameworks | problem-framing-canvas | 459 | MITRE problem framing |
| pm-frameworks | pol-probe-advisor | 485 | Proof-of-life probe selection |
| pm-frameworks | context-engineering-advisor | 764 | Context stuffing diagnosis |
| domain-tools | competitive-teardown | 451 | 12-dimension scoring + Python scripts |
| domain-tools | marketing-strategy-pmm | 386 | GTM, launches, battlecards |
| domain-tools | marketing-demand-acquisition | 318 | Multi-channel demand gen |
| domain-tools | revenue-operations | 294 | Pipeline and GTM efficiency |
| domain-tools | financial-analyst | 186 | DCF, ratios, forecasting + scripts |
| document-tools | docx | 595 | Word doc generation — comprehensive |
| document-tools | pptx | 237 | PowerPoint creation |
| document-tools | xlsx | 296 | Excel with formulas/charts |
| document-tools | pdf | 342 | PDF manipulation suite |
| meta-tools | skill-creator | 253 | Skill authoring + benchmarking |
| meta-tools | deploy-rsync | 188 | Rsync deployment automation |
| meta-tools | project-bootstrap | 185 | Zero-interview project setup |
| meta-tools | automation-planner | 167 | Background automation planning |
| meta-tools | health-check-monitor | 154 | Cross-project health monitoring |
| meta-tools | context-sync-setup | 139 | Scheduled context sync |
| meta-tools | adr-writer | 118 | Architecture decision records |
| meta-tools | operational-discipline | 110 | Co-founder mindset, session rituals |
| context-management | context-management | 173 | Cross-session context maintenance |

### Tier B — Solid (adequate structure, good scaffolds, 50-200 lines)

| Pack | Skill | Lines | Notes |
|------|-------|-------|-------|
| pm-frameworks | user-story | 273 | Clear user story framework |
| pm-frameworks | user-story-splitting | 304 | Vertical slice methodology |
| pm-frameworks | user-story-mapping | 286 | Journey hierarchy mapping |
| pm-frameworks | press-release | 270 | Amazon Working Backwards |
| pm-frameworks | storyboard | 253 | 6-frame visual narrative |
| pm-frameworks | problem-statement | 247 | User-perspective problem framing |
| pm-frameworks | positioning-statement | 231 | Geoffrey Moore positioning |
| pm-frameworks | proto-persona | 327 | Assumption-based persona creation |
| pm-frameworks | epic-hypothesis | 278 | Testable hypothesis framing |
| pm-frameworks | recommendation-canvas | 376 | AI solution evaluation |
| pm-frameworks | eol-message | 349 | End-of-life messaging |
| pm-frameworks | pol-probe | 210 | Lightweight validation probes |
| pm-frameworks | finance-metrics-quickref | 302 | 32+ SaaS finance metrics lookup |
| pm-frameworks | altitude-horizon-framework | 251 | PM career transition model |
| pm-frameworks | skill-authoring-workflow | 168 | Skill publishing workflow |
| pm-frameworks | career-growth-advisor | 77 | Career transition coaching |
| pm-frameworks | workshop-facilitation | 88 | Workshop facilitation guide |
| pm-frameworks | product-manager-toolkit | 130 | RICE + interview scripts |
| pm-agents | strategy-craft | 166 | Strategic thinking frameworks |
| pm-agents | behavioral-design | 174 | Behavioral psychology for product |
| pm-agents | analytical-thinking | 160 | Metrics, ecosystem, tradeoffs |
| pm-agents | growth-systems | 160 | Growth loops, retention, virality |
| pm-agents | product-riff | 152 | Multi-angle product exploration |
| pm-agents | pm-operating-system | 144 | Personalized PM operating system |
| pm-agents | simulation | 140 | Cognitive empathy for decisions |
| pm-agents | spec-review | 164 | Structured spec interview/review |
| pm-agents | stakeholder-buyin | 121 | Stakeholder alignment tactics |
| pm-agents | opportunity-evaluation | 115 | 5-question opportunity framework |
| pm-agents | metrics-design | 106 | Metrics hierarchy design |
| pm-agents | solution-creativity | 103 | 20 creativity techniques |
| pm-agents | vision-narrative | 96 | 3-part vision narrative |
| analytics-tools | ab-test-analysis | 112 | Statistical A/B test analysis |
| gtm-tools | beachhead-segment | 158 | Beachhead market scoring |
| gtm-tools | growth-loops | 138 | Flywheel design |
| gtm-tools | competitive-battlecard | 89 | Sales battlecard creation |
| meta-tools | web-artifacts-builder | 73 | Interactive HTML artifacts |
| meta-tools | webapp-testing | 59 | Playwright-based web testing |
| meta-tools | security-guidance | 52 | Security pattern monitoring hook |
| engineering-tools | incident-response | 75 | Incident triage + postmortem |
| engineering-tools | architecture | 61 | ADR creation/evaluation |
| engineering-tools | code-review | 52 | Code review checklist |
| operations-tools | capacity-plan | 60 | Workload analysis |
| operations-tools | change-request | 66 | Change management |
| operations-tools | vendor-review | 60 | Vendor TCO evaluation |
| operations-tools | runbook | 53 | Operational procedures |
| operations-tools | process-doc | 52 | SOP/RACI documentation |
| operations-tools | status-report | 51 | Leadership status updates |
| sales-tools | pipeline-review | 60 | Pipeline health analysis |
| sales-tools | forecast | 59 | Weighted sales forecasting |
| sales-tools | call-summary | 51 | Call notes → action items |
| sales-tools | call-prep | 50 | Pre-call account prep |
| sales-tools | daily-briefing | 49 | Morning sales priorities |
| sales-tools | account-research | 45 | Company/person research |
| design-tools | accessibility-review | 71 | WCAG 2.1 AA audit |
| design-tools | design-critique | 69 | Structured design feedback |
| design-tools | design-system | 67 | Design system management |
| design-tools | ux-copy | 63 | Microcopy writing/review |
| design-tools | design-handoff | 59 | Developer handoff specs |
| design-tools | research-synthesis | 56 | Research → themes + actions |

---

## Bucket 2: Improve (7 skills)

These skills are genuinely thin — their output quality would materially improve with more structure. Expansions are generic (not domain-specific) so they benefit any operator-kit user.

| Skill | Lines | Problem | Proposed Improvement |
|-------|-------|---------|---------------------|
| **operations-tools/compliance-tracking** | 39 | Lists 5 frameworks with no depth. Missing audit prep workflow, control mapping, evidence collection. For a skill triggered by "compliance" and "audit prep," this is inadequate. | Add FedRAMP, NIST CSF, CMMC, HITRUST. Add control-to-feature mapping template, 90/30/0-day audit prep checklist, evidence workflow, framework decision guide. Target: ~220 lines. |
| **meta-tools/internal-comms** | 59 | Has 3P format + generic guidelines. Missing templates for the 9 other communication types it claims to handle (newsletter, FAQ, etc.). The trigger promises more than the skill delivers. | Add structured templates for: roadmap update, launch announcement, RFC, exec briefing, decisions-needed memo, release notes, sprint review summary, incident one-pager. Add audience-adaptation matrix and anti-patterns. Target: ~280 lines. |
| **analytics-tools/cohort-analysis** | 119 | Good 5-step process but assumes consumer/PLG data. Missing B2B cohort definitions, output format templates, and common analytical pitfalls. | Add B2B SaaS cohort dimensions table, output format templates (retention heatmap spec, cohort comparison table spec), common pitfalls section. Target: ~170 lines. |
| **design-tools/user-research** | 38 | Barely a skeleton. Claims to handle "plan, conduct, and synthesize" but has no interview templates, no research plan structure, no synthesis framework. | Could expand with research plan template, interview guide template, synthesis framework. **Deferred** — the existing design-tools/research-synthesis (56 lines) handles synthesis, and pm-frameworks/discovery-interview-prep (411 lines) handles interview prep. Low priority. |
| **operations-tools/risk-assessment** | 40 | Lists basic risk matrix concepts but no structured output template or risk categories. | Could add risk category taxonomy, probability/impact matrix template, mitigation plan format. **Deferred** — works as a scaffold; Claude fills in the structure. |
| **operations-tools/process-optimization** | 36 | Very thin scaffold. | **Deferred** — low usage frequency for most users. |
| **meta-tools/frontend-design** | 39 | Thin but intentionally opinionated (anti-AI-slop aesthetics). The constraint *is* the skill. | **Keep as-is** — expanding would dilute the opinionated stance. |

**Expanding now:** compliance-tracking, internal-comms, cohort-analysis.
**Deferred:** user-research, risk-assessment, process-optimization (adequate as scaffolds).

---

## Bucket 3: Archive Candidates (1 skill)

High bar: only archive if the skill is genuinely useless or actively harmful to output quality.

| Skill | Lines | Reason | Recommendation |
|-------|-------|--------|---------------|
| **analytics-tools/sql-queries** | 92 | Claude generates SQL natively with full schema awareness. This skill adds a layer of indirection that produces *worse* SQL than asking Claude directly, because it constrains the generation process. Zero value add. | Archive to `/archive/analytics-tools/sql-queries/`. Remove from CLAUDE.md routing table. |

**That's it.** One skill. The brief's recommendation to archive ~30 skills was based on a "PM-only" lens. Since you use operator-kit as a builder/operator, not just a PM, virtually all skills have valid use cases. Skills that sit dormant cost nothing.

---

## Notes

### PRD Duplication
`prd-partner` (428 lines) and `pm-frameworks/prd-development` (656 lines) overlap significantly. Both create PRDs. `prd-partner` has mode detection, scope creep detection, 3 output formats. `prd-development` has more structured section-by-section guidance. **Recommendation:** keep both for now. They serve different trigger patterns — `prd-partner` for quick "write me a PRD" requests, `prd-development` for structured guided walkthroughs. If you find yourself never using one, archive it then.

### Linx-Specific Work
All Linx domain adaptations (security glossary, buyer personas, competitive overlays, compliance-to-feature mappings) belong in the separate `Lorch19/Linx-Operator-Kit` repo. See the Phase 2 plan in the Linx Claude Code session brief.

### Thin Engineering/Sales/Design Skills (32-60 lines)
Many skills in engineering-tools, sales-tools, and design-tools are thin (32-60 lines). These work as scaffolds — they trigger Claude's existing knowledge and shape the output format. Expanding them would add words without adding output quality. Leave them unless a specific skill consistently produces weak results.
