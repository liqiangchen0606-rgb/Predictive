# Appendix A: Agent Usage Log

This appendix records meaningful agent interactions that materially affected the project.

## Logging Standard

For each entry include:
- date/time,
- task requested,
- key prompt/interaction summary,
- output produced by agent,
- your verification action,
- outcome and impact.

## Entries

### Entry 001

- Date: `2026-02-21`
- Task: Scaffold coursework repository for required artefacts (2, 3, 4)
- Interaction summary: Asked agent to create required folder structure and starter templates for reproducibility, workflow evidence, and appendix logs.
- Agent output: Created project directories and files including `requirements.txt`, `data/README.md`, `docs/workflow_evidence.md`, `appendix/decision_register.md`, `src/pipeline.py`, tests scaffold, and updated `README.md`.
- Verification performed: Manual review of file inventory and template coverage against coursework brief.
- Outcome: Accepted with minor future edits pending project-specific details.
- Impact: Established compliant structure and reduced setup overhead.

### Entry 002

- Date: `2026-02-21`
- Task: Create first executable churn modeling pipeline script
- Interaction summary: Asked agent to implement loading, cleaning, stratified split, preprocessing, baseline + multiple model training, evaluation, and artifact export.
- Agent output: Implemented end-to-end script in `src/pipeline.py`; updated `requirements.txt`; added smoke test in `tests/test_smoke.py`; updated dataset instructions in `data/README.md`.
- Verification performed: `py_compile` passed; inline data-cleaning smoke check passed; `pytest` command failed due to missing local package in current interpreter.
- Outcome: Accepted as interim reproducibility scaffold.
- Impact: Established executable baseline and artifact generation path.

### Entry 003

- Date: `2026-02-21`
- Task: Switch to notebook-first workflow and rebuild project notebook
- Interaction summary: User requested option 1 (notebook-first). Agent rebuilt `MSIN0097_Individual.ipynb` around staged ML workflow and included exact user-provided KaggleHub dataset import snippet.
- Agent output: Replaced minimal notebook with 21-cell workflow covering problem framing, EDA, prep, model comparison, evaluation, and artifact saving.
- Verification performed: Confirmed notebook JSON validity and section headers; confirmed KaggleHub download cell present.
- Outcome: Accepted; notebook designated as primary project implementation path.
- Impact: Aligns execution path with user preference and coursework narrative flow.

## Evidence Attachments

- Add screenshot/export references here as they become available.
- Example: `images/agent_log_2026-02-21_setup.png`
