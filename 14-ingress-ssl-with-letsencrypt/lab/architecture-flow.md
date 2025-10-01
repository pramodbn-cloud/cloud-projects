# Architecture Flow

## Purpose of this file
This file explains the logical security and certificate flow used in the Ingress SSL with Let’s Encrypt lab before implementation begins.

This module is about certificate-driven trust at the ingress boundary — how a public hostname is validated, how a certificate is issued and stored, and how the ingress controller uses that certificate to serve HTTPS traffic.

## High-level architecture view
The workflow begins with a working hostname-based ingress route. That route already exposes the application publicly. TLS now adds the trust and encryption layer.

At a high level, the flow looks like this:

- a public hostname already resolves to the ingress endpoint
- cert-manager runs inside the cluster as a certificate lifecycle controller
- an Issuer or ClusterIssuer defines how certificates should be obtained from Let’s Encrypt
- an ingress or certificate resource requests a certificate for the hostname
- Let’s Encrypt validates control of the hostname, often through an HTTP-01 challenge served via ingress
- cert-manager receives the signed certificate and stores it as a Kubernetes TLS secret
- the ingress uses that TLS secret to serve HTTPS traffic securely

This turns a reachable hostname into a trusted HTTPS endpoint.

## Component roles

- **Client / External User** — connects to the application through HTTPS  
- **Azure DNS** — resolves the hostname to the ingress endpoint  
- **Ingress Endpoint** — the public entry point serving the application  
- **Ingress Resource** — defines both routing and TLS association  
- **cert-manager** — manages certificate request, issuance, storage, and renewal lifecycle  
- **Issuer / ClusterIssuer** — defines the certificate authority configuration, such as Let’s Encrypt  
- **Let’s Encrypt** — the certificate authority issuing the public certificate  
- **Kubernetes TLS Secret** — stores the issued certificate and private key for ingress use  

## End-to-end flow

1. A hostname resolves to the ingress endpoint.  
2. cert-manager is available in the cluster.  
3. A Let’s Encrypt Issuer or ClusterIssuer is defined.  
4. An ingress or certificate resource requests a certificate for the hostname.  
5. Let’s Encrypt validates ownership of the hostname, often through HTTP-01 challenge flow.  
6. cert-manager stores the issued certificate in a TLS secret.  
7. The ingress references that secret and terminates TLS for incoming HTTPS requests.  
8. Clients now access the application securely over HTTPS.  

## Dependency awareness
This module depends on:
- Folder 11 for Azure DNS authority
- Folder 12 for automated DNS alignment
- Folder 13 for hostname-based ingress routing
- a working ingress endpoint and public hostname

This module also prepares the learner for:
- more production-grade ingress security
- secure application exposure practices
- understanding how naming, traffic routing, and trust combine at the platform edge

## Operational view
From a platform-engineering perspective, the learner should pay attention to:
- hostname correctness
- ingress readiness
- challenge-path reachability
- issuer configuration correctness
- TLS secret lifecycle
- renewal as an operational process, not just first issuance

These are the qualities that make TLS automation reliable in real environments.

## What to keep in mind before implementation
Before starting the steps:
- TLS depends on the hostname being correct and reachable
- cert-manager automates lifecycle, but it still depends on valid ingress and DNS state
- the certificate secret is an output of the lifecycle, not the starting point
- challenge validation is a real runtime path and should be treated that way
- think in terms of trust lifecycle, not only HTTPS enablement
