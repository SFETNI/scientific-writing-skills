# Skill: Supplementary Materials Writing

## Mandate

Draft the Supplementary Materials (SM) section: determine scope (what belongs in SM vs. main text), establish numbering conventions, draft content, and ensure all SM items are correctly cross-referenced in the main text. The skill does not invent scientific content — it organises what the human provides.

## Required inputs

- `@templates/AUTHOR_CONTEXT.md` — target journal, `TARGET_JOURNAL_FAMILY` (some journals have strict SM policies)
- `@templates/NUMERICAL_REGISTRY.md` — all accepted quantitative claims
- List of content the human designates for SM (figures, tables, derivations, extended methods, sensitivity analyses)
- Main manuscript sections (to verify cross-references)

## Acceptance criteria

1. Every SM figure and table has a unique label (`Figure S1`, `Table S1`, etc.) that follows the journal's convention.
2. Every SM item is referenced at least once in the main text with consistent cross-reference syntax.
3. No critical result that must be in the main text for reproducibility is placed only in SM.
4. Every quantitative value in SM appears in `NUMERICAL_REGISTRY.md` or is clearly flagged as supplementary-only.
5. The SM opens with a table of contents listing all SM items.
6. Extended methods in SM do not contradict the main Methods section.

## Human-in-the-loop checkpoint

Human must:
- Approve the SM scope (which items go in SM vs. main text) **before** content is drafted
- Check that journal policies permit SM (some open-access journals fold SM into main text)
- Confirm all cross-references in main text are syntactically correct for the target journal
- Verify that critical reproducibility information is not hidden in SM when the journal requires it in the main text

## What belongs in SM vs. main text

| SM-appropriate | Main text required |
|---|---|
| Extended derivations | Core model equations |
| Sensitivity / ablation results | Primary performance metrics |
| Supporting figures for supplementary claims | Figures directly supporting the main message |
| Raw data tables | Aggregated summary statistics |
| Additional experimental conditions not part of the main story | Main protocol |

## Fail conditions

Reject the output if:
- SM numbering conflicts with main text figure/table numbers.
- A main-text cross-reference points to an SM item that does not exist.
- Primary results (the core contribution) are buried in SM.
- Quantitative values in SM differ from corresponding entries in `NUMERICAL_REGISTRY.md`.

## Journal-specific SM policies

Read `@agent_context/JOURNAL_POLICY.md` for the target journal family. Note:
- Some journals require SM to be submitted as a separate file.
- Some journals limit SM to specific file types.
- Some journals do not allow SM (verify before investing in SM content).
