# Appendix B: Decision Register (Agent Contributions)

Use this table to record key agent suggestions and your adjudication.

| ID | Date | Project stage | Agent contribution | Risk if wrong | Verification done | Decision (accepted/modified/rejected) | Rationale | Evidence link |
|---|---|---|---|---|---|---|---|---|
| DR-001 | 2026-02-21 | Setup | Proposed complete repository scaffold for artefacts 2, 3, 4 | Medium (missing required items) | Compared scaffold against coursework requirements and required artefacts | Accepted | Structure directly maps to brief and improves traceability | `docs/project_checklist.md`, `README.md` |
| DR-002 | 2026-02-21 | Implementation | Implemented reusable churn pipeline script in `src/pipeline.py` | Medium (incorrect assumptions before dataset run) | Static compile and inline cleaning check passed; pending full run with downloaded dataset | Modified | Keep as reproducibility backup; notebook-first chosen as primary execution path | `src/pipeline.py`, `tests/test_smoke.py` |
| DR-003 | 2026-02-21 | Implementation | Rebuilt `MSIN0097_Individual.ipynb` with notebook-first end-to-end structure including user KaggleHub code | Medium (workflow mismatch with user expectations) | Verified notebook structure, section coverage, and Kaggle import presence | Accepted | Matches user-requested workflow and coursework process narrative | `MSIN0097_Individual.ipynb`, `docs/workflow_evidence.md` |

## Notes

- Keep entries concise and specific.
- Add one row for each meaningful contribution.
- Explicitly include at least one caught mistake and correction later in project.
