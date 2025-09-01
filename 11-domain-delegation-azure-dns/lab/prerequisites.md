# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Domain Delegation to Azure DNS lab.

This module is less about Kubernetes manifests and more about DNS authority, naming control, and public platform integration.

## Required account access
You should have working access to:
- Azure
- Azure DNS
- a domain registrar account or an existing DNS provider account if doing this practically
- the ability to review or update name server delegation for the chosen domain or subdomain

## Required tools
The following should be available:

- Azure portal or Azure CLI
- a browser for registrar or DNS-provider access
- optional terminal tools for DNS testing such as `nslookup` or `dig`
- optional note-taking for recording delegation design and propagation observations

Azure CLI can also be used later to manage Azure DNS records once the zone is in place. Microsoft documents Azure DNS record management through the CLI after zone creation.

## Required permissions
You should be able to:
- create a public DNS zone in Azure
- view the zone’s assigned name servers
- update the registrar-side or parent-zone delegation if doing this practically
- verify public DNS resolution behavior for the chosen domain or subdomain

## Required prior understanding
Before starting this module, the learner should already understand:
- ingress basics from Folder 09
- path-based routing from Folder 10
- that public application naming is a separate concern from internal service routing
- that later ExternalDNS and domain-based ingress patterns require a DNS authority layer

## Required environment state
Before starting:
- an Azure subscription with DNS access should be available
- the learner should know which domain or subdomain will be used
- the learner should understand whether this is a real registrar-backed lab or a conceptual modeled lab
- the learner should be ready to think in terms of authority transfer, not only record creation

## Domain strategy recommendation
For a clean learning scenario, a delegated subdomain is often easier than moving an entire root domain.

Recommended example:
- root domain remains where it is
- one subdomain such as `apps.example.com` is delegated to Azure DNS

This keeps the learning boundary safer and more operationally realistic.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- Azure DNS zone: `apps.example.com`
- intended future ingress hostnames: `app1.apps.example.com`, `app2.apps.example.com`

Keep the names readable so later ExternalDNS and hostname-routing modules can extend them naturally.

## Definition of ready
The learner is ready to start this lab when:
- Azure DNS access is working
- a domain or subdomain strategy has been chosen
- registrar-side or parent-zone access is available, or the delegation can be modeled clearly
- the learner is ready to think about DNS authority as a platform layer
