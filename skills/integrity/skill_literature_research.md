# Skill: Literature Research

## Mandate

Search for references to fill citation gaps identified by `skill_citation_check.md` or `skill_claim_evidence_verification.md`. This skill requires **explicit human authorization** before any web search is performed. The human specifies which claims need citations and approves the search terms. The skill returns candidate references for human review — it does not add citations to the manuscript.

## Required inputs

- Explicit human authorization statement: "Authorized: search for references for claims X, Y, Z"
- List of specific claims needing citations (from `CLAIM_REGISTER.md` or human)
- `@templates/AUTHOR_CONTEXT.md` — target journal, field

## Authorization gate (mandatory)

**This skill cannot activate without explicit human authorization.**

Before any search:
1. Present the list of claims needing citations.
2. Propose search terms for each.
3. Wait for human to confirm: "Authorized to search for [specific items]."
4. Proceed only for the authorized items.

Do not search beyond the authorized scope.

## Search protocol

For each authorized claim:
1. Search using the proposed terms (PubMed, Semantic Scholar, arXiv, CrossRef depending on field).
2. Return the top 5–10 candidates with: title, authors, year, venue, abstract excerpt, DOI.
3. Do NOT add any found reference to the `.bib` file without human confirmation.
4. Label each candidate as: `POTENTIALLY_RELEVANT`, `PROBABLY_RELEVANT`, or `NEEDS_HUMAN_REVIEW`.

## Acceptance criteria

1. Human authorized the search explicitly before it ran.
2. Candidate references are returned with full metadata (title, authors, year, venue, DOI).
3. No reference is added to the manuscript or `.bib` without human confirmation.
4. The human reads the abstract of each candidate before accepting it.
5. Every accepted reference starts at `METADATA_VERIFIED` tier in the citation audit.

## Human-in-the-loop checkpoint

Human must:
- Authorize the search scope before the skill runs
- Read the abstract of each candidate reference
- Confirm which candidates to add to the `.bib` file
- After adding to `.bib`, run `skill_citation_check.md` to verify the new entries

## Fail conditions

- Skill runs a search without human authorization.
- A found reference is added to the manuscript without human confirmation.
- Search results are presented as "confirmed" — they are candidates only.
- The skill invents references or DOIs (hallucination risk — all found references must be real and verifiable).

## Risk note

Literature search is the highest-risk skill in this framework. AI-generated citations that do not exist are a documented failure mode in scientific writing. This skill mitigates that risk by:
1. Requiring explicit authorization
2. Presenting candidates with metadata for human review
3. Never adding anything to the `.bib` without human confirmation
4. Starting all new citations at `METADATA_VERIFIED` tier, not `FULL_TEXT_SUPPORTS_CLAIM`
