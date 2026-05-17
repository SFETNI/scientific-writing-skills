# Example Project — Synthetic Illustrative Case

> **DISCLAIMER: This is an illustrative example only.**
> **All data, figures, numbers, models, authors, and references are synthetic and have no scientific validity.**
> **This example exists solely to demonstrate the workflow of scientific-redaction-skills.**
> **Do not cite, reproduce, or present any content from this example as real science.**

---

## Synthetic study

**Working title**: "Thermal conductivity of graphene-reinforced polymer composites: a surrogate modelling approach"

**What this example demonstrates**:
- A filled `AUTHOR_CONTEXT.md` and `STYLE_GUIDE.md`
- A populated `NUMERICAL_REGISTRY.md` with ~20 synthetic values
- A `CLAIM_REGISTER.md` with example claim-source mappings
- A partial LaTeX manuscript with 5 sections (Introduction through SM)
- A synthetic `.bib` file with clearly fake citation keys (`Author2024_ILLUSTRATIVE`)
- A pre-run output of `scripts/check_manuscript_integrity.py`
- An example agent handoff document showing a mid-project state

## Synthetic domain

This example uses polymer-composite thermal conductivity as the domain because:
- Physics and materials science are broadly familiar to STEM PhD students
- The domain is clearly different from the author's private research
- It supports a natural set of variables (filler content, aspect ratio, conductivity)
- All values are completely invented

## How to use this example

```bash
# From the repository root:
python scripts/check_manuscript_integrity.py \
    --main-tex example/manuscript/main.tex \
    --bib example/manuscript/references/example_references.bib \
    --registry example/NUMERICAL_REGISTRY.md

# Expected output is pre-generated at:
cat example/outputs/example_integrity_check.txt
```

## Fake citation keys

All references in this example use the convention `AuthorYYYY_ILLUSTRATIVE` or `AuthorYYYY_fake`. These are not real papers. They do not correspond to any published work.

## License

All content in this directory is dedicated to the public domain under CC0.
See the root LICENSE file for details.
