# Folder 09 — AKS Ingress Basics
![Week-9 Plan](../Posts/9.png)

## Overview
This module begins the advanced AKS delivery engineering phase by introducing ingress as the traffic-entry layer for workloads running inside Azure Kubernetes Service. It helps the learner understand how external HTTP and HTTPS traffic reaches services inside a cluster and why ingress becomes one of the first major platform-engineering concerns after application deployment.

This is the point where the course moves from Azure DevOps workflow foundations into runtime architecture. The learner now starts thinking in terms of traffic flow, exposure boundaries, controllers, and how Kubernetes application access is managed at scale.

## Why this module matters
A deployed application inside Kubernetes is not automatically reachable in a clean, scalable, or production-friendly way. Teams need a controlled method to route external traffic to internal services, consolidate entry points, and prepare for later concepts such as path-based routing, domain-based routing, DNS automation, and TLS.

Ingress in AKS is a Kubernetes resource that manages external HTTP-like traffic access to services in the cluster and can provide capabilities such as load balancing, SSL termination, and name-based virtual hosting. In current AKS guidance, the application routing add-on is the recommended managed ingress option, while the course material you’re basing this on also explicitly starts the advanced track with Ingress Basics and updates ingress examples to use `ingressClassName`.

## What you will learn
- What ingress is in Kubernetes and why AKS needs it for application exposure
- The difference between service exposure and ingress-based traffic management
- The role of an ingress controller in making ingress resources actually work
- Why ingress is the foundation for later advanced modules like routing, DNS, and SSL

## Workflow position
This module begins the advanced phase, so its purpose is different from the earlier Azure DevOps modules. The learner is no longer focused mainly on planning, pipelines, and package flow. Instead, the learner is now focused on runtime traffic architecture in AKS.

This module also prepares the learner directly for:
- Folder 10 — Ingress Context Path Routing
- Folder 11 — Domain Delegation to Azure DNS
- Folder 12 — ExternalDNS with Azure DNS
- Folder 14 — Ingress SSL with Let’s Encrypt

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain ingress in AKS in practical platform-engineering terms
- understand why an ingress controller is required
- deploy a simple ingress-based application exposure model
- explain how traffic moves from an external endpoint to a Kubernetes service

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the traffic-entry flow carefully  
5. Do not move ahead until ingress feels clear as an architecture concept, not only a manifest object  

## Next module
The next module is **Ingress Context Path Routing**.

That module builds directly on this one by showing how one ingress entry point can route requests to different backend services based on URL paths. This is where ingress starts becoming not just an entry mechanism, but a traffic-control mechanism.
