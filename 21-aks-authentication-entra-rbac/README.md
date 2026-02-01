# Folder 21 — AKS Authentication with Microsoft Entra ID and Kubernetes RBAC
![Week-21 Plan](../Posts/21.png)

## Overview
This module introduces cluster-access governance in AKS through Microsoft Entra ID authentication and Kubernetes RBAC authorization. It helps the learner understand how human access to the cluster should be authenticated centrally and then restricted according to least-privilege role design inside Kubernetes.

This is where the course shifts from platform delivery and runtime operation into platform access governance. The learner is no longer only thinking about how workloads run or how traffic reaches them. The learner is now thinking about who may view, modify, or administer cluster resources, and how that access should be scoped responsibly.

## Why this module matters
A cluster can be technically healthy and still be operationally unsafe if too many users have broad access or if authentication is weak and unmanaged. In shared AKS environments, access control is one of the clearest lines between a demo platform and a production platform.

Microsoft documents AKS integration with Microsoft Entra ID for user authentication, and then supports Kubernetes RBAC to grant permissions to users or groups at namespace or cluster scope. Microsoft also documents Azure RBAC for Kubernetes Authorization as another authorization option, and AKS identity best-practices guidance recommends Entra integration and least-privilege access design. 

## What you will learn
- How Microsoft Entra ID fits into AKS authentication
- How Kubernetes RBAC controls what authenticated users can do
- Why group-based access is usually stronger than user-by-user access design
- How namespace scoping and RBAC connect to earlier namespace and governance modules

## Workflow position
This module builds directly on:
- Folder 16 — Kubernetes Namespaces
- earlier AKS platform-governance modules
- the full delivery/runtime sequence already covered

That ordering matters. The learner already understands how workloads are organized and governed technically. Now the learner applies that same maturity to human access and operator permissions.

This module also prepares the learner directly for:
- production-cluster governance
- Azure RBAC for Kubernetes Authorization discussions
- more advanced policy and security controls later

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain AKS authentication with Microsoft Entra ID clearly
- explain Kubernetes RBAC in practical namespace- and cluster-scope terms
- bind access to users or groups in a controlled way
- explain why cluster access governance is a major production-readiness concern

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the authentication and authorization flow carefully  
5. Do not move ahead until cluster access feels clear as a governed identity pattern, not only a kubectl login flow  

## Next module
The next module is **AKS Autoscaling**.

That module shifts the platform story from human governance into runtime elasticity, where the cluster responds to changing workload demand at node and/or pod level.
