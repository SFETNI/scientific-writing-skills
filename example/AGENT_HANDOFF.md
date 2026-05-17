# Agent Handoff — ILLUSTRATIVE EXAMPLE

> **ILLUSTRATIVE ONLY. This shows a mid-project handoff document.**

---

## Current state

```
CURRENT_PHASE:      Drafting — Results
ACTIVE_TASK:        Draft Results §3.3 (feature importance analysis) and §3.4 (sensitivity analysis)
LAST_UPDATED:       2026-05-16
LAST_SESSION_AGENT: Claude
```

## Read-first list

1. `example/AUTHOR_CONTEXT.md`
2. `example/NUMERICAL_REGISTRY.md`
3. `example/CLAIM_REGISTER.md`
4. `example/manuscript/sections/03_results.tex` (current state)

---

## HiTL checkpoint log

```
HG0a — Integrity check cleared — 2026-05-16 (illustrative)
       2 hard errors found and resolved: fixed orphan figure path fig_sensitivity.pdf,
       corrected citation key Doe2021_ILLUSTRATIVE (was Doe2021_illustrate)
HG0c — Style calibration approved — 2026-05-16 (illustrative)
       Key outcomes: low hedging in Results, past tense throughout, end-of-sentence citations
HG1  — Introduction section plan approved — 2026-05-16 (illustrative)
HG2c — Introduction accepted — 2026-05-16 — gate PASS (illustrative)
HG1  — Methods section plan approved — 2026-05-16 (illustrative)
HG2c — Methods accepted — 2026-05-16 — gate PASS (illustrative)
HG1  — Results section plan approved — 2026-05-16 (illustrative)
```

---

## Section status

| Section | Status | Gate | Date |
|---|---|---|---|
| Introduction | Accepted | PASS | 2026-05-16 |
| Methods | Accepted | PASS | 2026-05-16 |
| Results | In progress — §3.1 and §3.2 done; §3.3 and §3.4 pending | — | |
| Discussion | Not started | — | |
| Conclusions | Not started | — | |
| SM | Not started | — | |

---

## Deferred items

| Item | Priority | Description |
|---|---|---|
| U001 — UNSUPPORTED claim | High | "The model is more accurate than most reported models" — needs systematic comparison or removal |
| Balandin2011 citation | Medium | At ABSTRACT_RELEVANT only — full text not confirmed |
| DC002 — EMT literature | Medium | Discussion claim about effective medium theories needs citation — authorized literature search needed |

---

## Process trace log

```
SESSION 1 — 2026-05-16
  Skills invoked: skill_task_protocol, skill_section_drafting (Introduction), skill_claim_calibration
  Checkpoints cleared: HG0a, HG0c, HG1 (Intro), HG2c (Intro)
  Next: Methods section drafting

SESSION 2 — 2026-05-16
  Skills invoked: skill_methods_writing, skill_claim_evidence_verification
  Checkpoints cleared: HG1 (Methods), HG2c (Methods)
  Next: Results §3.1 and §3.2

SESSION 3 — 2026-05-16
  Skills invoked: skill_results_writing, skill_claim_calibration (Results §3.1–3.2)
  Checkpoints cleared: HG1 (Results)
  Next: Results §3.3 and §3.4 — use NUMERICAL_REGISTRY IDs R007–R010
```
