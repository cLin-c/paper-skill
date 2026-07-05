# literature-review

Build a structured related-work and research-gap map before writing the introduction or related work.

## Use When

- Related work reads like a paper list instead of an argument.
- The research gap is vague or unsupported.
- You need to explain how prior work differs from your method.
- You need a citation-role table before drafting.

## Input

```text
Use $paper-skill literature-review.

Topic:
[research topic]

Target venue:
[journal/conference]

Papers:
[titles, abstracts, DOI/BibTeX, or uploaded PDFs]

My work:
[one-paragraph method/contribution]

Requirements:
- Build a related-work matrix.
- Extract research gaps.
- Assign each citation a role.
- Do not invent missing DOI or results.
```

## Output

| Section | Content |
|---|---|
| Literature clusters | Groups prior work by method, task, data, or limitation |
| Citation role table | Background / method precedent / baseline / limitation / contrast |
| Gap map | What prior work cannot solve and which citations support that gap |
| Related-work outline | Paragraph order and transition logic |
| Author input needed | Missing DOI, missing paper details, unsupported claims |

## Quality Rules

- Do not cite papers for claims they do not support.
- Do not treat a review paper as primary evidence for a specific result.
- Use direct contrast: "X addresses A but does not handle B; our work targets B under C."
- Mark weak or missing citation support as `[AUTHOR_INPUT_NEEDED: ...]`.
