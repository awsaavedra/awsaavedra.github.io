---
name: ai-instructions
description: Operating rules and engineering principles for all agents. Plucked from rules.md + software-engineering, debug, and code-review skills.
when_to_use: Always active. Apply rules automatically; invoke referenced skills explicitly for focused audits.
---

# AI Instructions

## Rules

0. No internet without permission.
1. Before coding: describe approach, ask clarifying questions if ambiguous, await approval.
2. Tasks touching >3 files: stop and split into subtasks first.
3. After coding: list breakage risks, suggest covering tests.
4. Bugs: write failing reproduction test, then fix until passing. Test must fail without the fix.
5. On correction: add rule to prevent recurrence.
6. Caveman speech; minimize tokens, preserve utility.
7. Dependency trees, build artifacts, and language envs (`public/`, `node_modules/`, `venv/`, `target/`, etc.) are local noise: exclude from all search, never read.

---

## Design

Apply automatically when writing or reviewing code.

### Rules
- **Names:** Exact. Verbs→functions, nouns→classes. No abbreviations, no magic numbers.
- **Functions:** One thing. ≤3 args (else object). No side effects. No flag args. ≤20 lines.
- **Comments:** Explain *why*, never *what*. No commented-out code. Block needs explaining → extract to named function.
- **Classes:** SRP. DIP. Prefer composition over inheritance.
- **DRY:** One authoritative home per piece of knowledge.
- **KISS/YAGNI:** Simplest solution that works. Don't build for imaginary futures.
- **Fail fast:** Validate at boundary; surface errors early.
- **Boy Scout Rule:** Leave every file cleaner than found.

---

## Documentation

### Rules
- **Reflect actual state.** Document what is implemented, not what was planned or is aspirational.
- **Atomic updates.** Docs update in the same commit as the code change. Never lag.
- **No historical archaeology.** Remove outdated content; don't append corrections to stale text.
- **Commit messages:** `#type, what; what; what` — type is the intent (`add` · `fix` · `doc` · `refactor` · `stabilize` · `edit` · `clean` · `post` · `warning` · `test` · `draft`), clauses semicolon-separated, no Co-Authored-By.

---

## Debug

Engage before proposing any fix for bugs, errors, or unexpected behavior.

### Iron Laws
1. **No fix without confirmed root cause.** Symptom patches = failure.
2. **No "done" without fresh verification.** "Should work" ≠ evidence.
3. **Eliminate, never confirm.** Tests must disprove hypotheses, not validate them.

### Phases
1. **Reproduce & Evidence** — read full error/stack/line numbers; state expected vs. actual in one sentence.
2. **Pattern Analysis** — find a working example; list every diff, even trivial.
3. **Hypothesize & Eliminate** — 3–5 candidates; test most falsifiable first.
4. **Fix** — failing test first; one change at root cause only.
5. **Verify & Guard** — run full command fresh; paste output; zero new failures.

---

## Code Review

Invoke explicitly. Output: actionable diffs, imperative feedback, or PASS.

### Priority
- **Critical** — correctness · security · broken contracts
- **High** — missing seams · infrastructure in logic layer · SRP violations
- **Medium** — DRY · naming · function shape · smells
- **Low** — style · minor verbosity

### Gates
- [ ] No infrastructure imports at logic layer
- [ ] All external dependencies injected
- [ ] No magic numbers · no dead code
- [ ] SRP: one reason to change per module
- [ ] Docs match committed implementation
