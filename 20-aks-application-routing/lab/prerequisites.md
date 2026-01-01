# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the AKS Application Routing lab.

This module depends on current AKS-managed routing behavior, so the prerequisites are specifically tied to the modern Application Routing add-on rather than the retired HTTP Application Routing add-on.

## Required account access
You should have working access to:
- Azure
- an AKS cluster you can manage
- Azure DNS if DNS integration is part of the lab
- kubectl access to that cluster

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for reviewing manifests
- optional DNS lookup tools if Azure DNS integration is being validated

## Required permissions
You should be able to:
- inspect or enable AKS add-ons
- inspect the cluster identity model
- deploy or review ingress resources
- inspect namespaces and controller objects related to application routing
- inspect Azure DNS resources if DNS integration is in scope

## Required prior understanding
Before starting this module, the learner should already understand:
- ingress basics from Folder 09
- path-based routing from Folder 10
- domain delegation and DNS automation from Folders 11 and 12
- hostname-based routing from Folder 13
- that AKS can support both self-managed and managed ingress-controller approaches

## Required environment state
Before starting:
- an AKS cluster should already exist
- the cluster should use managed identity
- the learner should understand that the older HTTP Application Routing add-on is retired
- the learner should be ready to work with the modern Application Routing add-on instead

Microsoft states that the Application Routing add-on requires managed identity and supports up to five Azure DNS zones. Microsoft also documents the retirement of the old HTTP Application Routing add-on on March 3, 2025.

## Application-routing note
This module intentionally modernizes the older course topic. If the learner sees “HTTP Application Routing” in older AKS material, that should now be interpreted as historical context rather than the recommended current implementation. The current Microsoft-recommended pattern is the Application Routing add-on.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- namespace references should remain readable
- ingress resources should clearly indicate application-routing usage
- any Azure DNS zone integration should stay aligned to previously delegated zones

## Definition of ready
The learner is ready to start this lab when:
- the AKS cluster is reachable
- the cluster uses managed identity
- the learner understands the difference between the retired and current routing add-on models
- the learner is ready to compare managed and self-managed ingress operationally
