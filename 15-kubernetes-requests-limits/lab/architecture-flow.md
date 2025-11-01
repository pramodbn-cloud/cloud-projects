# Architecture Flow

## Purpose of this file
This file explains the logical resource-governance flow used in the Kubernetes Requests + Limits lab before implementation begins.

This module is about workload resource behavior — how Kubernetes decides where a pod can run, how much CPU and memory it is entitled to request, and how resource usage can be constrained at runtime.

## High-level architecture view
The workflow begins with a pod or deployment that needs CPU and memory to run. Kubernetes cannot schedule that workload intelligently unless it knows what the workload expects. Requests and limits provide that missing contract.

At a high level, the flow looks like this:

- a workload declares CPU and memory requests
- the scheduler uses requests to determine where the workload can fit
- the workload may also declare CPU and memory limits
- the runtime enforces the limits during execution
- the cluster now has better control over how resources are reserved and how resource overuse is contained

This turns workload deployment into a more predictable contract between the application and the cluster.

## Component roles

- **Workload / Deployment** — the application whose resources must be governed  
- **Pod Spec** — the place where requests and limits are declared  
- **Kubernetes Scheduler** — uses requests to make placement decisions  
- **Node Capacity** — the actual CPU and memory available on a node  
- **Kubelet / Runtime Enforcement** — enforces resource constraints at execution time  
- **AKS Cluster** — the shared environment where multiple workloads compete for resources  

## End-to-end flow

1. A workload is defined for deployment.  
2. CPU and memory requests describe what the workload regularly needs.  
3. The scheduler checks whether any node can satisfy those requests.  
4. The pod is scheduled only where those requests fit.  
5. CPU and memory limits constrain how far the workload may grow at runtime.  
6. The cluster gains better predictability, fairness, and protection against uncontrolled usage.  

## Dependency awareness
This module depends on:
- a working AKS cluster
- familiarity with deployments and pods
- an understanding that earlier ingress and DNS work solved access, not resource behavior

This module also prepares the learner for:
- namespaces and LimitRange/ResourceQuota style governance
- autoscaling discussions later
- production-grade cluster design and capacity planning

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- scheduler predictability
- resource fairness
- workload reliability
- protection against noisy neighbors
- cluster capacity interpretation
- how runtime behavior changes once limits exist

These are the qualities that make resource governance useful in real clusters.

## What to keep in mind before implementation
Before starting the steps:
- requests are not the same as limits
- scheduling and runtime control are related but different concerns
- requests shape placement; limits shape containment
- unmanaged workloads are harder to reason about in shared clusters
- the goal is predictability, not only “making the YAML pass”
