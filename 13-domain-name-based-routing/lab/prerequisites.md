# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Domain Name Based Routing lab.

This module is the convergence point of ingress, DNS authority, and DNS automation, so the prerequisites are both runtime- and naming-oriented.

## Required account access
You should have working access to:
- Azure
- Azure DNS
- an AKS cluster you can manage
- kubectl access to that cluster
- the ability to inspect ingress resources and Azure DNS records

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for manifests
- DNS lookup tools such as `nslookup` or `dig`
- optional browser or curl-style testing tools for host-header-based validation

## Required permissions
You should be able to:
- deploy multiple workloads into AKS
- create Services
- create or modify Ingress resources
- view the Azure DNS zone from Folder 11
- inspect ExternalDNS behavior from Folder 12 if that is part of the chosen lab flow

## Required prior understanding
Before starting this module, the learner should already understand:
- ingress basics from Folder 09
- path-based routing from Folder 10
- Azure DNS delegation from Folder 11
- ExternalDNS automation from Folder 12
- the difference between path-based routing and hostname-based routing

## Required environment state
Before starting:
- the Azure DNS zone should already be authoritative
- the ingress-controller strategy should already be active
- ExternalDNS should already be deployed or at least understood
- two or more backend applications/services should already exist or be easy to deploy
- the learner should have one or more hostname examples inside the delegated zone ready to use

## Hostname-routing scenario recommendation
Keep the lab simple and deterministic.

Recommended example:
- `app1.apps.example.com` routes to backend service A
- `app2.apps.example.com` routes to backend service B

This keeps validation and troubleshooting clear and prepares naturally for TLS in the next module.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- service: `app1-service`
- service: `app2-service`
- ingress: `multi-app-host-ingress`
- hostname: `app1.apps.example.com`
- hostname: `app2.apps.example.com`

Keep names readable so TLS and later platform reasoning can extend them naturally.

## Definition of ready
The learner is ready to start this lab when:
- the AKS cluster is reachable
- the Azure DNS zone is authoritative
- hostname examples are chosen inside the delegated zone
- ingress basics and ExternalDNS basics are already understood
- the learner is ready to think in public application identity terms
