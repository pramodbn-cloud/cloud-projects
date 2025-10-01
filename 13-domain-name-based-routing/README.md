# Folder 13 — Domain Name Based Routing
![Week-13 Plan](../Posts/13.png)

## Overview
This module moves ingress design from path-based differentiation into hostname-based differentiation. It helps the learner understand how one AKS ingress layer can route requests to different backend services based on the requested domain name, such as `app1.apps.example.com` and `app2.apps.example.com`.

This is where ingress starts looking much closer to real production application exposure. The learner is no longer only organizing traffic by URL path under one hostname. The learner is now assigning distinct public identities to different applications while still keeping routing centralized at the ingress layer.

## Why this module matters
In many real AKS platforms, hostname-based routing is more natural and scalable than path-based routing for public-facing services. Different applications, teams, or environments often need their own domain identities even when they still share one ingress entry point or one ingress-controller layer.

AKS ingress guidance states that ingress can provide name-based virtual hosting, and Azure ingress-controller documentation notes that one ingress controller and one IP can route traffic to multiple services through ingress rules. Azure’s multitenant AKS guidance also calls out explicit path-based or host-based routing rules as an important design pattern. This makes domain-name-based routing a natural next step after path-based ingress and Azure DNS automation.

## What you will learn
- How hostname-based ingress routing works in AKS
- Why domain-name-based routing is often preferable to path-only routing for public application separation
- How Azure DNS and ExternalDNS support ingress hostnames operationally
- Why this pattern prepares the platform for TLS and more production-like ingress design

## Workflow position
This module builds directly on:
- Folder 11 — Domain Delegation to Azure DNS
- Folder 12 — ExternalDNS with Azure DNS

Now that Azure DNS owns the delegated zone and ExternalDNS can automate records, the learner can use real hostnames as routing keys inside ingress. This is the logical next step after path-based routing.

This module also prepares the learner directly for:
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
- explain hostname-based routing in AKS clearly
- route different hostnames to different backend services
- connect Azure DNS automation to ingress routing behavior
- explain why domain-based routing is a stronger production-style exposure model than path-only routing in many cases

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the hostname-routing flow carefully  
5. Do not move ahead until host-based routing feels clear as a naming-and-routing platform pattern, not only an ingress manifest variation  

## Next module
The next module is **Ingress SSL with Let’s Encrypt**.

That module builds directly on this one by securing the hostname-based routing layer with TLS so that public application access becomes both human-friendly and encrypted.
