# Lab Guide — Zero-Trust AKS Security with mTLS + Azure API Management

## Lab objective
The objective of this lab is to help the learner understand and implement a **zero-trust API exposure architecture for AKS** using Azure API Management, mutual TLS, Key Vault, and identity-aware access patterns.

This lab focuses on:
- APIM as secure API front door
- client certificate validation
- APIM-to-backend mutual TLS
- certificate and secret management through Key Vault
- backend protection and trust-chain design
- centralized governance and observability

The goal is not to create a simple published API. The goal is to help the learner understand how to design a **secure enterprise API edge for AKS**.

## What you will build or configure
In this lab, you will design or implement:
- Azure API Management as the API entry layer
- secure client access using mTLS and/or identity-aware API controls
- secure backend calls from APIM to AKS-backed services using client certificates
- Key Vault-backed certificate handling
- centralized API and security monitoring assumptions

This creates the most security-specialized module in the repository.

## Why this lab matters
Microsoft documents that APIM can require client certificates from callers and can also authenticate to backend services using client certificates. Microsoft also documents using managed identity from APIM to securely access Azure resources such as Key Vault. This makes APIM a strong control point for zero-trust API security patterns.

## Estimated time
80 to 110 minutes

## Lab file reading order
Follow the files in this order:

1. `architecture-flow.md`
2. `prerequisites.md`
3. `implementation-steps.md`
4. `validation-checks.md`
5. `troubleshooting.md`
6. `cleanup.md`

## Expected final outcome
By the end of this lab, the learner should have:
- a clear zero-trust AKS API security model
- a working or clearly modeled APIM + mTLS architecture
- a strong understanding of where certificates are validated and used
- confidence in explaining this design in enterprise architecture terms

## Skills gained
- Advanced API security architecture
- APIM + AKS integration thinking
- mTLS trust-chain reasoning
- Key Vault and managed identity integration for secure certificate handling
- Zero-trust exposure design for AKS workloads

## Real-world relevance
This is exactly the kind of topic that signals high-level cloud security and platform architecture understanding. It goes far beyond “deploy an API” and into enterprise-grade **secure API front door design**. Microsoft’s APIM documentation and architecture guidance support this pattern strongly.

## Completion standard
A learner should not mark this lab complete until:
- the trust chain is clear
- APIM’s role is clear
- mTLS usage is understandable on both relevant paths
- the learner can explain why this is a zero-trust architecture rather than just API publishing