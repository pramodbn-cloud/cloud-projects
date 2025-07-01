# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Security + Compliance lab.

This module depends on the learner already having working repositories and pipeline context, because security controls are most meaningful when attached to real workflow surfaces.

## Required account access
You should have working access to:
- Azure DevOps
- the organization used in earlier modules
- the project used for this learning repository
- Azure Pipelines
- Project Settings
- Azure Artifacts or service connection areas if applicable

## Required tools
The following should be available:

- a web browser for Azure DevOps access
- access to the CI/CD and package-management setup from earlier modules
- optional local note-taking for recording security decisions and rationale

No heavy local tooling is required for the basic conceptual DevSecOps lab, though Azure access may be needed if you create an Azure Resource Manager service connection.

## Required permissions
You should be able to:
- review project settings
- inspect or create service connections if your role allows it
- inspect or create variable groups if your role allows it
- view pipeline configuration
- review permission and security-related project areas

If working in a restricted environment, it is still acceptable to model the security design conceptually.

## Required prior modules
You should complete:
- Folder 01 — Azure DevOps Foundation Setup
- Folder 04 — CI Pipelines: Build + Test + Artifacts
- Folder 05 — CD Pipelines: Deployments + Approvals + Rollback
- Folder 06 — Azure Artifacts: Package Management Strategy

These earlier modules provide the workflow context that security is meant to protect.

## Required environment state
Before starting:
- at least one working pipeline should exist
- the learner should understand what service connections might be needed for
- the learner should understand that secrets and shared variables can appear in delivery workflows
- Project Settings and pipeline/library areas should be accessible

## Security scenario recommendation
Keep the lab practical and simple.

Recommended focus areas:
- review project-level permissions at a basic level
- create or inspect one service connection
- use one variable group with one secret and one non-secret variable
- discuss least privilege and safe secret patterns

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- variable group: `shared-dev-variables`
- variable group: `security-demo-config`
- service connection: `azure-dev-service-connection`
- secret label names that reveal purpose but not secret values

Keep names understandable so later modules can reference them clearly.

## Definition of ready
The learner is ready to start this lab when:
- project and pipeline access is working
- Project Settings is accessible
- a simple security scenario has been chosen
- the learner is ready to think about trust boundaries, not just functional workflow
- the learner understands that security controls should support delivery, not block it blindly
