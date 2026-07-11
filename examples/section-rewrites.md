# Synthetic section rewrite examples

These examples are original and intentionally generic. Bracketed values must come from the author's evidence.

## 1. Abstract: vague superiority to evidence-calibrated result

### Before

> Existing methods have many problems. We propose a novel and robust framework with several effective modules. Extensive experiments demonstrate that our method achieves superior performance.

### Diagnosis

- no setting or residual gap;
- modules replace mechanism;
- “extensive” and “superior” have no comparator or metric;
- scope is unlimited.

### After

> Outdoor localization degrades when transient obstacles break the static correspondences assumed by map-based estimators. We introduce an uncertainty-gated update rule that suppresses inconsistent landmarks before pose optimization. On [dataset/site], the method reduced [metric] from [baseline] to [result] relative to [comparator] under [condition]. These results support improved localization in the evaluated environments; performance outside those conditions remains untested.

## 2. Introduction: architecture jump to insight-led necessity

### Before

> Robot perception is important and has been widely studied. Many deep-learning methods have achieved good results, but they still have limitations. Therefore, we propose a network containing a temporal module, an attention module, and a fusion module.

### After

> Field robots must maintain object tracks while illumination and viewpoint change faster than labeled observations can be collected. Current appearance-driven trackers handle short occlusion but often reuse stale features after long interruptions [verified citations needed]. The resulting failure is not simply insufficient model capacity: the tracker lacks an explicit estimate of whether a historical feature remains trustworthy. This observation motivates a reliability-conditioned memory that updates only when geometric and appearance cues agree. The proposed pipeline implements this principle through temporal reliability estimation and gated fusion; each component is evaluated against the corresponding failure mode.

### Why it is stronger

The revision connects task → observed failure → mechanism → insight → design. It does not present three modules as three independent innovations.

## 3. Related Work: paper list to technical synthesis

### Before

> Smith et al. proposed Method A. Wang et al. proposed Method B. Lee et al. proposed Method C. These methods perform well, but our method is better.

### After

> Existing approaches address temporal inconsistency through feature aggregation or explicit state propagation. Aggregation methods combine nearby observations and are effective under short disturbances, but their fixed temporal window limits recovery after long gaps [R1–R3]. State-propagation methods preserve longer histories, although their updates typically assume that incoming observations remain reliable [R4–R6]. Our method targets this assumption by estimating observation reliability before memory update; the comparison is therefore about update validity rather than model size.

## 4. Method: component description to Need–Design–Effect

### Before

> We use an attention module to improve features. The input passes through three convolutional layers and a sigmoid function. The output is multiplied by the original feature.

### After

> Occluded regions produce activations that are locally strong but inconsistent with the preceding state, so magnitude alone cannot determine whether a feature should update memory. Given the current feature map \(F_t\) and projected historical state \(H_{t-1}\), we compute a compatibility score \(S_t=g([F_t,H_{t-1}])\) and obtain an update gate \(G_t=\sigma(S_t)\). The gated feature \(\tilde F_t=G_t\odot F_t\) supplies the memory update. This design predicts reduced drift after occlusion; Experiment [E3] tests that effect by removing compatibility-conditioned gating while holding the backbone fixed.

### Remaining author inputs

- define function \(g\), tensor dimensions, and training objective;
- confirm that Experiment E3 holds parameter count or compute sufficiently constant.

## 5. Experiments: table narration to question-driven evidence

### Before

> Table 2 shows the results. Our method obtains 81.4, which is higher than A at 79.1 and B at 80.0. This proves the effectiveness and robustness of our model.

### After

> We first tested whether reliability-conditioned updates improve tracking under long occlusion (C1). On the held-out long-occlusion subset, the proposed method achieved [81.4 metric units], compared with [79.1] for A and [80.0] for B (Table 2). The gain is consistent with C1 in this subset, but it does not by itself establish robustness to other disturbances. Results across [seeds/sequences] and the corresponding uncertainty are required before judging stability.

## 6. Discussion: generic limitation to claim-specific boundary

### Before

> Our method has some limitations and will be improved in future work.

### After

> The evaluation used recordings from one field site, so the observed reduction in localization error supports C1 only for environments represented by that site. Seasonal appearance changes and different sensor placements may alter the reliability estimates that drive the update gate. External-site evaluation is therefore required before claiming geographic or hardware generalization.

## How to use these examples

Do not copy their scientific content. Reuse the reasoning pattern, replace every bracketed item with verified evidence, and preserve unresolved fields as `AUTHOR_INPUT_NEEDED`.

