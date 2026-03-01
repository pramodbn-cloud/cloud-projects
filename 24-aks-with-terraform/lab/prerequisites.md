# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the AKS with Terraform lab.

This module depends on Azure provisioning access and Terraform readiness, so the prerequisites are subscription-, tooling-, and IaC-oriented.

## Required account access
You should have working access to:
- Azure
- an Azure subscription suitable for AKS creation
- the ability to create resource groups, networking resources, and AKS clusters

## Required tools
The following should be available:

- Terraform
- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for Terraform files

## Required permissions
You should be able to:
- authenticate to Azure
- create and manage AKS-related Azure resources
- inspect created resources in Azure
- retrieve cluster credentials after provisioning

## Required prior understanding
Before starting this module, the learner should already understand:
- AKS architecture at a practical level
- node pools, networking, namespaces, ingress, and delivery concepts from earlier folders
- that infrastructure provisioning and workload deployment are separate lifecycle concerns

## Required environment state
Before starting:
- Terraform should already be installed
- Azure CLI authentication should already work
- the learner should understand whether state will be local for the lab or structured for later remote-state usage
- the learner should be ready to provision a new AKS cluster or model one clearly

## Terraform strategy recommendation
Keep the first scenario simple and deterministic.

Recommended approach:
- one resource group
- one AKS cluster
- one clear node-pool definition
- minimal but readable variable usage
- optional supporting resources only when they improve understanding

This keeps the IaC story clear and prepares naturally for the pipeline-driven module that follows.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- resource group names aligned to environment
- cluster names aligned to environment and purpose
- file names that clearly reflect provider, variables, outputs, and AKS resources

Keep names readable so Folder 25 can build on them naturally.

## Definition of ready
The learner is ready to start this lab when:
- Terraform is installed and usable
- Azure authentication is working
- an AKS-capable subscription is available
- the learner is ready to think in terms of infrastructure state and reproducibility
