# Architecture Flow

## Purpose of this file
This file explains the logical CI/CD delivery flow used in the Azure DevOps with AKS lab before implementation begins.

This module is about platform delivery orchestration — how source code becomes a built image, how that image becomes a registry artifact, and how that artifact becomes a running workload in AKS through a controlled pipeline.

## High-level architecture view
The workflow begins with source code stored in a repository. Azure DevOps becomes the orchestrator of the next stages in the lifecycle.

At a high level, the flow looks like this:

- source code changes are committed to the repository
- Azure Pipelines builds the container image
- the image is pushed to ACR
- deployment manifests reference the image or are updated with the image tag
- Azure DevOps uses a service connection to reach AKS
- the Kubernetes manifest task deploys the workload into the cluster
- rollout status becomes visible through pipeline execution and cluster state

This creates one continuous path from source to runtime.

## Component roles

- **Repository / Source Code** — the starting point for the delivery lifecycle  
- **Azure Pipelines** — orchestrates build, push, and deployment stages  
- **Docker Build Step** — creates the container image  
- **Azure Container Registry (ACR)** — stores the built image  
- **Azure DevOps Service Connection** — provides trusted access to ACR and AKS-related resources  
- **Kubernetes Manifests** — define the target workload state  
- **AKS Cluster** — receives the new workload deployment  
- **KubernetesManifest Task** — applies manifests and tracks rollout behavior  

## End-to-end flow

1. A code change enters Azure DevOps source control.  
2. The pipeline starts and builds a container image.  
3. The image is pushed into ACR.  
4. The deployment stage references the image and deployment manifests.  
5. Azure DevOps connects to AKS through a trusted service connection.  
6. The manifests are deployed to the AKS cluster.  
7. The rollout is validated through pipeline and cluster feedback.  

## Dependency awareness
This module depends on:
- Azure DevOps foundation understanding from earlier folders
- Folder 18 for ACR and AKS integration
- a working AKS cluster
- a sample application and deployment manifests

This module also prepares the learner for:
- more advanced deployment strategies
- staged promotion models
- stronger release-governance and production-deployment patterns

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- image identity consistency
- trusted registry and cluster access
- manifest-driven deployment control
- rollout visibility
- service connection governance
- reducing manual deployment drift

These are the qualities that make pipeline delivery trustworthy in real environments.

## What to keep in mind before implementation
Before starting the steps:
- the build stage and deployment stage solve different parts of the lifecycle
- ACR is the handoff point between them
- AKS deployment should be driven from a clear image identity
- service connections are trust boundaries, not just convenience objects
- the goal is repeatable delivery, not only “pipeline success”
