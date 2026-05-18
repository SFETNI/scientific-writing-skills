# Example Project - Concrete Ridge Worked Example

> **DISCLAIMER: This is an illustrative workflow example only.**
> The manuscript, authorship, local fallback data, figures, and numerical results are demonstration artifacts.
> Real references are included to demonstrate citation discipline, but the reported fallback metrics must not be cited or presented as scientific findings.
> The current generated artifacts are labelled `DETERMINISTIC_FALLBACK_NOT_UCI`; they are not verified observations from the official UCI Concrete Compressive Strength dataset.

## Worked Example

**Working title**: "A ridge-regression worked example for concrete compressive-strength manuscript drafting"

This example demonstrates:

- A filled project context in `AUTHOR_CONTEXT.md` and current handoff in `AGENT_HANDOFF.md`.
- A concrete-specific `STYLE_GUIDE.md`, `SECTION_PLAN.md`, `NUMERICAL_REGISTRY.md`, and `CLAIM_REGISTER.md`.
- A reproducible artifact script: `scripts/generate_example_artifacts.py`.
- Generated local data, manuscript tables, manuscript figures, and a generation log.
- A LaTeX manuscript built around generated artifacts and conservative provenance language.
- Real bibliography entries for dataset context, ridge regression, cross-validation, and concrete-ML background.
- Reader-facing audit outputs under `outputs/`.
- Current package readiness notes in `AUDIT_STATUS.md`.

## Data Provenance

The workflow is designed around the variable schema of the UCI Concrete Compressive Strength dataset. The current local file `data/concrete_compressive_strength.csv` was loaded by the artifact-generation script, but the generation log records:

```text
Dataset source_label: DETERMINISTIC_FALLBACK_NOT_UCI
```

Therefore, all reported metrics describe the local demonstration artifacts only. UCI/Yeh references support the intended public-data context and schema, not the fallback-derived numbers.

## Current Audit Snapshot

| Area | Status | Notes |
|---|---|---|
| Generated artifacts | Current | Data, figures, tables, and generation log are present. |
| Manuscript PDF | Builds with warnings | `outputs/example_manuscript.pdf` is refreshed; LaTeX overfull/underfull warnings remain for visual polish. |
| Numerical registry | Current | Integrity checker reports no numerical warnings. |
| Claim register | Current | Claims are mapped to generated artifacts, citations, or human-decision items. |
| Figure/table/visual QC | Current | Reports identify only minor polish items. |
| Provenance | Limited by design | Current numbers are fallback demonstration outputs, not official UCI results. |

## Current Integrity-Check Result

The saved checker transcript at `outputs/example_integrity_check.txt` was refreshed on 2026-05-18. It reports 0 hard errors and 0 warnings. It also reports informational notes for three uncited bibliography entries and AI-disclosure wording detection.

## How To Regenerate

```bash
# From the repository root:
python example/scripts/generate_example_artifacts.py

python scripts/check_manuscript_integrity.py \
    --main-tex example/manuscript/main.tex \
    --bib example/manuscript/references/example_references.bib \
    --registry example/NUMERICAL_REGISTRY.md
```

To rebuild the manuscript PDF, run LaTeX from `example/manuscript/`:

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

## License

All demonstration content in this directory is dedicated to the public domain under CC0. See the root LICENSE file for details.
