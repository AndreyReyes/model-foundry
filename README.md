# model-foundry

A modular, production-minded ML lifecycle platform built incrementally to support training, registration, deployment, inference, monitoring, drift detection, and retraining across different model types.

## Purpose

`model-foundry` is a reference project for learning and demonstrating the core concepts behind modern ML platforms and MLOps systems.

The goal is not to compete with large existing tools, but to build a smaller system that is fully understood and engineered with clean structure, testing, packaging, CI/CD, and Kubernetes readiness in mind.

## Project Goals

- Support a general pipeline for training and deploying different ML models.
- Build incrementally, starting with a modular monorepo before evolving toward microservices.
- Follow production-minded engineering practices:
  - clear architecture
  - testability
  - packaging
  - CI/CD
  - containerization
  - Kubernetes deployment
- Keep the implementation understandable enough to explain in interviews and technical discussions.

## Initial Scope

The initial version of `model-foundry` will support:

- dataset ingestion from files
- data validation and preprocessing
- feature engineering
- model training and evaluation
- local model registry
- inference
- prediction logging
- drift detection
- retraining trigger

## High-Level Architecture

The project starts as a **modular monorepo** with clearly separated domains:

- `data` — ingestion, validation, preprocessing
- `features` — feature engineering
- `models` — model abstractions and concrete model implementations
- `training` — training and evaluation workflows
- `registry` — model artifact and metadata management
- `inference` — model loading and prediction logic
- `monitoring` — drift checks and retraining triggers
- `api` — external inference API and health endpoints

Over time, selected modules may be promoted into independently deployable services.

## Development Philosophy

This project is intentionally being built in layers:

1. **Docs and architecture first**
2. **Package and test scaffold**
3. **GitHub CI**
4. **Core modular implementation**
5. **FastAPI service layer**
6. **Docker packaging**
7. **Monitoring and retraining loop**
8. **Kubernetes deployment**

The goal is to understand each concept before adding the next one.

## Repository Layout

```text
model-foundry/
  .github/
    workflows/
  README.md
  .gitignore
  pyproject.toml
  docs/
    adr/
    architecture.md
    implementation-plan.md
    milestones.md
    development-workflow.md
  src/
    model_foundry/
      __init__.py
  tests/
    unit/
    integration/
    contract/
  scripts/
  data/
    sample/
```

## Planned Milestones

- Repository scaffold and documentation
- Package and test scaffold
- GitHub CI
- Core data pipeline
- Generalized training pipeline
- Inference API
- Containerization
- Monitoring and drift detection
- Kubernetes basics

See `docs/milestones.md` for more detail.

## Development Workflow

This repository uses:

- short-lived topic branches
- Conventional Commits
- small, atomic commits
- Draft PRs for work in progress when using GitHub

See `docs/development-workflow.md` for details.

## Status

Current status:
- repository scaffold complete
- initial documentation in progress
- implementation not yet started in the new codebase

## Future Direction

Longer-term goals include:
- multiple model backends
- API and worker separation
- Dockerized services
- Kubernetes Deployments and Jobs/CronJobs
- production-style CI/CD pipeline
