# Author Context

Copy this file into a manuscript project and replace every bracketed value before drafting or review. All agent skills read this file at startup.

---

## Project identity

```text
PROJECT_NAME:          [e.g., Surrogate modelling of polymer composite thermal conductivity]
MANUSCRIPT_TITLE:      [Working title]
SUBMISSION_STATUS:     [In preparation / Under review / Revision / Accepted]
TARGET_JOURNAL:        [Full journal name, e.g., Composites Science and Technology]
TARGET_JOURNAL_FAMILY: [Elsevier / Springer Nature / Nature Portfolio / IEEE / MDPI / Other]
FIELD:                 [e.g., Materials science, machine learning]
CONTRIBUTION_LEVEL:    [Incremental / Solid / High-impact]
```

## File paths

Paths are relative to the project root unless an absolute path is required.

```text
MAIN_TEX_PATH:         manuscript/main.tex
BIB_PATH:              manuscript/references/refs.bib
REGISTRY_PATH:         NUMERICAL_REGISTRY.md
CLAIM_REGISTER_PATH:   CLAIM_REGISTER.md
STYLE_GUIDE_PATH:      STYLE_GUIDE.md
SECTION_PLAN_PATH:     SECTION_PLAN.md
AGENT_HANDOFF_PATH:    AGENT_HANDOFF.md
BANNED_PHRASES_PATH:   [leave blank to use script defaults, or: docs/banned_phrases.json]
```

## Result flexibility

This parameter controls which changes to figures, tables, and numbers are permitted.

```text
RESULT_FLEXIBILITY:    LOCKED
```

Options:

- `LOCKED` - figures, tables, and all numbers are frozen. The agent may not suggest changes to registered values.
- `FIGURES_IMPROVABLE` - numbers are fixed; figures may be re-styled, relabelled, or reformatted, but values must not change.
- `MINOR_ANALYSIS_ALLOWED` - core findings are fixed; optional supplementary plots or additional analyses may be suggested with explicit human authorization.

## Quality standard

```text
QUALITY_STANDARD:      [e.g., Peer-reviewed journal with average impact factor 4-6]
LANGUAGE:              English
HEDGING_LEVEL:         [Conservative / Standard / Assertive]
```

## Evidence and provenance constraints

```text
DATA_PROVENANCE:       [Dataset/source status and license constraints]
LOCKED_RESULTS:        [List result files or registry IDs that must not change]
KNOWN_LIMITATIONS:     [Scope boundaries the manuscript must preserve]
HUMAN_DECISIONS_NEEDED:[Open decisions requiring author approval]
```

## Collaborators

```text
CORRESPONDING_AUTHOR:  [Name]
CO_AUTHORS:            [Comma-separated list or N/A]
AUTHOR_VOICE_NOTES:    [Preferred tone, terminology, spelling, or lab conventions]
```

## Phase and task tracking

Update this section at the start of each session.

```text
CURRENT_PHASE:         [Pre-draft / Drafting / Review / Final QC / Submitted]
ACTIVE_SECTION:        [Introduction / Methods / Results / Discussion / SM / All]
LAST_SESSION_DATE:     [YYYY-MM-DD]
LAST_SESSION_AGENT:    [Claude / Codex / other]
```

## Required completion checklist

Before asking an agent to draft or review manuscript text, confirm:

- `PROJECT_NAME`, `MANUSCRIPT_TITLE`, `TARGET_JOURNAL_FAMILY`, and `FIELD` are filled.
- `RESULT_FLEXIBILITY` is set intentionally.
- `MAIN_TEX_PATH`, `BIB_PATH`, and `REGISTRY_PATH` point to real files.
- Known provenance limits and locked results are listed.
- `AGENT_HANDOFF.md` has the latest phase, active task, and read-first list.

## Checkpoint log

Record HiTL checkpoint clearances here (append, do not overwrite):

```text
# Example:
# HG0a - Integrity check cleared - 2026-05-16
# HG0c - Style calibration approved - 2026-05-16
```
