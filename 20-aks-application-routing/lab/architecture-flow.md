# Architecture Flow

## Purpose of this file
This file explains the logical managed-routing flow used in the AKS Application Routing lab before implementation begins.

This module is about AKS-managed ingress behavior — how AKS provides and integrates a managed NGINX ingress-controller path so that the cluster operator owns less of the ingress-control-plane lifecycle directly.

## High-level architecture view
The workflow begins with an AKS cluster that needs ingress traffic management. In a self-managed pattern, the team installs and owns the ingress controller more explicitly. In the managed-routing pattern, AKS provides the add-on and integrates it more tightly with Azure-managed behaviors.

At a high level, the flow looks like this:

- the AKS cluster exists with managed identity
- the Application Routing add-on is enabled
- AKS provisions the managed ingress-controller system
- ingress resources are handled through that managed routing layer
- Azure DNS integration can be used through the add-on model
- workloads are exposed through the managed ingress path

This turns ingress-controller ownership from a more manual platform concern into a more managed AKS concern.

## Component roles

- **AKS Cluster** — the base platform environment  
- **Application Routing Add-on** — the AKS-managed ingress-controller capability  
- **Managed NGINX Ingress Layer** — the managed traffic-entry implementation  
- **Ingress Resource** — the Kubernetes object expressing routing intent  
- **Azure DNS Integration** — the Azure-native DNS support path for this add-on  
- **Backend Services and Pods** — the workloads receiving routed traffic  

## End-to-end flow

1. An AKS cluster exists and meets the add-on prerequisites.  
2. The Application Routing add-on is enabled.  
3. AKS deploys and manages the ingress-controller system.  
4. The learner applies or reviews ingress resources using that system.  
5. The managed routing layer exposes traffic to backend services.  
6. Azure DNS integration can support public/private naming as part of the managed pattern.  

## Dependency awareness
This module depends on:
- a working AKS cluster
- prior ingress understanding from earlier folders
- awareness of DNS integration concepts from earlier DNS-related folders

This module also prepares the learner for:
- stronger AKS operational design decisions
- choosing between managed and self-managed platform components
- later cluster access governance topics

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- managed versus self-managed responsibility split
- Azure integration boundaries
- add-on constraints and prerequisites
- what can and cannot be customized safely
- how this pattern fits into cluster operations

These are the qualities that make managed routing a real platform decision rather than only a feature choice.

## What to keep in mind before implementation
Before starting the steps:
- this module does not replace ingress fundamentals; it builds on them
- managed routing changes operational ownership more than routing concepts
- Azure DNS integration is part of the value proposition
- managed identity is a prerequisite
- the goal is to understand platform trade-offs, not only enable the feature
