# Before / After: Chinese Abstract to Submission-Ready English

## Input

```text
我们提出了一个新的机器人路径规划方法，可以在复杂环境里面更稳定。我们的方法用了图结构和不确定性权重，实验结果比传统方法好，能减少重新规划次数。
```

## Weak Direct Translation

```text
We propose a new robot path planning method, which can be more stable in complex environments. Our method uses graph structure and uncertainty weights. The experimental results are better than traditional methods and can reduce replanning times.
```

## paper-skill Output Shape

```text
Paper type: methods paper

Storyline:
partially observed outdoor navigation remains unreliable -> graph planners often treat map edges as fixed -> uncertainty-aware edge weighting and online map repair -> improved completion rate and fewer unnecessary replanning events

Rewritten abstract:
Field robots often fail when planning algorithms are evaluated only under clean and fully observed conditions. We propose an uncertainty-aware graph planning framework for partially observed outdoor environments. The method assigns reliability-aware edge weights, repairs local map inconsistencies online, and checks route-level consistency before execution. In outdoor navigation logs, the proposed planner improves task completion and reduces replanning frequency compared with conventional graph-based baselines. These results suggest that explicitly modeling graph uncertainty can improve deployment robustness without changing the robot hardware.

AUTHOR_INPUT_NEEDED:
- Baseline names and settings
- Number of environments and trials
- Exact completion-rate and replanning metrics
- Dataset or platform details
```

## Why This Is Stronger

| Direct translation problem | paper-skill behavior |
|---|---|
| Generic "new method" wording | Identifies the paper type and contribution arc |
| "Better than traditional methods" over-claims | Requests exact baselines and metrics |
| Missing experimental setting | Marks required author input |
| Chinglish structure | Rewrites into journal-style problem-method-evidence-contribution flow |
