# figure-audit

Check whether manuscript figures actually support the claims made in the text.

## Use When

- A figure looks attractive but its scientific message is unclear.
- The caption does not match the figure.
- The text claims more than the figure shows.
- A reviewer may question whether the experiment supports the conclusion.

## Input

```text
Use $paper-skill figure-audit.

Figure:
[image path or figure description]

Caption:
[current caption]

Related manuscript text:
[paragraphs that cite this figure]

Target journal:
[journal/conference]

Requirements:
- Tell me what the figure actually proves.
- Check whether the caption over-claims.
- Check whether the manuscript text is supported.
- Suggest caption and text revisions.
```

## Output

| Check | Output |
|---|---|
| Core claim | One sentence describing what the figure can support |
| Evidence shown | What panels, axes, tables, or visual elements prove |
| Over-claim risk | Claims not supported by the figure |
| Caption revision | Clear and evidence-calibrated caption |
| Text revision | Safer in-text reference wording |
| Missing evidence | Extra data, labels, statistics, or baselines needed |

## Quality Rules

- Separate visual appeal from scientific evidence.
- Do not infer missing baselines or statistics from the figure.
- Check units, labels, axes, legends, sample size, and baseline names.
- Use conservative language if the figure supports only a limited claim.
