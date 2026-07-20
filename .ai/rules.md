# Skills

Drop into any AI tool's skills dir. Writing cluster + dependencies for a Hugo blog.

| Skill | Trigger | Purpose |
|---|---|---|
| [`writing`](skills/writing/SKILL.md) | `/writing` · "edit my writing" · "proofread this" | Type-first prose craft — thesis, structure, sentences, revision protocol |
| [`writing-draft`](skills/writing-draft/SKILL.md) | `/writing-draft` · "here's my outline" · "trim this draft" | Author-first loop: outline → angles → expand/trim → hand off |
| [`writing-ship`](skills/writing-ship/SKILL.md) | `/writing-ship` · "is this post ready" | Blocking publish gate: substance → craft → adversarial → clarity → rights → privacy → mechanics |
| [`research`](skills/research/SKILL.md) | "research" · "compare" · "literature review" | Multi-source web research, cross-validated citations, named gaps |
| [`argumentation`](skills/argumentation/SKILL.md) | `/steelyman` · "you sure?" · "tear this apart" | Argument hygiene, self-audit, adversarial review, double-crux |
| [`diagnostic`](skills/diagnostic/SKILL.md) | `/pre-mortem` · `/feynman-test` · "what could go wrong" | Pre-mortem, five-whys, clarity audit, decision journal |
| [`legal`](skills/legal/SKILL.md) | `/legal` · "disclaimer" · "no warranty" | Protective boilerplate — AS-IS, attribution, trademark |
| [`privacy`](skills/privacy/SKILL.md) | `/privacy` · "is this PII" · "should this be public" | PII hygiene for public posts — never auto-fill personal identifiers |
| [`communication`](skills/communication/SKILL.md) | `/communication` · "status update" · "draft an RFC" | BLUF short-form — one message, one ask, deadline + default |
| [`planning`](skills/planning/SKILL.md) | `/planning` · "break this down" · "scope this" | Ambiguous goal → done-checks, milestones, NOT-doing list |

---

# Rules

0. No internet without permission.
1. Before coding: describe approach, ask clarifying questions if ambiguous, await approval.
2. Tasks touching >3 files: stop and split into subtasks first.
3. After coding: list breakage risks, suggest covering tests.
4. Bugs: write failing reproduction test, then fix until passing. Test must fail without the fix.
5. On correction: add rule to `.ai-instructions/rules.md` to prevent recurrence.
6. Caveman speech; minimize tokens, preserve utility.
7. Dependency trees, build artifacts, and language envs (venv/, node_modules/, target/, etc.) are local noise: gitignore + exclude from all search, never read.
---

# Repo README template

## Project
[One line: what this does, who uses it]

## Quickstart
[One line per step to get running, e.g. install deps, set env vars, run dev server]

## Stack
[Framework, language, database, deployment]

## Commands
- Dev: `[cmd]`
- Build: `[cmd]`
- Test single: `[cmd] -- [path]`
- Test all: `[cmd]`
- Lint: `[cmd]`
- Type check: `[cmd]`
## Architecture
- [folder] → [what lives here]   (one line per folder)
- [file] → [what this file does]
## Rules
- [Rule preventing a specific mistake]   (3-5 entries)
- IMPORTANT: [The one rule ai-tool keeps breaking]
## Workflow
- [Task approach]
- [Commit conventions]
- [Testing expectations]
- [Ask vs act]
## Design Principles
[Key constraints and tradeoffs this project optimizes for, e.g. composable; non-destructive; local-first]
## Out of scope
- [Don't-touch areas]
- [Manually-maintained files]
- [Off-limits integrations]
---

# High-impact rule examples
- IMPORTANT: type check after every code change (prevents shipping broken types)
- Minimal changes; no unrelated refactoring (prevents whole-file rewrites)
- Separate commit per logical change (prevents 47-file monster commits)
- When unsure, present alternatives; I choose (prevents unilateral architecture decisions)
- Static export only, no SSR (prevents server-side code in static sites)
