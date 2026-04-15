---
name: compliance-tracking
description: Track compliance requirements and audit readiness across regulatory and industry frameworks. TRIGGER when user mentions "compliance", "audit prep", "SOC 2", "ISO 27001", "GDPR", "FedRAMP", "HIPAA", "PCI DSS", "NIST", "CMMC", "HITRUST", "regulatory requirement", "control mapping", or needs help tracking, preparing for, or documenting compliance activities.
---

# Compliance Tracking

Track compliance requirements, prepare for audits, maintain regulatory readiness, and map product capabilities to control frameworks.

## When to use this skill

- Preparing for a first-time or recurring audit (Type 1 / Type 2)
- Mapping product features to control requirements
- Running a gap analysis before an audit engagement
- Designing evidence collection workflows
- Explaining compliance posture to customers, prospects, or leadership
- Evaluating whether pursuing a new framework is worth the investment
- Responding to customer security questionnaires (SIG, CAIQ, custom RFI)

## Framework Reference

### Primary frameworks

| Framework | Owner | Focus | Typical buyer | Audit cadence |
|-----------|-------|-------|---------------|---------------|
| **SOC 2** | AICPA | Trust services: Security (mandatory), Availability, Confidentiality, Processing Integrity, Privacy | US mid-market & enterprise SaaS | Type 1 (point-in-time), then Type 2 annually (6-12mo observation) |
| **ISO 27001** | ISO | Information Security Management System (ISMS) | Global enterprise, especially EU | Certification + surveillance audits yearly, recert every 3 years |
| **ISO 27701** | ISO | Privacy extension to 27001 | Companies handling personal data at scale | With 27001 cycle |
| **GDPR** | EU | Data protection & privacy rights | Any processor of EU resident data | Continuous; supervisory authority audits on complaint |
| **HIPAA / HITECH** | HHS (US) | PHI protection | US healthcare, BAAs | OCR enforcement is complaint-driven |
| **PCI DSS 4.0** | PCI SSC | Payment card data | Anyone handling cards | Annually (ROC/SAQ depending on level) |
| **FedRAMP** | GSA/FedRAMP PMO | Cloud services for US federal | Public sector SaaS | Moderate/High baselines; 3PAO assessment + ongoing ConMon |
| **StateRAMP** | StateRAMP PMO | FedRAMP-style for US state/local | SLED SaaS | Similar to FedRAMP cadence |
| **CMMC 2.0** | DoD | Defense contractor cybersecurity | US DoD supply chain | Triennial assessment (Level 2/3) |
| **NIST CSF 2.0** | NIST | Cybersecurity framework (voluntary) | US critical infrastructure, commonly adopted | Self-assessment or third-party |
| **NIST 800-53** | NIST | Federal security/privacy controls | Federal + FedRAMP underpinning | Continuous monitoring |
| **HITRUST CSF** | HITRUST | Harmonized healthcare+ framework | US healthcare, regulated industries | e1 / i1 / r2 levels; annual |
| **TX-RAMP / Cal-ISO / AZ-RAMP** | State PMOs | State cloud authorizations | Regional SLED | Varies |

### Framework relationships (reduce duplicate work)

- **SOC 2 + ISO 27001** share ~70% of controls. Pursue both if selling internationally; map controls once.
- **FedRAMP Moderate + NIST 800-53** — FedRAMP is 800-53 with federal overlays. If you have FedRAMP, most 800-53 work is done.
- **CMMC Level 2 ≈ NIST 800-171** (110 controls).
- **HITRUST** harmonizes HIPAA, PCI, ISO 27001, NIST — heavy but reusable.
- **PCI DSS** is orthogonal to everything else; scoped to cardholder data environment only.

## Tracking Components

### 1. Control inventory

Maintain a single source of truth mapping each control to:

```markdown
| Control ID | Framework(s) | Description | Owner | Evidence type | Frequency | Last collected | Status |
|------------|--------------|-------------|-------|---------------|-----------|----------------|--------|
| CC6.1 | SOC 2 | Logical access security | Security Eng | IAM policy export + screenshot | Quarterly | YYYY-MM-DD | Green |
| A.9.2.3 | ISO 27001 | Privileged access management | Security Eng | PAM config + access review log | Quarterly | YYYY-MM-DD | Green |
| AC-2 | NIST 800-53 | Account management | IT | Onboarding/offboarding tickets | Continuous | YYYY-MM-DD | Yellow |
```

### 2. Control-to-feature mapping

Maps product features to the controls they satisfy. Used for two reasons: (a) convincing customers your product helps their compliance, (b) identifying feature gaps when you want to claim a framework.

```markdown
| Product feature | Frameworks satisfied | Specific controls | Evidence artifact |
|-----------------|---------------------|-------------------|-------------------|
| SSO + MFA enforcement | SOC 2, ISO 27001, HIPAA | CC6.1, A.9.4.2, §164.312(a)(2)(i) | Config export |
| Access review workflow | SOC 2, ISO 27001, FedRAMP | CC6.3, A.9.2.5, AC-2(3) | Review completion log |
| Audit log immutability | SOC 2, HIPAA, PCI | CC7.2, §164.312(b), Req 10 | Log retention policy + sample |
```

### 3. Audit calendar

```markdown
## Audit Calendar — YYYY

### Upcoming
- [Month] SOC 2 Type 2 observation window begins — [date] to [date]
- [Month] ISO 27001 surveillance audit — auditor: [firm]
- [Month] Customer SOC 2 report refresh deadline (contract obligation)

### Evidence collection deadlines
- Monthly: access review exports, change log extracts
- Quarterly: privileged access review, vendor reviews, DR test
- Annually: penetration test, tabletop exercise, policy refresh, training completion

### Remediation deadlines
- [ID] Finding from last audit — due [date] — owner [person]
```

### 4. Gap analysis

Used before committing to a new framework, or before an audit engagement.

```markdown
## Gap Analysis: [Framework]

### Scope
- In scope: [products/environments]
- Out of scope: [exclusions and why]

### Summary
- Controls in scope: N
- Fully implemented: X (Y%)
- Partially implemented: X (Y%)
- Not implemented: X (Y%)
- Estimated remediation: [effort / timeline]

### Priority gaps (fix first)
1. [Control ID]: [description] — blocks [audit phase] — owner, target date
2. ...

### Medium priority
...

### Risk-accepted / compensating control
- [Control ID]: [why accepted, what compensates]
```

## Audit Prep Checklist

### 90 days before
- [ ] Confirm scope (products, environments, locations, people)
- [ ] Confirm auditor & engagement letter
- [ ] Gap analysis complete; remediation plan in flight
- [ ] Evidence collection workflow running for at least one full cycle
- [ ] Policy set reviewed, versioned, published to employees
- [ ] Training completion at target threshold
- [ ] Vendor/subservice organization list + attestations gathered

### 30 days before
- [ ] All policies signed off by exec sponsor
- [ ] Sample evidence reviewed by internal audit / compliance lead for each control
- [ ] Interview schedule set with control owners
- [ ] Auditor portal access provisioned
- [ ] Remediation items either closed or formally risk-accepted with rationale

### During fieldwork
- [ ] Daily standup with compliance lead + auditor PoC
- [ ] Log every auditor request with timestamp, responder, artifact
- [ ] Escalate any finding immediately to exec sponsor; don't wait for the report

### Post-audit
- [ ] Review draft report for factual accuracy (you can challenge findings)
- [ ] Management response drafted for any exceptions
- [ ] Remediation plan for findings with owners and dates
- [ ] Lessons learned retro → feed back into next cycle's control inventory

## Evidence Collection Workflow

Good evidence has five properties: **authentic** (comes from the system of record), **complete** (covers the entire observation period), **timestamped**, **reproducible** (same query → same result), and **tied to a control**.

### Pattern: continuous evidence over point-in-time

Auditors increasingly prefer continuous evidence (daily/weekly automated exports) over point-in-time screenshots. Automate where possible:

- IAM: scheduled export of user-to-role, role-to-permission, privileged accounts
- Change management: webhook from change tool → evidence bucket
- Monitoring: retain alert logs + on-call response logs
- Access reviews: completion records with attestation timestamps
- Training: LMS completion exports

### Anti-patterns

- **Screenshot-only evidence** — auditors flag as weak; it's a single point in time and easy to fabricate.
- **Evidence collected the week before audit** — doesn't demonstrate control operated throughout the period.
- **Evidence in personal drives** — chain of custody is broken.
- **No control owner** — "Security team" isn't an owner; one named person is.

## Compliance as Competitive Advantage

Compliance is product marketing for regulated buyers. How to position:

- **Don't say "we are SOC 2 compliant."** Say "SOC 2 Type 2 report available under NDA; ISO 27001 certified; GDPR-ready with DPA."
- **Map to buyer's framework, not yours.** A FedRAMP-pursuing federal buyer doesn't care that you have SOC 2; translate your controls to their 800-53 needs.
- **Security portal** — hosting your SOC 2 report, pen test summary, DPA, sub-processor list behind a simple NDA-gated portal cuts procurement time from weeks to days.
- **Turnaround time on security questionnaires** is a sales KPI. Track it.
- **Shared responsibility matrix** — be explicit about what you cover vs. what the customer must implement.

## Framework Decision Guide

When leadership asks "should we pursue X?":

| Signal | Consider |
|--------|----------|
| Deals lost citing compliance | SOC 2 Type 2 (US), ISO 27001 (global), both if both |
| Regulated vertical target (healthcare/fin/fed) | HIPAA+BAA / PCI DSS / FedRAMP |
| Federal pipeline >10% of revenue plan | FedRAMP Moderate (18-24 month investment) |
| DoD pipeline | CMMC Level 2 |
| EU customer concerns | GDPR first, then ISO 27701 |
| Healthcare at scale | HITRUST e1 → i1 → r2 progressive |

Don't chase certifications that don't unlock revenue. Each framework is a sustained operational commitment, not a one-time project.

## Output formats

Based on the request, produce:

- **Compliance status dashboard** — framework × control × status × owner × next evidence date
- **Gap analysis report** — as formatted above
- **Audit prep plan** — 90/30/0-day checklist tailored to the specific framework
- **Control-to-feature mapping** — product team deliverable
- **Security questionnaire response** — per-question answer with evidence pointer
- **Framework ROI memo** — projected revenue unlock × effort estimate × ongoing cost
- **Shared responsibility matrix** — customer-facing

## Common pitfalls

- Treating compliance as a one-time project, not an ongoing program
- Letting policies drift from reality — auditors interview people; mismatches blow up the audit
- Over-scoping (auditing systems that don't need to be in scope)
- Under-scoping (carving out a system that the auditor will rightly pull back in)
- Confusing frameworks: SOC 2 is an attestation, ISO 27001 is a certification, PCI is a validation — they have different artifacts and different meanings to a buyer
- Hiring a compliance firm that doubles as your auditor → independence problem
- Letting sales promise a SOC 2 Type 2 date the observation window mathematically can't meet
