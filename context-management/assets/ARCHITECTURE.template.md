# Architecture Guide

This document routes you to the right spec. Don't read everything — read what you need.

## Document Map
| What you need | Read this | Location |
|---|---|---|
| Agent instructions | CLAUDE.md | `CLAUDE.md` |
| Current build status | STATE.md | `STATE.md` |
| [Domain 1] | [Doc name] | `docs/[domain].md` |

<!-- Example (portfolio-system):
| What you need          | Read this              | Location                        |
|---|---|---|
| Agent instructions     | CLAUDE.md              | `CLAUDE.md`                     |
| Current build status   | STATE.md               | `STATE.md`                      |
| Pipeline spec          | System Design v4       | `docs/portfolio_system_design_v4.md` |
| Agent spec             | Michael Design Doc     | `docs/michael_design_doc.md`    |
| Prior burns            | Lessons Learned        | `docs/LESSONS.md`               |
| Config reference       | Settings               | `config/settings.py`            |
-->

## System Layers
```
[Top-level components and how they relate — fill in per project]
```

<!-- Example (portfolio-system):
```
Michael (Autonomous Agent)
  ├── uses → Scout (screening funnel)
  ├── reads → Radar (regime detection)
  ├── respects → Guardian (risk rules)
  └── logs via → Chronicler (audit trail)

Pipeline (Infrastructure)
  ├── Data Pipeline → yfinance, SEC EDGAR
  ├── Evaluator → return tracking, attribution
  └── Config → settings.py (all tunable params, zero magic numbers)

Infrastructure: VPS, Alpaca API, SQLite
```
-->

## Key Principles
- [1-2 architectural invariants that should never be violated]

<!-- Example (portfolio-system):
- Config centralization: all tunable parameters live in `config/settings.py` — zero magic numbers in code
- Data integrity: LLM is never a data source — only yfinance/SEC EDGAR
- Guardian fails closed: if in doubt, block the trade
-->

## When Domains Overlap
[How to resolve conflicts between specs/docs — fill in when it happens]

<!-- Example: Pipeline spec governs component behavior. Michael spec governs agent reasoning.
If Michael wants to override a Guardian rule → pipeline spec wins. Document the exception in LESSONS.md. -->
