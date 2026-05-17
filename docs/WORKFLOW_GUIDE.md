# Workflow Guide — 10-Step Onboarding for a New Project

This guide walks through the complete workflow from project setup to submission-ready manuscript, using the synthetic example as a reference.

---

## Before you start

You need:
- A manuscript project with an existing LaTeX structure (or a blank project to build from)
- Your accepted results (figures, tables, numbers) — not necessarily final, but fixed enough to register
- The target journal identified
- Claude Code installed and configured

---

## Step 1 — Copy templates to your manuscript project

```bash
cp -r /path/to/scientific-redaction-skills/templates docs/templates/
cp docs/templates/AUTHOR_CONTEXT.md AUTHOR_CONTEXT.md
cp docs/templates/NUMERICAL_REGISTRY.md NUMERICAL_REGISTRY.md
cp docs/templates/STYLE_GUIDE.md STYLE_GUIDE.md
cp docs/templates/AGENT_HANDOFF.md AGENT_HANDOFF.md
```

Reference: `docs/SETUP.md`

---

## Step 2 — Fill in AUTHOR_CONTEXT.md

Open `AUTHOR_CONTEXT.md` and fill in:
- `TARGET_JOURNAL` and `TARGET_JOURNAL_FAMILY`
- `MAIN_TEX_PATH`, `BIB_PATH`, `REGISTRY_PATH`
- `RESULT_FLEXIBILITY` — start with `LOCKED` unless you know results may change

This takes 5 minutes and is required before any other step.

---

## Step 3 — Fill in NUMERICAL_REGISTRY.md

Open `NUMERICAL_REGISTRY.md` and add every accepted quantitative claim:
- All metrics from your results (R², RMSE, accuracy, effect sizes, p-values)
- Dataset sizes and characteristics
- Model parameters and hyperparameters
- Physical constants you will cite

**Rule: nothing goes in the manuscript that is not in this registry.**

Look at `example/NUMERICAL_REGISTRY.md` for a filled example.

---

## Step 4 — Place reference papers in context/

Place `.md` extracts of 3–5 target journal papers in `context/target_journal/`. These drive style calibration. See `context/README.md` for the conversion workflow.

Even one or two papers is better than none. Running style calibration without any context papers produces family-defaults only.

---

## Step 5 — Run /srs-check (Step 0a)

Open Claude Code in your manuscript project directory and run:
```
/srs-check
```

This runs the integrity checker. Resolve all hard errors before proceeding.

Common hard errors:
- Citation key in `.tex` not in `.bib` — fix the key or add the entry
- Figure path in `.tex` not found — fix the path or add the file

**Gate HG0a: hard errors must be zero before drafting.**

---

## Step 6 — Run /srs-calibrate (Step 0c)

```
/srs-calibrate
```

This reads your `context/` papers and produces a style calibration report. Read the report and confirm it matches your experience with the target journal.

**Gate HG0c: style calibration must be approved before any section drafting begins.**

Record approval in `AGENT_HANDOFF.md`.

---

## Step 7 — Plan each section

Before drafting any section, fill in a copy of `templates/SECTION_PLAN.md` for that section.

The section plan contains:
- The main message the section must deliver
- The argument chain (each step = one paragraph or subsection)
- Key findings to present (for Results) or interpretations to develop (for Discussion)
- Scope boundaries (what this section explicitly does NOT cover)

Run the appropriate `/srs-*` command. The command will ask you to provide the section plan and will wait for your approval before generating any prose.

**Gate HG1: section plan must be approved before prose is written.**

---

## Step 8 — Draft each section

Use the section-specific commands:

| Section | Command | Key skills invoked |
|---|---|---|
| Introduction | `/srs-intro` | Benchmark positioning → drafting → claim calibration |
| Methods | `/srs-methods` | Methods writing → claim evidence verification |
| Results | `/srs-results` | Results writing → figure QC → claim calibration |
| Discussion | `/srs-discussion` | Argument flow → drafting → claim calibration → reviewer perspective |
| SM | `/srs-sm` | SM writing → figure QC |

After each section:
- Review the draft and the claim-source map
- Resolve all UNSUPPORTED and NEEDS_HUMAN_DECISION items
- Run the quality gate: `/srs-gate`

**Gate HG2c: quality gate must PASS before the section is accepted.**

Record acceptance in `AGENT_HANDOFF.md`.

---

## Step 9 — Review figures and tables

```
/srs-figures
```

This runs:
1. Figure QC for all figures
2. Caption review and drafting
3. Visual consistency check across all figures
4. Table design review

Codex handles the file-level changes once you approve the QC recommendations.

**Gate HG3a/HG3b: figure QC and caption confirmation required.**

---

## Step 10 — Full manuscript review and gate

```
/srs-review
```

This runs a 4-role reviewer simulation (methodologist, domain expert, generalist, data integrity reviewer). Read the full report and decide what to address, rebut, or accept as-is.

**Gate HG4a/HG4b: reviewer report must be read; decisions recorded.**

Then run the final quality gate:
```
/srs-gate
```

The gate checks the full manuscript plus the policy checklist (AI disclosure, data availability, competing interests).

**Gate HG5c: author certifies all content before submission.**

---

## Common failure modes

| Failure mode | How to recover |
|---|---|
| Integrity check finds many warnings | Triage: fix hard errors first; review warnings in order of risk |
| Style calibration report doesn't match expectations | Override specific recommendations in `STYLE_GUIDE.md`; re-run if needed |
| Claim map has many UNSUPPORTED items | Add missing sources to `NUMERICAL_REGISTRY.md` and `CLAIM_REGISTER.md`; or remove unsupported claims |
| Quality gate fails on citation tier | Run `/srs-check` on the `.bib` file; advance critical citations to ABSTRACT_RELEVANT |
| Reviewer simulation finds major structural gaps | Check `skill_argument_flow_review.md` output; revise the section plan and redraft |
| Registry has unregistered numbers | Run `check_manuscript_integrity.py` to find them; add to registry or remove from manuscript |
