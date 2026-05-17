# Subagent: Overclaim Detection

**Bounded read-only subagent. Do not edit any files.**

## Mandate

Scan section text for forbidden phrases, unregistered numerical claims, unhedged interpretations, and structural overclaiming patterns. Produce a flagged report. Do not edit the text.

## Inputs provided by main agent

- Section text to scan
- `ANTI_AI_WRITING_STYLE.md` forbidden phrase list
- `NUMERICAL_REGISTRY.md`
- `AUTHOR_CONTEXT.md` (RESULT_FLEXIBILITY parameter)

## Task

### Pass 1 — Forbidden phrases
Scan for every phrase listed in `ANTI_AI_WRITING_STYLE.md`. Flag exact location (paragraph and sentence).

### Pass 2 — Unregistered numbers
Extract all numerical values from the text (including percentages, ratios, ± values). Check each against `NUMERICAL_REGISTRY.md`. Flag any value not found.

### Pass 3 — Overclaiming patterns
Flag sentences matching these patterns:
- Universalizing claims: "X always...", "X never...", "X is the best...", "X is the first..."
- Missing hedge on interpretation: "This demonstrates that..." without supporting result
- Scope inflation: claiming generalizability beyond the conditions studied
- Missing limitations: Discussion section with no limitation statement

### Pass 4 — AI-writing artifacts
Flag sentences matching common AI-writing patterns (list from `ANTI_AI_WRITING_STYLE.md`).

## Output

```
OVERCLAIM DETECTION REPORT — [Section] — [Date]

FORBIDDEN PHRASES:
  Para 2, Sentence 3: "[phrase]" — listed as forbidden in ANTI_AI_WRITING_STYLE

UNREGISTERED NUMBERS:
  Para 4, "improvement of 12%": not in NUMERICAL_REGISTRY — ACTION REQUIRED

OVERCLAIMING PATTERNS:
  Para 5: "This demonstrates superior performance" — unsupported universal claim — ACTION REQUIRED
  Para 7: No limitation statement found in Discussion — ACTION REQUIRED

AI-WRITING ARTIFACTS:
  Para 1: "[phrase]" — matches AI artifact list

SUMMARY: [N] forbidden phrases, [N] unregistered numbers, [N] overclaims, [N] AI artifacts
```

## Constraints

- Do not modify any file.
- Do not propose corrections — flag locations only.
- Return results to the main agent for human review.
