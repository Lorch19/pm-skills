# Operator-Kit Audit

**Date:** 2026-04-15
**Auditor:** Claude (via Claude Code)
**Scope:** Full operator-kit skill inventory, assessed for a user who operates both as a general builder/Claude Code operator *and* as a PM at Linx Security (identity governance).
**Companion doc:** Linx-specific adaptations, net-new skills, and overlays live in a separate repo: `Lorch19/Linx-Operator-Kit`. This audit only covers operator-kit itself.

---

## Methodology

Every skill bucketed into one of three:

1. **Keep as-is** — skill is substantively good and does its job.
2. **Suggest improve** — skill works but is thin. Expansion would pay off. Not broken.
3. **Suggest archive** — skill is structurally redundant (Claude does this natively, another skill does it better) or genuinely low-value.

Archive bar is intentionally high. Dormant cost in operator-kit is near-zero — skills are loaded on demand, not auto-injected. "Don't use it" is cheaper than "delete it and regret it later." When in doubt → keep.

Linx-specific adaptations are **not** proposed as operator-kit changes. Those are overlays in `Linx-Operator-Kit` that reference (not replace) operator-kit skills.

---

## Bucket 1 — Suggest Archive (1 skill)

| Skill | Reason |
|-------|--------|
| `analytics-tools/sql-queries` | Claude writes SQL natively from table schema and plain-English questions. The 92-line prompt scaffold adds negligible lift over what the base model does on its own. R1/R3 from the original refit brief. **Not urgent** — if the skill's explicit guidance helps you in practice, keep it. |

No other skill crosses the "useless or bad" bar. Several are thin (see Bucket 2), but thin ≠ useless.

---

## Bucket 2 — Suggest Improve (16 skills)

### 2a. Executed on this branch (3 skills)

These are expanded in this branch via additive, generic improvements (no Linx-specific content). See corresponding commits.

| Skill | Before | Rationale |
|-------|--------|-----------|
| `operations-tools/skills/compliance-tracking` | 39 lines | Too thin for a PM/ops audit-prep tool. Missing framework coverage (FedRAMP, NIST CSF 2.0, CMMC, HITRUST), control-to-feature mapping, audit prep checklist, evidence workflow, anti-patterns. |
| `meta-tools/internal-comms` | 59 lines | Core PM/ops communication skill with only one structured template (3P). Missing: roadmap update, launch announcement, RFC, exec briefing, release notes, decisions-needed format, audience adaptation rules, anti-patterns. |
| `analytics-tools/cohort-analysis` | 119 lines | Already reasonable. Light additive pass: B2B SaaS cohort definitions, common pitfalls (survivorship bias, small-sample traps), output format contracts, Python skeleton. |

### 2b. Deferred — thin but not executing now

Two reasons not to expand these speculatively:
- Each is a ported Anthropic `knowledge-work-plugins` skill. They work as prompt scaffolds.
- Best to expand *after* you run one and find its output weak. Premature expansion creates bloat.

| Skill | Lines | One-line improvement angle |
|-------|-------|---------------------------|
| `engineering-tools/skills/documentation` | 35 | Add doc-type templates (README, API ref, ADR index, onboarding) + audience matrix. |
| `engineering-tools/skills/standup` | 35 | Add async template, per-role variants (engineer vs PM vs TL). |
| `engineering-tools/skills/system-design` | 32 | Add diagram conventions, non-functional requirement checklist, decision log template. |
| `engineering-tools/skills/tech-debt` | 32 | Add debt-classification matrix, interest/principal framing, payoff prioritization. |
| `engineering-tools/skills/testing-strategy` | 32 | Add pyramid template, coverage ratios by service type, flakiness playbook. |
| `engineering-tools/skills/deploy-checklist` | 49 | Add rollback decision tree, canary patterns, feature flag hygiene. |
| `engineering-tools/skills/code-review` | 52 | Add review-depth-by-risk matrix, anti-patterns, security checklist. |
| `engineering-tools/skills/debug` | 50 | Add reproduction harness template, 5-whys structure, hypothesis log. |
| `operations-tools/skills/process-optimization` | 36 | Add value-stream mapping template, cycle-time measurement, bottleneck types. |
| `operations-tools/skills/risk-assessment` | 40 | Add risk register template, likelihood/impact matrix, mitigation taxonomy. |
| `sales-tools/skills/draft-outreach` | 36 | Add persona-specific openers, anti-spam patterns, follow-up cadence. |
| `sales-tools/skills/competitive-intelligence` | 31 | Add structured search methodology (already partially in `competitive-teardown`), battlecard linkage. |
| `sales-tools/skills/create-an-asset` | 32 | Add asset-type templates (deck, one-pager, landing page), quality checklist. |
| `design-tools/skills/user-research` | 38 | Add interview guide templates, recruiting criteria, analysis workflow. |
| `meta-tools/frontend-design` | 39 | Add anti-AI-slop checklist, distinctive-aesthetic refs, component-library conventions. |

**When to expand a deferred skill:** after you invoke it and the output is thin → tell me which one and I'll expand it following the pattern used for compliance-tracking/internal-comms.

---

## Bucket 3 — Keep as-is (strong skills)

Not individually enumerated. These are the skills already producing good output: `prd-partner`, `doc-coauthoring`, `pm-frameworks/discovery-process`, `pm-frameworks/product-strategy-session`, `pm-frameworks/prd-development`, `pm-frameworks/opportunity-solution-tree`, `pm-frameworks/prioritization-advisor`, `domain-tools/competitive-teardown`, `domain-tools/financial-analyst`, `domain-tools/revenue-operations`, `domain-tools/marketing-strategy-pmm`, `design-tools/skills/research-synthesis`, `operations-tools/skills/status-report`, `operations-tools/skills/vendor-review`, `gtm-tools/beachhead-segment`, `gtm-tools/growth-loops`, `meta-tools/skill-creator`, `meta-tools/operational-discipline`, `meta-tools/automation-planner`, `meta-tools/adr-writer`, `meta-tools/project-bootstrap`, `context-management`, `document-tools/*`, and the rest of `pm-frameworks/*`.

Also keeping the original refit brief's "archive" candidates that it wanted to remove on R1 (wrong-audience) grounds:
- `engineering-tools/skills/*` — useful reference for a builder/PM at a security company, even if rarely primary.
- `meta-tools/deploy-rsync`, `health-check-monitor`, `webapp-testing`, `context-sync-setup` — dormant-cost-is-zero, occasionally useful for builder work.
- `domain-tools/financial-analyst`, `marketing-demand-acquisition` — a seed/Series A PM will touch unit economics and GTM eventually.
- `document-tools/pdf`, `docx` — programmatic doc generation is rarely needed but when it is, it's load-bearing.

---

## Merge candidates (not executed)

| Winner | Loser | Why deferred |
|--------|-------|--------------|
| `prd-partner` | `pm-frameworks/prd-development` | Merge is probably right but needs a content diff first. `prd-development` may have framework coverage (press-release, user-story linkage, acceptance criteria) worth preserving in `prd-partner/references/`. Recommend doing the diff as a standalone task before merging. |
| `domain-tools/competitive-teardown` | `sales-tools/skills/competitive-intelligence` | Different scopes in practice: teardown is deep strategic analysis, competitive-intelligence is sales-facing quick research. Keep both; adopt a naming convention in routing so they aren't confused. |

---

## Linx-specific work (goes to `Linx-Operator-Kit`, not here)

Captured for reference. **Do not execute in operator-kit.**

### New skills to build in `Linx-Operator-Kit`

1. **`linx-security-domain-context`** — shared glossary, positioning, competitive landscape, buyer personas, market anchors, compliance framework relevance. Sourced from Linx Notion via MCP connectors, not public search.
2. **`security-buyer-personas`** — CISO / Security Architect / SOC Analyst / GRC Manager deep library. Goals, pains, buying criteria, objections, evaluation questions.
3. **`compliance-feature-mapper`** — bidirectional mapping between product features and compliance controls (SOC 2 CC6.x, ISO 27001 A.9.x, FedRAMP AC-x, NIST CSF, CMMC).
4. **`pm-weekly-rhythm`** — Linx-flavored PM operating cadence. Mon priorities / Tue-Wed deep work / Thu reviews / Fri reflection.
5. **`pm-standup`** — PM-specific standup (customer signals, decisions pending, cross-team blockers) distinct from the engineering-tools version.
6. **`product-decision-record`** — PDR variant of ADR, product-shaped (problem → options → decision → trade-offs → revisit trigger).

### Linx overlays (thin skills that reference, not replace, operator-kit skills)

Each of these is a short wrapper that invokes the operator-kit skill and injects Linx context from `linx-security-domain-context`:

- `prd-partner` overlay — adds identity-security PRD conventions, compliance section, CISO persona re-personalization.
- `discovery-process` overlay — CISO/Security Architect/SOC Analyst/GRC Manager interview templates.
- `jobs-to-be-done` overlay — identity security JTBD examples (provisioning, audit prep, deprovisioning, service accounts, identity alerts).
- `positioning-workshop` overlay — cybersecurity positioning patterns, platform vs point solution framing.
- `tam-sam-som-calculator` overlay — IGA market data anchors (Gartner IGA MQ, IDC, Forrester Wave, $8.6B→$24B trajectory).
- `competitive-teardown` overlay — security scoring dimensions (protocol coverage, SIEM/SOAR depth, NHI support, compliance coverage) + stub profiles for SailPoint, CyberArk, Saviynt, ConductorOne, Veza, Opal, Lumos, Zluri.
- `beachhead-segment` overlay — identity security segment candidates.
- `competitive-battlecard` overlay — security objection bank ("we have SailPoint", "CyberArk covers identity", "Okta is our IDP").
- `compliance-tracking` overlay — SOC 2 / FedRAMP / ISO 27001 → Linx feature mapping. (Operator-kit version, now expanded, is the generic base.)
- `call-summary` PM overlay — reframe "deal impact" → "product insights" (feature requests, pain points, JTBD signals, feedback classification).

### Execution path for Linx-Operator-Kit

Separate session, separate repo. My current MCP scope is locked to `lorch19/operator-kit`; Linx-Operator-Kit work needs a fresh Claude Code session opened against that repo. Build order:

1. `linx-security-domain-context` first — sourced from Notion connectors. Everything references it.
2. Net-new skills (`pm-weekly-rhythm`, `pm-standup`, `product-decision-record`, `security-buyer-personas`, `compliance-feature-mapper`).
3. Overlays in priority order: `prd-partner` → `competitive-teardown` → `discovery-process` → `jobs-to-be-done` → rest.
4. Root `CLAUDE.md` in Linx-Operator-Kit routes to overlays first, falls through to operator-kit skills.

---

## What this audit does NOT cover

- **Skill quality under actual invocation.** Line count is a proxy, not ground truth. A 35-line skill can outperform a 200-line one. Real signal comes from using the skill and judging the output.
- **`pm-agents` system internals.** The multi-agent commands (`/pm:spec`, `/pm:review`, etc.) are a separate subsystem and weren't evaluated here.
- **Linx-internal state** — your team, current roadmap, OKRs — that context belongs in `Linx-Operator-Kit` sourced from Notion.
