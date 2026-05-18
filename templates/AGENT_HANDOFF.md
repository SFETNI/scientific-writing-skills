# Agent Handoff

The agent reads this file at the start of every session to understand the current state of the project. Update it at the end of every session.

## Current state

```text
CURRENT_PHASE:      [Pre-draft / Drafting - Introduction / Drafting - Methods / Review / Final QC / Submitted]
ACTIVE_TASK:        [Brief description of what to do next]
LAST_UPDATED:       [YYYY-MM-DD]
LAST_SESSION_AGENT: [Claude / Codex / other]
```

## Read-first list

Files the agent must read at the start of the next session, in order:

1. `AUTHOR_CONTEXT.md`
2. `NUMERICAL_REGISTRY.md`
3. `CLAIM_REGISTER.md`
4. `STYLE_GUIDE.md`
5. `SECTION_PLAN.md`
6. [Add any section-specific files or latest review reports for the current task]

---

## HiTL checkpoint log

Record every human checkpoint clearance here (append, do not overwrite):

```text
# HG0a - Integrity check cleared - [date]
# HG0c - Style calibration approved - [date]
# HG1  - Section plan approved - [section] - [date]
# HG2c - Section accepted - [section] - [date] - gate [PASS/FAIL]
# [Add entries as work progresses]
```

---

## Section status

| Section | Status | Gate | Date |
|---|---|---|---|
| Introduction | [Not started / In progress / Drafted / Accepted] | [PASS / FAIL / Needs review / -] | |
| Methods | | | |
| Results | | | |
| Discussion | | | |
| Conclusions | | | |
| Supplementary Material | | | |

## Review and subagent outputs

Track bounded review reports and whether they are current with the manuscript.

| Output | Status | Last updated | Notes |
|---|---|---|---|
| Citation audit | [Missing / Draft / Current / Stale] | | |
| Figure QC | [Missing / Draft / Current / Stale] | | |
| Table design QC | [Missing / Draft / Current / Stale] | | |
| Visual consistency | [Missing / Draft / Current / Stale] | | |
| Reviewer simulation | [Missing / Draft / Current / Stale] | | |
| Argument flow | [Missing / Draft / Current / Stale] | | |
| Editorial decision estimate | [Missing / Draft / Current / Stale] | | |
| Revision quality gate | [Missing / Draft / Current / Stale] | | |

## Deferred items

Tasks that were identified but not completed - address in next session:

| Item | Priority | Description |
|---|---|---|
| [e.g., Citation check for Doe2023] | High | Abstract not yet confirmed - at KEY_EXISTS only. |
| | | |

## Process trace log

Append process traces here after each session (from `skill_process_trace.md`):

```text
[Process traces appended here]
```
