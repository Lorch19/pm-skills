# Operator Kit — Backlog

## Urgent

- [ ] **Learning session on Operator Kit** — Walk through the full kit end-to-end: what each pack does, when to use which skill, how routing works (CLAUDE.md → NAVIGATOR.md → SKILL.md), and hands-on practice with the top 5 daily drivers. Goal is fluency, not just awareness.

## Priority

- [ ] **Split skill-creator into SKILL.md + references** — At 486 lines, skill-creator exceeds the 500-line guideline and reads like documentation. Extract the eval-viewer workflow, Claude.ai/Cowork-specific instructions, and description optimization into `references/` files. Keep SKILL.md under 300 lines with the core loop + pointers.
- [ ] **Add worked examples to pm-frameworks skills** — Several pm-frameworks skills (strategy-craft, prioritization-advisor, pestel-analysis, opportunity-solution-tree) reference templates without showing concrete output. Add a short "Example Output" section to the 5-10 most-used skills showing what good output looks like.

## Strategic

- [ ] **Add NAVIGATOR.md to analytics-tools and gtm-tools** — pm-frameworks, domain-tools, and pm-agents each have a NAVIGATOR.md decision tree. analytics-tools (3 skills) and gtm-tools (3 skills) are missing one. Small packs but a navigator helps routing.
- [ ] **Reduce doc-coauthoring to under 250 lines** — Currently 326 lines. The Stage 2 section (Refinement & Structure) is verbose with repeated step patterns. Consolidate the 6 sub-steps into a tighter loop description.

## Non-priority

- [ ] **Add `type`/`best_for` to remaining pm-agents skills** — 12 of 13 pm-agents skills still lack `best_for` frontmatter (only strategy-craft has it). Low urgency since pm-agents routes via commands, but standardizing improves discoverability.
- [ ] **Verify pdf skill references exist** — pdf/SKILL.md references `REFERENCE.md` and `FORMS.md`. Verify these files exist and are up to date; add a table of contents if they exceed 300 lines.
