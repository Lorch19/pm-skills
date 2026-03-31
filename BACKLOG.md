# Operator Kit — Backlog

## Urgent

- [ ] **Learning session on Operator Kit** — Walk through the full kit end-to-end: what each pack does, when to use which skill, how routing works (CLAUDE.md → NAVIGATOR.md → SKILL.md), and hands-on practice with the top 5 daily drivers. Goal is fluency, not just awareness.

## High

- [ ] **Build `project-bootstrap` skill** — Scaffold CLAUDE.md + STATE.md + BACKLOG.md + docs/ + launch.json + context-sync for any project. Handles greenfield and retrofit. Mission: `missions/project-bootstrap-skill.md`
- [ ] **Build `context-sync-setup` skill** — Parameterized generator for context-sync scheduled tasks. Mission: `missions/context-sync-setup-skill.md`
- [ ] **Evaluate GitHub MCP integration** — Check claude.ai integrations page for GitHub MCP. Would unlock PR management, issue tracking from Claude directly. All 7 repos on GitHub (Lorch19).

## Priority

- [ ] **Split skill-creator into SKILL.md + references** — At 486 lines, skill-creator exceeds the 500-line guideline and reads like documentation. Extract the eval-viewer workflow, Claude.ai/Cowork-specific instructions, and description optimization into `references/` files. Keep SKILL.md under 300 lines with the core loop + pointers.
- [ ] **Add worked examples to pm-frameworks skills** — Several pm-frameworks skills (strategy-craft, prioritization-advisor, pestel-analysis, opportunity-solution-tree) reference templates without showing concrete output. Add a short "Example Output" section to the 5-10 most-used skills showing what good output looks like.
- [ ] **Build `deploy-rsync` skill** — Codify the rsync+SSH deploy pattern from portfolio-system/scripts/deploy.sh into a reusable meta-tool. Mission: `missions/deploy-rsync-skill.md`
- [ ] **Build `health-check-monitor` skill** — Unified cross-project health digest (VPS, Railway, scheduled tasks) → single Telegram message. Mission: `missions/health-check-monitor-skill.md`
- [ ] **Evaluate Supabase MCP integration** — Direct DB queries and schema inspection for first-bloom-build + lorchprotfoliotracker.
- [ ] **Extract shared CLAUDE.md boilerplate** — Co-founder persona, session discipline, operational protocol sections are identical across 5 projects. Move to `~/.claude/skills/operational-discipline/SKILL.md`, replace with one-line pointers.

## Strategic

- [ ] **Add NAVIGATOR.md to analytics-tools and gtm-tools** — pm-frameworks, domain-tools, and pm-agents each have a NAVIGATOR.md decision tree. analytics-tools (3 skills) and gtm-tools (3 skills) are missing one. Small packs but a navigator helps routing.
- [ ] **Reduce doc-coauthoring to under 250 lines** — Currently 326 lines. The Stage 2 section (Refinement & Structure) is verbose with repeated step patterns. Consolidate the 6 sub-steps into a tighter loop description.
- [ ] **Evaluate Telegram MCP integration** — Custom bot code per-project could be replaced with unified MCP. Would simplify notification layer across portfolio-system and scheduled tasks.
- [ ] **Migrate existing packs to .claude-plugin format** — New packs (operations, engineering, sales, design) use `.claude-plugin/plugin.json`. Older packs (pm-frameworks, domain-tools, analytics-tools, gtm-tools, meta-tools) still use SKILL.md only. Migration enables marketplace publishing and claude.ai compatibility. Start with meta-tools (most active).
- [ ] **Add CONNECTORS.md to existing packs** — New packs use the `~~category` connector pattern for tool-agnostic integration. Add CONNECTORS.md to domain-tools, analytics-tools, and gtm-tools.
- [ ] **Port financial-services-plugins deep models** — Anthropic's financial-services-plugins repo has 3-statement-model, DCF, LBO, comps-analysis, PE due diligence skills. Significantly deeper than current financial-analyst. Port as extension to domain-tools or new finance-tools pack.
- [ ] **Evaluate claude-md-management plugin** — Anthropic's official plugin that audits/improves CLAUDE.md files and captures session learnings. Could enhance context-management skill.
- [ ] **Add hooks support to operator-kit** — Security-guidance hook is added to meta-tools. Consider adding SessionStart hooks for auto-loading context and PreToolUse hooks for quality gates. Follow Anthropic's hookify pattern for creating hooks from conversation patterns.

## Non-priority

- [ ] **Add `type`/`best_for` to remaining pm-agents skills** — 12 of 13 pm-agents skills still lack `best_for` frontmatter (only strategy-craft has it). Low urgency since pm-agents routes via commands, but standardizing improves discoverability.
- [ ] **Verify pdf skill references exist** — pdf/SKILL.md references `REFERENCE.md` and `FORMS.md`. Verify these files exist and are up to date; add a table of contents if they exceed 300 lines.
- [ ] **Build `fastapi-scaffold` skill** — Template for FastAPI+Uvicorn+Pydantic+Docker+health-check backend. Only justified when a 3rd project needs this pattern (currently 2: WatchTogether, IL-ecommerce).
