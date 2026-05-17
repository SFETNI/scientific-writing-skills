# Skill: Methods Writing

## Mandate

Draft or improve the Methods section from the author's study design files, protocol documents, and software/hardware specifications. The Methods section must be reproducible: a reader with domain expertise should be able to replicate the study from the section alone. The skill does not invent procedure details — it organises and writes from what the human provides.

## Required inputs

- Study design document or bullet-point outline of the methodology (provided by human)
- `@templates/AUTHOR_CONTEXT.md` — field, target journal, RESULT_FLEXIBILITY
- `@templates/NUMERICAL_REGISTRY.md` — sample sizes, parameter values, split ratios, thresholds
- `@templates/SECTION_PLAN.md` (filled for Methods) — subsection structure, key claims, scope

Optional:
- Existing Methods draft (if this is a revision pass)
- Software/model specifications to include

## Acceptance criteria

1. Every numerical parameter (sample size, split ratio, threshold, hyperparameter) is in `NUMERICAL_REGISTRY.md`.
2. Every subsection has a clear reproducibility purpose: materials, procedure, metrics, statistical analysis, or software/hardware.
3. Past tense is used throughout (standard for experimental methods).
4. No interpretation of results appears in this section.
5. Data availability, software versions, and reproducibility statements are included as required by the target journal.
6. The section ends with a sentence linking the protocol to the results being reported.

## Human-in-the-loop checkpoint

Human must:
- Approve the subsection structure (from `SECTION_PLAN.md`) before prose drafting begins
- Confirm all numerical values against the actual study design
- Verify that the description of each method step matches what was actually done
- Confirm that any software/model names used match the `STYLE_GUIDE.md` preferred naming

## Fail conditions

Reject the output if:
- A procedure step is described that the human did not provide in the study design document.
- A numerical value is used that is not in `NUMERICAL_REGISTRY.md`.
- Results or interpretations appear in the Methods section.
- Claims about novelty appear here (they belong in Introduction/Discussion).

## Subsection template (for reference)

A standard Methods section in most STEM journals includes:
1. Study design / experimental framework
2. Materials / dataset / subjects
3. Procedure / protocol
4. Analytical methods / model architecture
5. Evaluation metrics
6. Statistical analysis / uncertainty quantification
7. Software and reproducibility statement
