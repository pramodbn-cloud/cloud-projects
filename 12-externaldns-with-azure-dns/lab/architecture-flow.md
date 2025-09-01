# Architecture Flow

## Purpose of this file
This file explains the logical DNS automation flow used in the ExternalDNS with Azure DNS lab before implementation begins.

This module is about controller-driven naming lifecycle — how Kubernetes intent becomes public DNS state in Azure DNS without manual record creation for each change.

## High-level architecture view
The workflow begins with a Kubernetes resource that expresses hostname intent, usually through annotations or host-related configuration. ExternalDNS watches those resources, determines which DNS records should exist, and then uses Azure DNS APIs to reconcile the public zone into the desired state.

At a high level, the flow looks like this:

- Azure DNS already owns the delegated domain or subdomain
- ExternalDNS runs inside the AKS cluster as a controller
- ExternalDNS watches ingresses and/or services for DNS intent
- ExternalDNS determines the required DNS records
- ExternalDNS authenticates to Azure and updates Azure DNS
- the Azure DNS zone receives new or updated record sets
- public hostname resolution now reflects Kubernetes-driven intent

This is the shift from manual DNS administration into automated DNS lifecycle management.

## Component roles

- **Client / External User** — later resolves and uses the public hostname  
- **Kubernetes Resource** — usually an ingress or service expressing DNS intent  
- **ExternalDNS Controller** — watches cluster resources and calculates desired DNS changes  
- **Azure Authentication Model** — gives ExternalDNS permission to update the DNS zone  
- **Azure DNS Zone** — the authoritative DNS zone where records are created or updated  
- **Ingress Endpoint / Service Endpoint** — the value that the DNS record points to  
- **Public DNS Resolution Path** — the external lookup path that consumes the record  

## End-to-end flow

1. A delegated Azure DNS zone already exists.  
2. ExternalDNS runs in the AKS cluster with Azure DNS permissions.  
3. An ingress or service expresses a hostname or DNS annotation.  
4. ExternalDNS detects that intent.  
5. ExternalDNS calculates the DNS record that should exist.  
6. ExternalDNS uses Azure credentials to update the Azure DNS zone.  
7. The hostname resolves publicly to the intended AKS-facing endpoint.  

## Dependency awareness
This module depends on:
- Folder 11 for Azure DNS authority
- Folder 09 and 10 for ingress and routing understanding
- an AKS cluster and an ingress/service exposure pattern already in place

This module also prepares the learner for:
- hostname-based ingress routing
- certificate issuance and DNS-backed validation patterns
- more advanced automation and governance of public application naming

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- zone authority correctness
- controller scope
- safe Azure permissions
- clear DNS ownership boundaries
- deterministic hostname lifecycle
- avoiding manual record drift

These are the qualities that make automated DNS trustworthy in real environments.

## What to keep in mind before implementation
Before starting the steps:
- ExternalDNS does not replace DNS authority; it depends on it
- Azure DNS must already control the delegated scope
- the controller should have only the permissions needed for DNS updates
- DNS automation is a platform convenience only when it is also a governance success
- think in terms of reconciliation, not one-time record creation
