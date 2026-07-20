---
name: paper-skill
description: End-to-end, Chinese-first academic research and publication workflow for reading papers, literature reviews, research framing, manuscript planning and writing, Chinese-English translation, LaTeX, figures, citation verification, reporting-guideline checks, journal selection, peer review, rebuttals, revisions, and submission packages. Use for SCI, IEEE, Nature-family, IJCAI, TRO, theses, systematic reviews, clinical/observational/animal studies, and any task where claims, evidence, references, manuscript files, or journal requirements must be checked rather than invented.
---

# paper-skill

Turn research materials into evidence-calibrated academic outputs. Treat the manuscript as a traceable system of claims, evidence, citations, figures, and submission requirements—not as a free-form writing task.

## Non-negotiable rules

1. Never invent data, experiments, statistics, quotations, references, DOI values, journal policies, author contributions, ethics approvals, funding, or revision locations.
2. Separate three states explicitly: `VERIFIED`, `UNVERIFIED`, and `AUTHOR_INPUT_NEEDED`.
3. Preserve scientific meaning before improving style. Flag contradictions instead of silently repairing them.
4. Map every material claim to evidence. Downgrade or remove unsupported claims.
5. Verify time-sensitive journal policies and bibliographic metadata against primary sources when tools permit. Record source and access date.
6. Never promise acceptance, impact factor outcomes, or detector evasion. Quality scores are internal triage, not publication predictions.
7. Keep a change ledger for manuscript edits: location, original, revision, reason, evidence affected.

Read [references/verification-policy.md](references/verification-policy.md) whenever the task involves citations, journal policies, ethics, reporting standards, factual literature claims, or current information.

## Route the task

First classify the request, then load only the indicated resources.

| Route | Typical requests | Required resources |
|---|---|---|
| `read` | Read, summarize, critique, bilingual notes | [references/paper-writing-prompts.md](references/paper-writing-prompts.md) |
| `literature` | Search strategy, review, gap map, related work | [workflows/literature-review.md](workflows/literature-review.md), [citation-integrity.md](citation-integrity.md) |
| `write` (`plan-write`) | Storyline, outline, draft, rewrite, polish, translate | Load the matching section guide below plus [references/output-contracts.md](references/output-contracts.md) |
| `figures` | Method diagram, result figure, caption, figure audit | [references/figure-prompts.md](references/figure-prompts.md), [workflows/figure-audit.md](workflows/figure-audit.md) |
| `review` | Pre-submission review, rejection risks, adversarial audit | [quality-gates.md](quality-gates.md), [references/output-contracts.md](references/output-contracts.md) |
| `rebuttal` | Reviewer response, R&R, rebuttal, revision verification | [references/output-contracts.md](references/output-contracts.md), [quality-gates.md](quality-gates.md) |
| `citations` | DOI audit, hallucination scan, claim-source match | [citation-integrity.md](citation-integrity.md), [workflows/reference-tools.md](workflows/reference-tools.md) |
| `journal` | Venue selection, transfer, policy, formatting | [journal-strategy.md](journal-strategy.md), [references/verification-policy.md](references/verification-policy.md) |
| `submit` (`submission`) | Cover letter, highlights, declarations, final package | [workflows/submission-package.md](workflows/submission-package.md), [references/output-contracts.md](references/output-contracts.md) |
| `reporting` | CONSORT, PRISMA, STROBE, ARRIVE, CARE, SPIRIT | [references/reporting-guidelines.md](references/reporting-guidelines.md), [references/verification-policy.md](references/verification-policy.md) |
| `full-verify` | DOI lookup, journal policy evidence, manuscript/rebuttal consistency | [workflows/full-verification.md](workflows/full-verification.md) |

For IEEE Transactions on Robotics, also load [references/venues/ieee-tro.md](references/venues/ieee-tro.md). Treat every venue profile as a dated starting point and re-check its official links before submission.

For a multi-route request, load the smallest combination that covers it. Do not load the general prompt bank unless the routed resources are insufficient; then use [references/prompt-bank.md](references/prompt-bank.md).

### Section-writing selector

| Target | Load |
|---|---|
| Paragraph flow or full-section structure | [references/section-guides/paragraph-architecture.md](references/section-guides/paragraph-architecture.md) |
| Abstract | [references/section-guides/abstract.md](references/section-guides/abstract.md) |
| Introduction | [references/section-guides/introduction.md](references/section-guides/introduction.md) |
| Related Work | [references/section-guides/related-work.md](references/section-guides/related-work.md) |
| Method | [references/section-guides/method.md](references/section-guides/method.md) |
| Experiments/Results | [references/section-guides/experiments.md](references/section-guides/experiments.md) |
| Discussion/Conclusion | [references/section-guides/discussion-conclusion.md](references/section-guides/discussion-conclusion.md) |

For worked patterns, load [examples/section-rewrites.md](examples/section-rewrites.md). The examples are synthetic; reuse reasoning structure, never their facts.

## Core workflow

### 1. Intake and provenance

Create a compact intake record:

- task and intended artifact;
- paper type and discipline;
- target venue and deadline, if supplied;
- authoritative source files and version order;
- available evidence: datasets, experiments, figures, tables, code, references;
- required output format;
- unresolved author decisions.

If several manuscript versions exist, ask which is authoritative only when it cannot be inferred safely. Never merge conflicting values silently.

### 2. Build the argument model

Before drafting or reviewing, state:

- research question;
- one-sentence central claim;
- 2–5 supporting claims;
- evidence supporting each claim;
- scope conditions and limitations;
- novelty relative to named prior work.

Use IDs (`C1`, `E1`, `R1`, `F1`) so claims, evidence, references, and figures can be traced.

### 3. Choose the operation

- **Draft:** build from the argument model, not from generic section templates.
- **Rewrite:** diagnose structure first; preserve facts, equations, citations, and numbers.
- **Translate:** translate meaning and rhetorical function; keep a terminology table and ambiguity log.
- **Review:** separate fatal validity issues, major evidence gaps, minor clarity issues, and optional improvements.
- **Rebuttal:** map every reviewer point to response, manuscript change, exact location, and verification status.
- **Submission:** reconcile title, abstract, highlights, figures, declarations, and cover letter against the manuscript.

### 4. Verify

Run checks proportional to the task:

- claim ↔ evidence;
- claim ↔ citation;
- text ↔ figure/table;
- response letter ↔ revised manuscript;
- journal policy ↔ official current source;
- reporting checklist ↔ study design;
- terminology, symbols, units, sample sizes, and metric consistency.

When a submission-package JSON is available, run:

```bash
python tools/paper_skill_gate.py path/to/package.json
```

Use `--format json` for machine-readable output and `--strict` to treat warnings as a nonzero exit.

For a complete online and cross-file verification run, use:

```bash
python tools/run_full_workflow.py path/to/workflow-config.json --output full-report.json
```

### 5. Deliver with uncertainty visible

Every substantial output must include:

1. the requested artifact;
2. evidence/traceability notes appropriate to the task;
3. unresolved items labeled `AUTHOR_INPUT_NEEDED`;
4. verification summary—what was checked, what was not, and why;
5. next gate, if the artifact is part of a longer workflow.

Follow the schemas in [references/output-contracts.md](references/output-contracts.md).

## File and artifact handling

- Preserve the original; write revisions to a new file unless replacement is explicitly requested.
- For DOCX, PDF, spreadsheets, or slides, use the relevant artifact skill and render/inspect the final output.
- For LaTeX, compile when a TeX toolchain is available; inspect warnings, references, floats, and rendered pages.
- For figures, inspect axes, units, legends, panel labels, sample sizes, uncertainty, and caption agreement.
- Never claim a file was modified, compiled, or visually checked unless it actually was.

## Completion gates

Do not call work “submission-ready” while any critical item remains:

- unsupported central claim;
- unresolved contradictory data;
- fabricated or unverified high-risk citation;
- missing ethics/registration information when applicable;
- reviewer response without a matching manuscript change;
- figure/table inconsistent with the text;
- journal requirement not checked against a current official source.

Use `READY`, `READY_WITH_WARNINGS`, or `NOT_READY`; always state the blocking evidence.
