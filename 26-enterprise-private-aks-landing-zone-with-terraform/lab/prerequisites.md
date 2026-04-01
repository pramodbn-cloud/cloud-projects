# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Enterprise Private AKS Landing Zone with Terraform lab.

This module depends on Azure networking, private connectivity concepts, Terraform readiness, and AKS design maturity.

## Required account access
You should have working access to:
- Azure
- an Azure subscription capable of hosting AKS and supporting platform resources
- resource groups, virtual networks, private endpoints, DNS zones, and AKS creation rights
- Terraform-ready Azure access

## Required tools
The following should be available:

- Terraform
- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for Terraform structure

## Required permissions
You should be able to:
- create AKS clusters
- create virtual networks and subnets
- create private endpoints
- create and link private DNS zones
- create or assign managed identities and supporting role bindings
- inspect created infrastructure in Azure

## Required prior understanding
Before starting this module, the learner should already understand:
- AKS architecture basics
- ingress, DNS, TLS, and ACR from earlier modules
- namespaces and RBAC at a conceptual level
- Terraform basics from Folder 24
- Terraform + Azure DevOps delivery from Folder 25

## Required environment state
Before starting:
- Terraform should be installed and working
- Azure CLI authentication should be working
- the learner should be comfortable reasoning about private clusters
- the learner should understand that this module is designing a new platform baseline, not retrofitting a quick demo environment

## Architecture strategy recommendation
Keep the first enterprise pattern **clear and opinionated**.

Recommended approach:
- one environment
- one resource group strategy
- one segmented VNet model
- one private AKS cluster
- one private endpoint strategy for ACR and Key Vault
- one private DNS design
- one logging/monitoring baseline

This keeps the design deep without turning it into uncontrolled sprawl.

## Important design note
Microsoft’s baseline AKS architecture is a strong reference for this module, but this folder intentionally emphasizes the **private and enterprise-restricted** interpretation of that design. Private clusters, private DNS, and private endpoint-based dependency access are central to this learning path.

## Definition of ready
The learner is ready to start this lab when:
- Azure provisioning access is ready
- Terraform is ready
- private cluster and private endpoint concepts are understood at least conceptually
- the learner is ready to think like a platform architect, not only a cluster deployer