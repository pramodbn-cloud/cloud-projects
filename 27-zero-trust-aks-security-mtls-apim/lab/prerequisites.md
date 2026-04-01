# Prerequisites

## Purpose of this file
This file defines everything that must already be ready before starting the Zero-Trust AKS Security with mTLS + Azure API Management lab.

This module depends on APIM readiness, AKS exposure understanding, certificate concepts, and high-level security architecture maturity.

## Required account access
You should have working access to:
- Azure
- Azure API Management
- Azure Key Vault
- an AKS cluster or a clearly modeled AKS backend service
- Azure networking and DNS if the backend is protected privately
- the ability to configure certificates and access policies

## Required tools
The following should be available:

- Azure CLI
- kubectl
- a terminal such as PowerShell or Bash
- a code editor for manifests, APIM policy/config references, and documentation
- certificate handling readiness for test or modeled mTLS scenarios

## Required permissions
You should be able to:
- configure or inspect API Management
- configure backend settings and policies in APIM
- upload or reference certificates as required
- use or inspect Key Vault integration
- inspect AKS ingress/backend configuration
- inspect logs or monitoring data for validation

## Required prior understanding
Before starting this module, the learner should already understand:
- ingress and TLS from earlier folders
- private AKS landing-zone design from Folder 26
- AKS authentication and policy governance concepts
- ACR, AKS, and Azure DevOps delivery flow
- the difference between authentication and authorization

## Required environment state
Before starting:
- APIM should already exist or be easy to provision for the lab
- an AKS backend workload should already exist or be easy to model
- the learner should understand whether the backend is public, internal, or privately protected
- certificate trust flow should be conceptually understood before configuration begins

## Security architecture strategy recommendation
Keep the first scenario **high-trust and understandable**.

Recommended approach:
- one APIM instance
- one AKS backend
- one client-certificate validation story
- one APIM-to-backend client-certificate trust story
- one Key Vault-backed certificate management assumption

This keeps the architecture premium without becoming unreadable.

## Important technical note
Microsoft documents two different but related certificate patterns in APIM:
- client certificate authentication **to APIM**
- client certificate authentication **from APIM to the backend**

This distinction is central to the module and should be kept explicit from the start.

## Definition of ready
The learner is ready to start this lab when:
- APIM access is ready
- AKS backend context is ready
- certificate concepts are understood at a basic level
- the learner is ready to think in trust-chain terms, not only API-exposure terms