# MSIN0097 Predictive Analytics Individual Coursework

This repository contains deliverables for:
- Coursework artefact 2: code repository and reproducibility assets
- Coursework artefact 3: workflow evidence using an agentic methodology
- Coursework artefact 4: appendix evidence (agent usage log + decision register)

## Project Status

- Module: `MSIN0097 Predictive Analytics`
- Assessment type: `Individual coursework`
- Repository initialized: `2026-02-21`
- Current implementation: scaffold and templates ready

## Repository Structure

```text
.
├── README.md
├── CHANGELOG_SESSION.md
├── requirements.txt
├── MSIN0097_Individual.ipynb
├── src/
│   ├── __init__.py
│   └── pipeline.py
├── data/
│   └── README.md
├── docs/
│   ├── workflow_evidence.md
│   └── project_checklist.md
├── appendix/
│   ├── agent_usage_log.md
│   └── decision_register.md
├── artifacts/
│   └── README.md
└── tests/
    ├── README.md
    └── test_smoke.py
```

## Setup

1. Create and activate environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Run

Current scaffold command (placeholder):
```bash
python -m src.pipeline
```

## Reproducibility Requirements (to keep updated)

- Pin package versions in `requirements.txt`
- Keep data access and licensing notes in `data/README.md`
- Save metrics and plots to `artifacts/`
- Document every significant agent-assisted change in:
  - `docs/workflow_evidence.md`
  - `appendix/agent_usage_log.md`
  - `appendix/decision_register.md`
  - `CHANGELOG_SESSION.md`

## Submission Checklist (quick links)

- Repo instructions complete: `README.md`
- Environment spec complete: `requirements.txt`
- Data access documented: `data/README.md`
- Workflow evidence complete: `docs/workflow_evidence.md`
- Agent usage appendix complete: `appendix/agent_usage_log.md`
- Decision register complete: `appendix/decision_register.md`
