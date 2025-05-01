# Lab Guide — CI Pipelines: Build + Test + Artifacts

## Lab objective
The objective of this lab is to help the learner create a basic but professional CI workflow in Azure DevOps that validates repository changes automatically.

This lab focuses on connecting a repository to a pipeline, defining a simple build flow, introducing a test stage or verification step, and producing an artifact that can later be used in deployment workflows.

## What you will build or configure
In this lab, you will create a CI pipeline connected to the repository created in the previous module. You will configure it to respond to repository changes, run a build process, include a test or validation step, and publish an artifact.

This creates the first full automation layer in the repository journey.

## Why this lab matters
Source control tells the team what changed. CI tells the team whether that change is still healthy enough to move forward.

This lab matters because it teaches the learner that good delivery systems do not rely only on developer confidence. They rely on repeatable automated validation that gives fast, visible feedback on every change.

## Estimated time
45 to 60 minutes

## Lab file reading order
Follow the files in this order:

1. `architecture-flow.md`
2. `prerequisites.md`
3. `implementation-steps.md`
4. `validation-checks.md`
5. `troubleshooting.md`
6. `cleanup.md`

## Expected final outcome
By the end of this lab, the learner should have:
- a working CI pipeline in Azure DevOps
- repository-triggered pipeline execution
- a visible build and validation flow
- a published artifact from the pipeline run
- confidence in explaining how CI supports delivery quality

## Skills gained
- Connecting Azure Repos to Azure Pipelines
- Defining a simple CI workflow with structured stages
- Understanding the role of build and test steps
- Publishing artifacts for downstream use

## Real-world relevance
In real engineering teams, CI is one of the most important confidence mechanisms in the delivery lifecycle. It reduces integration risk, shortens feedback loops, and creates a predictable standard for how code is accepted into the system.

This lab reflects that same real-world automation pattern.

## Completion standard
A learner should not mark this lab complete until:
- the pipeline is connected to the repository
- a build process runs successfully
- a test or validation step is included and understood
- an artifact is published and visible
- validation confirms the full workflow works correctly
