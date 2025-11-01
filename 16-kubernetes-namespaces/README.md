# Folder 16 — Kubernetes Namespaces
![Week-16 Plan](../Posts/16.png)

## Overview
This module expands the AKS platform story from individual workload governance into namespace-based logical isolation. It helps the learner understand how namespaces create structure inside a cluster so that workloads can be grouped, separated, governed, and reasoned about more cleanly across teams, environments, and application domains.

This is where the course moves from “how one workload behaves” into “how many workloads coexist safely and meaningfully inside one cluster.” The learner is now thinking not only about pods and services, but about cluster organization and governance boundaries.

## Why this module matters
A cluster without namespace structure becomes increasingly difficult to operate as more teams, applications, and environments are introduced. Even when workloads are technically correct, the absence of clear logical boundaries leads to naming confusion, poor policy scoping, harder access control, and weak governance.

Kubernetes documentation defines namespaces as a mechanism for isolating groups of resources within a single cluster, especially in environments with many users spread across multiple teams or projects. Namespace-based structure becomes even more valuable when combined with resource quotas, limit ranges, and RBAC. This makes namespaces one of the most important internal platform-organization tools in Kubernetes. 

## What you will learn
- What Kubernetes namespaces are and why they matter in AKS
- How namespaces support logical separation inside a shared cluster
- Why namespaces are foundational for quotas, limits, and policy boundaries
- Why namespace design is one of the clearest signals of platform maturity in multi-team clusters

## Workflow position
This module builds directly on Folder 15, where the learner understood resource discipline at the workload level. Now the learner moves to a broader operational level: how workloads should be grouped and governed at the namespace level.

This module also prepares the learner directly for:
- resource quotas and limit ranges as namespace-level governance patterns
- RBAC and access segmentation later in the course
- more production-grade AKS design thinking

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain namespaces in practical AKS terms
- create and use namespaces intentionally
- understand why namespaces are not just labels, but governance boundaries
- explain how namespace structure supports more scalable cluster operations

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the namespace structure and workload placement carefully  
5. Do not move ahead until namespaces feel clear as a cluster-organization pattern, not only a Kubernetes command  

## Next module
The next module is **AKS Virtual Nodes**.

That module shifts the platform story from logical isolation into execution model expansion, where workloads can be placed across standard nodes and virtual-node-backed capacity patterns.
