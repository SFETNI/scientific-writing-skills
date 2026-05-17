# Style Guide

Fill in this file for your project. The agent reads it before every drafting session.

---

## Target journal style summary

```
JOURNAL_CITATION_STYLE:   [Author–year (APA) / Numbered / Vancouver]
TENSE_RESULTS:            [Past / Present]
TENSE_METHODS:            [Past / Present]
TENSE_FACTS:              [Present]
PASSIVE_ACTIVE:           [Mostly passive / Mixed / Mostly active]
CAPTION_PLACEMENT:        [Below figure / Above table]
MAX_SENTENCE_WORDS:       [e.g., 35]
```

## Preferred model / method names

List the canonical names to use for every model, dataset, and method in this manuscript.

| Canonical name | Do not use |
|---|---|
| [e.g., Gradient Boosting Regressor (GBR)] | [Gradient boosted trees, GBT, GBR model] |
| [e.g., Root Mean Square Error (RMSE)] | [RMS error, root-mean-squared error] |
| [Add rows as needed] | |

## Preferred terminology

| Use | Avoid |
|---|---|
| [e.g., composite filler] | [reinforcement, additive — if ambiguous] |
| [Add rows as needed] | |

## Forbidden phrases (project-specific additions)

These phrases are banned in addition to the defaults in `agent_context/ANTI_AI_WRITING_STYLE.md`.

```
BANNED_PHRASES_PROJECT:
  - "[phrase specific to this project]"
  - "[another project-specific phrase]"
```

## Hedging conventions

From the style calibration report (fill in after running `/srs-calibrate`):

```
PREFERRED_RESULT_HEDGES:       [e.g., "demonstrates", "shows", "indicates"]
PREFERRED_INTERPRETATION_HEDGES: [e.g., "suggests", "is consistent with", "may indicate"]
SPECULATION_MARKER:            [e.g., "Future work may...", "It is conceivable that..."]
```

## Abbreviations

List all abbreviations used in the manuscript. Check journal policy on abbreviation introduction (most require first use in abstract + first use in main text).

| Abbreviation | Full form | First use location |
|---|---|---|
| [e.g., GBR] | Gradient Boosting Regressor | Abstract, §2.2 |
| [Add rows] | | |

## Notes for agent

```
STYLE_NOTES:
  - [Any project-specific style instruction not covered above]
```
