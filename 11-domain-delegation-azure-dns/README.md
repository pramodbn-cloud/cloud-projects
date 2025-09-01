# Folder 11 — Domain Delegation to Azure DNS
![Week-11 Plan](../Posts/11.png)

## Overview
This module moves the ingress story from traffic routing into real naming ownership. It helps the learner understand how a domain becomes usable in Azure by creating an Azure DNS zone and delegating authority for that domain or subdomain to Azure DNS.

This is where the advanced AKS track starts feeling more production-oriented. The learner is no longer only exposing applications by IP or raw ingress endpoint. The learner now begins working with externally meaningful naming, which is the foundation for hostname-based routing, automated DNS records, and TLS.

## Why this module matters
Ingress routing by itself is not enough for a production-style external access pattern. Teams need stable, human-meaningful DNS names that map to their ingress entry points and can later support domain-based routing, certificate issuance, and automated DNS management.

Microsoft’s Azure DNS guidance states that to use Azure DNS for a custom domain, you must first delegate the domain to Azure DNS. Once the domain is delegated to the Azure DNS zone, you can then configure the DNS records you need. The StackSimplify AKS sequence places Azure DNS delegation before ExternalDNS and domain-based routing, which is the correct architecture progression.

## What you will learn
- What domain delegation means in practical DNS terms
- Why Azure DNS zones are required before Azure-managed DNS records can be used
- How delegation fits between ingress exposure and later ExternalDNS automation
- Why naming ownership is a platform concern, not just a portal configuration task

## Workflow position
This module builds directly on Folder 10, where one ingress endpoint routed multiple services by path. Now the learner moves into naming and DNS authority, which is the next required layer before domain-based ingress patterns become realistic.

This module also prepares the learner directly for:
- Folder 12 — ExternalDNS with Azure DNS
- Folder 13 — Domain Name Based Routing
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
- explain Azure DNS delegation clearly
- create or review an Azure DNS zone for a domain or subdomain
- understand how registrar-side name server delegation connects to Azure DNS
- explain why this is a required step before automated DNS and hostname routing

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the naming and delegation flow carefully  
5. Do not move ahead until DNS delegation feels clear as an ownership and control concept, not just a setup task  

## Next module
The next module is **ExternalDNS with Azure DNS**.

That module builds directly on this one by automating record management inside the Azure DNS zone. This is where naming moves from manual control into controller-driven DNS lifecycle management.
