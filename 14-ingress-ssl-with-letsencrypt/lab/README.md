# Lab Guide — Ingress SSL with Let’s Encrypt

## Lab objective
The objective of this lab is to help the learner implement HTTPS for a hostname-based AKS ingress flow using cert-manager and Let’s Encrypt.

This lab focuses on certificate issuance, challenge validation, TLS secret creation, ingress attachment, and secure public application access. The goal is not to build a highly customized PKI model, but to make the learner comfortable with one of the most common production-style certificate automation patterns used in Kubernetes platforms.

## What you will build or configure
In this lab, you will prepare or confirm a hostname-based ingress route, deploy or review cert-manager, define a ClusterIssuer or Issuer for Let’s Encrypt, request a certificate through ingress, and validate that HTTPS works with a trusted certificate.

This creates the first true secure-public-exposure workflow in the course.

## Why this lab matters
Public naming without TLS leaves an application operationally incomplete. Teams need not only correct DNS and correct routing, but also encryption in transit and trusted certificates that can be renewed without brittle manual work.

Microsoft documents cert-manager as the certificate automation tool for Kubernetes on AKS, and cert-manager guidance explains how certificates are issued, stored as Kubernetes TLS secrets, and renewed automatically. This is exactly the kind of lifecycle automation that makes ingress security operationally sustainable. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/aks/app-routing-dns-ssl?utm_source=chatgpt.com))

## Estimated time
60 to 75 minutes

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
- a hostname-based ingress route ready for TLS
- a certificate issuer flow for Let’s Encrypt
- a certificate stored as a Kubernetes TLS secret
- HTTPS working on the chosen hostname
- confidence in explaining the full certificate lifecycle

## Skills gained
- Understanding ingress TLS architecture in AKS
- Connecting DNS, ingress, and certificate issuance together
- Thinking in terms of certificate lifecycle rather than only certificate files
- Preparing for more secure production-style ingress operations

## Real-world relevance
In real AKS platforms, HTTPS is usually non-negotiable for public applications. A robust ingress design therefore needs hostname routing, DNS automation, and certificate automation working together. Let’s Encrypt and cert-manager provide one of the clearest and most common ways to achieve that in Kubernetes environments. ([cert-manager.io](https://cert-manager.io/docs/tutorials/getting-started-aks-letsencrypt/?utm_source=chatgpt.com))

## Completion standard
A learner should not mark this lab complete until:
- the TLS concept is clear
- certificate issuance is understood
- the ingress is serving HTTPS correctly
- validation confirms that the certificate and route lifecycle work end to end
