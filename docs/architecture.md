# Architecture

## Overview

`model-foundry` is a modular ML lifecycle platform designed to support the full path from raw data to trained model to deployed inference and monitoring.

The architecture is intentionally phased:

- start as a single codebase with clear module boundaries
- later promote selected modules into independently deployable services
- eventually support containerization, CI/CD, and Kubernetes-native deployment patterns

## Architectural Principles

### 1. Incremental complexity
The system should begin as a local, modular Python project before introducing distributed runtime concerns.

### 2. Strong boundaries
Different responsibilities should be separated clearly even before they are split into services.

### 3. Reproducibility
Training, registry, and inference paths should preserve enough metadata and artifacts to support repeatability and auditability.

### 4. Production-minded design
Even early code should be structured in a way that can grow into:
- containerized services
- CI/CD pipelines
- Kubernetes workloads
- health and readiness patterns

### 5. Testability
Pure logic should remain testable in isolation, while workflow behavior should be validated with integration tests.

## High-Level Components

### Data
Responsible for:
- ingesting raw datasets
- validating schema and data quality
- preprocessing and normalization
- writing processed dataset artifacts

### Features
Responsible for:
- derived feature creation
- transformation logic shared by training and inference
- preserving consistency between train-time and inference-time feature generation

### Models
Responsible for:
- defining model interfaces
- implementing concrete model types
- encapsulating fit/predict/evaluate behavior

### Training
Responsible for:
- orchestrating training runs
- evaluating candidate models
- producing trained model artifacts and metrics

### Registry
Responsible for:
- storing model artifacts
- storing metadata
- versioning models
- selecting the current approved/latest model

### Inference
Responsible for:
- loading the current model
- performing predictions
- logging inference events
- later exposing inference through an API

### Monitoring
Responsible for:
- tracking prediction logs
- computing drift signals
- deciding when retraining should occur

### API
Responsible for:
- exposing external HTTP endpoints
- providing health/readiness endpoints
- eventually acting as the main long-running service

## Data Flow

### Training path
1. Raw data is ingested.
2. Data is cleaned and validated.
3. Processed data artifact is created.
4. Features are generated.
5. A model is trained and evaluated.
6. The resulting model artifact and metadata are stored in the registry.

### Inference path
1. A prediction request is received.
2. The current model version is loaded.
3. Input is transformed into feature form.
4. Prediction is produced.
5. Prediction and metadata are logged.

### Monitoring path
1. Prediction logs are analyzed.
2. Data drift or quality changes are detected.
3. Retraining may be triggered.

## Initial Deployment Shape

The first implementation is expected to remain a single local codebase.

Later runtime promotion may look like:

- Inference API service — long-running Deployment
- Training worker — Job or on-demand task
- Monitoring/drift worker — CronJob
- Ingestion/processing worker — API or batch job depending on source

## Storage Layers

The platform conceptually separates:

### Raw data store
Stores unprocessed inputs for traceability and replay.

### Processed data store
Stores cleaned datasets, likely in Parquet format.

### Model artifact store
Stores serialized models and model metadata.

### Logging/metrics store
Stores prediction logs and operational monitoring data.

## Why modular monorepo first

A modular monorepo is the right first shape because it:
- keeps the project understandable
- encourages shared contracts and testability
- avoids premature distributed complexity
- maps cleanly to future microservice boundaries

## Future Microservice Direction

Potential future service split:

- `inference-api`
- `training-worker`
- `monitoring-worker`
- `ingestion-service`

Not every component must become a long-running HTTP service. Some workloads are more naturally modeled as jobs.

## Kubernetes Mapping (future)

Long-running services:
- Deployments
- Services
- Ingress
- health/readiness probes

Batch or scheduled workloads:
- Jobs
- CronJobs

Configuration:
- ConfigMaps
- Secrets

Persistence:
- object storage and/or persistent volumes depending on use case

## Scope Boundary

This architecture is not trying to replicate large platforms such as MLflow or Kubeflow. Instead, it is a smaller, more understandable implementation of the core concerns those systems address.
