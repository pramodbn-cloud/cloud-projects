# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the ExternalDNS with Azure DNS lab.

This module sits at the intersection of AKS runtime state, Azure identity, and Azure DNS authority, so the prerequisites are both Kubernetes- and Azure-governance-oriented.

## Required account access
You should have working access to:
- Azure
- Azure DNS
- an AKS cluster you can manage
- kubectl access to that cluster
- the ability to assign or review the Azure permissions needed for DNS updates

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for reviewing or applying manifests
- optional Helm if you choose a Helm-based deployment flow for ExternalDNS
- optional DNS lookup tools such as `nslookup` or `dig`

## Required permissions
You should be able to:
- view the delegated Azure DNS zone
- create or assign the Azure identity model used by ExternalDNS
- grant Azure DNS permissions to that identity
- deploy workloads/controllers into the AKS cluster
- inspect ingresses or services used as DNS automation sources

## Required prior understanding
Before starting this module, the learner should already understand:
- ingress basics from Folder 09
- path-based routing from Folder 10
- Azure DNS delegation from Folder 11
- that DNS authority and DNS automation are different concerns

## Required environment state
Before starting:
- the Azure DNS zone from Folder 11 should already exist and be authoritative for the chosen scope
- an AKS cluster should already exist
- an ingress-controller strategy should already be active
- a simple ingress or service target for DNS automation should already exist or be easy to create

## Authentication strategy recommendation
Choose one Azure authentication pattern for ExternalDNS and stay consistent for the lab.

The source material and Azure/Azure-community guidance commonly discuss two main choices:
- Service Principal
- Managed Identity

StackSimplify’s AKS ExternalDNS guide explicitly highlights both and presents Managed Identity as the preferred modern direction there. The ExternalDNS Azure tutorial also documents managed-identity-based approaches. 

## Managed-platform note
If the learner is using AKS application routing instead of a self-managed ExternalDNS deployment, note that current AKS app routing documentation supports Azure DNS integration and requires managed-identity-based AKS clusters. This is useful context even if the lab focuses on explicit ExternalDNS concepts. 

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- namespace: `external-dns`
- deployment: `external-dns`
- Azure DNS zone: delegated scope from Folder 11
- hostname example: `app1.apps.example.com`

Keep names readable so later hostname-routing and TLS modules can extend them naturally.

## Definition of ready
The learner is ready to start this lab when:
- Azure DNS authority is already in place
- the AKS cluster is reachable
- an Azure identity model for DNS updates has been chosen
- a hostname source object such as an ingress is available
- the learner is ready to think in controller-driven reconciliation terms
