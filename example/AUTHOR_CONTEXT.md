# Author Context - Concrete Ridge Worked Example

Fill-equivalent context for the demonstration project. Use this file as the context record for the example package.

---

## Project identity

```text
PROJECT_NAME:         Concrete compressive-strength ridge worked example
MANUSCRIPT_TITLE:     A ridge-regression worked example for concrete compressive-strength manuscript drafting
SUBMISSION_STATUS:    In preparation (demonstration only)
TARGET_JOURNAL:       Elsevier-style demonstration manuscript
TARGET_JOURNAL_FAMILY: Elsevier
FIELD:                Civil/materials engineering, predictive modelling, scientific writing workflow
CONTRIBUTION_LEVEL:   Incremental workflow demonstration
```

## File paths

```text
MAIN_TEX_PATH:        example/manuscript/main.tex
BIB_PATH:             example/manuscript/references/example_references.bib
REGISTRY_PATH:        example/NUMERICAL_REGISTRY.md
CLAIM_REGISTER_PATH:  example/CLAIM_REGISTER.md
STYLE_GUIDE_PATH:     example/STYLE_GUIDE.md
SECTION_PLAN_PATH:    example/SECTION_PLAN.md
BANNED_PHRASES_PATH:
```

## Result flexibility

```text
RESULT_FLEXIBILITY:   FIGURES_IMPROVABLE
```

Generated numerical values should remain fixed unless `example/scripts/generate_example_artifacts.py` is intentionally rerun and the registry, manuscript, and reports are regenerated together. Figure styling, labels, and captions may be improved if values do not change.

## Quality standard

```text
QUALITY_STANDARD:     Auditable worked example; not a submit-ready scientific article
LANGUAGE:             English
HEDGING_LEVEL:        Conservative
```

## Provenance constraints

```text
DATASET_CONTEXT:      UCI Concrete Compressive Strength schema and citation context
CURRENT_SOURCE_LABEL: DETERMINISTIC_FALLBACK_NOT_UCI
PROVENANCE_LIMIT:     Do not present fallback-derived metrics as official UCI findings.
```

Use UCI/Yeh citations for public dataset context and schema attribution only. Use generated artifacts and registries for local fallback numbers.

## Collaborators

```text
CORRESPONDING_AUTHOR: Scientific Redaction Skills Demonstration Team
CO_AUTHORS:           N/A - demonstration authorship only
```

## Phase and task tracking

```text
CURRENT_PHASE:        Review and registry/QC remediation
ACTIVE_SECTION:       All
LAST_SESSION_DATE:    2026-05-18
LAST_SESSION_AGENT:   Automated audit
```

## Checkpoint log

```text
2026-05-18 - Concrete fallback draft, generated artifacts, registries, and audit outputs refreshed.
2026-05-18 - Concrete numerical registry and claim register refreshed for the current manuscript.
2026-05-18 - Integrity checker reports 0 hard errors and 0 warnings; remaining items are reader-facing polish and human provenance decisions.
```
