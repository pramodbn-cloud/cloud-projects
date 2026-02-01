# Architecture Flow

## Purpose of this file
This file explains the logical elasticity flow used in the AKS Autoscaling lab before implementation begins.

This module is about runtime elasticity — how changing demand results in more pod replicas, and how increased pod demand can then require more cluster node capacity.

## High-level architecture view
The workflow begins with a workload that experiences changing demand. One layer of the platform reacts by scaling the workload horizontally. Another layer reacts if the cluster no longer has enough room to place those extra pods.

At a high level, the flow looks like this:

- workload demand increases
- observed metrics rise on the running pods
- HPA increases the number of replicas
- the scheduler tries to place the new pods
- if node capacity is insufficient, some pods become pending
- Cluster Autoscaler detects unschedulable pods and scales the node pool
- new node capacity allows the pending pods to be scheduled

This creates a two-level elasticity model:
- pod-level elasticity
- node-level elasticity

## Component roles

- **Workload / Deployment** — the application that needs more or fewer replicas  
- **Horizontal Pod Autoscaler (HPA)** — adjusts replica count based on observed metrics  
- **Scheduler** — attempts to place pods based on resource requests and node capacity  
- **Node Pool** — the compute backing where pods run  
- **Cluster Autoscaler** — adjusts node-pool size when scheduling demand changes  
- **Metrics Pipeline** — provides the utilization signals HPA reacts to  
- **AKS Cluster** — the overall runtime environment containing these scaling layers  

## End-to-end flow

1. A workload runs with defined CPU and/or memory requests.  
2. Load increases and resource utilization rises.  
3. HPA raises the desired replica count.  
4. The scheduler tries to place those new replicas.  
5. If no node capacity exists, pods remain pending.  
6. Cluster Autoscaler detects pending pods and adds node capacity within configured bounds.  
7. The pods are scheduled and the workload scales successfully.  

## Dependency awareness
This module depends on:
- workload resource definitions from Folder 15
- namespace and governance maturity from Folder 16
- a working AKS cluster and node pool

This module also prepares the learner for:
- cost/performance optimization
- multi-pool scaling strategy
- stronger policy design where scale and governance meet

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- workload requests as scheduler inputs
- HPA as workload elasticity
- Cluster Autoscaler as infrastructure elasticity
- pending pods as a key operational signal
- min/max boundaries and autoscaler profile tuning
- scale-down behavior and cost consequences

These are the qualities that make autoscaling useful rather than merely enabled.

## What to keep in mind before implementation
Before starting the steps:
- HPA does not add nodes
- Cluster Autoscaler does not decide desired replica count
- resource requests matter because scheduling and node-autoscaling reason from them
- pod scaling and node scaling are complementary, not interchangeable
- the goal is adaptive and observable behavior, not only “more replicas”
