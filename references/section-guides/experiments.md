# Experiments writing guide

Design and write experiments as tests of claims, not as a sequence of tables.

## Question-first plan

Create an experiment map before prose:

| Question ID | Scientific question | Claim tested | Experiment | Comparator/control | Metric | Expected interpretation |
|---|---|---|---|---|---|---|

Typical questions include:

1. Does the full method solve the stated task better under the target condition?
2. Which component or mechanism causes the difference?
3. Under which conditions does the method fail or degrade?
4. Is the comparison fair in data, compute, tuning, and evaluation protocol?
5. Are results stable across seeds, samples, sites, or subgroups?

## Section order

1. **Setup:** datasets/participants, splits, preprocessing, baselines, metrics, implementation, statistics.
2. **Main comparison:** test the central claim first.
3. **Mechanism evidence:** ablation, mediation, sensitivity, visualization, or controlled analysis.
4. **Robustness and scope:** perturbations, external data, subgroups, seeds, or alternative settings.
5. **Failure analysis:** representative errors and boundary conditions.

## Result paragraph contract

Each paragraph should contain:

1. question;
2. comparison and metric;
3. result with uncertainty when available;
4. interpretation limited to the tested condition;
5. link to the corresponding claim.

Do not describe every table cell. Report the pattern that answers the question, then identify exceptions.

## Fairness audit

- same data splits and preprocessing;
- comparable tuning budget and model capacity where relevant;
- baseline implementations and versions identified;
- no selective omission of stronger comparators;
- metrics defined consistently;
- statistical tests match the design and assumptions;
- number of runs/samples and uncertainty reported;
- negative or contradictory results not hidden.

## Ablation logic

An ablation is informative only when removal or replacement isolates a claimed mechanism. “Full model minus module” is insufficient when removal changes parameter count, training stability, or input information. Name confounds explicitly.

## Figure/table contract

Captions must state what is shown, evaluation setting, metric direction, uncertainty/error bars, and statistical annotations. Text, caption, axes, legends, and manuscript claims must agree.

Use [examples/section-rewrites.md](../../examples/section-rewrites.md) for a synthetic before/after example.

