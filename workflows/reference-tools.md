# reference-tools

Lightweight reference consistency workflow for manuscripts and reference lists.

## Use When

- You suspect AI-generated or incorrect references.
- In-text citations do not match the reference list.
- DOI, title, year, or venue details may be incomplete.
- You need a quick pre-submission reference checklist.

## Input

```text
Use $paper-skill reference-tools.

Manuscript citations:
[in-text citations or manuscript file]

Reference list:
[reference list or BibTeX]

Requirements:
- Match in-text citations to references.
- Flag missing references.
- Flag unused references.
- Flag incomplete DOI/title/year/venue.
- Do not invent missing metadata.
```

## Output

| Check | Output |
|---|---|
| In-text to reference match | Missing or unmatched citations |
| Reference to in-text match | Unused references |
| Metadata completeness | Missing DOI, title, year, venue, pages |
| Suspicious references | Generic titles, impossible years, inconsistent venues |
| Claim support warning | References used for claims that need closer source checking |

## Quality Rules

- Do not fabricate DOI, title, venue, or page numbers.
- Mark unverifiable metadata as `[AUTHOR_INPUT_NEEDED: ...]`.
- For high-risk claims, route to `citation-integrity` for claim-level support checking.
- Prefer primary sources over reviews for specific empirical claims.
