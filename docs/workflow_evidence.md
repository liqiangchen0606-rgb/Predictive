# Workflow Evidence (Agentic Methodology)

This file documents stage-by-stage evidence of the workflow:
`plan -> delegate -> verify -> revise`.

## Project Metadata

- Project: `MSIN0097 Individual Coursework`
- Owner: `Chen Liqiang`
- Restarted: `2026-02-22`
- Current stage: `Step 3 feature engineering added`

## Evidence Log

| Date | Stage | Goal | Delegated to agent | Verification performed | Decision | Notes |
|---|---|---|---|---|---|---|
| 2026-02-22 | Restart planning | Reframe project setup using coursework six-step structure before rerun | Asked agent for practical structure on problem definition, churn metrics, reproducible repo, and agent documentation | Reviewed proposed problem statement, recall-first metric stack, repo layout, and logging templates for consistency with brief | Accepted | Established clean restart baseline and consistent documentation approach |
| 2026-02-22 | EDA + reproducibility | Add missing churn-focused EDA visuals, pitfalls notes, and reproducible plot-saving workflow | Asked agent to edit notebook directly only for missing items | Verified notebook contains class-imbalance percentages, segment churn visuals, pitfalls notes, and `save_plot()` output to `artifacts/figures` | Accepted | Step 2 evidence strengthened and figures are now reproducible from code |
| 2026-02-22 | Step 3 preprocessing | Build leakage-safe preprocessing pipeline in notebook only (no tuning) | Asked agent to implement modular Step 3 code in notebook part 3 | Verified stratified split, train-only preprocessing fit, safe categorical encoding, missing-value handling, and saved `preprocessing_pipeline.joblib` | Accepted | Step 3 now satisfies brief requirements with explicit leakage safeguards |
| 2026-02-22 | Mistake correction | Fix duplicate-handling logic that could collapse distinct customers after ID drop | Asked agent to revise Step 3 dedup logic after identifying flaw | Verified dedup now occurs on exact raw rows before dropping `customerID`; prior approach explicitly rejected | Accepted correction | Provides explicit agent-mistake evidence for verify/revise requirement |
| 2026-02-22 | Step 4 model comparison | Compare multiple models with CV using training/validation only and export results | Asked agent to implement structured CV comparison code for four classifiers and save outputs to CSV | Verified requested models/metrics present, no test usage in Section 4, and CSV output path exists in code | Accepted | Established evidence-based shortlist workflow with recall-priority ranking |
| 2026-02-22 | Metric correction | Correct Section 4 primary metric choice from recall-first to PR-AUC-first for imbalanced targeting | Asked agent to revise Section 4 ranking/scoring strategy after identifying mismatch with business objective | Verified PR-AUC is now primary metric in CV and validation ranking while recall/F1/ROC-AUC/log-loss remain tracked | Accepted correction | Aligns model selection with precision-sensitive targeting under class imbalance |
| 2026-02-22 | Step 3 feature engineering | Add engineered predictors after split with leakage-safe application across train/val/test | Asked agent to create three features and show a preview of the current engineered dataset | Verified new variables (`is_new_customer`, `avg_charge_per_tenure`, `service_count`) and `X_train.head()` preview are present in Step 3 cell | Accepted | Improved predictor set transparency and interpretability before tuning |

## Stage Checklist

### 1. Obtain a Dataset and Frame the Predictive Problem
- [x] Define target and prediction type
- [x] Define success metrics and constraints
- [x] Record assumptions and limitations

### 2. Explore the Data to Gain Insights
- [x] Distribution analysis
- [x] Missingness and quality checks
- [x] Leakage/failure risk checks

### 3. Prepare the Data
- [x] Reproducible preprocessing pipeline
- [x] Validation checks documented

### 4. Explore Different Models and Shortlist the Best Ones
- [x] Baseline established
- [x] Multiple models compared
- [x] Evidence-based shortlist

### 5. Fine-Tune and Evaluate
- [ ] Tuning strategy recorded
- [ ] Robust error analysis done
- [x] At least one agent mistake identified and corrected

### 6. Present the Final Solution
- [ ] Final model rationale
- [ ] Limitations and risks
- [ ] Model-card style summary
