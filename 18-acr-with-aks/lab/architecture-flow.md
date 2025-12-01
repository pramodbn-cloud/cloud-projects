# Architecture Flow

## Purpose of this file
This file explains the logical image-supply flow used in the ACR with AKS lab before implementation begins.

This module is about trusted image sourcing — how container images are stored in a private registry, how AKS gains pull access to that registry, and how workloads use those images at runtime.

## High-level architecture view
The workflow begins with a container image that must be stored somewhere trustworthy. ACR becomes that trusted storage and distribution point, while AKS becomes the consumer of those images.

At a high level, the flow looks like this:

- an image is built locally or through a build process
- the image is pushed into Azure Container Registry
- AKS is integrated with ACR through identity-based access
- the workload manifest references the ACR image
- the cluster pulls the image from ACR at pod startup
- the pod runs using the private image successfully

This turns image sourcing into a governed platform path instead of a casual dependency on public registries.

## Component roles

- **Build Source / Developer / Pipeline** — produces the image  
- **Azure Container Registry (ACR)** — stores and serves the private image  
- **AKS Managed Identity / Kubelet Identity** — authenticates to the registry for image pulls  
- **AcrPull Role Assignment** — authorizes registry read access  
- **Deployment / Pod Spec** — references the private image path  
- **AKS Cluster** — pulls and runs the image as part of workload startup  

## End-to-end flow

1. An image is built.  
2. The image is pushed into ACR.  
3. AKS is granted permission to pull from that ACR.  
4. A workload references the ACR-hosted image.  
5. AKS pulls the image using its identity.  
6. The pod starts successfully using the private image.  

## Dependency awareness
This module depends on:
- a working AKS cluster
- Azure identity understanding
- readiness to deploy workloads from private images rather than only public sources

This module also prepares the learner for:
- Azure DevOps deployment pipelines into AKS
- image-version promotion strategy
- secure supply-chain reasoning in production cluster design

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- registry trust boundaries
- image naming and tagging discipline
- managed-identity-based pull flow
- minimum necessary registry access
- image-pull reliability at deployment time
- avoiding registry drift and image ambiguity

These are the qualities that make image supply reliable in real environments.

## What to keep in mind before implementation
Before starting the steps:
- ACR is not just storage; it is the trusted image source
- AKS pull success depends on both registry presence and registry authorization
- managed identity plus AcrPull is the normal integrated model
- image tags and version clarity matter for platform reliability
- think in terms of supply-chain trust, not just “push and pull”
