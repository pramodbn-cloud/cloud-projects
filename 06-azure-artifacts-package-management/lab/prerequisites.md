# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Azure Artifacts lab.

This module depends on the Azure DevOps project being ready and on the learner having a basic understanding of build outputs from earlier modules.

## Required account access
You should have working access to:
- Azure DevOps
- the organization used in earlier modules
- the project used for this learning repository
- Azure Artifacts inside that project

## Required tools
The following should be available:

- a web browser for Azure DevOps access
- the repository and project structure from earlier modules
- optional local tooling depending on the package type you choose

Possible package-specific tools may include:
- NuGet or dotnet tooling for NuGet packages
- npm for npm packages
- Python packaging tooling for Python packages
- Azure CLI or Azure DevOps tooling if using Universal Packages in a simplified scenario

For this learning module, the package scenario can remain lightweight.

## Required permissions
You should be able to:
- create or access an Azure Artifacts feed
- view feed settings
- publish a package to the feed
- connect a consumer to the feed
- review feed visibility and upstream source settings

If working in a controlled environment, verify feed creation and publish permissions before starting.

## Required prior modules
You should complete:
- Folder 01 — Azure DevOps Foundation Setup
- Folder 04 — CI Pipelines: Build + Test + Artifacts
- Folder 05 — CD Pipelines: Deployments + Approvals + Rollback

These earlier modules help the learner understand why reusable outputs matter beyond a single run.

## Required environment state
Before starting:
- Azure Artifacts should be visible in the project
- the learner should understand the difference between repository content and build outputs
- the learner should be ready to think in terms of reusable, versioned components
- a simple package scenario should be chosen

## Package scenario recommendation
Keep the lab simple.

Recommended options:
- a basic npm package scenario
- a simple NuGet package scenario
- a lightweight internal reusable component example
- a Universal Package style reusable bundle scenario

Azure Artifacts supports feeds for multiple package types, including NuGet, npm, Maven, Python, Cargo, and Universal Packages.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- feed name: `ado-shared-packages`
- feed name: `job-ready-shared-feed`
- package name: aligned to the chosen sample scenario
- version format: simple semantic-style numbering

Keep names readable so later modules can reference them clearly.

## Definition of ready
The learner is ready to start this lab when:
- Azure Artifacts is accessible
- feed creation permissions are available
- a simple package scenario has been selected
- the learner understands that package management is about reusable, versioned components
- the learner is ready to distinguish one-time artifacts from reusable packages
