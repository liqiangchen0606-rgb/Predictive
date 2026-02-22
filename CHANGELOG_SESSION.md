# Session Change Log

Session restarted: 2026-02-22

| # | Action | File(s) | Description |
|---:|--------|---------|-------------|
| 1 | Update | `docs/workflow_evidence.md`, `appendix/agent_usage_log.md`, `appendix/decision_register.md` | Project restart baseline: defined predictive problem, recall-first metric strategy, reproducible repo structure, and agent-usage documentation approach |
| 2 | Update | `MSIN0097_Individual.ipynb`, `docs/workflow_evidence.md`, `appendix/agent_usage_log.md`, `appendix/decision_register.md` | Implemented churn-focused EDA additions and reproducible figure export (class imbalance with percentages, segment churn patterns, pitfalls notes, and saved plots under `artifacts/figures`) |
| 3 | Update | `MSIN0097_Individual.ipynb`, `docs/workflow_evidence.md`, `appendix/agent_usage_log.md`, `appendix/decision_register.md` | Implemented Step 3 leakage-safe preprocessing in notebook: modular cleaning/split functions, stratified train/validation/test split, train-only fitted `Pipeline` + `ColumnTransformer`, and saved fitted preprocessing object (`artifacts/preprocessing_pipeline.joblib`) |
| 4 | Update | `MSIN0097_Individual.ipynb`, `docs/workflow_evidence.md`, `appendix/agent_usage_log.md`, `appendix/decision_register.md` | Caught and corrected preprocessing mistake: duplicate removal order was too late; updated logic to deduplicate exact raw records before dropping ID fields and marked the earlier approach as rejected |
| 5 | Update | `MSIN0097_Individual.ipynb`, `docs/workflow_evidence.md`, `appendix/agent_usage_log.md`, `appendix/decision_register.md` | Implemented Section 4 model comparison via train-only cross-validation (Dummy, LogisticRegression, RandomForest, HistGradientBoosting), set recall as primary ranking metric, and exported results to `artifacts/model_comparison_section4_cv.csv` |
| 6 | Update | `MSIN0097_Individual.ipynb`, `docs/workflow_evidence.md`, `appendix/agent_usage_log.md`, `appendix/decision_register.md` | Corrected Section 4 metric strategy mistake: rejected recall-primary ranking and switched to PR-AUC-primary ranking (with recall/F1/ROC-AUC/log-loss as supporting metrics) for imbalanced churn targeting |
