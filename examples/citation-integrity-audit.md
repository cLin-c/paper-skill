# Example: Citation Integrity and Over-Claim Audit

## User Input

```text
Use $paper-skill. 请检查下面这段引言有没有引用幻觉和主张过强的问题。不要联网编造文献；只基于我提供的信息判断。

Paragraph:
Recent studies have demonstrated that semantic mapping can fully solve dynamic obstacle avoidance in indoor navigation [12-14]. Based on these works, our method achieves state-of-the-art robustness in all real-world scenes.

References:
[12] A paper about semantic mapping for static indoor scene understanding.
[13] A paper about dynamic obstacle prediction in simulation only.
[14] A review paper about robot navigation challenges.
```

## Expected paper-skill Workflow

1. Check whether each citation supports the sentence.
2. Flag claim-support mismatch.
3. Rewrite the paragraph with evidence-calibrated language.
4. Ask for missing proof before allowing stronger claims.

## Example Output Shape

```text
Citation integrity audit:

Claim 1:
"semantic mapping can fully solve dynamic obstacle avoidance in indoor navigation [12-14]"

Risk:
High. The references described by the author do not support "fully solve".
- [12] covers static scene understanding, not dynamic obstacle avoidance.
- [13] covers simulation only, not real-world indoor navigation.
- [14] is a review and may support motivation, but not a solved-problem claim.

Suggested revision:
Recent studies have shown that semantic mapping can improve scene understanding for indoor navigation, while dynamic obstacle prediction remains challenging in real-world environments [12-14].

Claim 2:
"our method achieves state-of-the-art robustness in all real-world scenes"

Risk:
High. This requires broad benchmarks, multiple real-world scenes, strong baselines, and quantitative metrics.

Suggested revision:
Our method improves planning stability in the evaluated real-world scenarios compared with [AUTHOR_INPUT_NEEDED: baselines], but broader validation is needed to establish general robustness.

Author input needed:
- Exact titles and DOI for [12-14]
- Baseline methods
- Real-world scenario count
- Metrics supporting robustness
- Whether "state-of-the-art" is justified by public benchmarks
```

## Why This Demo Works

It shows that paper-skill is not only a writing assistant. It also checks whether citation evidence actually supports the manuscript's claims.
