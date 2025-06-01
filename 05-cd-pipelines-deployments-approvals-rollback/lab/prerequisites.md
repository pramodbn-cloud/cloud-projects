# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the CD Pipelines lab.

This module depends heavily on the CI output from the previous module and on a stable Azure DevOps project setup.

## Required account access
You should have working access to:
- Azure DevOps
- the organization used in earlier modules
- the project used for this learning repository
- Azure Pipelines
- environment or deployment-related configuration areas if available in your project

## Required tools
The following should be available:

- a web browser for Azure DevOps access
- access to the CI pipeline created in Folder 04
- the repository and local working structure from earlier modules
- optional note-taking for recording stage logic and approval flow

No advanced local CLI tooling is required for the basic conceptual CD lab.

## Required permissions
You should be able to:
- view and configure pipelines
- reference artifacts from earlier runs
- define or review environments or deployment stages
- create or simulate approval logic if supported in your setup
- rerun or inspect previous CI artifacts

If your environment is restricted, you should still be able to model the stage and approval thinking conceptually.

## Required prior modules
You should complete:
- Folder 01 — Azure DevOps Foundation Setup
- Folder 03 — Source Control Strategy
- Folder 04 — CI Pipelines: Build + Test + Artifacts

Folder 04 is especially important because this module depends on the artifact produced there.

## Required environment state
Before starting:
- at least one successful CI pipeline run should exist
- the artifact from that run should be visible
- the learner should understand the difference between repository change and artifact output
- Azure Pipelines should be accessible
- the learner should be ready to think in stages and environments

## Deployment scenario recommendation
Keep the lab simple.

Recommended examples:
- deploy artifact to a sample development environment
- simulate promotion from Dev to Test
- use logical stages even if the deployment target is simplified
- treat the lab as a release workflow exercise rather than full infrastructure deployment

The goal is to understand CD structure, not production complexity yet.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- pipeline name: `cd-release-pipeline`
- stage name: `Deploy_Dev`
- stage name: `Deploy_Test`
- approval label: `Pre-Deployment Approval`

Keep stage names and purpose obvious for later modules.

## Definition of ready
The learner is ready to start this lab when:
- a CI artifact exists and is accessible
- Azure Pipelines is working
- the learner understands the concept of promotion between stages
- a simple deployment scenario has been chosen
- the learner is ready to think about safe delivery rather than only successful automation
