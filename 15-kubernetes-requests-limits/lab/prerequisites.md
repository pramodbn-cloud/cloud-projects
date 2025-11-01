# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Kubernetes Requests + Limits lab.

This module is a runtime-governance topic, so the prerequisites are cluster- and workload-oriented rather than traffic-oriented.

## Required account access
You should have working access to:
- Azure
- an AKS cluster you can manage
- kubectl access to that cluster
- the ability to deploy workloads and inspect pod/resource state

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for reviewing or applying manifests
- optional metrics visibility if your environment supports it

## Required permissions
You should be able to:
- create or update Deployments
- inspect Pods and node status
- view workload descriptions
- view scheduling outcomes
- inspect resource settings in manifests and live objects

## Required prior understanding
Before starting this module, the learner should already understand:
- basic Deployments and Pods
- basic Kubernetes Services
- earlier ingress and exposure modules solved access, not workload resource governance
- that multiple workloads in a cluster share finite node resources

## Required environment state
Before starting:
- an AKS cluster should already exist
- at least one simple workload should be available or easy to deploy
- the learner should be ready to compare workload behavior before and after defining resources
- node capacity should be healthy enough to schedule the sample workload

## Workload scenario recommendation
Keep the lab simple and deterministic.

Recommended approach:
- use one small deployment
- observe it first with minimal or no explicit requests/limits
- then add clear CPU and memory requests and limits
- compare scheduling and runtime reasoning before and after

This keeps the resource-governance lesson easy to understand.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- deployment: `resource-demo-app`
- namespace: keep simple and readable if one is used
- manifest file names that clearly indicate “before” and “after” resource definitions

Keep names readable so later namespace and quota modules can build on them naturally.

## Definition of ready
The learner is ready to start this lab when:
- the AKS cluster is reachable
- a sample workload can be deployed
- the learner understands that nodes have finite CPU and memory
- the learner is ready to think about scheduler logic and runtime boundaries together
