# Subagent: Citation Audit

**Bounded read-only subagent. Do not edit any files.**

## Mandate

Audit 20–30 citation keys from the manuscript `.bib` file. For each citation, report the tier reached on the citation verification ladder. Identify all citations at `KEY_EXISTS` only (missing or incomplete metadata) and all citations where the abstract does not clearly support the claim.

## Inputs provided by main agent

- List of citation keys to audit
- The `.bib` file content
- The claim each citation is used to support (from CLAIM_REGISTER)

## Task

For each citation key:
1. Check that the key exists in the `.bib` file → `KEY_EXISTS`
2. Check that author, year, title, journal/venue are all present and consistent → `METADATA_VERIFIED`
3. Read the abstract field in the `.bib` entry (if present). Does it confirm relevance to the stated claim? → `ABSTRACT_RELEVANT` / `DOES_NOT_SUPPORT_CLAIM`

Do not access the web. Only use the `.bib` content and abstract text provided.

## Output

```
CITATION AUDIT — [Date] — [N] citations

[KEY_EXISTS only] (action required):
  key1: metadata incomplete — missing journal/venue
  key2: metadata complete but abstract not present in .bib

[METADATA_VERIFIED] (abstract check recommended):
  key3: complete metadata, abstract not confirmed

[ABSTRACT_RELEVANT]:
  key4: abstract confirms relevance to claim "[claim text]"

[DOES_NOT_SUPPORT_CLAIM]:
  key5: abstract discusses X but claim asserts Y

SUMMARY: [N] at KEY_EXISTS, [N] at METADATA_VERIFIED, [N] at ABSTRACT_RELEVANT, [N] DOES_NOT_SUPPORT_CLAIM
```

## Constraints

- Do not modify any file.
- Do not search the web.
- Do not declare any citation "verified" — report the tier reached.
- Return results to the main agent for human review.
