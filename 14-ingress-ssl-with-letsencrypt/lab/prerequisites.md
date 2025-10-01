# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Ingress SSL with Let’s Encrypt lab.

This module sits at the intersection of DNS, ingress, and certificate automation, so the prerequisites are heavily production-readiness oriented.

## Required account access
You should have working access to:
- Azure
- Azure DNS
- an AKS cluster you can manage
- kubectl access to that cluster
- the ability to inspect ingress resources and public hostname behavior

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for manifests
- DNS lookup tools such as `nslookup` or `dig`
- browser and/or curl-style HTTPS testing tools
- optional Helm if cert-manager will be installed through Helm in your chosen flow

## Required permissions
You should be able to:
- deploy cert-manager into the cluster or inspect an existing installation
- create Issuer or ClusterIssuer resources
- create or modify ingress resources
- inspect TLS secrets
- validate public hostname resolution and ingress behavior

## Required prior understanding
Before starting this module, the learner should already understand:
- ingress basics from Folder 09
- hostname-based routing from Folder 13
- Azure DNS delegation from Folder 11
- ExternalDNS or equivalent hostname record management from Folder 12
- that HTTPS depends on both naming correctness and ingress reachability

## Required environment state
Before starting:
- the Azure DNS zone should already be authoritative
- the application hostname should already resolve to the ingress endpoint
- the ingress route should already work correctly over HTTP
- the learner should have a clear hostname target ready for certificate issuance
- cert-manager installation strategy should already be chosen

## Issuer strategy recommendation
Keep the first TLS lab simple and deterministic.

Recommended approach:
- use one public hostname
- use one Let’s Encrypt issuer model
- use HTTP-01 challenge flow through ingress
- issue one certificate successfully before adding complexity

This keeps validation clear and prepares naturally for renewal thinking later.

## Naming convention to follow
Use clear and professional names.

Recommended examples:
- hostname: `app1.apps.example.com`
- ClusterIssuer: `letsencrypt-prod`
- ClusterIssuer: `letsencrypt-staging` for initial safe testing
- TLS secret: `app1-tls-secret`

Keep names readable so troubleshooting and later operational reasoning remain clear.

## Definition of ready
The learner is ready to start this lab when:
- the hostname already resolves correctly
- the ingress route already works without TLS
- cert-manager installation strategy is known
- the learner is ready to think in terms of certificate lifecycle, not only endpoint access
- the environment is stable enough for ACME challenge validation
