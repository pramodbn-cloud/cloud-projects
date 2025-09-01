# Lab Guide — ExternalDNS with Azure DNS

## Lab objective
The objective of this lab is to help the learner understand and implement a basic ExternalDNS workflow with Azure DNS so that Kubernetes resources can automatically manage public DNS records.

This lab focuses on controller-driven DNS automation, Azure DNS integration, permission design, and the connection between ingress metadata and public DNS record creation. The goal is not to build the most customized ExternalDNS deployment possible, but to make the learner comfortable with how DNS automation works operationally in AKS.

## What you will build or configure
In this lab, you will prepare Azure DNS for automation, ensure ExternalDNS has the necessary Azure access model, deploy or review ExternalDNS in the cluster, and validate that a Kubernetes resource such as an ingress can result in a DNS record being created or updated automatically in Azure DNS.

This is the first true DNS-lifecycle automation workflow in the course.

## Why this lab matters
Without ExternalDNS, platform teams often have to translate cluster changes into DNS changes manually. That breaks flow, slows delivery, and creates room for DNS drift. ExternalDNS closes that gap by using Kubernetes as the source of truth for DNS intent.

ExternalDNS is designed to control DNS records dynamically through Kubernetes resources, and Azure DNS integrations require the controller to have permission to modify Azure DNS record sets. StackSimplify’s AKS guide also highlights that Azure can provide those permissions through either a Service Principal or a Managed Identity. 

## Estimated time
55 to 70 minutes

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
- a clear understanding of how ExternalDNS works with Azure DNS
- an authentication and permission model for DNS updates
- a Kubernetes resource that can drive Azure DNS record creation
- confidence in explaining the end-to-end DNS automation lifecycle

## Skills gained
- Understanding DNS automation in AKS platform design
- Connecting ingress or service metadata to Azure DNS record lifecycle
- Thinking about controller permissions as part of platform safety
- Preparing for domain-based ingress and TLS automation later

## Real-world relevance
In real AKS platforms, ExternalDNS is often one of the clearest signs of platform maturity because it reduces manual DNS work and ties external naming directly to cluster intent. It also forces teams to think properly about DNS authority, controller permissions, and automation boundaries. 

## Completion standard
A learner should not mark this lab complete until:
- the ExternalDNS concept is clear
- the Azure DNS permission model is understandable
- the controller-to-zone relationship is visible
- a DNS record is created or managed through Kubernetes intent
- validation confirms the automation flow end to end
