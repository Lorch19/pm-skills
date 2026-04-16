---
name: compliance-tracking
description: Track compliance requirements and audit readiness. TRIGGER when user mentions "compliance", "audit prep", "SOC 2", "ISO 27001", "GDPR", "FedRAMP", "NIST", "CMMC", "regulatory requirement", or needs help tracking, preparing for, or documenting compliance activities.
---

# Compliance Tracking

Track compliance requirements, prepare for audits, and maintain regulatory readiness across multiple frameworks simultaneously.

---

## Framework Reference

### Tier 1 — Most Common

| Framework | Focus | Scope | Key Requirements |
|-----------|-------|-------|-----------------|
| **SOC 2** | Service organizations | US, global adoption | 5 Trust Services Criteria (TSC): security, availability, processing integrity, confidentiality, privacy. Type I = point-in-time; Type II = over a period (typically 6-12 months). |
| **ISO 27001** | Information security management | Global | Annex A controls (93 controls in 4 themes). Risk assessment → Statement of Applicability → continuous improvement cycle. Certification valid 3 years with annual surveillance audits. |
| **GDPR** | Data privacy | EU/EEA + any org processing EU resident data | Lawful basis for processing, data subject rights (access, erasure, portability), 72-hour breach notification, Data Protection Officer, Data Protection Impact Assessments. |
| **HIPAA** | Healthcare data | US | PHI safeguards: administrative, physical, technical. Business Associate Agreements. Breach notification (60 days to HHS). No formal certification — compliance is self-attested + auditable. |
| **PCI DSS** | Payment card data | Global (any org handling cardholder data) | 12 requirements across 6 goals. Annual assessment (SAQ or QSA audit). Quarterly vulnerability scans by ASV. |

### Tier 2 — Government & Sector-Specific

| Framework | Focus | Scope | Key Requirements |
|-----------|-------|-------|-----------------|
| **FedRAMP** | Cloud services for US federal agencies | US federal | NIST 800-53 control baseline (Low/Moderate/High). 3PAO assessment. Continuous monitoring (ConMon). Authorization through JAB or agency. |
| **StateRAMP** | Cloud services for US state/local government | US state/local | Mirrors FedRAMP structure. Three security categories. Growing adoption across states. |
| **NIST CSF 2.0** | Cybersecurity risk management | US (voluntary, widely adopted) | 6 functions: Govern, Identify, Protect, Detect, Respond, Recover. Framework profiles + tiers. Not a certification — a risk management guide. |
| **NIST 800-53** | Security and privacy controls | US federal systems | 20 control families, 1000+ controls. Basis for FedRAMP. Rev 5 adds supply chain and privacy. |
| **CMMC 2.0** | Defense supply chain cybersecurity | US DoD contractors | 3 levels: Foundational (17 practices), Advanced (110 practices = NIST 800-171), Expert. Level 2+ requires 3rd-party assessment. |
| **HITRUST CSF** | Healthcare + cross-industry | US healthcare ecosystem | Harmonizes HIPAA, SOC 2, ISO 27001, NIST. r2 assessment (2-year certification). Prescriptive controls mapped across frameworks. |
| **ISO 27701** | Privacy information management | Global | Extension to ISO 27001 for privacy. Maps to GDPR requirements. Covers PII controllers and processors. |
| **TX-RAMP** | Cloud services for Texas state agencies | Texas | Three levels (1-3). Aligns with NIST 800-53 and FedRAMP. Required for Texas state agency contracts. |

### Framework Relationships

Understanding how frameworks overlap saves duplicate work:

```
NIST 800-53 (master control set)
├── FedRAMP (federal cloud subset + ConMon)
│   └── StateRAMP (mirrors FedRAMP for state/local)
├── NIST 800-171 (CUI protection subset)
│   └── CMMC Level 2 (= NIST 800-171 + assessment)
└── NIST CSF 2.0 (risk management overlay — maps to 800-53)

ISO 27001 (international standard)
└── ISO 27701 (privacy extension → maps to GDPR)

HITRUST CSF (harmonization layer)
└── Maps to: HIPAA, SOC 2, ISO 27001, NIST, PCI DSS

SOC 2 Trust Services Criteria
└── Maps closely to ISO 27001 Annex A (significant overlap)
```

**Practical implication:** If you're SOC 2 Type II compliant, you're ~60-70% of the way to ISO 27001. If you have a NIST 800-53 Moderate baseline, you cover most of FedRAMP. Plan your compliance roadmap to stack frameworks efficiently.

---

## Control-to-Feature Mapping

Map product features to compliance controls to answer: "Which controls does this feature satisfy?" and "What features do we need to satisfy this control?"

### Mapping Template

```markdown
## Control Mapping: [Feature Name]

**Feature:** [Name and brief description]
**Owner:** [Team/person responsible]

| Framework | Control ID | Control Name | How Feature Satisfies | Evidence Type |
|-----------|-----------|-------------|----------------------|---------------|
| SOC 2 | CC6.1 | Logical access security | [Specific mechanism] | [Config screenshot / log export / policy doc] |
| ISO 27001 | A.8.3 | Access restriction | [Specific mechanism] | [Same or different evidence] |
| NIST 800-53 | AC-2 | Account management | [Specific mechanism] | [Same or different evidence] |

**Gaps:** [Controls this feature partially covers — what else is needed]
**Dependencies:** [Other features/processes required for full control coverage]
```

### How to Build the Mapping

1. **Start from your feature list** — for each shipped feature, identify which access, security, privacy, or logging controls it touches
2. **Cross-reference framework control catalogs** — SOC 2 TSC, ISO 27001 Annex A, NIST 800-53 families
3. **Note partial vs. full coverage** — a feature may address the technical requirement but not the policy/procedural requirement
4. **Track evidence type per control** — auditors need specific evidence artifacts; know what you'll provide before audit day

---

## Audit Preparation

### 90-Day Countdown

**Days 90-60: Foundation**
- [ ] Confirm audit scope (which systems, which frameworks, which trust services criteria)
- [ ] Identify audit firm and lead auditor; schedule kickoff call
- [ ] Inventory all in-scope systems, vendors, and data flows
- [ ] Review prior audit findings and verify remediation is complete
- [ ] Update control-to-feature mappings for any product changes since last audit
- [ ] Verify all required policies are current (review dates within 12 months)

**Days 60-30: Evidence Collection**
- [ ] Pull evidence for each control per the evidence matrix
- [ ] Validate that automated evidence (logs, configs, scan reports) covers the full audit period
- [ ] Conduct internal testing on 10-15% of controls (sample the way auditors will)
- [ ] Remediate any gaps found during internal testing
- [ ] Brief control owners on auditor expectations and interview format
- [ ] Prepare the evidence repository (organized by control family, labeled consistently)

**Days 30-0: Final Prep**
- [ ] Conduct readiness review with all control owners
- [ ] Verify no policy exceptions are outstanding without documented risk acceptance
- [ ] Run vulnerability scan and remediate critical/high findings
- [ ] Prepare the management assertion letter (SOC 2) or Statement of Applicability (ISO 27001)
- [ ] Schedule auditor access to systems, rooms, and key personnel
- [ ] Create a "day of" logistics doc: Wi-Fi, room bookings, point of contact, escalation path

### Evidence Workflow

For each control, maintain:

```markdown
## Evidence: [Control ID] — [Control Name]

**Control owner:** [Name]
**Evidence type:** [Automated / Manual / Policy document]
**Collection frequency:** [Continuous / Quarterly / Annual]
**Storage location:** [Path or system]
**Last collected:** [Date]
**Audit period coverage:** [Start] to [End]

### Evidence artifacts
1. [Artifact name] — [Description] — [Location]
2. [Artifact name] — [Description] — [Location]

### Auditor notes
- [Any context the auditor will need to interpret this evidence]
```

**Evidence quality checklist:**
- Covers the full audit period (no gaps)
- Includes timestamps proving when the control was in effect
- Shows the control operating effectively, not just that it exists
- Is readable without deep product knowledge (auditors aren't your engineers)
- Doesn't contain sensitive data beyond what's needed (redact PII from samples)

---

## Gap Analysis

### Gap Analysis Template

```markdown
## Compliance Gap Analysis: [Framework]

**Assessment date:** [Date]
**Assessor:** [Name/team]
**Target certification date:** [Date]

| Control ID | Requirement Summary | Current State | Gap | Severity | Remediation | Owner | Target Date |
|-----------|-------------------|--------------|-----|----------|-------------|-------|------------|
| [ID] | [What's required] | [What exists today] | [What's missing] | Critical/High/Medium/Low | [Specific fix] | [Person] | [Date] |

### Summary
- **Controls assessed:** [N]
- **Fully met:** [N] ([%])
- **Partially met:** [N] ([%])
- **Not met:** [N] ([%])
- **Not applicable:** [N]

### Critical path items
1. [Highest-severity gap with timeline risk]
2. [Second-highest]
3. [Third]

### Estimated effort to close all gaps
- Engineering: [N] person-weeks
- Policy/process: [N] person-weeks
- Vendor/procurement: [N] items
```

---

## Framework Decision Guide

Use this when deciding which framework to pursue next:

| If you need to... | Start with... | Why |
|---|---|---|
| Sell to US enterprise SaaS | SOC 2 Type II | Table stakes — most enterprise procurement requires it |
| Sell to EU customers | GDPR compliance + SOC 2 | GDPR is legal requirement; SOC 2 builds trust |
| Sell to US federal | FedRAMP (Moderate) | Required for federal cloud contracts; build on NIST 800-53 |
| Sell to US state/local | StateRAMP or TX-RAMP | Growing requirement for state contracts |
| Sell to DoD supply chain | CMMC Level 2 | Required for CUI handling in defense contracts |
| Sell to healthcare | HIPAA + HITRUST | HIPAA is legal; HITRUST r2 differentiates |
| Go international | ISO 27001 | Globally recognized; good foundation for ISO 27701 (privacy) |
| Stack efficiently | SOC 2 → ISO 27001 → FedRAMP | Each builds on the prior; ~60-70% control overlap between SOC 2 and ISO 27001 |

---

## Compliance as Competitive Advantage

Compliance isn't just a checkbox — it's a GTM lever:

1. **Sales acceleration** — "SOC 2 Type II certified" removes a procurement blocker and shortens sales cycles by 2-4 weeks
2. **Market access** — FedRAMP/StateRAMP/CMMC open government markets that competitors without certification can't enter
3. **Trust signal** — In security-sensitive markets, compliance certifications signal operational maturity
4. **Pricing power** — Compliance-certified products command premium pricing vs. uncertified alternatives
5. **Competitive moat** — Certification takes 6-18 months; competitors who start later face a real time disadvantage

When positioning compliance work to leadership, frame it as market access and revenue acceleration, not just risk mitigation.

---

## Output

Produce any combination of:
- **Compliance status dashboard** — framework-by-framework readiness percentage with control-level detail
- **Gap analysis** — per the template above, with severity ranking and remediation plan
- **Audit prep checklist** — 90/60/30/0-day countdown with assigned owners
- **Evidence collection plan** — per-control evidence matrix with collection schedule
- **Control-to-feature mapping** — which product features satisfy which controls
- **Framework recommendation** — which framework to pursue next based on business goals
- **Compliance roadmap** — multi-framework stacking plan with timeline and effort estimates
