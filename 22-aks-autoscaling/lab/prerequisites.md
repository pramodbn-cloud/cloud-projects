# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the AKS Autoscaling lab.

This module depends on both workload configuration quality and cluster node-pool readiness, so the prerequisites are runtime- and scaling-oriented.

## Required account access
You should have working access to:
- Azure
- an AKS cluster you can manage
- the node pools in that AKS cluster
- kubectl access to the cluster

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for workload and HPA manifests
- metrics visibility in the cluster for HPA-based reasoning
- optional load-generation tooling for a simple scaling demonstration

## Required permissions
You should be able to:
- inspect and modify deployments
- create or update an HPA
- inspect or enable Cluster Autoscaler on the cluster or node pool
- inspect pods, events, and node-pool status

## Required prior understanding
Before starting this module, the learner should already understand:
- requests and limits from Folder 15
- namespaces from Folder 16
- that scheduling depends on resource requests
- that runtime demand can be different from static deployment assumptions

## Required environment state
Before starting:
- an AKS cluster should already exist
- at least one sample workload should already exist or be easy to deploy
- the node pool should have clear min/max scaling boundaries available or configurable
- the cluster should expose the metrics needed for HPA to function in the chosen scenario

## Autoscaling strategy recommendation
Keep the first scenario simple and deterministic.

Recommended approach:
- one deployment
- one HPA targeting CPU or another simple supported metric
- one node pool with Cluster Autoscaler min/max boundaries
- one clear scale-up story

This keeps the autoscaling chain easy to observe and explain.

## Node-pool note
AKS documents Cluster Autoscaler enablement at cluster or node-pool scope, and node pools can have their own min/max settings. AKS also documents autoscaler profiles for cluster-wide tuning and notes that one profile affects all node pools using Cluster Autoscaler.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- deployment: `autoscale-demo-app`
- hpa: `autoscale-demo-hpa`
- node pool names that remain readable and clearly tied to the lab

Keep names readable so later cost/performance and governance modules can extend them naturally.

## Definition of ready
The learner is ready to start this lab when:
- the AKS cluster is reachable
- the sample workload is ready
- requests are already understood and preferably defined
- the learner is ready to think about pod scaling and node scaling together
