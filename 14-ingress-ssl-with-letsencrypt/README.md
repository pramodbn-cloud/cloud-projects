# Folder 14 — Ingress SSL with Let’s Encrypt
![Week-14 Plan](../Posts/14.png)

## Overview
This module secures the hostname-based ingress layer by introducing TLS and certificate automation. It helps the learner understand how AKS ingress, DNS, and certificate management come together so that applications are not only reachable through meaningful hostnames, but also reachable securely over HTTPS.

This is one of the clearest production-readiness transitions in the AKS track. The learner is no longer only thinking about traffic entry and hostname selection. The learner is now thinking about trust at the browser and client level, certificate lifecycle, and how public-facing ingress should be protected in a modern platform.

## Why this module matters
A hostname without TLS is only partially production-ready. Most real applications need encrypted transport, certificate trust, and a repeatable renewal model. Without that, teams are left with insecure HTTP access, browser warnings, manual certificate handling, or inconsistent operational processes.

AKS ingress guidance states that ingress can provide SSL/TLS termination, and Microsoft’s cert-manager guidance explains how certificate issuance and renewal can be automated in Kubernetes environments. Let’s Encrypt is commonly used as the public certificate authority for this automation pattern, typically using HTTP-01 challenge flows through ingress. This makes cert-manager + Let’s Encrypt one of the most important ingress maturity steps for public application exposure. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/aks/concepts-network-ingress?utm_source=chatgpt.com))

## What you will learn
- Why TLS matters at the ingress layer
- How Let’s Encrypt and cert-manager fit into AKS ingress security
- How certificates are requested, validated, stored, and attached to ingress
- Why DNS, hostname routing, and ingress readiness had to come before this module

## Workflow position
This module builds directly on:
- Folder 11 — Domain Delegation to Azure DNS
- Folder 12 — ExternalDNS with Azure DNS
- Folder 13 — Domain Name Based Routing

Now that hostnames exist and route correctly, the learner can add HTTPS and certificate lifecycle management. This is the logical next step toward secure public application exposure.

This module also prepares the learner for later advanced platform patterns where trust, security, and application identity all converge at the ingress layer.

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain TLS at ingress in AKS clearly
- understand how cert-manager works with Let’s Encrypt
- attach a valid certificate to an ingress hostname
- explain why certificate automation is operationally stronger than manual certificate management

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the certificate and HTTPS flow carefully  
5. Do not move ahead until TLS feels clear as a certificate lifecycle pattern, not only an ingress annotation change  

## Next module
The next module is **Kubernetes Requests + Limits**.

That module shifts the focus from traffic exposure into workload resource governance, which is another major production-readiness concern for AKS platforms.
