# Citation Audit Report

Date: 2026-05-18
Scope: `example/manuscript/main.tex`, `example/manuscript/sections/*.tex`, and `example/manuscript/references/example_references.bib`.

## Overall Status

**PASS for key existence and conservative citation use; human full-text verification remains required for any final scientific release.**

The bibliography contains real references rather than illustrative fake keys. The manuscript uses citations conservatively: external sources support dataset context, method definitions, and broad concrete-ML background, while local performance values are supported by generated artifacts and the numerical registry.

## Cited Keys Reviewed

| Key | Current use | Status | Caution |
|---|---|---|---|
| `Yeh1998_UCIConcreteDataset` | UCI dataset context, repository attribution, intended schema | METADATA_VERIFIED | Does not support fallback-derived numerical results. |
| `Yeh1998_ConcreteANN` | Historical concrete-strength modelling context | METADATA_VERIFIED | Does not imply the example reproduces Yeh's ANN model. |
| `NunezMaraniFlahNehdi2021_ConcreteMLReview` | Broad concrete ML context | METADATA_VERIFIED | Should not be used to imply this ridge example is state of the art. |
| `HoerlKennard1970_Ridge` | Ridge-regression method definition | METADATA_VERIFIED | Supports method background, not local performance. |
| `Stone1974_CrossValidation` | Cross-validation method context | METADATA_VERIFIED | Supports validation concept, not the generated metrics. |

## Uncited Bibliography Entries

The integrity checker reports three defined but uncited keys: `AsterisMokos2020_ConcreteStrengthANN`, `HastieTibshiraniFriedman2009_ESL`, and `Kohavi1995_CrossValidationBootstrap`. These are not hard errors, but they should either be cited for a specific claim or removed before a polished release.

## Claim-Support Boundaries

- UCI/Yeh references support public dataset context and schema only.
- Local values such as RMSE, MAE, R2, ablation deltas, and age-bin summaries are supported by generated tables, figures, logs, and `NUMERICAL_REGISTRY.md`.
- No citation should be used to transform deterministic fallback outputs into official UCI findings.

## Recommendation

Accept the citation structure for a demonstration package. Before any claim of scientific readiness, perform human full-text verification for all sources used to support substantive domain claims.
