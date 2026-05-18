# Table Design Report

Date: 2026-05-18
Scope: generated tables in `example/manuscript/tables/` and their manuscript integration.

## Overall Status

**PASS with minor layout polish recommended.**

The generated tables are compact and aligned with the manuscript narrative. They report current concrete fallback values, include reader-facing units, and use reader-facing placeholders where values are not applicable. The main remaining issue is LaTeX width polish.

## Table-Level Review

| Table | File | Status | Findings |
|---|---|---|---|
| Table 1 | `table_dataset_summary.tex` | PASS | Useful summary; caption states mixture variables are kg/m3, age is days, and compressive strength is MPa. |
| Table 2 | `table_model_performance.tex` | PASS | Metrics align with the manuscript; baseline alpha uses `--` for not applicable. |
| Table 3 | `table_error_by_age.tex` | PASS | Age-bin diagnostics are clear; headers include days and MPa units. |
| Table 4 | `table_ablation.tex` | PASS | Ablation values align with the manuscript; RMSE headers include MPa units. |
| Table S1 | `table_supplementary_cv.tex` | PASS | CV table supports ridge-penalty selection; RMSE/MAE headers include MPa units. |

## LaTeX/Layout Notes

The manuscript compiles, but LaTeX reports overfull boxes for some tables and long monospaced filenames. Consider smaller table fonts, shorter captions, or `tabular*`/`resizebox` only if needed for the demonstration PDF.

## Recommendation

Accept the tables for a transparent demonstration package. For a polished release, review the compiled PDF for overfull boxes and table width.
