# Before / After: Citation Integrity Audit

## Draft Claim

```text
Graph-based planners are the most robust solution for all outdoor robotic navigation tasks [12-15].
```

## Risky Output

```text
The claim is acceptable because several references support graph-based planning.
```

## paper-skill Output Shape

```text
Risk level: high

Problem:
The phrase "the most robust solution for all outdoor robotic navigation tasks" is broader than what a typical reference set can support. It turns a method family into a universal superiority claim.

Required checks:
- Verify whether references [12-15] are surveys, benchmark papers, or method papers.
- Confirm whether they compare graph-based planners against sampling-based, learning-based, and hybrid planners.
- Check whether the environments match the manuscript setting: outdoor, partially observed, field robot deployment.

Safer rewrite:
Graph-based planners remain widely used for outdoor robot navigation because they provide interpretable route structure and efficient replanning interfaces. However, their robustness depends on map quality, uncertainty modeling, and recovery behavior under partial observability [12-15].

AUTHOR_INPUT_NEEDED:
- DOI/title list for [12-15]
- Which reference supports "widely used"
- Which reference supports "uncertainty modeling"
- Which experiment in this manuscript supports the robustness claim
```

## Why This Is Stronger

| Risk | paper-skill behavior |
|---|---|
| Universal claim | Narrows to supportable language |
| Citation hallucination risk | Requests DOI/title verification |
| Claim not tied to manuscript evidence | Requires local experiment support |
