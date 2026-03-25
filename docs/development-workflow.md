# Development Workflow

## Overview

This repository uses a lightweight GitHub-style workflow designed for disciplined solo development that can scale cleanly to collaboration later.

The workflow is built around:
- short-lived topic branches
- Conventional Commits
- small, atomic commits
- Draft PRs for work in progress
- early use of tests and CI
- local validation with formatting, linting, type checking, and tests

The goal is to keep the repository easy to understand, easy to review, and safe to evolve incrementally.

---

## Branching Strategy

### Main branch
- `main` is the canonical branch.
- It should remain in a healthy, reviewable state.
- Work should not be developed directly on `main`.

### Topic branches
All work should be done in short-lived topic branches created from `main`.

Recommended branch prefixes:
- `feat/`
- `fix/`
- `docs/`
- `test/`
- `refactor/`
- `chore/`
- `ci/`

Examples:
- `feat/data-pipeline`
- `docs/initial-project-docs`
- `test/training-pipeline`
- `chore/repo-scaffold`
- `ci/github-actions`

### Branch scope
A branch should represent one coherent goal.

Good examples:
- scaffold repo docs
- add cleaning module
- add pytest configuration
- add inference API skeleton

Bad examples:
- add cleaning, training, API, Docker, and CI in one branch

If a branch starts to grow beyond one coherent purpose, split it before merging.

---

## Branch Lifecycle

Typical branch lifecycle:

1. Create a topic branch from `main`
2. Make small, focused commits
3. Push branch to GitHub
4. Open a Draft PR if work is not ready
5. Perform self-review on the PR diff
6. Mark the PR ready when the scope is coherent and validated
7. Merge into `main`
8. Delete the branch

---

## Commit Convention

This repository uses Conventional Commits.

Format:

`type(scope): short summary`

Examples:
- `feat(data): add dataset cleaning pipeline`
- `docs(architecture): add initial system design`
- `test(training): add trainer unit tests`
- `chore(repo): scaffold repository structure`
- `ci(github): add pytest workflow`

### Preferred commit types
- `feat`
- `fix`
- `docs`
- `test`
- `refactor`
- `chore`
- `ci`

### Scope guidance
Use a scope when it helps identify the subsystem affected.

Common scopes for this project may include:
- `repo`
- `data`
- `features`
- `models`
- `training`
- `registry`
- `inference`
- `monitoring`
- `api`
- `github`
- `architecture`

Examples:
- `feat(training): add trainer interface`
- `test(data): add missing-value normalization tests`
- `docs(repo): add local development instructions`

---

## Atomic Commit Rule

Commits should be small and focused.

A useful rule of thumb:

> If you cannot describe the commit without using the word “and,” the commit is probably too large.

Examples:

Good:
- `feat(data): add missing-value normalization`
- `test(data): add unit tests for timestamp parsing`

Too broad:
- `feat(data): add cleaning and feature engineering and tests`

When possible:
- separate refactors from features
- separate file moves from logic changes
- separate docs updates from implementation unless tightly coupled

---

## Pull Requests

Even for solo development, pull requests are encouraged.

They provide:
- a remote backup of branch state
- a self-review surface
- a clean merge boundary
- a more realistic engineering workflow for the project

### Draft PRs
Draft PRs should be used for:
- work in progress
- remote backup of unfinished branches
- self-review before merge

A Draft PR should be marked ready only when:
- the branch has a coherent scope
- local validation has been run
- the diff is reviewable
- obvious TODO-level breakage has been removed

### PR size guidance
A PR should be small enough to review without confusion.

If a PR contains several unrelated concerns, it should be split.

---

## Self-Review Expectations

Before marking a PR ready or merging a branch, review your own diff and ask:

- Is the branch doing one clear thing?
- Are there unrelated file changes?
- Do commit messages reflect the actual logical changes?
- Does the documentation need updating?
- Are tests present for stable logic and contracts?

Use `git diff`, GitHub PR diff view, and test output to validate the branch before merge.

---

## Merge Criteria

Before merging a branch:
- the scope is still focused
- documentation is updated if needed
- tests for the touched area pass
- unrelated changes are not bundled into the same branch
- the diff has been self-reviewed
- formatting, linting, type checking, and tests should all be green locally and in CI

### Merge style
For now, a normal merge or squash merge are both acceptable.

Preferred default:
- keep history clean
- avoid preserving noisy WIP commits if they reduce readability

If the branch contains a clean set of meaningful commits, preserving commit history is fine.
If the branch contains many noisy intermediate commits, squash merge is preferable.

---

## Local Development Expectations

Before committing or merging, prefer to:
- run the local validation sequence:
  - `ruff format .`
  - `ruff check .`
  - `mypy src tests`
  - `pytest`
- inspect diffs before committing
- keep commits coherent and reviewable
- avoid committing broken states unless intentionally isolated in WIP

---

## Documentation Expectations

Documentation should be updated when:
- architecture changes materially
- workflow expectations change
- milestone scope changes
- external behavior or developer workflow changes

At minimum, keep the following aligned with reality:
- `README.md`
- `docs/architecture.md`
- `docs/implementation-plan.md`
- `docs/milestones.md`

---

## TDD Guidance

Test-first development is encouraged where it improves clarity and confidence.

Recommended areas for test-first development:
- pure data transformations
- feature engineering
- registry logic
- drift calculations
- API behavior
- config validation

For exploratory work, it is acceptable to begin with a small implementation spike, but the result should be quickly followed by tests once the intended contract is clear.

### Practical rule
Use test-first for:
- deterministic logic
- contracts and interfaces
- bug fixes

Use exploratory-first, then test, for:
- framework wiring
- uncertain architecture spikes
- early integration discovery

---

## Scope Control

This project is intentionally incremental.

When in doubt:
- prefer smaller changes
- prefer fewer moving parts
- prefer clarity over premature completeness
- prefer understanding over premature optimization
