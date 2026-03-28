# Session: Linx Security — PM Onboarding & Leadership Trajectory

## Who I Am
I'm Omri, starting as a PM at Linx Security. I have autonomy to challenge, ideate, and build. My goal is to grow into a product leadership role. I'm hands-on — I code, I ship, I think strategically.

## About Linx Security
- **What:** AI-native identity security & governance platform. Graph-based, agentless. Covers human identities, non-human identities (service accounts, API keys, bots), and agentic AI identities.
- **Stage:** Series A ($33M raised — $6M seed + $27M Series A from Index Ventures + Cyberstarts). Emerged from stealth July 2024. ~60 people.
- **Founders:** Israel Duanis (CEO, ex-Check Point, Talpiot) and Niv Goldenberg (CPO, ex-Transmit Security/Adallom, Talpiot). Wiz founders are angel investors.
- **Customers:** Peloton, Wiz, Aramark, Discount Tire, Achieve, New American Funding — mix of mid-market and Fortune 500.
- **Product pillars:** Modern IGA, Identity Security Posture Management (ISPM), Just-In-Time Access, Identity Lifecycle Management, Non-Human & Agentic Identity Governance.
- **Latest launch:** "Autopilot" (March 2026) — autonomous AI agent for identity security. Demoed at RSA 2026.
- **Analyst recognition:** Listed in Forrester's "Workforce Identity Security Platforms Landscape, Q4 2025" across 3 categories: identity governance, AI agent identity management (called "the top disruptor"), and identity security posture management.

## Linx's Strategic Narrative (from their blog)
Linx's thought leadership centers on three pillars — internalize these, they reveal how the company thinks:

1. **Agentic identity as a first-class governance problem.** Linx defines agentic identities as autonomous AI systems that "determine paths, tools, and systems to use, and then act on those decisions without continuous human oversight." Three specific risks: sequential risk (benign individual actions, dangerous chains), compound access (agents autonomously expand permissions as they encounter obstacles), and delegation context loss (IAM systems see fragments, miss the unified decision-maker). Linx's answer: treat "decision sequences as first-class security objects" — not just individual entitlements.

2. **JIT access from humans to agents.** Their model has 4 layers: visibility → policy/decision → intelligence → fulfillment/audit. Key differentiator: agents are distinct identities (not service account wrappers), agents cannot self-escalate beyond allow-lists, human approvers remain central. Kill-switch capabilities tied to anomaly detection.

3. **Autopilot = autonomous but guardrailed.** Continuous monitoring + contextual risk evaluation + autonomous action OR human escalation. The philosophical bet: move from periodic access reviews (rubber-stamp theater) to continuous autonomous governance. The trust challenge: enterprise CISOs are skeptical of "autonomous" anything — Linx's guardrail design is the answer.

## Competitive Landscape
- **SailPoint** — Re-IPO'd. Dominant incumbent. Launched AI-powered adaptive identity, privilege discovery, machine identity lifecycle, and Harbor Pilot agents. The 800-lb gorilla moving fast.
- **ServiceNow/Veza** — ServiceNow acquired Veza for ~$1B (closed March 2026). Graph-based identity + massive ITSM distribution.
- **CyberArk** — Acquired Zilla Security ($175M) for IGA + Venafi ($1.54B) for machine identity. PAM + IGA + machine identity convergence play.
- **ConductorOne** — $111M raised. Unified human + NHI governance. Strong content marketing.
- **Lumos** — Launched "Albus" (first AI multi-agent IGA system). Pinterest, MongoDB, GitHub as customers.
- **Opal Security** — Developer-friendly, JIT access, Terraform/Slack integrations. Mid-market focused.
- **Zluri** — Expanded to NHI governance (March 2026). 200+ customers.
- **Saviynt** — Converged IGA + PAM. Strong in SAP/Workday fine-grained controls. Regulated industries.

## Market Context
- IGA market: ~$8.6B (2024) → $24B+ by 2032 (13.8% CAGR)
- NHI market: $11.3B standalone. Machine-to-human identity ratio: 17:1 (up 44% YoY)
- RSA 2026 dominant theme: agentic AI governance. 85% of orgs adopting AI agents, only 5% at production scale — blocked by identity/access questions.
- Series B benchmarks: $7-10M ARR, sub-2x burn multiple, 120%+ NRR, diversified customer base, 3-5 referenceable logos.
- Buyer pain: 89% of orgs have integrated <50% of apps with IGA. Legacy deployments take 12-18 months. Access reviews are rubber-stamp theater.

## My PM Assignment (Completed — Build On This)
I already completed a PM assignment for Linx: designing an AI Agent MVP for "Continuous Identity Risk Detection & Remediation." This represents my product thinking — the next session should build on and challenge these ideas, not start from scratch.

### The Problem I Framed (3 compound crises)
1. **Identity Explosion** — 93% breach involvement, NHI:human ratio 45:1, NHI growing 56% YoY
2. **Capacity Collapse** — 100k+ annual findings, teams cover only ~20%, 80% backlog
3. **The Reactive Trap** — Risk accumulates 24/7, governance is periodic (monthly/quarterly)

### My Solution: Virtual Security Analyst
An AI agent that continuously monitors risks (human & NHI), autonomously remediates clear issues, and escalates complex cases with full governance context. Core value prop: "The agent doesn't just fix the leak; it suggests a policy to patch the pipe."

### Key Design Decisions
- **Confidence × Risk Matrix** — 4 quadrants determining agent autonomy:
  - High confidence + Low risk → AUTO-REMEDIATE (act immediately, notify after)
  - High confidence + High risk → RECOMMEND (present case, human approves)
  - Low confidence + Low risk → FLAG & MONITOR (surface for review)
  - Low confidence + High risk → ESCALATE (full investigation, human decides)
- **Risk Score** = Environment (Prod > Dev) × Data Sensitivity × Permission Level × Blast Radius
- **Signal categories:** Identity (type, creator, HR status), Behavioral (API freq, login anomalies), Permissions (admin flags, peer comparison), Graph (owner chain, nested paths)

### Progressive Autonomy Model (4 phases)
1. **Shadow Mode** (~1-2 weeks) — Observe only, logs "I would have done X." Gates: detection coverage >80%, zero critical false positives.
2. **Recommend** (~3-4 weeks) — Surfaces findings, human executes all. Gates: precision >85%, approval rate >70%.
3. **Supervised** (~4-6 weeks) — Auto: low risk. Recommend: med/high risk. Gates: zero auto-incidents, MTTR improvement >20%.
4. **Trusted Auto** (ongoing) — Auto: low + med risk. Recommend: high risk only. Per-risk-category progression.

### The Autonomy Loop (key innovation)
Alex (analyst) decides → Agent learns patterns (e.g., 10x similar approvals) → Agent proposes new policy rule → Sam (director) approves → Policy codified → Agent gains autonomy for future matches.

### Personas
- **Alex Chen** (Identity Security Analyst, 4yr exp, 3-person IAM team) — Spends 60% gathering context, only 20% on decisions. Drowning in alerts.
- **Sam Williams** (Director Security Ops, reports to CISO, 15 people, <$100K budget) — Needs measurable risk reduction, not activity metrics. Can't get more headcount.
- **Collaborators:** App owners (Jordan Park, Eng Manager — Slack escalations), GRC analyst (Morgan Lee — audit logs), IT Service Desk (manual tasks)

### Capabilities Roadmap
- **MVP:** Continuous Remediation (remediation is the market gap — competitors focus on detection or workflow)
- **V1.1:** Governance + Collaboration (policy AI, natural language rule creation, Slack integration)
- **V2:** Full IGA Suite (JIT access, compliance reviews, reporting, access approvals, onboarding)
- **Platform:** AI-Powered Identity Security OS

### Success Metrics I Defined
- MTTR: 4h (↓92% from 2-day manual average)
- Attack surface reduction: -35% YoY
- Acceptance rate: 88%
- False positives: <2%
- Investigation time: 2min (↓8x from 15-30min manual)
- Throughput: 5x findings per week, same headcount
- Autonomy level: L3 target
- Policy creation: 12/month from agent learning

### Building Principles (3 pillars)
1. **Trust** — Conservative start (shadow mode), proven accuracy, earned autonomy
2. **Control** — Granular modes per risk category, kill switch, undo button
3. **Visibility** — Reasoning traces ("why I think this" before "what I did"), decision logs, context links

### Key Assumptions to Validate
- ML risk scoring is accurate enough for automated decisions
- Graph architecture can identify remediation paths, not just risks
- NHI remediation is lower-stakes starting point than human identity changes
- Customers will grant remediation permissions after shadow mode proves value
- Trust must be earned incrementally through transparency

## Reference Materials (on disk — load if needed)
- `/Users/omrilorch/Desktop/Linx Onboarding/Linx Assignment.pdf` — My completed assignment deck (19 slides)
- `/Users/omrilorch/Desktop/Linx Onboarding/How to Securely Delegate Access to Agents.pdf` — Agent delegation security patterns
- `/Users/omrilorch/Desktop/Linx Onboarding/IAM for LLM-Based AI Agents.pdf` — IAM architecture for AI agents
- `/Users/omrilorch/Desktop/Linx Onboarding/Market Guide for IGA.pdf` — Gartner Market Guide for IGA
- `/Users/omrilorch/Desktop/Linx Onboarding/Reduce Your IAM Attack Surface.pdf` — IAM attack surface reduction strategies

## What I Need From This Session

### Phase 1: Competitive Positioning (Week 1-2)
Using `competitive-teardown` and `positioning-workshop`:
- Build a structured competitive map: Linx vs. SailPoint vs. ServiceNow/Veza vs. CyberArk vs. ConductorOne vs. Lumos vs. Opal vs. Zluri
- Score across 12 dimensions (feature depth, deployment speed, NHI coverage, AI maturity, integrations, pricing, etc.)
- Define Linx's positioning: what's our category? What's the "only we" statement?
- Identify the 2-3 competitive battles we can win and the ones we should avoid

### Phase 2: Strategic Bets (Week 2-4)
Using `/pm:strategy` and `tam-sam-som-calculator`:
- Map the IGA market segments: which verticals, company sizes, and use cases should Linx prioritize?
- Size the NHI + agentic AI governance opportunity specifically (this is where Linx has differentiation)
- Stress-test the Autopilot strategy: is autonomous identity governance the right bet? What are the trust barriers?
- Define the "must-win battles" for Series B readiness

### Phase 3: Product Roadmap & Metrics (Month 2-3)
Using `prd-development`, `metrics-design`, and `roadmap-planning`:
- Design the metrics framework: what should Linx track for product-led growth in enterprise security?
- Write a PRD for the highest-impact feature I identify
- Build a roadmap proposal that balances customer requests, competitive pressure, and the NHI/agentic frontier

### Phase 4: Leadership Trajectory (Ongoing)
Using `career-growth-advisor` (Phase 1: PM→Director):
- Build my internal credibility playbook: how do I move from "new PM" to "trusted strategic voice" at a 60-person startup?
- Identify the high-leverage problems that, if I own them, position me for leadership
- Design my stakeholder map: who are the key relationships (CPO Niv, CEO Israel, engineering leads, customer-facing teams)?

## Skills to Load
- `alireza/competitive-teardown`
- `dean-peters/positioning-workshop`
- `compound-pm` → `/pm:strategy`
- `dean-peters/tam-sam-som-calculator`
- `dean-peters/prd-development`
- `compound-pm/skills/metrics-design`
- `dean-peters/roadmap-planning`
- `alireza/marketing-strategy-pmm`
- `dean-peters/career-growth-advisor`
- `compound-pm/skills/stakeholder-buyin`

## How to Work With Me
- Be direct. Challenge my assumptions. I'd rather hear "that's wrong" than get polished agreement.
- When I'm excited about something, stress-test it harder — that's when I'm most likely to have blind spots.
- Ground everything in data and evidence. If we don't have data, say so and suggest how to get it.
- Think like a co-founder, not an assistant. Push back, suggest alternatives, flag risks I'm not seeing.

## Start Here
Begin with Phase 1 — competitive positioning. Use `competitive-teardown` to build the competitive map, then `positioning-workshop` to define Linx's positioning. I'll share what I learn in my first weeks to refine.
