# Example: Chinese Abstract to Academic English

## User Input

```text
我的论文目标期刊是 IEEE TRO。下面是中文摘要草稿，请帮我改成地道英文摘要，并检查是否有主张大于证据的问题。不要编造实验数据。

中文摘要：
移动机器人在复杂室内环境中容易受到动态障碍物和传感器噪声影响，导致路径规划不稳定。本文提出一种融合局部语义地图和风险代价评估的路径规划方法。该方法首先根据激光雷达和视觉信息构建局部语义地图，然后结合障碍物运动趋势计算风险代价，最后在改进的采样规划框架中生成安全路径。实验结果表明，该方法在仿真和真实场景中均能提高路径安全性和规划成功率。
```

## Expected paper-skill Workflow

1. Identify the paper type as a methods paper.
2. Ask for missing quantitative evidence if needed.
3. Rewrite the abstract in concise academic English.
4. Flag unsupported claims such as "提高路径安全性和规划成功率" if no numbers are provided.
5. Produce a version that uses placeholders instead of invented results.

## Example Output Shape

```text
Paper type: methods
Target style: IEEE TRO

Unsupported or underspecified claims:
- "提高路径安全性和规划成功率" needs quantitative evidence, e.g., success rate, collision rate, minimum clearance, or path cost.
- "仿真和真实场景" needs dataset/scenario details and baseline methods.

Rewritten abstract:
Mobile robots operating in cluttered indoor environments often face unstable planning behavior caused by dynamic obstacles and sensor noise. This paper presents a path-planning method that integrates a local semantic map with risk-aware cost evaluation. The method first constructs a local semantic representation from LiDAR and visual observations, estimates motion-related risk costs for nearby obstacles, and then generates collision-aware trajectories within an improved sampling-based planning framework. Experiments in simulated and real-world scenarios show that the proposed method improves planning safety and success rate compared with [AUTHOR_INPUT_NEEDED: baseline methods], with [AUTHOR_INPUT_NEEDED: key numerical results]. These results suggest that semantic risk modeling can improve local navigation robustness in dynamic indoor environments.

Author input needed:
- Baselines
- Number of simulation and real-world scenarios
- Success rate, collision rate, clearance, planning time, or other metrics
- Whether the method runs in real time
```

## Why This Demo Works

It shows the main promise quickly: paper-skill improves English while refusing to invent missing evidence.
