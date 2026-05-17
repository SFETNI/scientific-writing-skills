# CODEX.md — scientific-redaction-skills

Codex/GPT-4 agent orientation for this repository.

## What Codex should do here

Codex is the right agent for **file operations, LaTeX mechanics, batch edits, and script execution**. It should not touch scientific prose, claim calibration, argument logic, or citation verification — those are Claude tasks.

## Codex-appropriate tasks

### Pre-flight checks
```bash
# Run the integrity checker and capture output
python scripts/check_manuscript_integrity.py \
  --main-tex manuscript/main.tex \
  --bib manuscript/references/refs.bib \
  --registry docs/NUMERICAL_REGISTRY.md \
  --banned-phrases docs/banned_phrases.json > outputs/integrity_check.txt
```

### LaTeX operations
- Compile `manuscript/main.tex` and report errors (`pdflatex -halt-on-error`)
- Insert `\input{sections/XX_newfile.tex}` lines in `main.tex`
- Renumber figures and tables when sections are reordered
- Update `\label{fig:X}` and `\ref{fig:X}` consistently across all `.tex` files
- Run `bibtex` and report missing keys or undefined references
- Export to DOCX using `pandoc` for non-LaTeX co-authors

### Bibliography maintenance
- Check that all `\cite{key}` entries exist in the `.bib` file
- Identify orphan `.bib` entries (keys in bib not cited in the manuscript)
- Normalize field formatting in `.bib` (consistent author format, page ranges)

### Figure and table insertion
- Insert `\includegraphics` commands from a figure list
- Verify that all figure paths in `main.tex` resolve to real files
- Reorder figure files and update all references consistently

### Batch text operations
- Search and replace model display names across all `.tex` files
- Apply STYLE_GUIDE.md preferred terms via regex substitution (with human approval)
- Strip trailing whitespace and normalize line endings

### Registry and template operations
- Check that all numbers in `NUMERICAL_REGISTRY.md` appear in `main.tex` (coverage report)
- Extract all `\num{}` or `±` values from `.tex` and list them for registry verification

## What Codex must NOT do

- Generate or revise scientific prose (Introduction, Methods, Discussion, Conclusions)
- Make claims about results or findings
- Modify citation content (reference text, author names, DOIs)
- Accept or certify any section — that requires human review
- Run web searches for references

## Handoff to Claude

When Codex finishes a mechanical task, it should output a one-paragraph summary stating:
- What was changed
- What was not changed
- Any issues that require scientific judgment

Claude then picks up from the handoff for prose quality, claim calibration, or argument review.

## Python requirements

The `check_manuscript_integrity.py` script uses Python standard library only (`re`, `os`, `json`, `argparse`, `pathlib`). No `pip install` required for the base checker.

Optional for v0.2: `pdfminer.six` for `pdf_to_context.py` PDF extraction.
