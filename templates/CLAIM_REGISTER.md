# Claim Register

Maps every substantive claim in the manuscript to its evidence source. Updated after each claim calibration pass.

---

## How to use

- After running `skill_claim_calibration.md` on a section, add all new claim-source mappings here.
- Use the evidence status labels: RESULT_SUPPORTED / LITERATURE_SUPPORTED / METHOD_DEFINITION / INTERPRETATION / SPECULATION.
- Every LITERATURE_SUPPORTED claim must have a citation key and a tier (KEY_EXISTS → FULL_TEXT_SUPPORTS_CLAIM).

---

## Introduction claims

| ID | Claim (brief) | Label | Source | Citation tier | Section |
|---|---|---|---|---|---|
| I001 | [e.g., "X has received increasing attention in the last decade"] | LITERATURE_SUPPORTED | Smith2022, Doe2023 | ABSTRACT_RELEVANT | §1.1 |
| I002 | [e.g., "Current methods struggle with Y"] | LITERATURE_SUPPORTED | Jones2021 | ABSTRACT_RELEVANT | §1.2 |
| I003 | [e.g., "This paper proposes a GBR model for..."] | METHOD_DEFINITION | — | — | §1.4 |

## Methods claims

| ID | Claim (brief) | Label | Source | Citation tier | Section |
|---|---|---|---|---|---|
| M001 | | METHOD_DEFINITION | | | |

## Results claims

| ID | Claim (brief) | Label | Source | Registry ID | Section |
|---|---|---|---|---|---|
| RL001 | [e.g., "R² = 0.847 ± 0.031"] | RESULT_SUPPORTED | model_eval.csv | R001 | §3.1 |
| RL002 | | | | | |

## Discussion claims

| ID | Claim (brief) | Label | Source | Notes | Section |
|---|---|---|---|---|---|
| DC001 | [e.g., "Results suggest that X"] | INTERPRETATION | Based on R001 | Hedged: "suggests" | §4.1 |
| DC002 | | | | | |

---

## Unresolved claims

Claims that were flagged during calibration but not yet resolved:

| ID | Claim (brief) | Status | Required action |
|---|---|---|---|
| U001 | | UNSUPPORTED | Find citation or remove |
| U002 | | NEEDS_HUMAN_DECISION | Human judgment required |

---

## Register integrity

- Last updated: [YYYY-MM-DD]
- Sections covered: [list]
- Total claims registered: [N]
- UNSUPPORTED remaining: [N] ← must be zero before submission
- NEEDS_HUMAN_DECISION remaining: [N] ← must be zero before submission
