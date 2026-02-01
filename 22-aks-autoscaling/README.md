# Folder 22 — AKS Autoscaling
![Week-22 Plan](../Posts/22.png)

## Overview
This module introduces autoscaling in AKS as the runtime elasticity layer that allows workloads and cluster capacity to respond automatically to changing demand. It helps the learner understand that scaling in Kubernetes is not one mechanism but a coordinated system involving pod-level scaling and node-level scaling.

This is where the course moves from static platform operation into adaptive platform behavior. The learner is no longer only thinking about how workloads are delivered, exposed, and governed. The learner is now thinking about how the platform reacts under load, how capacity is added or reduced, and how scaling decisions are driven by metrics and scheduling constraints.

## Why this module matters
A cluster with no autoscaling can work for steady demand, but it becomes brittle under variable traffic or uneven workload pressure. If pods need to scale but nodes do not, pods may remain pending. If nodes can scale but the workload never requests more replicas, application capacity may still remain insufficient.

Kubernetes documents that the Horizontal Pod Autoscaler automatically updates workload replica count based on observed metrics such as CPU or memory. AKS documents that the Cluster Autoscaler automatically adjusts node-pool size when pods can't be scheduled or when nodes are underutilized. AKS guidance also recommends thinking about pod autoscaling and cluster autoscaling together because they solve different levels of the same capacity problem.

## What you will learn
- What HPA and Cluster Autoscaler do and how they differ
- Why pod scaling and node scaling must be understood together
- How requests and limits from earlier modules influence scaling behavior
- Why autoscaling is a major production-readiness capability in AKS

## Workflow position
This module builds directly on:
- Folder 15 — Kubernetes Requests + Limits
- Folder 17 — AKS Virtual Nodes
- Folder 21 — AKS Authentication with Microsoft Entra ID and Kubernetes RBAC

That ordering matters. The learner already understands workload resource contracts, execution models, and operational governance. Now the learner moves into adaptive runtime behavior, where those earlier decisions strongly influence how autoscaling works.

This module also prepares the learner directly for:
- stronger performance and cost optimization discussions
- production-capacity planning
- more advanced cluster design and multi-pool scaling strategy

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain HPA and Cluster Autoscaler clearly
- understand how HPA depends on workload metrics and requests
- understand how Cluster Autoscaler depends on schedulability and node-pool bounds
- explain why autoscaling is a coordinated platform behavior rather than one switch

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the pod-scaling and node-scaling flow carefully  
5. Do not move ahead until autoscaling feels clear as an elasticity system, not only an AKS feature  

## Next module
The next module is **Azure Policy with AKS**.

That module shifts the platform story from elastic runtime behavior into governance enforcement, where the cluster can be made to reject or audit workloads that do not comply with organizational rules.
