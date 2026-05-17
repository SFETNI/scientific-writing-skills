# Skill: Process Trace

## Purpose

Required end-of-task report for every agent task. The process trace provides an auditable record of what was done, what was found, and what requires human action. It is appended to `AGENT_HANDOFF.md` after human review.

## Process trace template

```
=== PROCESS TRACE ===
Date: [YYYY-MM-DD]
Session: [Brief description of the session goal]
Agent: [Claude / Codex / subagent]

SKILLS INVOKED
  1. [skill name] — [result in one line]
  2. [skill name] — [result in one line]

FILES READ
  - [file path]
  - [file path]

FILES MODIFIED (Codex tasks only)
  - [file path] — [change description]

OUTPUTS PRODUCED
  - [output description] — [status: AWAITING HUMAN REVIEW / APPROVED / REJECTED]

HUMAN DECISIONS REQUIRED
  - [item 1] — NEEDS_HUMAN_DECISION — [brief description]
  - [item 2] — NEEDS_HUMAN_DECISION — [brief description]

STOP CONDITIONS ENCOUNTERED
  - [any emergency stops — what triggered them, what was needed]

NEXT STEP
  [What should happen next in the workflow]

CHECKPOINT STATUS
  [List which HG checkpoints were cleared in this session]

=== END TRACE ===
```

## Usage

1. At the end of every task, produce a process trace using this template.
2. Present it to the human alongside the task output.
3. After human review and approval, append it to `AGENT_HANDOFF.md`.
4. Update `AGENT_HANDOFF.md` to reflect the current phase and next task.

## Why process traces matter

Without a trace, subsequent sessions have no record of what was done, what was approved, and what was deferred. Traces prevent:
- Repeating work that was already completed
- Missing items that were flagged but not resolved
- Losing the record of which HiTL checkpoints were cleared

A session without a process trace is an incomplete session.
