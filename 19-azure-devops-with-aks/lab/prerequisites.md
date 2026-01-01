# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Azure DevOps with AKS lab.

This module depends on both Azure DevOps pipeline readiness and AKS runtime readiness, so the prerequisites span source control, registry, cluster, and access configuration.

## Required account access
You should have working access to:
- Azure DevOps
- Azure
- Azure Container Registry
- an AKS cluster you can manage
- the ability to create or review service connections in Azure DevOps

## Required tools
The following should be available:

- Azure DevOps project access
- Azure CLI
- kubectl
- Docker or equivalent build tooling
- a code editor for application source and manifests
- pipeline YAML or classic pipeline editing access

## Required permissions
You should be able to:
- create or edit Azure Pipelines
- create or inspect service connections
- push images to ACR
- deploy workloads to AKS
- inspect pipeline runs and deployment outcomes

## Required prior understanding
Before starting this module, the learner should already understand:
- Azure DevOps pipeline basics from earlier foundation modules
- ACR with AKS from Folder 18
- deployments and manifests in Kubernetes
- that image build, registry push, and cluster rollout are separate but connected concerns

## Required environment state
Before starting:
- an AKS cluster should already exist
- ACR should already exist and be usable
- the AKS-to-ACR trust path should already work
- a sample application and manifest set should already exist or be easy to create
- Azure DevOps should have access to the repository holding the app and manifests

## Pipeline strategy recommendation
Keep the first scenario simple and deterministic.

Recommended approach:
- one build stage
- one push-to-ACR step
- one deployment stage
- one AKS target namespace or workload

This keeps the first end-to-end flow easy to understand and troubleshoot.

## Service-connection note
The deployment flow usually depends on:
- an Azure Resource Manager or similar service connection for Azure-related tasks
- and/or a Kubernetes-targeted deployment connection pattern depending on the chosen Azure DevOps setup

Microsoft’s AKS pipeline guidance and Kubernetes resource documentation in Azure Pipelines describe deployment through Kubernetes resources/environments and the `KubernetesManifest` task.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- pipeline: `aks-build-and-deploy`
- registry repository: `sample-app`
- deployment namespace: clear and intentional
- service connection names that reflect ACR and AKS purpose separately

Keep names readable so later rollout and scaling modules can extend them naturally.

## Definition of ready
The learner is ready to start this lab when:
- Azure DevOps can access the source repository
- ACR is available
- AKS is available
- service connections are available or can be created
- the learner is ready to think in full build-to-runtime lifecycle terms
