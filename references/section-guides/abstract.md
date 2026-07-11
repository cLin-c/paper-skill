# Abstract writing guide

Build the abstract from the verified argument model, not from the Introduction's first sentences.

## Required semantic slots

1. **Problem and setting** — the concrete task under the conditions that make it difficult.
2. **Gap** — what existing approaches fail to model, measure, or support.
3. **Core insight** — the observation that makes the method plausible.
4. **Method** — what was changed and how it acts; avoid a module inventory.
5. **Evidence** — named dataset/setting, comparator, metric, and numeric result when supplied.
6. **Scope** — the strongest conclusion warranted by that evidence.

Use 4–7 sentences unless the venue imposes another structure. Omit a slot only when the study type makes it irrelevant.

## Three legitimate arcs

- **Problem → gap → method → evidence → implication**: default methods paper.
- **Observation → unresolved mechanism → test → finding → implication**: discovery paper.
- **Resource need → resource design → validation → access/use**: dataset or platform paper.

Do not use “multiple contributions” as an arc unless the contributions support one central claim. A list of modules is not a story.

## Evidence calibration

Replace vague superiority with a four-part result:

```text
On [evaluation setting], [method] changed [metric] from [baseline value] to [value]
relative to [named comparator], under [scope condition].
```

If any field is unavailable, mark it. Never manufacture a number to complete the sentence.

## Compression order

When over the word limit, remove in this order:

1. generic field importance;
2. implementation details already implied by the method;
3. adjective claims such as novel, robust, comprehensive;
4. secondary results;
5. future-work language.

Do not remove the gap, central mechanism, primary evidence, or scope limitation.

## Quality gate

- Can a reader identify the task, gap, method mechanism, and primary evidence?
- Does every numeric statement occur consistently in the Results?
- Is the final claim narrower than or equal to the evidence?
- Are unexplained abbreviations absent?
- Could the abstract describe a competitor simply by replacing the method name? If yes, it is too generic.

Use [examples/section-rewrites.md](../../examples/section-rewrites.md) for a synthetic before/after example.

