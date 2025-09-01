# Folder 12 — ExternalDNS with Azure DNS
![Week-12 Plan](../Posts/12.png)

## Overview
This module moves the platform from DNS ownership into DNS automation. It helps the learner understand how ExternalDNS watches Kubernetes resources and automatically creates, updates, or removes DNS records in Azure DNS so that application naming can evolve directly from cluster state.

This is where the AKS track becomes noticeably more production-oriented. The learner is no longer manually thinking “I created an ingress, now I should go create a DNS record.” Instead, the learner starts thinking in controller-driven lifecycle terms: Kubernetes intent becomes DNS state automatically.

## Why this module matters
In real AKS environments, manually managing DNS records for every ingress or service change does not scale well. It adds operational delay, increases the chance of record drift, and weakens the connection between cluster state and external naming.

ExternalDNS is designed to control DNS records dynamically from Kubernetes resources, and Azure-based implementations require Azure DNS permissions so that record sets can be added, updated, or deleted. The StackSimplify Azure AKS module also explicitly describes ExternalDNS as needing Azure DNS permissions and highlights two Azure authentication approaches: Service Principal and Managed Identity. Managed identity is presented there as the modern preferred direction. 

## What you will learn
- What ExternalDNS does in an AKS platform architecture
- How Kubernetes resources can drive public DNS record lifecycle
- Why Azure DNS permissions are required for ExternalDNS
- Why this module is the bridge between DNS authority and fully automated hostname exposure

## Workflow position
This module builds directly on Folder 11, where the learner delegated a domain or subdomain to Azure DNS. Now that Azure is authoritative for the delegated scope, the cluster can begin managing records in that zone automatically.

This module also prepares the learner directly for:
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
- explain ExternalDNS in Azure DNS terms clearly
- understand how DNS records can be created from Kubernetes resources
- explain the role of Azure permissions and identity in DNS automation
- describe why automated DNS is a major platform maturity step

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the DNS automation flow carefully  
5. Do not move ahead until ExternalDNS feels clear as a controller-driven lifecycle pattern, not just another deployment  

## Next module
The next module is **Domain Name Based Routing**.

That module builds directly on this one by using real hostnames instead of only path-based routing. ExternalDNS makes those hostnames manageable at scale, and hostname-based ingress rules give those DNS names meaningful routing behavior.
