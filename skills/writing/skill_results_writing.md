# Skill: Results Writing

## Mandate

Draft the Results section as a structured reporting of accepted figures and tables. Each subsection reports what was found — in measured, hedged, factual language — without interpretation. Interpretation belongs in the Discussion. The skill organises the argument plan approved by the human into prose, using only registered numerical values.

## Required inputs

- Accepted figures and tables (provided or listed by human)
- `@templates/NUMERICAL_REGISTRY.md` — all accepted quantitative claims
- `@templates/SECTION_PLAN.md` (filled for Results) — argument chain: subsection order, key findings per subsection
- `@templates/AUTHOR_CONTEXT.md` — RESULT_FLEXIBILITY, target journal
- Figure captions (from `skill_figure_caption_writing.md`, if available)

## Acceptance criteria

1. Every quantitative value is drawn from `NUMERICAL_REGISTRY.md`.
2. No interpretation appears in Results (flag any sentence beginning with "This suggests," "This demonstrates," "These results indicate that...").
3. Each subsection opens with a sentence stating what was measured or compared.
4. Each subsection closes with a sentence summarising the key finding of that subsection.
5. Every figure or table in the manuscript is referenced at least once in the Results section.
6. Uncertainty values (± or confidence intervals) are reported for all primary metrics.
7. Past tense throughout (results were observed, were measured, showed, etc.).

## Human-in-the-loop checkpoint

Human must:
- Approve the argument plan (subsection order, key finding per subsection) **before** any prose is written
- Confirm that all quantitative values in the draft match `NUMERICAL_REGISTRY.md`
- Confirm that no interpretation has crossed over from Discussion
- Run `skill_claim_calibration.md` on the completed draft

No Results subsection is accepted without the argument plan being approved first.

## Fail conditions

Reject the output if:
- A number appears that is not in `NUMERICAL_REGISTRY.md`.
- An interpretation sentence appears (move it to Discussion).
- A subsection presents results that were not in the approved argument plan.
- `RESULT_FLEXIBILITY: LOCKED` is set and any value was modified.

## Boundary: Results vs. Discussion

Results states what was observed. Discussion explains what it means.

Allowed in Results:
- "The model achieved R² = 0.847 ± 0.031 on the test set."
- "Feature importance analysis identified variable X as the dominant predictor."

Not allowed in Results:
- "This suggests that the model generalises well to unseen conditions."
- "The high R² demonstrates the effectiveness of the proposed approach."
