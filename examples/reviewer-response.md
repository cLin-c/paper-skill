# Example: Reviewer Response

## User Input

```text
Use $paper-skill. 帮我回复审稿人意见。我的回复思路是中文的，请改成英文 point-by-point response。

Reviewer comment:
The authors claim that the proposed planner is robust in dynamic environments, but the experiments only include two simple obstacle configurations. The paper should either add more dynamic scenarios or soften the claim.

我的思路：
我们同意这个意见。暂时不能补充新实验，所以把 robustness 的说法改弱，改成在已有测试场景中表现稳定。论文摘要、引言贡献点和实验结论都改了。
```

## Expected paper-skill Workflow

1. Classify the comment as a scope/evidence mismatch.
2. Avoid claiming new experiments were added.
3. Draft a respectful but concise response.
4. Map the response to manuscript locations.
5. Mark exact page/line numbers as author input if not provided.

## Example Output Shape

```text
Triage:
- Type: claim-evidence mismatch
- Risk: high if "robust in dynamic environments" remains unchanged
- Revision strategy: soften the claim and align it with the available scenarios

Response:
We thank the reviewer for pointing out the mismatch between the scope of our robustness claim and the current experimental coverage. We agree that the original wording was too broad given that the experiments include two dynamic obstacle configurations. Since the present revision does not add new dynamic scenarios, we have revised the manuscript to avoid over-claiming. Specifically, we now describe the method as showing stable planning performance in the tested dynamic scenarios rather than being generally robust across dynamic environments.

Revision locations:
- Abstract: revised the robustness statement. [AUTHOR_INPUT_NEEDED: page and line numbers]
- Introduction: revised the contribution statement. [AUTHOR_INPUT_NEEDED: page and line numbers]
- Experiments / Conclusion: softened the interpretation of the dynamic-obstacle results. [AUTHOR_INPUT_NEEDED: page and line numbers]

Quality check:
- No new experiment is claimed.
- The response directly addresses the reviewer's concern.
- The revised claim is aligned with the available evidence.
```

## Why This Demo Works

It shows a practical R&R scenario where paper-skill helps authors sound professional without fabricating revisions.
