# Skill: Style Calibration

## Mandate

Read the `.md` extracts in `context/` (target journal papers, group papers, reference papers) and produce a style calibration report: preferred hedges, claim density norms, tense conventions, citation placement patterns, sentence length norms, and terminology conventions for the target journal. This report is used by all drafting skills. Human must approve the report before any drafting begins (Step 0c).

## Required inputs

- `context/target_journal/` — `.md` extracts of 3–5 papers from the target journal (provided by user)
- `context/group_papers/` — `.md` extracts of group papers (optional but recommended)
- `@templates/AUTHOR_CONTEXT.md` — `TARGET_JOURNAL_FAMILY`, field

If `context/` is empty, produce a generic calibration report based on `TARGET_JOURNAL_FAMILY` from `AUTHOR_CONTEXT.md` and state clearly that it is based on journal family defaults, not on actual papers.

## Analysis dimensions

### Hedging patterns
- What hedging verbs are most common? ("shows," "suggests," "demonstrates," "indicates," "appears to")
- What is the typical hedging level for results vs. interpretations in this journal?

### Claim density
- Average number of quantitative claims per paragraph in Results sections
- Average number of citations per paragraph in Introduction sections

### Tense conventions
- Past tense or present tense for results?
- Present tense for established facts?
- Past or present for Methods?

### Citation placement
- In-sentence or end-of-sentence citation placement?
- Superscript or author–year style?

### Sentence structure
- Mean sentence length in target papers
- Passive/active voice ratio

### Terminology
- Preferred discipline-specific terms observed in target papers
- Terms to avoid (outdated terminology, non-standard abbreviations)

## Acceptance criteria

1. Report is based on actual papers in `context/` (or clearly labeled as family defaults).
2. Each dimension has a concrete recommendation (not just an observation).
3. Terminology recommendations do not conflict with `STYLE_GUIDE.md`.
4. The report is short enough to read in 5 minutes (one page).

## Human-in-the-loop checkpoint

Human must:
- Read the style calibration report
- Confirm that the recommendations match their experience with the target journal
- Approve the report before any section drafting begins
- Add any corrections to `STYLE_GUIDE.md`

**No section drafting may begin until the style calibration report is approved (Step 0c).**

## Output format

```
STYLE CALIBRATION REPORT — [Date]
Based on: [N] target journal papers, [N] group papers
Target journal family: [from AUTHOR_CONTEXT.md]

HEDGING LEVEL
  Results: low hedging ("shows," "demonstrates") — journal accepts direct factual reporting
  Interpretations: moderate ("suggests," "is consistent with") — explicit hedging expected

CLAIM DENSITY
  Results: ~3–4 quantitative claims per paragraph
  Introduction: ~2–3 citations per paragraph

TENSE CONVENTIONS
  Results: past tense (was observed, showed)
  Established facts: present tense (is known, remains a challenge)
  Methods: past tense

CITATION PLACEMENT
  End of sentence, before period, author–year style

SENTENCE LENGTH
  Mean: ~22 words; longest sentences in Methods (~35 words)
  Recommendation: keep Results sentences under 28 words

PREFERRED TERMS (from target papers)
  [list observed terminology]

AVOID
  [list outdated or non-standard terms found in group papers but absent from target journal]

STATUS: AWAITING HUMAN APPROVAL
```
