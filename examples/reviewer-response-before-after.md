# Before / After: Reviewer Response

## Reviewer Comment

```text
The manuscript claims that the proposed planner is robust, but the experiments do not clearly show whether the improvement comes from uncertainty weighting or from online map repair. Please clarify this point.
```

## Weak Reply

```text
Thank you for your valuable comment. We have revised the manuscript and clarified the robustness of our method.
```

## paper-skill Output Shape

```text
Response:
We thank the reviewer for pointing out that the source of the robustness improvement was not sufficiently separated in the original submission. We have added an ablation study that disables online map repair while keeping the uncertainty-aware edge weighting unchanged. The new results show that uncertainty weighting mainly improves route selection under partial observability, whereas online map repair reduces unnecessary replanning after local map inconsistencies are detected.

Manuscript changes:
- Section IV-C, paragraph 2: added the ablation protocol.
- Table II: added the "without map repair" setting.
- Section V, paragraph 1: revised the claim from "our planner is robust" to "uncertainty weighting and online map repair contribute complementary robustness gains."

Remaining limitation:
The ablation is still limited to the current outdoor navigation logs. We now state this limitation in Section V.
```

## Why This Is Stronger

| Weak reply problem | paper-skill behavior |
|---|---|
| Says "revised" without evidence | Maps reply to exact manuscript changes |
| Does not answer the mechanism question | Separates uncertainty weighting from map repair |
| Overstates robustness | Narrows the claim and adds limitation |
