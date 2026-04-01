# Architecture Flow

## Purpose of this file
This file explains the logical infrastructure-delivery flow used in the Terraform + Azure DevOps for AKS lab before implementation begins.

This module is about pipeline-driven infrastructure — how Terraform configuration becomes a reviewed and repeatable AKS provisioning lifecycle under Azure DevOps.

## High-level architecture view
The workflow begins with Terraform code stored in source control. Azure DevOps becomes the orchestrator of the Terraform lifecycle.

At a high level, the flow looks like this:

- Terraform code is stored in the repository
- Azure DevOps triggers a pipeline from that code
- the pipeline runs Terraform init
- the pipeline runs validation and/or plan
- the pipeline runs apply in a controlled stage
- Azure resources, including AKS, are created or updated
- the resulting infrastructure becomes pipeline-governed instead of locally governed

This turns infrastructure from a local operator action into a delivery workflow.

## Component roles

- **Repository** — stores Terraform code and pipeline definitions  
- **Azure DevOps Pipeline** — orchestrates Terraform execution  
- **Terraform Init / Plan / Apply Stages** — the infrastructure lifecycle steps  
- **Azure Service Connection** — the trust bridge for Azure resource access  
- **Terraform State Strategy** — the persistence layer for infrastructure lifecycle continuity  
- **AKS Infrastructure** — the Azure platform resources being created or changed  

## End-to-end flow

1. Terraform AKS code is committed to the repository.  
2. Azure DevOps triggers the infrastructure pipeline.  
3. The pipeline initializes Terraform.  
4. The pipeline validates or plans the desired infrastructure changes.  
5. A controlled apply stage provisions or updates AKS resources.  
6. Infrastructure change becomes repeatable, reviewable, and visible.  

## Dependency awareness
This module depends on:
- Folder 24 for Terraform AKS understanding
- earlier Azure DevOps foundation understanding
- Azure access and service connection readiness

This module completes the course and prepares the learner for:
- real-world platform team workflows
- multi-environment infrastructure promotion patterns
- stronger review, approval, and governance on infrastructure change

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- Terraform lifecycle separation
- service connection trust
- plan visibility
- controlled apply behavior
- state continuity
- infrastructure reviewability

These are the qualities that make infrastructure pipelines useful in real environments.

## What to keep in mind before implementation
Before starting the steps:
- application deployment pipelines and infrastructure pipelines solve related but different problems
- plan and apply should not be mentally merged
- state strategy matters even more once Terraform runs in pipelines
- the goal is governed infrastructure delivery, not only remote command execution
