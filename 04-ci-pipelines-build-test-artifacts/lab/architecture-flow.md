# Architecture Flow

## Purpose of this file
This file explains the logical CI workflow used in the CI Pipelines lab before implementation begins.

This module is about automation flow architecture — how a repository change becomes an automated pipeline run, how that run performs validation, and how the system produces a reusable output.

## High-level architecture view
The workflow begins with a code change in the repository. That change becomes the trigger for the CI system.

At a high level, the flow looks like this:

- a change is pushed into the repository
- Azure Pipelines detects the change
- the pipeline starts automatically or is run manually for testing
- build steps prepare or validate the project
- test or verification steps confirm basic health
- an artifact is produced and stored
- the pipeline result becomes visible to the team

This module helps the learner understand that CI is the first automated quality checkpoint in the delivery lifecycle.

## Component roles

- **Learner / Engineer** — creates and updates the repository and pipeline configuration  
- **Azure Repos** — stores the code and acts as the trigger source  
- **Azure Pipelines** — runs the CI workflow automatically or manually  
- **Build Step** — validates that the project can be prepared or compiled successfully  
- **Test / Verification Step** — checks that a basic quality condition is satisfied  
- **Artifact Output** — the reusable package or output produced by the pipeline  
- **Pipeline Run History** — the visible record of automation results over time  

## End-to-end flow

1. A code change is committed and pushed to the repository.  
2. Azure Pipelines detects the relevant branch or manual run request.  
3. The pipeline starts and executes the defined build steps.  
4. A test or validation step runs as part of the workflow.  
5. The pipeline produces an artifact if the workflow succeeds.  
6. The learner reviews the run result and artifact visibility.  

## Dependency awareness
This module depends on:
- Folder 01 for Azure DevOps project readiness
- Folder 03 for repository workflow readiness

This module also prepares for:
- Folder 05, where the artifacts created here become inputs to controlled deployment workflows

## Operational view
From an engineering workflow perspective, the learner should pay attention to:
- pipeline trigger logic
- clean and readable pipeline structure
- fast feedback
- visible failure signals
- artifact usefulness
- repeatability of execution

These are the qualities that make CI trustworthy and scalable.

## What to keep in mind before implementation
Before starting the steps:
- keep the pipeline simple in this module
- focus on understanding the flow, not tool complexity
- think of CI as an automated reviewer of basic code health
- treat artifacts as outputs that downstream stages can use
- aim for explainable automation, not only successful execution
