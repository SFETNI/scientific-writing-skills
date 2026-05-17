"""
check_manuscript_integrity.py — Manuscript integrity checker for scientific-redaction-skills.

Checks:
  1. Citation keys: all \\cite{} keys exist in the .bib file
  2. Figure paths: all \\includegraphics{} paths resolve to real files
  3. Forbidden phrases: scans for AI-writing artifacts and banned phrases
  4. Numerical discipline: cross-references numbers against NUMERICAL_REGISTRY.md
  5. Policy checklist: logs required disclosure items for final pre-submission review

Usage:
  python scripts/check_manuscript_integrity.py \\
      --main-tex manuscript/main.tex \\
      --bib manuscript/references/refs.bib \\
      --registry NUMERICAL_REGISTRY.md \\
      --banned-phrases docs/banned_phrases.json   # optional

Exit code: 0 = no hard errors, 1 = hard errors found
"""

import re
import os
import sys
import json
import argparse
from pathlib import Path


# ── Default banned phrases (AI-writing artifacts) ────────────────────────────

DEFAULT_BANNED_PHRASES = [
    "it is worth noting that",
    "it is important to note",
    "it is crucial to",
    "it is essential to",
    "needless to say",
    "in this regard",
    "delve into",
    "shed light on",
    "pave the way",
    "a plethora of",
    "a wealth of",
    "undeniably",
    "it goes without saying",
    "as previously mentioned",
    "as mentioned above",
    "it should be noted that",
    "moving forward",
    "going forward",
    "at the end of the day",
    "this work represents a significant advance",
    "this study opens up new possibilities",
    "these findings have broad implications",
    "leverage",
    "utilize",
    "facilitate",
]


# ── Helpers ───────────────────────────────────────────────────────────────────

def read_file(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def strip_comments(tex: str) -> str:
    """Remove LaTeX line comments (% ...) but not escaped percent signs."""
    return re.sub(r"(?<!\\)%[^\n]*", "", tex)


def collect_tex_files(main_tex: Path) -> list[Path]:
    """Recursively collect all .tex files via \\input{} and \\include{} from main_tex."""
    collected = [main_tex]
    base = main_tex.parent
    seen = {main_tex.resolve()}
    queue = [main_tex]
    while queue:
        current = queue.pop()
        content = read_file(current)
        for cmd in re.findall(r"\\(?:input|include)\{([^}]+)\}", content):
            sub = base / (cmd if cmd.endswith(".tex") else cmd + ".tex")
            resolved = sub.resolve()
            if resolved not in seen and sub.exists():
                seen.add(resolved)
                collected.append(sub)
                queue.append(sub)
    return collected


# ── Check 1: Citation keys ────────────────────────────────────────────────────

def check_citations(tex_files: list[Path], bib_path: Path) -> list[str]:
    errors = []
    if not bib_path.exists():
        return [f"HARD ERROR: .bib file not found: {bib_path}"]

    bib_content = read_file(bib_path)
    bib_keys = set(re.findall(r"@\w+\{([^,\s]+)\s*,", bib_content))

    cite_pattern = re.compile(r"\\cite[tp]?\*?\{([^}]+)\}")
    all_cite_keys: dict[str, list[str]] = {}

    for tex in tex_files:
        content = strip_comments(read_file(tex))
        for match in cite_pattern.finditer(content):
            for key in [k.strip() for k in match.group(1).split(",")]:
                all_cite_keys.setdefault(key, []).append(tex.name)

    for key, files in sorted(all_cite_keys.items()):
        if key not in bib_keys:
            errors.append(
                f"HARD ERROR [citation]: key '{key}' not in .bib (cited in: {', '.join(set(files))})"
            )

    orphan_keys = bib_keys - set(all_cite_keys.keys())
    for key in sorted(orphan_keys):
        errors.append(f"INFO [citation]: .bib key '{key}' is defined but never cited")

    return errors


# ── Check 2: Figure paths ─────────────────────────────────────────────────────

def check_figure_paths(tex_files: list[Path], main_tex: Path) -> list[str]:
    errors = []
    base = main_tex.parent

    graphicspath_dirs: list[Path] = [base]
    for tex in tex_files:
        content = strip_comments(read_file(tex))
        for gp in re.findall(r"\\graphicspath\{([^}]+)\}", content):
            for d in re.findall(r"\{([^}]+)\}", gp):
                candidate = base / d
                if candidate.is_dir():
                    graphicspath_dirs.append(candidate)

    fig_pattern = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
    for tex in tex_files:
        content = strip_comments(read_file(tex))
        for match in fig_pattern.finditer(content):
            fig_path_str = match.group(1).strip()
            found = False
            # Try exact path relative to main_tex directory
            candidates = [base / fig_path_str]
            # Try in graphicspath directories, with and without extension
            for gd in graphicspath_dirs:
                candidates.append(gd / fig_path_str)
                for ext in [".pdf", ".png", ".eps", ".jpg", ".jpeg", ".tiff"]:
                    if not fig_path_str.lower().endswith(ext):
                        candidates.append(gd / (fig_path_str + ext))
            for c in candidates:
                if c.exists():
                    found = True
                    break
            if not found:
                errors.append(
                    f"HARD ERROR [figure]: path '{fig_path_str}' not found "
                    f"(in {tex.name})"
                )
    return errors


# ── Check 3: Banned phrases ───────────────────────────────────────────────────

def check_banned_phrases(
    tex_files: list[Path], phrases: list[str]
) -> list[str]:
    warnings = []
    for tex in tex_files:
        content = strip_comments(read_file(tex)).lower()
        lines = content.splitlines()
        for phrase in phrases:
            phrase_lower = phrase.lower()
            for i, line in enumerate(lines, 1):
                if phrase_lower in line:
                    warnings.append(
                        f"WARNING [phrase]: '{phrase}' found in {tex.name}:{i}"
                    )
    return warnings


# ── Check 4: Numerical discipline ────────────────────────────────────────────

def extract_numbers_from_tex(tex_files: list[Path]) -> list[tuple[str, int, str]]:
    """Extract bare decimal numbers from .tex files (heuristic; not exhaustive)."""
    results = []
    number_pattern = re.compile(r"\b(\d+\.\d+)\b")
    for tex in tex_files:
        content = strip_comments(read_file(tex))
        for i, line in enumerate(content.splitlines(), 1):
            for m in number_pattern.finditer(line):
                results.append((tex.name, i, m.group(1)))
    return results


def load_registry_numbers(registry_path: Path) -> set[str]:
    """Extract all decimal numbers from the NUMERICAL_REGISTRY.md file."""
    if not registry_path.exists():
        return set()
    content = read_file(registry_path)
    return set(re.findall(r"\b(\d+\.\d+)\b", content))


def check_numerical_discipline(
    tex_files: list[Path], registry_path: Path
) -> list[str]:
    warnings = []
    if not registry_path.exists():
        warnings.append(
            "WARNING [registry]: NUMERICAL_REGISTRY.md not found — "
            "numerical discipline check skipped"
        )
        return warnings

    registry_numbers = load_registry_numbers(registry_path)
    tex_numbers = extract_numbers_from_tex(tex_files)

    for fname, lineno, value in tex_numbers:
        if value not in registry_numbers:
            warnings.append(
                f"WARNING [registry]: value '{value}' in {fname}:{lineno} "
                f"not found in NUMERICAL_REGISTRY.md"
            )
    return warnings


# ── Check 5: Policy checklist ─────────────────────────────────────────────────

def check_policy(tex_files: list[Path]) -> list[str]:
    info = []
    all_content = "\n".join(read_file(t) for t in tex_files).lower()

    checks = [
        ("AI disclosure statement", ["ai-assisted", "ai assisted", "generative ai", "chatgpt", "claude", "gpt"]),
        ("Data availability statement", ["data availability", "data available", "available at", "deposited"]),
        ("Competing interests", ["competing interest", "conflict of interest", "no conflict"]),
        ("Author contributions", ["author contribution", "conceptualization", "methodology", "writing"]),
    ]

    for label, keywords in checks:
        found = any(kw in all_content for kw in keywords)
        status = "PASS" if found else "INFO"
        info.append(
            f"{status} [policy]: {label} — {'detected' if found else 'NOT detected — verify before submission'}"
        )
    return info


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Manuscript integrity checker for scientific-redaction-skills"
    )
    parser.add_argument("--main-tex", required=True, help="Path to main.tex")
    parser.add_argument("--bib", required=True, help="Path to .bib file")
    parser.add_argument("--registry", default="NUMERICAL_REGISTRY.md",
                        help="Path to NUMERICAL_REGISTRY.md")
    parser.add_argument("--banned-phrases", default=None,
                        help="Path to JSON file with banned phrases list")
    parser.add_argument("--no-numerical", action="store_true",
                        help="Skip numerical discipline check (faster)")
    args = parser.parse_args()

    main_tex = Path(args.main_tex)
    bib_path = Path(args.bib)
    registry_path = Path(args.registry)

    if not main_tex.exists():
        print(f"HARD ERROR: main.tex not found: {main_tex}", file=sys.stderr)
        return 1

    # Load banned phrases
    banned = list(DEFAULT_BANNED_PHRASES)
    if args.banned_phrases:
        bp_path = Path(args.banned_phrases)
        if bp_path.exists():
            with bp_path.open() as f:
                extra = json.load(f)
                if isinstance(extra, list):
                    banned.extend(extra)
        else:
            print(f"WARNING: banned-phrases file not found: {bp_path}")

    print("=" * 60)
    print("MANUSCRIPT INTEGRITY CHECK")
    print(f"Main TeX:  {main_tex}")
    print(f"Bib file:  {bib_path}")
    print(f"Registry:  {registry_path}")
    print("=" * 60)

    tex_files = collect_tex_files(main_tex)
    print(f"\nTeX files found: {len(tex_files)}")
    for tf in tex_files:
        print(f"  {tf}")

    all_messages: list[str] = []

    print("\n--- CHECK 1: Citation keys ---")
    citation_results = check_citations(tex_files, bib_path)
    for m in citation_results:
        print(f"  {m}")
    all_messages.extend(citation_results)

    print("\n--- CHECK 2: Figure paths ---")
    figure_results = check_figure_paths(tex_files, main_tex)
    for m in figure_results:
        print(f"  {m}")
    all_messages.extend(figure_results)

    print("\n--- CHECK 3: Banned phrases ---")
    phrase_results = check_banned_phrases(tex_files, banned)
    for m in phrase_results[:20]:  # cap output at 20 warnings
        print(f"  {m}")
    if len(phrase_results) > 20:
        print(f"  ... and {len(phrase_results) - 20} more phrase warnings (run with --verbose to see all)")
    all_messages.extend(phrase_results)

    if not args.no_numerical:
        print("\n--- CHECK 4: Numerical discipline ---")
        num_results = check_numerical_discipline(tex_files, registry_path)
        for m in num_results[:20]:
            print(f"  {m}")
        if len(num_results) > 20:
            print(f"  ... and {len(num_results) - 20} more numerical warnings")
        all_messages.extend(num_results)
    else:
        print("\n--- CHECK 4: Numerical discipline --- SKIPPED")

    print("\n--- CHECK 5: Policy checklist ---")
    policy_results = check_policy(tex_files)
    for m in policy_results:
        print(f"  {m}")
    all_messages.extend(policy_results)

    # Summary
    hard_errors = [m for m in all_messages if m.startswith("HARD ERROR")]
    warnings = [m for m in all_messages if m.startswith("WARNING")]
    info = [m for m in all_messages if m.startswith("INFO")]
    passes = [m for m in all_messages if m.startswith("PASS")]

    print("\n" + "=" * 60)
    print("SUMMARY")
    print(f"  Hard errors : {len(hard_errors)}")
    print(f"  Warnings    : {len(warnings)}")
    print(f"  Info        : {len(info)}")
    print(f"  Policy pass : {len(passes)}")
    print("=" * 60)

    if hard_errors:
        print("\nHARD ERRORS (must resolve before any drafting):")
        for e in hard_errors:
            print(f"  {e}")
        return 1

    print("\nNo hard errors. Review warnings before proceeding.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
