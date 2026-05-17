# Author Context

Fill in this file for your project. All agent skills read it at startup.

---

## Project identity

```
PROJECT_NAME:         [e.g., "Surrogate modelling of polymer composite thermal conductivity"]
MANUSCRIPT_TITLE:     [Working title]
SUBMISSION_STATUS:    [In preparation / Under review / Revision / Accepted]
TARGET_JOURNAL:       [Full journal name, e.g., "Composites Science and Technology"]
TARGET_JOURNAL_FAMILY: [Elsevier / Springer Nature / Nature Portfolio / IEEE / MDPI / Other]
FIELD:                [e.g., "Materials science, machine learning"]
CONTRIBUTION_LEVEL:   [Incremental / Solid / High-impact]
```

## File paths (used by scripts and /srs-check)

```
MAIN_TEX_PATH:        manuscript/main.tex
BIB_PATH:             manuscript/references/refs.bib
REGISTRY_PATH:        NUMERICAL_REGISTRY.md
BANNED_PHRASES_PATH:  [leave blank to use script defaults, or: docs/banned_phrases.json]
```

## Result flexibility

This parameter controls which changes to figures, tables, and numbers are permitted.

```
RESULT_FLEXIBILITY:   LOCKED
```

Options:
- `LOCKED` — figures, tables, and all numbers are frozen. The agent may not suggest changes to registered values.
- `FIGURES_IMPROVABLE` — numbers are fixed; figures may be re-styled (colours, labels, layout) but values must not change.
- `MINOR_ANALYSIS_ALLOWED` — core findings are fixed; optional supplementary plots or additional analyses may be suggested with explicit human authorization.

## Quality standard

```
QUALITY_STANDARD:     [e.g., "Peer-reviewed journal with average impact factor 4–6"]
LANGUAGE:             English
HEDGING_LEVEL:        [Conservative / Standard / Assertive — see style calibration report]
```

## Collaborators

```
CORRESPONDING_AUTHOR: [Name]
CO_AUTHORS:           [Comma-separated list or "N/A"]
```

## Phase and task tracking

Update this section at the start of each session.

```
CURRENT_PHASE:        [Pre-draft / Drafting / Review / Final QC / Submitted]
ACTIVE_SECTION:       [Introduction / Methods / Results / Discussion / SM / All]
LAST_SESSION_DATE:    [YYYY-MM-DD]
```

## Checkpoint log

Record HiTL checkpoint clearances here (append, do not overwrite):

```
# Example:
# HG0a — Integrity check cleared — 2026-05-16
# HG0c — Style calibration approved — 2026-05-16
```
