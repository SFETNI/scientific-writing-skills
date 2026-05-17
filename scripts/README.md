# Scripts

## check_manuscript_integrity.py

Manuscript integrity checker. Runs 5 checks:

1. **Citation keys**: all `\cite{}` keys exist in the `.bib` file
2. **Figure paths**: all `\includegraphics{}` paths resolve to real files
3. **Banned phrases**: scans for AI-writing artifacts (configurable list)
4. **Numerical discipline**: cross-references decimal values against `NUMERICAL_REGISTRY.md`
5. **Policy checklist**: checks for AI disclosure, data availability, competing interests, author contributions

**Exit code**: `0` = no hard errors, `1` = hard errors found

### Usage

```bash
python scripts/check_manuscript_integrity.py \
    --main-tex manuscript/main.tex \
    --bib manuscript/references/refs.bib \
    --registry NUMERICAL_REGISTRY.md \
    --banned-phrases docs/banned_phrases.json   # optional
```

### Arguments

| Argument | Required | Description |
|---|---|---|
| `--main-tex` | Yes | Path to `main.tex` |
| `--bib` | Yes | Path to `.bib` file |
| `--registry` | No | Path to `NUMERICAL_REGISTRY.md` (default: `NUMERICAL_REGISTRY.md`) |
| `--banned-phrases` | No | Path to JSON file with list of additional banned phrases |
| `--no-numerical` | No | Skip numerical discipline check (faster for large manuscripts) |

### Custom banned phrases

Create a JSON file with a list of strings:

```json
[
  "project-specific phrase to ban",
  "another domain-specific phrase"
]
```

Pass it with `--banned-phrases path/to/banned_phrases.json`.

The default list in the script covers field-neutral AI-writing artifacts. The `ANTI_AI_WRITING_STYLE.md` file documents all defaults.

### Python requirements

Standard library only (`re`, `os`, `sys`, `json`, `argparse`, `pathlib`). No `pip install` required.

### Integration with Claude Code

The `/srs-check` command reads `AUTHOR_CONTEXT.md` for the paths and calls this script. You can also run it directly from the terminal.

### Output interpretation

- `HARD ERROR`: must resolve before any drafting begins
- `WARNING`: should review; flag for human decision
- `INFO`: orphan `.bib` entries, policy items not yet present
- `PASS`: policy check item found in manuscript
