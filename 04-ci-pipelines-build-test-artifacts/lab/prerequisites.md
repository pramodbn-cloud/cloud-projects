# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the CI Pipelines lab.

This module depends on both the repository workflow and the Azure DevOps project structure already being in place.

## Required account access
You should have working access to:
- Azure DevOps
- the organization created or confirmed earlier
- the project used for this learning repository
- Azure Repos inside that project
- Azure Pipelines inside that project

## Required tools
The following should be available:

- a web browser for Azure DevOps access
- the local repository from Folder 03
- Git on the local machine
- a code editor such as Visual Studio Code

Optional depending on the sample build flow:
- Node.js
- Python
- a lightweight sample project structure

The exact project type can remain simple as long as the CI logic is understandable.

## Required permissions
You should be able to:
- view and configure Azure Pipelines
- connect a pipeline to the repository
- run a pipeline
- view pipeline history and artifacts
- push repository changes if needed for trigger testing

If working in a controlled environment, confirm pipeline creation permissions before starting.

## Required prior modules
You should complete:
- Folder 01 — Azure DevOps Foundation Setup
- Folder 03 — Source Control Strategy

Folder 02 is also useful because it connects the work context to what is being automated here.

## Required environment state
Before starting:
- the repository should exist and be usable
- the local working copy should be available
- the main branch and at least one recent change should exist
- Azure Pipelines should be visible inside the project
- the learner should understand the purpose of branch-based change flow

## Build scenario recommendation
Keep the lab simple.

Recommended examples:
- build a small markdown-based repo validation flow
- build a simple Node.js starter app
- run a basic script or verification step
- package the repository content into an artifact

The goal is to understand CI structure, not application complexity.

## Naming convention to follow
Use clear naming for the pipeline.

Recommended examples:
- `ci-main-pipeline`
- `build-test-artifact-pipeline`
- `repo-validation-ci`

Keep the naming readable so later modules can reference the pipeline clearly.

## Definition of ready
The learner is ready to start this lab when:
- the repository is working
- Azure Pipelines is accessible
- pipeline creation permissions are available
- the learner understands that CI should validate repository changes automatically
- a simple build scenario has been chosen
