# Skill: Human Checkpoints Manifest

## Purpose

This document lists all mandatory human-in-the-loop checkpoints in pipeline order. No content is accepted, and no stage advances, without the corresponding human decision.

## Mandatory checkpoint table

| Stage | Checkpoint ID | What the human must do | Blocking? |
|---|---|---|---|
| **0 — Pre-draft** | HG0a | Review integrity check output; resolve all hard errors | YES — no drafting until cleared |
| **0 — Pre-draft** | HG0b | Resolve all UNSUPPORTED claims from skill-based check | YES — no drafting until cleared |
| **0 — Pre-draft** | HG0c | Approve style calibration report | YES — no drafting until approved |
| **1 — Section plan** | HG1 | Approve argument chain for each section | YES — no prose before this |
| **2 — Drafting** | HG2a | Review and approve each section draft | YES |
| **2 — Drafting** | HG2b | Resolve claim-source map from skill_claim_calibration | YES — all UNSUPPORTED must be zero |
| **2 — Drafting** | HG2c | Run and approve revision quality gate | YES — gate must PASS |
| **3 — Figures & SM** | HG3a | Approve figure QC report | YES — before any figure revisions |
| **3 — Figures & SM** | HG3b | Confirm captions against registered values | YES |
| **3 — Figures & SM** | HG3c | Approve SM scope and structure | YES — before SM content is written |
| **4 — Review** | HG4a | Read complete reviewer simulation report | YES |
| **4 — Review** | HG4b | Decide: address or rebut each reviewer concern | YES — document decision in AGENT_HANDOFF |
| **5 — Final QC** | HG5a | Approve revision quality gate on revised manuscript | YES |
| **5 — Final QC** | HG5b | Complete and approve policy checklist | YES — AI disclosure, data availability |
| **5 — Submission** | HG5c | Author certifies all content is accurate and their own | YES — explicit sign-off required |

## What "blocking" means

A blocking checkpoint means the workflow cannot proceed to the next stage until the human provides explicit approval. The agent must wait — it must not guess, assume, or proceed autonomously.

## Non-blocking quality checks

Some checks are advisory and non-blocking:
- `skill_editorial_decision.md` — the estimate is informational; the decision to proceed is the author's
- `skill_argument_flow_review.md` concerns — the agent flags issues; the author decides scope
- `skill_visual_consistency.md` warnings — the author decides which corrections are worth making

## Documenting checkpoint completion

When a checkpoint is cleared, record it in `AGENT_HANDOFF.md`:
```
HG0c — Style calibration approved — 2026-05-16
HG1  — Section plan approved for Introduction — 2026-05-16
```
