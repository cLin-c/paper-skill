# Introduction writing guide

An Introduction must make the proposed work feel necessary, not merely announce that it exists.

## Reason backward before writing forward

Answer backward:

1. What is the exact central claim?
2. Which result makes that claim credible?
3. Which method decision caused that result?
4. Which unresolved limitation required that decision?
5. Which real task makes the limitation important?

Then write forward:

```text
task and stakes → precise limitation → why the limitation persists
→ enabling insight → solution principle → contributions and evidence
```

## Paragraph roles

### P1 — Task under a consequential setting

Define the task and the condition under which failure matters. Avoid a broad history of the entire field.

### P2 — Existing capability and residual failure

Group prior work by strategy. State what those strategies solve before describing the remaining limitation. Cite evidence for the limitation.

### P3 — Mechanistic gap

Explain why the limitation persists. Distinguish a symptom (“accuracy drops”) from a cause (“the representation assumes static correspondence”).

### P4 — Insight and solution principle

State the observation that connects the gap to the method. Introduce the method as a response to the mechanism, not as a list of components.

### P5 — Contributions and evidence preview

Use 2–4 contributions. Each contribution must identify an artifact or finding and its evidence. Do not repeat the Abstract verbatim.

## Gap validity test

A defensible gap has four fields:

| Field | Question |
|---|---|
| Population/setting | Where does the problem occur? |
| Existing capability | What can current methods already do? |
| Residual limitation | What remains unsupported or unreliable? |
| Consequence | Why does that limitation matter for the task? |

If the gap relies on “few studies,” establish this through a search, not memory.

## Contribution test

Reject contribution bullets that only say “we propose,” “we design,” or “we conduct experiments.” Require:

```text
Artifact/insight + distinguishing mechanism + supported outcome/scope
```

## Failure modes

- field history longer than the problem statement;
- criticizing prior work without evidence;
- jumping from limitation to architecture without an insight;
- presenting implementation modules as independent innovations;
- promising generality that appears nowhere in the experiments;
- citing a paper for a limitation it did not study.

Use [examples/section-rewrites.md](../../examples/section-rewrites.md) for a synthetic before/after example.

