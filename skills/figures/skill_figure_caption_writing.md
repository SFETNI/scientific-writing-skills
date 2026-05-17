# Skill: Figure Caption Writing

## Mandate

Draft captions for figures and tables that state the main message, describe what was plotted, specify the model or dataset, and declare scope limitations. Captions must be self-contained — a reader who sees only the figure and its caption should understand what was measured and what the finding is.

## Required inputs

- Figure file or description (provided by human)
- `@templates/NUMERICAL_REGISTRY.md` — values to include in captions
- `@templates/AUTHOR_CONTEXT.md` — target journal caption style
- The relevant Results subsection (for message alignment)

## Caption structure (per figure)

1. **Main message sentence** — what the figure shows or demonstrates (1 sentence, present tense)
2. **Description** — what was plotted: x-axis, y-axis, error bars, colour coding, lines (1–2 sentences)
3. **Scope statement** — which conditions, dataset, or subset the figure covers (1 sentence)
4. **Panel labels** — if the figure has panels (A, B, C...), describe each panel briefly

## Acceptance criteria

1. Caption opens with the main message (not "Figure X shows...").
2. All numerical values in the caption are in `NUMERICAL_REGISTRY.md`.
3. Error bars or uncertainty regions are described (what they represent: ± 1 SD, 95% CI, etc.).
4. Model or method names match `STYLE_GUIDE.md` preferred naming.
5. Caption is complete as a standalone description (no forward references to the main text required).
6. Caption length is within journal limits (typically 150–300 words for a complex multi-panel figure).

## Human-in-the-loop checkpoint

Human must:
- Confirm the main message sentence accurately reflects the finding
- Verify all numerical values in the caption against `NUMERICAL_REGISTRY.md`
- Check that the scope statement does not over- or under-state which conditions are shown

## Fail conditions

- Caption opens with "Figure X shows..." (rewrite to open with the finding).
- A value in the caption differs from `NUMERICAL_REGISTRY.md`.
- Error bars are described but not defined (SD? SE? CI? Range?).

## Table caption note

Table captions follow the same structure but precede the table (not follow, as for figures in most journals). Verify caption placement convention for the target journal.
