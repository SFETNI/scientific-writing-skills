# Data License And Provenance

## Preferred Dataset

This example is designed to use the UCI Machine Learning Repository dataset:

- Dataset: Concrete Compressive Strength
- Creator: I-Cheng Yeh
- Repository citation: Yeh, I. (1998). Concrete Compressive Strength [Dataset]. UCI Machine Learning Repository.
- DOI: https://doi.org/10.24432/C5PK67
- Repository page: https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength
- License stated by UCI: Creative Commons Attribution 4.0 International (CC BY 4.0)

The UCI repository describes the dataset as 1,030 instances, 8 input features, 1 regression target, and no missing values.

## Local CSV Policy

`concrete_compressive_strength.csv` is produced by `example/scripts/generate_example_artifacts.py`.

The script first attempts to retrieve the official UCI archive. If that retrieval or parsing step is unavailable in the local environment, the script creates a deterministic fallback dataset. The fallback is marked explicitly with the `source_label` column value:

```text
DETERMINISTIC_FALLBACK_NOT_UCI
```

That fallback is only for exercising the manuscript artifact pipeline. It must not be cited, described, or interpreted as the UCI dataset.

If the official UCI data are used, `source_label` is:

```text
UCI_CC_BY_4_0
```

## Attribution Requirement

Any manuscript text that uses the official UCI data should credit I-Cheng Yeh and the UCI Machine Learning Repository, include the dataset DOI, and state the CC BY 4.0 license.
