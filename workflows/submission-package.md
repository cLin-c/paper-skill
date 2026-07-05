# submission-package

Assemble the final materials needed before journal submission.

## Use When

- The manuscript is near submission.
- You need a cover letter, highlights, declarations, or final checklist.
- You want to make sure title, abstract, figures, references, and claims are aligned.

## Input

```text
Use $paper-skill submission-package.

Target journal:
[journal name]

Manuscript:
[file path or pasted text]

Figures/tables:
[file paths or descriptions]

References:
[BibTeX / reference list]

Need:
- title check
- abstract check
- cover letter
- highlights
- data availability statement
- conflict of interest statement
- final submission checklist
```

## Output

| Artifact | Output |
|---|---|
| Title | Clarity, specificity, target-journal fit |
| Abstract | Contribution, method, evidence, limitation check |
| Cover letter | Journal-fit paragraph and contribution paragraph |
| Highlights | 3-5 concise claims backed by evidence |
| Declarations | Data availability, funding, COI, ethics, AI use |
| Final checklist | Missing files, missing statements, risky claims |

## Quality Rules

- Do not invent journal policies. Ask for the target journal guideline or mark as missing.
- Do not invent data availability, ethics approval, funding, or COI statements.
- Keep every highlight supported by a figure, table, experiment, or cited result.
- Mark unresolved items as `[AUTHOR_INPUT_NEEDED: ...]`.
