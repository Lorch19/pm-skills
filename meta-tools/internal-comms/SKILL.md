---
name: internal-comms
description: Write internal communications — status reports, leadership updates, 3P updates, roadmap updates, launch announcements, RFCs, executive briefings, release notes, sprint reviews, incident one-pagers, FAQs, decisions-needed memos, project updates. TRIGGER when asked to write any internal communication document.
---

# Internal Communications

Write clear, audience-appropriate internal communications. Identify the document type, select the matching template, adapt tone for the audience, and run the pre-send checklist before delivering.

---

## Step 1: Identify Document Type

Ask yourself two questions:
1. **What action do I need from the reader?** (Inform / Decide / Align / Approve)
2. **Who is the primary audience?** (See audience matrix below)

Then select the matching template.

---

## Templates

### 1. 3P Update (Progress, Plans, Problems)

**Use when:** Regular team or cross-functional status update.
**Cadence:** Weekly or biweekly.

```markdown
## [Team/Project] — 3P Update ([Date])

### Progress (what we shipped/completed)
- [Accomplishment] — [Impact/metric]
- [Accomplishment] — [Impact/metric]

### Plans (next 1-2 weeks)
- [Work item] — [Owner] — [Target date]
- [Work item] — [Owner] — [Target date]

### Problems (blockers, risks, asks)
- [Issue] — [Impact if unresolved] — [Ask: what you need from the reader]
```

---

### 2. Roadmap Update

**Use when:** Communicating roadmap changes, reprioritization, or quarterly planning outcomes.
**Audience:** Cross-functional stakeholders, leadership.

```markdown
## Roadmap Update — [Quarter/Period]

### What changed and why
[1-2 sentences: the business context driving the change]

### New priorities
| Priority | Description | Target | Why now |
|----------|------------|--------|---------|
| 1 | [Feature/initiative] | [Date] | [Business driver] |
| 2 | [Feature/initiative] | [Date] | [Business driver] |

### What moved out or down
| Item | Previous priority | New status | Reason |
|------|------------------|------------|--------|
| [Item] | [Was P1/P2] | [Deferred / Descoped / Deprioritized] | [Reason] |

### What this means for your team
- **Engineering:** [Impact]
- **Sales:** [Impact on positioning/timelines]
- **Support:** [Impact on customer expectations]

### Questions? 
[Contact person] by [date] — or reply to this thread.
```

---

### 3. Feature Launch Announcement

**Use when:** Shipping a new feature or major update. Internal version (not customer-facing release notes).
**Audience:** All-hands or cross-functional.

```markdown
## [Feature Name] is live 🚀

**What:** [One sentence — what it does for users]
**Who it affects:** [Customer segment / all users / internal only]
**Available:** [Date] — [GA / Beta / Limited availability]

### Why we built this
[2-3 sentences: customer problem, business case]

### What to know
- **Sales:** [Talk track / positioning change / new objection handling]
- **Support:** [Known issues / expected questions / escalation path]
- **Marketing:** [Messaging approved? Launch campaign details?]

### Demo / Docs
- [Link to demo recording]
- [Link to help docs or internal wiki]

### Feedback
[Channel for internal feedback — Slack channel, form, or person]
```

---

### 4. RFC (Request for Comments)

**Use when:** Proposing a significant decision that needs cross-functional input before committing.
**Audience:** Stakeholders whose input you need.

```markdown
## RFC: [Proposal Title]

**Author:** [Name]
**Status:** Open for comments until [Date]
**Decision needed by:** [Date]
**Approver:** [Who makes the final call]

### Context
[What situation or problem prompted this proposal. 3-5 sentences max.]

### Proposal
[What you're proposing. Be specific enough that someone could implement it.]

### Alternatives considered
| Option | Pros | Cons | Why not chosen |
|--------|------|------|---------------|
| [Alt 1] | [Pros] | [Cons] | [Reason] |
| [Alt 2] | [Pros] | [Cons] | [Reason] |

### Impact
- **Cost:** [Engineering effort, infrastructure, money]
- **Risk:** [What could go wrong]
- **Timeline:** [How long to implement]
- **Reversibility:** [Easy to undo? Hard to undo?]

### Open questions
1. [Question you want input on]
2. [Question you want input on]

### How to comment
[Slack thread / doc comments / meeting on X date]
```

---

### 5. Executive Briefing

**Use when:** Updating C-suite or VP+ on a topic that requires their awareness or decision.
**Audience:** Executives (optimize for skimmability — they have 2 minutes).

```markdown
## [Topic] — Executive Briefing

**Date:** [Date]
**TL;DR:** [One sentence — the single most important thing]

### Situation (what's happening)
[2-3 bullet points. Facts only, no opinions.]

### Implication (why it matters)
[2-3 bullet points. Business impact: revenue, risk, timeline, competitive.]

### Recommendation (what to do)
[1-2 bullet points. Your recommended action with expected outcome.]

### Decision needed
- [ ] [Specific decision with options, if applicable]
- **Deadline:** [When you need the answer]

### Supporting detail
[Link to deeper doc for those who want to dig in. Don't put it inline.]
```

---

### 6. Decisions-Needed Memo

**Use when:** You need a decision from a specific person and want to make it easy for them.
**Audience:** The decision-maker.

```markdown
## Decision Needed: [Topic]

**Decision maker:** [Name]
**Deadline:** [Date — and why this date]
**Prepared by:** [Your name]

### Context
[3-5 sentences — just enough to frame the decision]

### Options

**Option A: [Name]**
- Pros: [Bullet points]
- Cons: [Bullet points]
- Cost/effort: [Estimate]

**Option B: [Name]**
- Pros: [Bullet points]
- Cons: [Bullet points]
- Cost/effort: [Estimate]

**Option C: [Name / "Do nothing"]**
- Pros: [Bullet points]
- Cons: [Bullet points]

### Recommendation
[Option X], because [1-2 sentence reasoning].

### What happens next
If approved, [who does what by when].
```

---

### 7. Release Notes (Customer-Facing)

**Use when:** Communicating product changes to customers.
**Audience:** End users, account managers, support team.

```markdown
## Release Notes — [Version / Date]

### New
- **[Feature name]** — [What it does, one sentence]. [Link to docs]

### Improved
- **[Feature name]** — [What changed and why it's better]

### Fixed
- **[Bug description]** — [What users experienced → what happens now]

### Breaking changes
- **[Change]** — [What you need to do before/after upgrading]

### Coming soon
- [Teaser for next release — optional, only if committed]
```

---

### 8. Sprint Review Summary

**Use when:** Summarizing sprint outcomes for stakeholders who didn't attend the review.
**Audience:** Cross-functional stakeholders, leadership.

```markdown
## Sprint Review — Sprint [N] ([Date Range])

### Sprint goal: [Goal statement]
**Outcome:** [Met / Partially met / Not met]

### What shipped
| Item | Status | Demo |
|------|--------|------|
| [Story/feature] | Done | [Link or "shown live"] |
| [Story/feature] | Done | [Link or "shown live"] |

### What didn't ship (and why)
| Item | Status | Reason | New target |
|------|--------|--------|------------|
| [Story] | Carried over | [Blocker/dependency] | Sprint [N+1] |

### Key learnings
- [Insight that affects future work]

### Next sprint focus
- [Top 2-3 priorities for next sprint]
```

---

### 9. Incident One-Pager

**Use when:** Post-incident summary for non-technical stakeholders (not the full postmortem).
**Audience:** Leadership, sales, support — anyone who needs to know what happened without the engineering detail.

```markdown
## Incident Summary: [Title]

**Severity:** [P1/P2/P3]
**Duration:** [Start time] to [End time] ([total hours])
**Customer impact:** [Who was affected and how]

### What happened
[3-5 sentences. Plain language, no jargon.]

### What we did
[Timeline of key response actions — 3-5 bullets]

### Current status
[Resolved / Monitoring / Ongoing mitigation]

### Customer communication
- [What we told customers, when, via what channel]
- [Follow-up communication planned?]

### What we're doing to prevent recurrence
1. [Action item] — [Owner] — [Target date]
2. [Action item] — [Owner] — [Target date]

### Full postmortem
[Link — available by [date]]
```

---

### 10. FAQ Document

**Use when:** Anticipated questions about a change, launch, or decision.
**Audience:** Varies — specify who this FAQ is for at the top.

```markdown
## FAQ: [Topic]

**Audience:** [Who this FAQ is written for]
**Last updated:** [Date]

### [Question 1 — written exactly as the reader would ask it]
[Direct answer — first sentence answers the question. Then 1-2 sentences of context. Keep under 100 words.]

### [Question 2]
[Direct answer.]

### [Question 3]
[Direct answer.]

---
*Don't see your question? Ask in [channel] or contact [person].*
```

---

## Audience Adaptation Matrix

Different audiences need different framing of the same information:

| Audience | Lead with | Tone | Length | Jargon level | What they care about |
|----------|----------|------|--------|-------------|---------------------|
| **Executives** | Business impact + recommendation | Direct, confident | Short (< 1 page) | Business terms only | Revenue, risk, timeline, competitive |
| **Engineering** | Technical context + requirements | Precise, detailed | Medium-long | Technical OK | Scope, constraints, dependencies |
| **Sales** | Customer impact + talk track | Action-oriented | Short (bullets) | Product terms, no eng jargon | What to say, what changed, how to position |
| **Support** | What customers will experience | Empathetic, practical | Medium (bullets + examples) | Customer-facing terms | Known issues, workarounds, escalation path |
| **All-hands** | "So what" + human story | Warm, clear | Short-medium | Minimal | Why this matters, what's changing, what's next |
| **Cross-functional** | Shared context + your ask | Collaborative | Medium | Define terms on first use | What you need from them, impact on their work |
| **Board / investors** | Metrics + strategy | Formal, data-backed | Short + appendix | Business/financial terms | Growth, unit economics, market position |

**Rule of thumb:** Write for the busiest person in your audience. They'll skim. The detail-oriented people will ask follow-up questions — that's fine.

---

## Anti-Patterns

Avoid these common failure modes:

| Anti-Pattern | What it looks like | Fix |
|---|---|---|
| **The Wall of Text** | 800-word email with no headers, bullets, or structure | Structure first, prose second. If it's longer than a screen, add a TL;DR. |
| **The Buried Lead** | The actual ask or news is in paragraph 4 | Put the most important thing in the first sentence. Always. |
| **The No-Ask** | "Just wanted to share an update..." with no clear action needed | Every comm should answer: "What do you want me to do with this information?" If the answer is "nothing," reconsider whether to send it. |
| **The Jargon Bomb** | Internal codenames, acronyms, and technical terms without definition | Define on first use. If your audience doesn't know what "the Kraken migration" is, say "the database migration (Project Kraken)." |
| **The Premature Send** | Sending before you've identified your audience and their "so what" | Always fill in: "This is for [audience] and the main point is [X]" before writing. |
| **The Apology Tour** | Leading bad news with excessive hedging and apologizing | State the fact, state the impact, state the fix. Empathy yes, groveling no. |
| **The FYI Flood** | CC'ing everyone "just in case" | Ask: "Would this person's week change based on this information?" If no, don't send. |

---

## Pre-Send Checklist

Before sending any internal communication:

- [ ] **Audience identified** — you know exactly who's reading this
- [ ] **"So what" clear** — the first sentence or TL;DR answers why this matters
- [ ] **Ask is explicit** — if you need something, it's stated clearly with a deadline
- [ ] **Right length for audience** — execs get 1 page, engineers get detail, sales gets bullets
- [ ] **Jargon check** — no unexplained acronyms or internal codenames
- [ ] **Tone matches context** — good news is warm, bad news is direct, asks are respectful
- [ ] **Links work** — every referenced doc, demo, or dashboard is accessible to the audience
- [ ] **Right channel** — email for formal/archival, Slack for quick/conversational, doc for collaborative

---

## Tone Guidelines

- **Clear over clever** — Say what you mean. Puns and wordplay waste the reader's time.
- **Concise** — Respect people's time. Cut every sentence that doesn't add information.
- **Action-oriented** — Every communication should answer "so what?" and "now what?"
- **Honest** — Bad news delivered early builds trust. Bad news discovered late destroys it.
- **Specific** — "Revenue is down" is useless. "MRR dropped 8% ($12K) due to 3 enterprise churns in March" is actionable.
