# /srs-check — Executable Integrity Check

Run the manuscript integrity checker as Step 0a. This command must be run before any drafting session, and again after any content changes.

## What this does

1. Reads `AUTHOR_CONTEXT.md` to find the manuscript paths.
2. Runs `scripts/check_manuscript_integrity.py` with the configured paths.
3. Reports all hard errors (citation key mismatches, figure path issues, forbidden phrases, unregistered numbers).
4. Presents results for human resolution.

## Protocol

Read `@templates/AUTHOR_CONTEXT.md` to get:
- `MAIN_TEX_PATH` — path to `main.tex`
- `BIB_PATH` — path to `.bib` file
- `REGISTRY_PATH` — path to `NUMERICAL_REGISTRY.md`
- `BANNED_PHRASES_PATH` — path to `banned_phrases.json` (if configured)

Then run:
```bash
python scripts/check_manuscript_integrity.py \
  --main-tex [MAIN_TEX_PATH] \
  --bib [BIB_PATH] \
  --registry [REGISTRY_PATH] \
  --banned-phrases [BANNED_PHRASES_PATH]
```

If paths are not configured in `AUTHOR_CONTEXT.md`, ask the user to provide them.

## After running

Present the output clearly:
- **HARD ERRORS** (must resolve before proceeding): citation key errors, figure path errors
- **WARNINGS** (should review): forbidden phrases, unregistered numbers
- **INFO**: items to log for final policy checklist

Ask: "There are [N] hard errors and [N] warnings. Which would you like to address first?"

Do not proceed to drafting until all hard errors are resolved.

## Human gate: HG0a

Hard errors must be resolved before any drafting. Record gate clearance in `AGENT_HANDOFF.md`.
