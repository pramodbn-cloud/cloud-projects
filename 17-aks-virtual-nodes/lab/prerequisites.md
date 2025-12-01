# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the AKS Virtual Nodes lab.

This module is highly dependent on cluster networking and execution-model prerequisites, so readiness matters more here than in many earlier modules.

## Required account access
You should have working access to:
- Azure
- an AKS cluster you can manage
- Azure networking resources related to that cluster
- kubectl access to the cluster
- the ability to enable or review virtual-node configuration

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for reviewing or applying manifests
- optional Helm if your chosen virtual-node deployment flow uses Helm

## Required permissions
You should be able to:
- inspect AKS cluster configuration
- inspect or create subnets as needed
- enable or review virtual-node configuration
- deploy workloads and inspect node placement

## Required prior understanding
Before starting this module, the learner should already understand:
- deployments and pods
- namespaces from Folder 16
- that standard AKS node pools are VM-backed
- that the platform can expose applications and organize workloads, but execution models can still vary

## Required environment state
Before starting:
- an AKS cluster should already exist
- the cluster should be compatible with the networking requirement for virtual nodes
- the learner should understand whether the cluster uses advanced networking / Azure CNI

Microsoft explicitly documents that virtual nodes require AKS clusters created with advanced networking (Azure CNI). StackSimplify’s AKS virtual nodes guide makes the same point.

## Workload scenario recommendation
Keep the lab simple and deterministic.

Recommended approach:
- use one lightweight sample workload
- target it to the virtual-node execution path
- compare it conceptually or operationally with a standard-node deployment

This keeps the execution-model lesson clear.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- namespace: `virtual-node-demo`
- deployment: `aci-demo-app`
- workload labels that make node-placement inspection easy

Keep names readable so later execution and scaling modules can extend them naturally.

## Definition of ready
The learner is ready to start this lab when:
- the AKS cluster is reachable
- networking compatibility is understood
- the virtual-node approach for the lab is chosen
- a lightweight workload is ready
- the learner is ready to think about execution backends, not only workloads themselves
