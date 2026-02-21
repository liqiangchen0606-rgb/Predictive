# Workflow Evidence (Agentic Methodology)

This file documents stage-by-stage evidence of the workflow:
`plan -> delegate -> verify -> revise`.

## Project Metadata

- Project: `MSIN0097 Individual Coursework`
- Owner: `Chen Liqiang`
- Started: `2026-02-21`
- Current stage: `Scaffolding`

## Evidence Log

| Date | Stage | Goal | Delegated to agent | Verification performed | Decision | Notes |
|---|---|---|---|---|---|---|
| 2026-02-21 | Setup | Initialize coursework repo structure for artefacts 2, 3, 4 | Asked agent to scaffold required files and templates | Manually reviewed created file list and template scope against brief | Accepted | Initial scaffolding complete |
| 2026-02-21 | Implementation | Build first end-to-end churn pipeline scaffold in code | Asked agent to create reusable script with preprocessing, model comparison, and artifact export | Ran static compile and inline smoke check of cleaning logic; noted pytest unavailable in current interpreter | Accepted (temporary baseline) | Later de-prioritized as primary path after notebook-first decision |
| 2026-02-21 | Implementation | Rebuild notebook as primary project workflow (option 1) | Asked agent to reconstruct `MSIN0097_Individual.ipynb` around KaggleHub ingestion and staged ML workflow | Checked notebook JSON validity, section coverage, and inclusion of user-provided Kaggle import code | Accepted | Notebook now primary execution path for coursework analysis |

## Stage Checklist

### 1) Problem framing
- [x] Define target and prediction type
- [x] Define success metrics and constraints
- [ ] Record assumptions and limitations

### 2) EDA
- [x] Distribution analysis
- [x] Missingness and quality checks
- [ ] Leakage/failure risk checks

### 3) Data preparation
- [x] Reproducible preprocessing pipeline
- [ ] Validation checks documented

### 4) Model exploration
- [x] Baseline established
- [x] Multiple models compared
- [ ] Evidence-based shortlist

### 5) Fine-tuning and evaluation
- [ ] Tuning strategy recorded
- [x] Robust error analysis done
- [ ] At least one agent mistake identified and corrected

### 6) Final solution
- [ ] Final model rationale
- [ ] Limitations and risks
- [ ] Model-card style summary
