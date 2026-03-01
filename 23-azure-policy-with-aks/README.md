# Folder 23 — Azure Policy with AKS
![Week-23 Plan](../Posts/23.png)

## Overview
This module introduces governance enforcement in AKS through Azure Policy. It helps the learner understand how platform rules can be applied to AKS clusters and Kubernetes workloads so that noncompliant configurations are audited, warned, or denied before they become long-term platform drift.

This is where the course moves from reactive platform operation into preventive platform governance. The learner is no longer only thinking about access, scaling, and workload delivery. The learner is now thinking about how the platform can actively enforce what is and is not allowed.

## Why this module matters
A cluster can be well designed on paper and still drift operationally if users deploy workloads that violate security, configuration, or reliability expectations. Manual review does not scale well, especially in shared or rapidly changing environments.

Azure Policy for Kubernetes makes it possible to manage and report the compliance state of Kubernetes cluster components centrally. In AKS, Azure Policy can apply built-in security and configuration policies to workloads and cluster resources, and Azure’s governance guidance explains that the AKS policy add-on extends Gatekeeper for policy enforcement.

## What you will learn
- What Azure Policy does in an AKS platform
- How Azure Policy connects governance to workload admission and compliance
- Why centralized built-in policies are useful in multi-team clusters
- Why policy enforcement is a major production-readiness step

## Workflow position
This module builds directly on:
- Folder 15 — Kubernetes Requests + Limits
- Folder 16 — Kubernetes Namespaces
- Folder 21 — AKS Authentication with Microsoft Entra ID and Kubernetes RBAC
- Folder 22 — AKS Autoscaling

That ordering matters. The learner already understands workload behavior, namespace boundaries, access governance, and elasticity. Now the learner adds a higher-level governance layer that can enforce expected standards across those earlier topics.

This module also prepares the learner directly for:
- stronger security baselines
- deployment safeguards and workload best-practice enforcement
- production-cluster compliance and audit readiness

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain Azure Policy in AKS clearly
- understand the difference between audit and deny-style policy behavior
- apply or review a built-in AKS policy assignment
- explain why policy enforcement matters in production clusters

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the policy-evaluation and enforcement flow carefully  
5. Do not move ahead until Azure Policy feels clear as a governance-enforcement pattern, not only an Azure feature  

## Next module
The next module is **AKS with Terraform**.
