# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Terraform + Azure DevOps for AKS lab.

This module depends on Terraform readiness, Azure DevOps readiness, and AKS provisioning design maturity, so the prerequisites are broad and capstone-oriented.

## Required account access
You should have working access to:
- Azure DevOps
- Azure
- Terraform-capable Azure permissions
- the ability to create or review Azure service connections
- the repository containing the Terraform configuration

## Required tools
The following should be available:

- Azure DevOps project access
- Terraform code from Folder 24
- Azure CLI
- a code editor for pipeline YAML and Terraform files
- access to the chosen Terraform state strategy

## Required permissions
You should be able to:
- create or edit Azure Pipelines
- create or inspect service connections
- run Terraform against Azure through the pipeline trust path
- inspect pipeline runs and resulting Azure resources

## Required prior understanding
Before starting this module, the learner should already understand:
- Azure DevOps foundations from earlier folders
- AKS provisioning with Terraform from Folder 24
- that Terraform state and execution context matter
- that infrastructure delivery needs review and governance too

## Required environment state
Before starting:
- the Terraform configuration for AKS should already exist
- Azure DevOps should already have repository access
- the service connection model should be ready or easy to create
- the learner should know how state is being handled for the lab

## Pipeline strategy recommendation
Keep the first scenario simple and deterministic.

Recommended approach:
- one pipeline
- one Terraform init step
- one validation/plan step
- one controlled apply step
- one AKS target environment

This keeps the capstone flow clear and avoids unnecessary pipeline sprawl.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- pipeline: `terraform-aks-provision`
- service connection names that clearly indicate Azure access purpose
- stage names that distinguish plan from apply cleanly

Keep names readable because this module should feel like a real team-owned infrastructure-delivery system.

## Definition of ready
The learner is ready to start this lab when:
- Terraform AKS code already exists
- Azure DevOps access is ready
- service connection design is ready
- the learner is ready to think in terms of governed infrastructure pipelines, not only local Terraform commands
