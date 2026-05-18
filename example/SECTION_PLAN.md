# Section Plan — Concrete Ridge Worked Example

## Manuscript Structure

| File | Section(s) | Purpose |
|---|---|---|
| `example/manuscript/main.tex` | Front matter, abstract, keywords, inputs, bibliography | Frames the manuscript as a concrete compressive-strength ridge-regression worked example. |
| `example/manuscript/sections/01_introduction.tex` | Introduction | Establishes concrete-strength prediction context, UCI as intended benchmark context, ridge/CV method background, and provenance limits. |
| `example/manuscript/sections/02_methods.tex` | Materials and Methods | Describes local fallback dataset, train/test split, standardization, ridge model, CV selection, metrics, and diagnostics. Inputs `table_dataset_summary.tex`. |
| `example/manuscript/sections/03_results.tex` | Results | Reports generated dataset overview, performance, parity/residual diagnostics, age-bin errors, coefficients, and ablation. Inputs generated result tables and figures. |
| `example/manuscript/sections/04_conclusions.tex` | Discussion; Conclusions; Data availability; AI disclosure; Competing interests; Author contributions | Interprets results conservatively, states limitations, and includes required policy sections. |
| `example/manuscript/sections/05_supplementary.tex` | Supplementary Material | Provides ridge penalty CV table, artifact list, and claim-boundary notes for registry maintenance. |

## Generated Tables Used

| Table file | Manuscript location |
|---|---|
| `table_dataset_summary.tex` | Methods, dataset and provenance |
| `table_model_performance.tex` | Results, predictive performance |
| `table_ablation.tex` | Results, coefficient and ablation diagnostics |
| `table_error_by_age.tex` | Results, residual and age-stratified error patterns |
| `table_supplementary_cv.tex` | Supplementary Material, ridge penalty cross-validation |

## Generated Figures Used

| Figure file | Manuscript location |
|---|---|
| `fig_dataset_overview.pdf` | Results, local data structure |
| `fig_parity_ridge.pdf` | Results, predictive performance |
| `fig_residuals.pdf` | Results, residual and age-stratified error patterns |
| `fig_coefficients.pdf` | Results, coefficient and ablation diagnostics |
| `fig_age_response.pdf` | Results, residual and age-stratified error patterns |

## Claim Boundaries to Preserve

- The current source label is `DETERMINISTIC_FALLBACK_NOT_UCI`.
- UCI may be cited as intended benchmark context and official schema/source context, not as support for fallback-derived numerical results.
- Ridge and cross-validation references support methods, not the reported performance values.
- Performance, ablation, coefficient, residual, and age-bin claims require mapping to generated artifacts and the numerical registry.
- The manuscript is a demonstration draft and should not claim novelty, state-of-the-art performance, causal effects, or field deployment readiness.
