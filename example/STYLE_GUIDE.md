# Style Guide — Concrete Ridge Worked Example

> Demonstration manuscript style guide for the concrete compressive-strength ridge-regression example. The current local artifacts are labelled `DETERMINISTIC_FALLBACK_NOT_UCI`; preserve that provenance limit in all scientific claims.

## Target Journal Style Summary

```text
JOURNAL_CITATION_STYLE:   Numbered (Elsevier elsarticle-num)
TENSE_RESULTS:            Past for generated results
TENSE_METHODS:            Past for completed pipeline steps
TENSE_FACTS:              Present for general methodological facts
PASSIVE_ACTIVE:           Mixed; prefer clear active voice outside Methods
CAPTION_PLACEMENT:        Below figures; generated tables retain their own captions
MAX_SENTENCE_WORDS:       35 target, except unavoidable technical statements
```

## Canonical Names

| Canonical name | Avoid |
|---|---|
| UCI Concrete Compressive Strength dataset | concrete UCI data, concrete dataset, Yeh data when provenance is ambiguous |
| local fallback data | UCI data, empirical observations, official dataset results |
| deterministic fallback data | synthetic UCI data, simulated UCI data |
| standardized ridge regression | Ridge Regressor, ridge model without first-use definition |
| ordinary least squares (OLS) | linear baseline when OLS is meant |
| training-mean baseline | naive model, dummy model |
| root mean square error (RMSE) | RMS error, root-mean-squared error |
| mean absolute error (MAE) | mean absolute deviation |
| coefficient of determination (\(R^2\)) | R-squared, R² |

## Evidence and Provenance Rules

| Claim type | Required wording |
|---|---|
| Official UCI context | "The workflow is designed around" or "the UCI repository describes" |
| Local numerical result | "the local fallback data/artifacts reported" |
| Model performance | Tie directly to generated tables/logs; do not cite external papers as evidence |
| Feature importance or ablation | "model diagnostic", "local fallback data", "not causal" |
| Concrete-science interpretation | Conservative background only unless later registry/citation work verifies support |

## Approved Citation Uses

| Key | Use for |
|---|---|
| `Yeh1998_UCIConcreteDataset` | Official UCI dataset attribution, license/context, intended schema |
| `Yeh1998_ConcreteANN` | Historical concrete-strength modelling context |
| `HoerlKennard1970_Ridge` | Ridge-regression origin/definition |
| `Stone1974_CrossValidation` | Cross-validation concept |
| `HastieTibshiraniFriedman2009_ESL` | Regularization, linear models, validation background |
| `NunezMaraniFlahNehdi2021_ConcreteMLReview` | Broad concrete ML context |
| `AsterisMokos2020_ConcreteStrengthANN` | Broad ANN/concrete-strength modelling context |

## Forbidden Phrases

```text
BANNED_PHRASES_PROJECT:
  - "the UCI results show" when referring to fallback outputs
  - "state-of-the-art"
  - "proves"
  - "causal effect"
  - "validated on the UCI dataset" unless official provenance is verified
```

## Hedging Conventions

```text
PREFERRED_RESULT_VERBS:           "reported", "achieved", "yielded"
PREFERRED_INTERPRETATION_HEDGES:   "suggests within the local fallback data", "is consistent with", "should be interpreted as"
PROVENANCE_MARKER:                "The current source label is DETERMINISTIC_FALLBACK_NOT_UCI."
LIMITATION_MARKER:                "This does not establish performance on the official UCI observations."
```

## Abbreviations

| Abbreviation | Full form | First use location |
|---|---|---|
| UCI | University of California, Irvine | Abstract or Introduction |
| OLS | ordinary least squares | Methods |
| RMSE | root mean square error | Abstract or Methods |
| MAE | mean absolute error | Abstract or Methods |
| CV | cross-validation | Methods or Supplementary |
