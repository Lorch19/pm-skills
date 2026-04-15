---
name: internal-comms
description: Write internal communications — status reports, leadership updates, 3P updates, roadmap updates, feature launch announcements, RFCs, executive briefings, release notes, company newsletters, FAQs, incident reports, decisions-needed memos, sprint review summaries. TRIGGER when asked to write any internal-facing communication document.
---

## When to use this skill

Any internal-facing written communication where clarity, audience-fit, and action-orientation matter. Includes:

- Status updates (3P, weekly, monthly)
- Roadmap updates
- Feature launch announcements
- Technical RFCs / proposals
- Executive briefings
- Release notes (internal + customer-facing)
- Sprint review summaries
- Decisions-needed memos
- Company newsletters
- FAQ responses
- Incident reports & post-mortems
- Team/project retros

## How to use this skill

1. **Identify the communication type.** If ambiguous, ask.
2. **Clarify the audience** — engineers, leadership, cross-functional, customers, board. Audience drives everything else.
3. **Clarify the ask.** Is the reader meant to *know*, *decide*, or *act*? If decide/act, make the ask explicit up front.
4. **Apply the format** from the templates below.
5. **Run the quality checks** at the bottom before delivering.

## Core principle: lead with the "so what"

Readers are busy. The first sentence should answer:
- What is this about?
- Why should I care?
- What (if anything) do you need from me?

Not: "As part of our ongoing effort to..."

---

## Templates

### 3P Update (Progress, Plans, Problems)

Best for weekly team status.

```markdown
## [Team/Project] — 3P Update ([Date])

### TL;DR
[One sentence: are we on track, at risk, or blocked?]

### Progress (shipped this period)
- [Accomplishment] → [Impact / metric moved]

### Plans (next period)
- [Planned work] → [Target date or milestone]

### Problems / Asks
- [Issue] → [Ask: who, what, by when]
```

### Roadmap Update

For stakeholders tracking a body of work over months.

```markdown
## [Product Area] Roadmap — [Quarter / Month]

### Where we are
- In flight: [item] ([% complete], target: [date])
- Shipped since last update: [items with links]
- Deferred: [item] — why

### What's next
- Next up: [item] — why this, why now
- After that: [item(s) with rough sequencing]

### Changes since last update
- Added: [item] — driver
- Removed/deferred: [item] — driver

### Risks
- [Risk] → [Mitigation or decision needed]

### Decisions needed
- [Decision] — from whom — by when
```

### Feature Launch Announcement (internal)

```markdown
## Launching: [Feature Name] — [Date]

### What it is (one paragraph)
[Plain-English description. No marketing fluff. Who gets it, what changes.]

### Why it matters
- Customer problem: [...]
- Business impact: [...]

### How to talk about it
- With customers: [one-liner positioning]
- With prospects: [competitive angle if relevant]
- Internally: [shorthand name]

### What's in / not in
- In: [capabilities]
- Not in (yet): [known gaps, to set expectations]

### Enablement
- Demo: [link]
- Docs: [link]
- FAQ: [link]
- Owner for questions: [person]

### Rollout
- GA: [date]
- Who gets it: [all / specific segment / opt-in]
- Rollback plan: [brief]
```

### Technical RFC / Proposal

```markdown
## RFC: [Title]
**Author:** [name]  **Status:** draft | in review | approved | rejected
**Deciders:** [names]  **Deadline for input:** [date]

### Problem
[What are we solving? Why now?]

### Constraints
[Budget, timeline, team, tech stack, compliance requirements]

### Proposal
[The recommended approach. One diagram if it helps.]

### Alternatives considered
1. [Alternative] — rejected because [...]
2. [Alternative] — rejected because [...]

### Trade-offs of the proposal
- Pro: [...]
- Con: [...]
- Risk: [...]

### Rollout plan
[How we ship this without breaking things]

### Open questions
- [Question] — needs [person] to weigh in
```

### Executive Briefing

For 1-pagers going to a CEO / VP audience. Every word earns its place.

```markdown
## [Topic] — [Audience]
**Author:** [name]  **Date:** [date]  **Ask:** [nothing / input / decision / approval]

### Bottom line
[One sentence. The key takeaway an exec should remember if they read nothing else.]

### Context (3-5 bullets)
- [Background they need]

### Options (if a decision is needed)
| Option | Pro | Con | Cost | Recommendation |
|--------|-----|-----|------|----------------|
| A | ... | ... | ... | ← Recommended |
| B | ... | ... | ... | |

### Recommendation
[Which option and why, in 2-3 sentences.]

### Risks
[2-3 bullets. What could go wrong, how we'd respond.]

### Next steps
- [Action] — [owner] — [date]
```

### Decisions Needed Memo

When you need a decision faster than an async thread can deliver.

```markdown
## Decision Needed: [Short framing of the question]
**From:** [author]  **To:** [decider(s)]  **By:** [deadline]

### The question
[One sentence.]

### Why it matters (1-3 bullets)
- [Impact if we decide Yes]
- [Impact if we decide No]
- [Cost of not deciding]

### Options
- **Option A: [name]** — [one paragraph]. Cost: [...]. Risk: [...].
- **Option B: [name]** — [one paragraph]. Cost: [...]. Risk: [...].

### My recommendation
[Which option and why. Be opinionated.]

### What I need from you
[Specific ask: approve / veto / weigh in on X / escalate.]
```

### Customer-Facing Release Notes

```markdown
## [Product] — [Version / Date]

### New
- **[Feature]** — [one-sentence benefit]. [Link to docs]

### Improved
- **[Area]** — [what changed, why it helps]

### Fixed
- [Issue that was visible to customers]

### Coming soon
- [Teaser of what's next, only if approved for external mention]
```

### Sprint Review Summary

For stakeholders who don't attend the live review.

```markdown
## Sprint [N] Review — [Date range]

### Shipped
- [Item] — [demo link if available]

### Didn't ship (and why)
- [Item] — [reason, carried to next sprint / deferred / descoped]

### What we learned
- [Insight from this sprint — technical, customer, process]

### Next sprint focus
- [Theme / top 3 items]
```

### Incident Report (brief)

For a full post-mortem, use `operations-tools/runbook` or `engineering-tools/incident-response`. This is the one-pager summary.

```markdown
## Incident: [Short title] — [Date]
**Severity:** Sev-X  **Duration:** [start] – [end]  **Customer impact:** [scope]

### What happened
[2-3 sentence summary.]

### Why it happened
[Root cause in plain English.]

### What we did
[Mitigation steps taken.]

### What we'll do
- [Action] — [owner] — [date]

### What went well
- [Things to preserve]

### Full post-mortem
[Link]
```

### FAQ Response

```markdown
**Q: [Question as asked]**

[Direct answer in the first sentence.]

[Context / reasoning in 1-2 sentences.]

[Anticipated follow-up handled or pointer to where to go next.]
```

---

## Audience Adaptation

Same facts, different framings. Pick based on who's reading.

| Audience | Leads with | Cares about | Length | Tone |
|----------|-----------|-------------|--------|------|
| **Engineering team** | Technical context, trade-offs | Correctness, maintainability, unknowns | Medium-long | Direct, precise |
| **Product peers** | Problem, hypothesis, outcome | User impact, prioritization trade-offs | Medium | Collaborative |
| **Leadership / exec** | Bottom line, business impact | Strategy fit, risk, resource use | Short | Concise, confident |
| **Cross-functional (sales/CS/marketing)** | What they can now say/do | Customer-facing implications | Short | Practical |
| **Company-wide** | The "why" and the "wow" | Story, culture, progress | Medium | Warm, clear |
| **Customers** | What changes for them | Benefit, not feature list | Short | Accessible, no jargon |
| **Board** | Scorecard, deviations from plan | Strategy, capital use, risk | Very short + appendix | Precise, unvarnished |

---

## Anti-patterns

- **The wall of text.** Nobody reads it. Break into sections with headers.
- **The buried lead.** The most important sentence is in paragraph 4. Move it to the top.
- **The no-ask.** Five paragraphs and no clear action for the reader. Every comm needs an "and therefore..." — even if it's "just FYI, no action needed."
- **The corporate-speak hedge.** "We're exploring opportunities to potentially optimize..." Say what you mean.
- **The false 3P.** Listing done tasks with no impact, and planned tasks with no dates. 3P is about *outcomes and direction*, not task tracking.
- **The decision dump.** Listing 8 options with no recommendation. If you're the author, have an opinion.
- **The surprise.** Bad news delivered late destroys trust. Surface it early even if incomplete.
- **Passive voice everywhere.** "It was decided that..." Name the decider.
- **Same update, every audience.** Tailor the framing; readers can tell when they're getting boilerplate.

## Tone guidelines

- **Clear over clever.** Say what you mean.
- **Concise.** Respect people's time. Cut every sentence that doesn't earn its place.
- **Action-oriented.** Every update answers "so what?" and "what now?"
- **Honest.** Bad news delivered early builds trust. Hedging destroys it.
- **Specific.** "We're on track" is weaker than "We're 3 days ahead of the 4/30 target." Dates and numbers > vibes.
- **Own it.** Write in first person (I/we) when you're the author. "This team..." is a dodge.

## Quality checks (run before sending)

- [ ] First sentence answers: what, why-care, what-you-want-from-me
- [ ] Length appropriate for audience (exec: short; engineering: as long as needed)
- [ ] Every ask has an owner and a date
- [ ] No jargon the audience won't recognize (or jargon is defined inline)
- [ ] No unnecessary qualifiers ("just", "maybe", "I think")
- [ ] Someone not in the room could act on this without a follow-up
