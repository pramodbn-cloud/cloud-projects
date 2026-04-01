# Architecture Flow

## Purpose of this file
This file explains the architecture and trust flow used in the Zero-Trust AKS Security with mTLS + Azure API Management lab before implementation begins.

This module is about **trust chaining at the API edge** — how clients are validated, how the API gateway is controlled, how the backend is protected, and how certificates and identities participate in the trust model.

## High-level architecture view
The workflow begins with a client that wants to access an API exposed by a workload running on AKS. In a normal setup, the client may reach an ingress endpoint directly over HTTPS. In this module, the architecture becomes more deliberate:

- API Management becomes the front door
- clients can be authenticated using certificates and/or token-based identity
- APIM validates access at the gateway
- APIM authenticates to the backend using a client certificate for mutual TLS
- backend trust is narrowed so that only APIM is intended to call it
- certificate lifecycle is managed more safely through Key Vault-integrated patterns

This creates a **zero-trust API chain** instead of a simple ingress exposure model.

## Core trust layers

### 1. Client to APIM
Microsoft documents that APIM can secure access to APIs using client certificates and mTLS at the gateway. APIM can validate the certificate presented by the connecting client and evaluate certificate properties.

### 2. APIM as policy and security control plane
APIM is not only a reverse proxy. Microsoft’s API Management guidance positions it as a place for API security, policy, transformation, and governance.

### 3. APIM to backend mutual TLS
Microsoft documents that APIM can authenticate to a backend service using a client certificate. This means the backend can be configured to trust APIM as a known caller through mTLS rather than only bearer trust or open network trust.

### 4. Key Vault and managed identity
Microsoft documents that APIM can use a managed identity to securely access Azure resources protected by Microsoft Entra ID, such as Azure Key Vault. This is important because zero-trust architecture should not depend on manually scattered certificate and secret handling.

### 5. AKS backend protection
The backend service in AKS is no longer treated as a general public target. Instead, the exposure model is:
- controlled gateway
- controlled certificate trust
- potentially private or restricted backend network design
- policy and monitoring at the edge

## End-to-end conceptual flow

1. A client attempts to call an API  
2. Azure API Management receives the request  
3. APIM validates the caller using configured security controls such as mTLS and/or identity-aware policy  
4. APIM applies policy and governance logic  
5. APIM calls the AKS backend using client-certificate authentication for mTLS  
6. The backend trusts APIM as an allowed caller  
7. Observability and governance occur at the API edge and platform layers  

## Why this is a specialty-grade architecture
This module is benchmark-grade because it combines:
- API gateway architecture
- certificate-led trust
- mutual TLS in both directional roles
- Key Vault-backed certificate hygiene
- managed identity
- secure backend exposure patterns
- zero-trust reasoning instead of perimeter-only reasoning

That is an advanced security architecture story, not just an API publishing story.

## What to keep in mind before implementation
Before starting the steps:
- TLS and mTLS are not the same thing
- APIM is both a security and governance layer
- backend trust should be explicit, not assumed
- certificate management hygiene matters
- this module is about **trusted API posture**, not only API reachability