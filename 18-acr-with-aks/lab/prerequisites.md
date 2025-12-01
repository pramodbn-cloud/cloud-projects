# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the ACR with AKS lab.

This module depends on both Azure registry capability and AKS cluster readiness, so the prerequisites are registry- and identity-oriented.

## Required account access
You should have working access to:
- Azure
- Azure Container Registry
- an AKS cluster you can manage
- the ability to inspect AKS identity configuration and role assignments

## Required tools
The following should be available:

- Azure CLI
- kubectl
- Docker or another image build/push toolchain
- a terminal such as PowerShell or Bash
- a code editor for reviewing manifests

## Required permissions
You should be able to:
- create or inspect an ACR registry
- log in to ACR and push images
- inspect or configure AKS–ACR integration
- deploy workloads into AKS
- inspect pod startup and image pull behavior

## Required prior understanding
Before starting this module, the learner should already understand:
- deployments and pods
- namespaces
- AKS cluster execution basics
- that workloads need a trustworthy image source
- that Azure identities and role assignments influence runtime capabilities

## Required environment state
Before starting:
- an AKS cluster should already exist
- an ACR instance should either exist or be easy to create
- the learner should know whether the cluster is already attached to ACR
- a sample image should be available or easy to build

## Integration strategy recommendation
Keep the first scenario simple and deterministic.

Recommended approach:
- one ACR registry
- one AKS cluster
- one sample image
- one clear AKS integration path using attach-acr or confirmed equivalent role assignment

Microsoft documents `az aks create --attach-acr` and `az aks update --attach-acr` as the standard integration paths, which configure AcrPull for the managed identity.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- registry: `myplatformacr`
- image repository: `sample-app`
- tag: versioned and readable, not `latest` only for learning conclusions
- deployment: `acr-demo-app`

Azure’s ACR best-practices guidance also recommends disciplined tagging/versioning strategy.

## Definition of ready
The learner is ready to start this lab when:
- the AKS cluster is reachable
- the ACR registry is reachable
- an image can be built and pushed
- the learner is ready to think about private-registry trust and pull authorization
