# Milestones

## Milestone 0 — Repository Foundation

### Deliverables
- repository scaffold
- `pyproject.toml`
- initial docs
- package root
- tests directory layout
- `.gitignore`

### Acceptance Criteria
- repository structure exists
- docs are present and coherent
- project can serve as a clean starting point for implementation

---

## Milestone 1 — Package and Test Scaffold

### Deliverables
- package subdirectories under `src/model_foundry`
- pytest scaffold
- initial placeholder tests
- sample dataset under `data/sample`

### Acceptance Criteria
- the package layout exists
- tests can be discovered and executed
- the repository is ready for feature implementation under a consistent test workflow

---

## Milestone 2 — GitHub CI

### Deliverables
- test workflow
- lint workflow or combined CI workflow

### Acceptance Criteria
- CI runs automatically on push or PR
- repository can fail fast on broken tests or invalid formatting/lint issues

---

## Milestone 3 — Data Pipeline

### Deliverables
- ingestion logic
- data cleaning/validation logic
- processed dataset artifact
- feature engineering module
- unit tests for data transformations

### Acceptance Criteria
- sample raw data can be ingested
- processed output is reproducible
- feature generation is testable and deterministic for sample inputs

---

## Milestone 4 — General Training Pipeline

### Deliverables
- model abstraction
- at least two model implementations
- training workflow
- evaluation logic
- local registry storing artifacts and metadata
- integration tests for train/register flow

### Acceptance Criteria
- a training run produces a model artifact and metadata
- at least two model backends can be trained through the same interface
- latest/current model can be identified from the registry

---

## Milestone 5 — Inference API

### Deliverables
- inference module
- prediction logging
- FastAPI app
- health endpoints
- API tests

### Acceptance Criteria
- a request can be sent to the inference API
- the current model is loaded correctly
- predictions are logged with model version metadata
- liveness/readiness endpoints exist

---

## Milestone 6 — Containerization

### Deliverables
- Docker packaging for selected runtime components
- reproducible local run path

### Acceptance Criteria
- core service(s) can run in Docker
- build and run steps are documented

---

## Milestone 7 — Monitoring and Retraining

### Deliverables
- drift check
- retraining trigger
- tests for monitoring logic

### Acceptance Criteria
- prediction logs can be analyzed
- drift logic produces expected output for test scenarios
- retraining can be triggered from drift conditions

---

## Milestone 8 — Kubernetes Basics

### Deliverables
- local Kubernetes deployment manifests
- Deployment/Service for API
- Job or CronJob for a background workload
- config examples
- health probe wiring

### Acceptance Criteria
- at least one long-running service runs in Kubernetes
- at least one batch/scheduled workload runs in Kubernetes
- readiness/liveness behavior is testable and understandable

## Notes

Milestones should remain small enough to be understood and explained clearly. If a milestone becomes too broad, it should be split before implementation continues.
