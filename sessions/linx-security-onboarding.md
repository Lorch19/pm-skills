# Session: Linx Security — PM Onboarding & Leadership Trajectory

## Who I Am
I'm Omri, joining Linx Security as a PM. I have autonomy to challenge, ideate, and build. My goal is to grow into a product leadership role.

**Background that's relevant here:**
- Head of Product at Cedar Money (seed-stage fintech) — led strategy, pivoted ICP, built compliance platform, co-led blockchain integration
- 6 years at Payoneer — Principal PM / Product Team Lead. Led China B2B platform (PMF + 20% growth in 6 months), launched Ecosystem (partnerships, embedded lending), owned KYC/Risk/Compliance/Account Security domains, managed 3 PMs
- Deep compliance & risk experience (KYC conversion +11%, operational revenue loss -35%, onboarding time -20%)
- MBA from Tel Aviv University (ML, Tech, Finance). Founded a non-profit adopted as a university course.
- Technical: Python, SQL, API-first thinking. Product: Amplitude, Figma, FullStory.
- I've built platforms, scaled teams, pivoted ICPs, and shipped in regulated environments. Identity security is new domain for me — I'm learning fast.

## About Linx Security
- **What:** AI-native identity security & governance platform. Graph-based, agentless. Unified coverage across human identities, non-human identities (service accounts, API keys, bots), and agentic AI identities.
- **Vision:** Become the one-stop-shop for identity security — all IGA, ISPM, JIT access, lifecycle management, NHI governance, compliance, and reporting on one platform. AI-powered from core, not bolted on.
- **Stage:** Series A ($33M raised — $6M seed + $27M Series A from Index Ventures + Cyberstarts). Emerged from stealth July 2024. ~60 people.
- **Founders:** Israel Duanis (CEO, ex-Check Point, Talpiot) and Niv Goldenberg (CPO, ex-Transmit Security/Adallom, Talpiot). Wiz founders are angel investors.
- **Customers:** Peloton, Wiz, Aramark, Discount Tire, Achieve, New American Funding — mix of mid-market and Fortune 500.
- **Analyst recognition:** Listed in Forrester's "Workforce Identity Security Platforms Landscape, Q4 2025" across 3 categories: identity governance, AI agent identity management (called "the top disruptor"), and identity security posture management.

### Product Platform (current + trajectory)
| Capability | Status | Market Gap |
|---|---|---|
| Risk Visibility (ISPM) | Live | Table stakes — Veza, Silverfort have this |
| AI-Powered Remediation (Autopilot) | Launched March 2026 | Gap — competitors detect, don't remediate autonomously |
| Governance & Policy | Building (V1.1) | Gap — no one combines AI + cross-identity governance |
| Access Approvals & Workflows | Roadmap | ConductorOne, Lumos play here |
| JIT Access | Roadmap | Opal's strength |
| Compliance & Reporting | Roadmap | SailPoint, Saviynt dominate |
| Identity Lifecycle (Joiner/Mover/Leaver) | Roadmap | Legacy IGA core |
| NHI + Agentic Identity Governance | Live | Linx's differentiation — emerging category |

### Linx's Strategic Narrative (from their blog — internalize this)
1. **Agentic identity as a first-class governance problem.** Three specific risks: sequential risk (benign actions form dangerous chains), compound access (agents autonomously expand permissions), delegation context loss (IAM sees fragments, misses the orchestrator). Linx's answer: treat decision sequences as first-class security objects.

2. **JIT access from humans to agents.** 4-layer model: visibility → policy/decision → intelligence → fulfillment/audit. Agents are distinct identities (not service account wrappers). Agents cannot self-escalate. Kill-switch tied to anomaly detection.

3. **Autopilot = autonomous but guardrailed.** Continuous monitoring + contextual risk evaluation + autonomous action OR human escalation. The bet: move from periodic access reviews to continuous autonomous governance. The trust barrier: CISOs are skeptical of "autonomous" — guardrails are the answer.

## The Identity Security Market

### Market Size & Dynamics
- IGA market: ~$8.6B (2024) → $24B+ by 2032 (13.8% CAGR)
- NHI market: $11.3B standalone. Machine-to-human identity ratio: 17:1 (up 44% YoY)
- RSA 2026 dominant theme: agentic AI governance. 85% of orgs adopting AI agents, only 5% at production scale — blocked by identity/access questions
- Heavy M&A consolidation validating the space (Veza→ServiceNow $1B, Zilla→CyberArk $175M, Venafi→CyberArk $1.54B)

### Enterprise Buyer Pain Points
- **Integration scalability** — 89% of orgs integrated <50% of apps with IGA. Legacy tools onboard ~10-20 apps/year, enterprises use thousands.
- **Access reviews are theater** — Quarterly certifications produce rubber-stamp approvals. Managers approve everything to clear queues.
- **Deployment kills projects** — Traditional IGA: 12-18 months. Budget holders lose patience, sponsors change roles.
- **NHI blind spots** — No governance over service accounts, API keys, AI agents. Elevated privileges, no lifecycle controls.
- **Role management is broken** — No single person has context to own business roles across hundreds of apps.
- **The reactive trap** — Risk accumulates 24/7, governance happens periodically. Always behind.

### Competitive Landscape
| Competitor | Position | Recent Moves | Linx's Edge |
|---|---|---|---|
| **SailPoint** | Dominant incumbent, re-IPO'd | AI-powered adaptive identity, Harbor Pilot agents, machine identity lifecycle | Autonomous action vs. their workflow automation |
| **ServiceNow/Veza** | $1B acquisition (March 2026) | Graph-based identity + massive ITSM distribution | Unified human+NHI+agentic vs. their authorization focus |
| **CyberArk** | PAM leader expanding to IGA | Acquired Zilla ($175M) + Venafi ($1.54B). PAM+IGA+machine identity convergence | AI-native vs. their acquisition-assembled stack |
| **ConductorOne** | Modern IGA challenger, $111M raised | Unified human+NHI governance. Strong content marketing | Autonomous remediation vs. their ticket workflows |
| **Lumos** | AI-first IGA, $35M Series B | Launched "Albus" (first AI multi-agent IGA). Pinterest, MongoDB, GitHub | Graph depth + NHI coverage vs. their SaaS focus |
| **Opal Security** | Developer-friendly JIT, $32M Series B | Cloud-native, Terraform/Slack/Jira integrations | Breadth of platform vs. their JIT-only focus |
| **Zluri** | NHI expansion, 200+ customers | Launched Identity Security Platform (March 2026) | AI autonomy + remediation vs. their discovery focus |
| **Saviynt** | Converged IGA+PAM, regulated industries | Strong SAP/Workday fine-grained controls | Speed-to-value + AI-native vs. their complexity |

### Series B Context
- ARR benchmarks: $7-10M for successful raise
- Must prove: repeatable sales motion, land-and-expand working, NRR >120%, sub-2x burn multiple
- Customer diversification needed (not over-indexed on 2-3 logos)
- The window for standalone identity governance startups is narrowing — must show platform trajectory

## My Prior Work (Assignment Context)
I completed a PM assignment for Linx designing an AI Agent MVP for "Continuous Identity Risk Detection & Remediation." Key design decisions I made that you should know about (build on these, challenge them):

- **Confidence × Risk Matrix** for agent autonomy: auto-remediate (high conf + low risk), recommend (high conf + high risk), flag & monitor (low conf + low risk), escalate (low conf + high risk)
- **Progressive Autonomy Model**: Shadow → Recommend → Supervised → Trusted Auto (per-risk-category, with success gates at each phase)
- **The Autonomy Loop**: analyst decides → agent learns patterns → proposes policy rule → director approves → policy codified → agent gains autonomy
- **Building principles**: Trust (earned incrementally), Control (granular per-category, kill switch, undo), Visibility (reasoning traces before actions, full audit trail)
- Full assignment deck: `/Users/omrilorch/Desktop/Linx Onboarding/Linx Assignment.pdf`

## Reference Materials (load if needed)
- `/Users/omrilorch/Desktop/Linx Onboarding/How to Securely Delegate Access to Agents.pdf`
- `/Users/omrilorch/Desktop/Linx Onboarding/IAM for LLM-Based AI Agents.pdf`
- `/Users/omrilorch/Desktop/Linx Onboarding/Market Guide for IGA.pdf` (Gartner)
- `/Users/omrilorch/Desktop/Linx Onboarding/Reduce Your IAM Attack Surface.pdf`

## What I Need From This Session

### Phase 1: Market Deep Dive & Competitive Positioning (Week 1-2)
Using `competitive-teardown` and `positioning-workshop`:
- Build a structured competitive map across all 8 competitors — score on 12 dimensions
- Define Linx's positioning as a PLATFORM (not a point solution): what's the "only we" statement?
- Map the full IGA capability landscape — where does Linx win today vs. where it needs to go?
- Identify which competitive battles to fight now vs. which to defer

### Phase 2: Platform Strategy & Market Segmentation (Week 2-4)
Using `/pm:strategy` and `tam-sam-som-calculator`:
- Map IGA market segments: verticals, company sizes, use cases, buying triggers
- Size the full opportunity (not just NHI — the whole identity security platform play)
- Define the platform expansion sequence: which capabilities to build next, in what order, for which segments
- Stress-test: is "one-stop-shop for identity security" achievable at Series A scale? What's the minimum viable platform?

### Phase 3: Product Roadmap & Metrics (Month 2-3)
Using `prd-development`, `metrics-design`, and `roadmap-planning`:
- Design the metrics framework for an identity security platform (not just the AI agent)
- Write PRDs for highest-impact features across the full capability roadmap
- Build a roadmap proposal that sequences platform buildout against competitive pressure and customer demand

### Phase 4: Leadership Trajectory (Ongoing)
Using `career-growth-advisor`:
- How do I move from "new PM" to "trusted strategic voice" at a 60-person startup?
- Which platform problems should I own to position for leadership?
- Stakeholder map: CPO Niv, CEO Israel, engineering leads, customer-facing teams

## Skills to Load
- `competitive-teardown` (domain-tools pack)
- `positioning-workshop` (pm-frameworks pack)
- `/pm:strategy` (pm-agents pack)
- `tam-sam-som-calculator` (pm-frameworks pack)
- `prd-development` (pm-frameworks pack)
- `metrics-design` (pm-agents pack)
- `roadmap-planning` (pm-frameworks pack)
- `marketing-strategy-pmm` (domain-tools pack)
- `career-growth-advisor` (pm-frameworks pack)
- `stakeholder-buyin` (pm-agents pack)

## How to Work With Me
- Be direct. Challenge my assumptions. I'd rather hear "that's wrong" than get polished agreement.
- When I'm excited about something, stress-test it harder — that's when I'm most likely to have blind spots.
- Ground everything in data and evidence. If we don't have data, say so and suggest how to get it.
- Think like a co-founder, not an assistant. Push back, suggest alternatives, flag risks I'm not seeing.
- I come from fintech/compliance — I understand regulated environments, but identity security is a new domain. Bridge the gap, don't assume I know IAM jargon.

## Start Here
Begin with Phase 1 — competitive positioning. Use `competitive-teardown` to build the competitive map, then `positioning-workshop` to define Linx's platform positioning.
