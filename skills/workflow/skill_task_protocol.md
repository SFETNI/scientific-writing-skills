# Skill: Task Protocol

## Purpose

Standard operating procedure for every agent task in this framework. All agents (Claude, Codex, subagents) must follow this protocol. This document does not require human approval — it is a process guide.

## Step 0 — Session startup (mandatory before any task)

```
Step 0a: Run check_manuscript_integrity.py — resolve all hard errors before proceeding
Step 0b: Read AUTHOR_CONTEXT.md, NUMERICAL_REGISTRY.md, ANTI_AI_WRITING_STYLE.md
Step 0c: If first drafting session — run /srs-calibrate and await human approval of style report
Step 0d: Read AGENT_HANDOFF.md — confirm current phase and active task
```

## Step 1 — Task scoping

Before starting any task:
1. State the task in one sentence.
2. List the skill(s) to be invoked.
3. List the input files to be read.
4. State the expected output format.
5. State the human-in-the-loop checkpoint.

Present this scope to the human and confirm before proceeding.

## Step 2 — Task execution

1. Read all required inputs (do not rely on memory from a previous session).
2. Apply the skill mandate exactly.
3. Produce output with inline evidence labels where required.
4. Do not exceed the skill mandate (no scope creep).

## Step 3 — Output presentation

1. Present the output clearly, with section headers.
2. Highlight all items requiring human decision (use `ACTION REQUIRED` or `NEEDS_HUMAN_DECISION`).
3. Do not act on the output — wait for human review.

## Step 4 — Human review

Wait for the human to:
- Approve, reject, or request revisions
- Resolve all `ACTION REQUIRED` items
- Confirm acceptance before proceeding to the next task

## Step 5 — Process trace

After every task, produce a process trace following `skill_process_trace.md`.

## Emergency stop

If at any point:
- A quantitative value is needed that is not in `NUMERICAL_REGISTRY.md` — stop and ask
- A claim is required that has no registered source — stop and ask
- A web search would be needed — stop and ask for explicit authorization
- The human has not confirmed the section plan — stop and ask before drafting

Do not proceed past a stop condition without human input.
