# Subagent: Style Calibration

**Bounded read-only subagent. Do not edit any files.**

## Mandate

Read the `.md` paper extracts in `context/` and produce a style calibration report covering hedging patterns, claim density, tense conventions, citation placement, and terminology norms for the target journal. Report findings only — do not apply any changes to manuscript files.

## Inputs provided by main agent

- Contents of `context/target_journal/` (`.md` files)
- Contents of `context/group_papers/` (`.md` files, if present)
- `AUTHOR_CONTEXT.md` (`TARGET_JOURNAL_FAMILY`, field)

## Task

For each paper extract provided:
1. Note the hedging verbs used in Results and Discussion.
2. Count citations per paragraph in Introduction.
3. Note tense usage in Results vs. Methods.
4. Note citation placement (in-sentence vs. end-of-sentence).
5. Note sentence length distribution.
6. Extract terminology specific to this journal/field.

Aggregate across all papers and derive recommendations.

## Output

```
STYLE CALIBRATION REPORT — [Date]
Papers read: [N target journal papers, N group papers]
Target journal family: [from AUTHOR_CONTEXT]

HEDGING LEVEL
  Results: [low/medium/high] — most common verbs: [list]
  Interpretations: [low/medium/high] — most common verbs: [list]

CLAIM DENSITY
  Results: ~[N] quantitative claims per paragraph
  Introduction: ~[N] citations per paragraph

TENSE CONVENTIONS
  Results: [past / present]
  Methods: [past / present]
  Established facts: [present]

CITATION PLACEMENT
  [End of sentence / In-sentence / Both]
  Style: [Author–year / Numbered]

SENTENCE LENGTH
  Mean: ~[N] words
  Recommended max: [N] words

PREFERRED TERMS (observed in target papers)
  [list]

TERMS TO AVOID (present in group papers but not target journal)
  [list]

NOTE: [If context/ was empty, state: "Report based on journal family defaults only — no papers read"]

STATUS: AWAITING HUMAN APPROVAL
```

## Constraints

- Do not modify any file.
- Do not apply recommendations — produce the report only.
- If `context/` is empty, produce a family-defaults report and label it clearly.
- Return the report to the main agent for human approval before any drafting begins.
