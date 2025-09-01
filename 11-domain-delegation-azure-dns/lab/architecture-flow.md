# Architecture Flow

## Purpose of this file
This file explains the logical DNS ownership and delegation flow used in the Domain Delegation to Azure DNS lab before implementation begins.

This module is about naming authority architecture — how a domain or subdomain becomes managed by Azure DNS so that later application records can be created, updated, and automated inside Azure.

## High-level architecture view
The workflow begins with a domain that is currently managed either by a registrar or by another DNS provider. Azure DNS cannot become authoritative for that domain simply because a zone is created in Azure. Authority must be delegated.

At a high level, the flow looks like this:

- a public DNS zone is created in Azure DNS
- Azure assigns authoritative name servers for that zone
- the domain owner updates delegation at the registrar or parent zone
- the registrar or parent zone points the domain or subdomain to Azure’s name servers
- once delegation is effective, Azure DNS becomes authoritative for that domain scope
- DNS records can then be managed in Azure DNS for later ingress integration

This is the exact ownership transition that must happen before Azure DNS can meaningfully support ingress-related naming. Microsoft explicitly states that delegation is required before using Azure DNS for custom domain records.

## Component roles

- **Domain Owner / Platform Engineer** — controls and coordinates the delegation change  
- **Registrar or Existing DNS Provider** — currently holds the delegation point for the domain  
- **Azure DNS Zone** — the new authoritative DNS zone inside Azure  
- **Azure Name Servers** — the authoritative name servers assigned to the Azure DNS zone  
- **Delegation Record / NS Update** — the mechanism that transfers DNS authority  
- **Future Ingress Records** — the records that will later point application names toward ingress endpoints  

## End-to-end flow

1. A DNS zone is created in Azure DNS.  
2. Azure assigns name servers to that zone.  
3. The domain owner identifies the registrar or parent zone currently holding authority.  
4. The registrar or parent zone is updated with the Azure name servers.  
5. DNS authority propagates so Azure DNS becomes authoritative for the delegated scope.  
6. Azure DNS is now ready to host records for later ingress-related naming.  

## Dependency awareness
This module depends on:
- a domain or subdomain that the learner controls or can model conceptually
- an Azure subscription with Azure DNS access
- understanding from earlier ingress modules that naming will later point at ingress endpoints

This module also prepares the learner for:
- ExternalDNS automation
- hostname-based ingress routing
- TLS and certificate validation flows
- production DNS troubleshooting

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- authoritative ownership
- clear delegation boundaries
- full-domain versus subdomain strategy
- propagation awareness
- future compatibility with automation
- avoiding split or confusing DNS control models

These are the qualities that make DNS manageable in real environments.

## What to keep in mind before implementation
Before starting the steps:
- creating a zone is not the same as gaining authority
- Azure DNS becomes useful only after delegation is actually in place
- subdomain delegation can be a cleaner learning or team boundary than moving a full root domain
- the goal is to establish authoritative naming control before automation
- think in terms of platform ownership, not just record entry




