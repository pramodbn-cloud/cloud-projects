# Folder 15 — Kubernetes Requests + Limits
![Week-15 Plan](../Posts/15.png)

## Overview
This module shifts the AKS track from network and edge exposure into workload resource governance. It helps the learner understand how CPU and memory requests and limits shape scheduling, fairness, stability, and runtime behavior inside a Kubernetes cluster.

This is one of the first major “inside the cluster” production-discipline topics. The learner is no longer only thinking about how traffic reaches applications. The learner is now thinking about how applications consume shared cluster resources and how that affects predictability, reliability, and multi-workload coexistence.

## Why this module matters
A workload that has no clear CPU and memory expectations is much harder for Kubernetes to schedule and much easier to let misbehave at runtime. In shared AKS environments, that can create noisy-neighbor problems, unstable performance, failed scheduling, or accidental resource starvation for other applications.

Official Kubernetes guidance explains that requests tell Kubernetes how much CPU or memory a container or pod needs, while limits cap how much it may consume. AKS best-practice guidance explicitly recommends defining requests and limits on all pods, both for scheduling correctness and for operational stability.

## What you will learn
- What CPU and memory requests and limits mean in Kubernetes
- How requests influence scheduler behavior
- How limits protect the cluster from uncontrolled consumption
- Why resource definitions are one of the clearest signs of production-aware workload design

## Workflow position
This module follows the ingress, DNS, and TLS sequence because the platform is now ready to shift from external access concerns to internal workload discipline.

This module also prepares the learner directly for:
- Folder 16 — Kubernetes Namespaces
- Folder 22 — AKS Autoscaling
- later production-cluster design thinking

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain requests and limits in practical AKS terms
- understand how Kubernetes uses requests during scheduling
- understand how limits affect runtime behavior and protection
- explain why unmanaged resource usage is risky in shared clusters

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the scheduling and runtime behavior carefully  
5. Do not move ahead until resource governance feels clear as a runtime-control pattern, not only YAML syntax  

## Next module
The next module is **Kubernetes Namespaces**.

That module builds directly on this one by introducing logical isolation and policy boundaries, which work naturally alongside requests, limits, quotas, and team/environment separation.
