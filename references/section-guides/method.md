# Method writing guide

Write the Method so a qualified reader can reconstruct both the design logic and the implementation.

## Pre-writing model

Record before drafting:

- inputs and outputs, including shapes/units;
- assumptions and operating conditions;
- objective or scientific hypothesis;
- module/data-flow graph;
- training/inference or experimental procedure;
- symbols and their first definitions;
- implementation parameters required for reproduction.

If this model is incomplete, mark missing items instead of hiding them in prose.

## Method overview

The overview must answer:

1. What enters and leaves the system?
2. What are the major stages and their dependencies?
3. Which stage embodies the central contribution?
4. What objective connects the stages?

Keep the overview aligned with the pipeline figure and subsection order.

## Module contract: Need–Design–Effect

For every substantive module, cover three functions:

### Need

Identify the upstream failure or requirement. This is a mechanistic reason, not “to improve performance.”

### Design

Define the transformation, variables, equations, algorithm, and interfaces. Explain what each symbol means before relying on it.

### Effect

State the technical consequence that should follow from the design and identify the experiment that tests it. Do not claim the effect as fact before presenting evidence.

This contract is related to the commonly used motivation–design–advantage pattern, but replaces “advantage” with a falsifiable expected effect.

## Equation contract

For every equation:

1. introduce its purpose;
2. define all new symbols, domains, dimensions, and units;
3. state whether variables are observed, learned, fixed, or optimized;
4. explain the equation's role after displaying it;
5. connect it to implementation or evaluation.

Delete equations that only restate prose and add no precision.

## Reproducibility split

Keep conceptual method and implementation details distinct. Implementation details should include applicable versions, hyperparameters, initialization, stopping criteria, random seeds, hardware, preprocessing, and inference settings.

## Cross-checks

- subsection order matches the data-flow order;
- symbols match figures, algorithms, and appendix;
- every claimed module effect maps to an ablation or analysis;
- no test-time information leaks into training;
- complexity claims specify the comparison basis;
- implementation choices are not promoted to contributions without justification.

Use [examples/section-rewrites.md](../../examples/section-rewrites.md) for a synthetic before/after example.

