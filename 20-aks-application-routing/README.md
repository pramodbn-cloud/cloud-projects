# Folder 20 — AKS Application Routing
![Week-20 Plan](../Posts/20.png)

## Overview
This module introduces the AKS-managed ingress experience through the Application Routing add-on. It helps the learner understand how AKS can provide a managed ingress-controller path with tighter Azure integration, reducing some of the manual controller-management burden seen in self-managed ingress patterns.

This module should be understood as the modern successor to the older HTTP Application Routing topic that appeared in earlier AKS learning paths. The platform direction has shifted, and current AKS guidance recommends the Application Routing add-on as the managed ingress-controller path.

## Why this module matters
Earlier modules in this course intentionally taught ingress through explicit controller- and manifest-driven patterns so the learner could understand traffic architecture deeply. But real AKS platforms also benefit from understanding when a managed routing option is available and how that changes operational responsibility.

Microsoft now documents the Application Routing add-on as the recommended way to configure an ingress controller in AKS. It provides a managed NGINX ingress-controller experience and integration with Azure DNS for public and private zone management. Microsoft also notes constraints such as requiring managed identity and supporting up to five Azure DNS zones.

## What you will learn
- What the AKS Application Routing add-on is
- How it differs from self-managed ingress-controller patterns
- Why managed ingress can reduce operational burden
- When this model fits well in an AKS platform design

## Workflow position
This module comes after:
- manual/self-managed ingress understanding
- DNS delegation and ExternalDNS automation
- Azure DevOps-to-AKS delivery automation

That ordering is intentional. The learner first learned the underlying architecture. Now the learner studies the AKS-managed routing alternative and can compare the two with real platform judgment.

This module also prepares the learner for:
- Folder 21 — AKS Authentication with Azure AD and Kubernetes RBAC
- later production-cluster design decisions about managed versus self-managed components

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain the Application Routing add-on clearly
- compare managed application routing with earlier self-managed ingress patterns
- understand how Azure DNS integration fits into this model
- explain why this module replaces the older HTTP Application Routing topic in a current-course version

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the managed-routing behavior carefully  
5. Do not move ahead until Application Routing feels clear as a managed platform pattern, not just “another ingress setup”  

## Next module
The next module is **AKS Authentication with Azure AD and Kubernetes RBAC**.

That module shifts the platform story from traffic-management choices into cluster access governance, which is a natural next step after understanding both self-managed and AKS-managed routing models.
