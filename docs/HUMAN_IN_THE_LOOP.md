# Human-in-the-Loop Design

## Why full automation is wrong for manuscript redaction

Scientific manuscripts are accountability documents. When a paper is published, the authors certify that the content is accurate, original, and ethically compliant. This certification cannot be delegated to an AI agent.

AI-assisted writing introduces specific quality risks that require human oversight at every stage:

**Citation fabrication.** AI language models hallucinate references — generating plausible-sounding but non-existent papers, fabricated DOIs, and blended author names. Recent analyses have raised concern about a documented and growing problem of AI-generated invalid citations reaching publication. The only defence is human review of every citation before the manuscript is submitted.

**Claim inflation.** AI models tend to generate assertive, confident prose. Left unchecked, AI-assisted text will overstate results, universalise findings, and understate limitations. Every claim must be checked against registered evidence.

**Context loss.** AI agents do not know which results are fixed, which interpretations are provisional, and what the scope of the contribution is. This context lives in the researcher's head and in the registered files. Without human review, AI-generated text will drift beyond the intended scope.

**Accountability.** Publishers require authors to take responsibility for all content, including AI-assisted content. An automated pipeline that accepts AI output without human review is not publisher-compliant and cannot be defended in a post-publication integrity audit.

This framework is built on one principle: **AI assists, humans decide.** Every skill produces a report or draft that the human reviews and accepts. No content is automatically committed to the manuscript.

---

## Mandatory checkpoint table

| Stage | Checkpoint ID | What the human must do | Blocking? |
|---|---|---|---|
| **0 — Pre-draft** | HG0a | Review integrity check output; resolve all hard errors | YES |
| **0 — Pre-draft** | HG0b | Resolve all UNSUPPORTED claims from skill-based pre-check | YES |
| **0 — Pre-draft** | HG0c | Read and approve style calibration report | YES |
| **1 — Section plan** | HG1 | Approve argument chain for each section before any prose is written | YES |
| **2 — Drafting** | HG2a | Review and confirm each section draft | YES |
| **2 — Drafting** | HG2b | Resolve claim-source map; zero UNSUPPORTED items | YES |
| **2 — Drafting** | HG2c | Run revision quality gate; confirm PASS | YES |
| **3 — Figures & SM** | HG3a | Approve figure QC report before initiating revisions | YES |
| **3 — Figures & SM** | HG3b | Confirm figure captions against registered values | YES |
| **3 — Figures & SM** | HG3c | Approve SM scope and structure | YES |
| **4 — Review** | HG4a | Read complete reviewer simulation report | YES |
| **4 — Review** | HG4b | Decide per concern: address / rebut / out of scope | YES |
| **5 — Final QC** | HG5a | Approve revision quality gate on revised manuscript | YES |
| **5 — Final QC** | HG5b | Complete and approve policy checklist | YES |
| **5 — Submission** | HG5c | Author certifies all content is accurate and their own | YES |

All 15 checkpoints are blocking. The workflow does not advance past a blocking checkpoint without explicit human confirmation.

---

## What "blocking" means in practice

When a blocking checkpoint is reached, the agent must:
1. Present the gate output clearly.
2. State which items require human decision.
3. Wait for explicit human confirmation before proceeding.
4. Record the checkpoint clearance in `AGENT_HANDOFF.md`.

The agent must never:
- Assume approval if the human does not respond immediately.
- Accept a section on behalf of the human.
- Proceed past a gate by treating silence as consent.

---

## Human decisions that cannot be delegated

These decisions always require the human author:

| Decision | Why it cannot be delegated |
|---|---|
| Whether a citation supports a specific claim | Requires reading the full text with scientific judgment |
| Whether a claim is in scope for this manuscript | Requires knowledge of the submission target and contribution |
| Whether an interpretation is appropriately hedged | Requires the author's assessment of the evidence |
| Whether a limitation must be stated | Requires judgment about what will be challenged in peer review |
| Whether a figure conveys the correct message | Requires the author's understanding of what was measured |
| Final submission certification | Required by all publisher policies |

---

## Recording checkpoint completion

After each checkpoint is cleared, record it in `AGENT_HANDOFF.md`:

```
HG0a — Integrity check cleared — [date] — [brief note on what was resolved]
HG1  — Introduction section plan approved — [date]
HG2c — Introduction quality gate — PASS — [date]
```

This record ensures that subsequent sessions know which stages have been completed and approved, and provides an audit trail for the final pre-submission review.
