# Architecture Flow

## Purpose of this file
This file explains the logical execution-model flow used in the AKS Virtual Nodes lab before implementation begins.

This module is about extending cluster execution — how the AKS control plane can continue to orchestrate pods while some pods run on ACI-backed virtual nodes instead of on standard VM-backed node pools.

## High-level architecture view
The workflow begins with a standard AKS cluster that normally places workloads on VM-backed nodes. Virtual nodes add a second execution model without changing the Kubernetes control-plane experience for the user.

At a high level, the flow looks like this:

- the AKS cluster already exists
- a virtual-node capability is added or enabled
- AKS exposes a virtual node representation inside the cluster
- selected workloads are targeted to that execution path
- those pods are actually run as ACI-backed container groups
- the cluster still manages them through standard Kubernetes constructs

This turns one AKS cluster into a hybrid execution environment.

## Component roles

- **AKS Control Plane** — continues to orchestrate workloads and scheduling intent  
- **Standard Node Pool** — the normal VM-backed execution path for most workloads  
- **Virtual Node** — the Kubernetes-visible representation of the ACI-backed execution path  
- **Azure Container Instances (ACI)** — the serverless infrastructure actually running those pods  
- **Workload / Pod Spec** — expresses placement intent and workload requirements  
- **VNet / Subnet Design** — provides the networking path required for ACI-backed workload communication  

## End-to-end flow

1. An AKS cluster exists with the correct networking model.  
2. Virtual-node capability is enabled or configured.  
3. AKS exposes the virtual node into the cluster view.  
4. A workload is targeted to the virtual node.  
5. The workload is executed on ACI-backed infrastructure.  
6. The learner compares this execution model with standard VM-node placement.  

## Dependency awareness
This module depends on:
- a working AKS cluster
- advanced networking compatibility
- basic understanding of deployments, scheduling, and namespaces

This module also prepares the learner for:
- secure image sourcing through ACR
- autoscaling trade-off discussions
- production-grade mixed execution design later

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- networking prerequisites
- workload fit
- execution trade-offs
- how scheduling intent maps to ACI-backed runtime
- when fast burst capacity is useful
- when standard node pools remain the better choice

These are the qualities that make virtual nodes useful in real architectures.

## What to keep in mind before implementation
Before starting the steps:
- virtual nodes are not “better nodes”; they are a different execution model
- ACI-backed pods still need correct networking and scheduling intent
- workload suitability matters
- the goal is fast, flexible execution where that trade-off is beneficial
- think in terms of platform capacity options, not feature novelty
