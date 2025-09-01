# Lab Guide — Domain Delegation to Azure DNS

## Lab objective
The objective of this lab is to help the learner understand and implement the DNS ownership flow required to use Azure DNS for ingress-related application naming.

This lab focuses on Azure DNS zones, registrar-side delegation, name server authority, and the relationship between DNS ownership and later ingress hostname patterns. The goal is not to build full record automation yet, but to make the learner comfortable with how DNS control moves into Azure before ExternalDNS is introduced.

## What you will build or configure
In this lab, you will create or review an Azure DNS public zone, identify the Azure name servers assigned to it, and map how domain or subdomain delegation from a registrar or existing DNS provider should point authority to Azure DNS.

You will also connect this DNS ownership model back to ingress so the learner can see why later hostname-based routing depends on this step.

## Why this lab matters
A public IP or ingress endpoint is not enough for clean platform exposure. Real environments need DNS authority and predictable naming. Without delegation, Azure DNS cannot serve as the trusted public DNS source for the domain, which blocks clean integration with later DNS automation and hostname-driven ingress.

Microsoft’s documentation makes this explicit: to use Azure DNS for a custom domain, the domain must first be delegated to Azure DNS, and only then can records be managed in that Azure DNS zone.

## Estimated time
45 to 60 minutes

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
- a clear understanding of Azure DNS zone ownership
- a DNS delegation design for a domain or subdomain
- awareness of how registrar changes and Azure DNS interact
- confidence in explaining why DNS delegation comes before ExternalDNS and hostname routing

## Skills gained
- Understanding Azure DNS zone delegation flow
- Thinking in terms of DNS authority rather than only record creation
- Connecting registrar-managed domains to Azure platform needs
- Preparing for later automated DNS and hostname-based ingress design

## Real-world relevance
In real AKS platforms, DNS delegation is usually the moment where networking, platform engineering, and public naming strategy meet. It defines who is authoritative for records, and that decision affects ingress naming, automation, certificates, and operational troubleshooting later. The StackSimplify AKS learning path correctly puts this module before ExternalDNS and domain-based routing.

## Completion standard
A learner should not mark this lab complete until:
- the concept of Azure DNS authority is clear
- the DNS zone and delegation model are understandable
- the learner can explain how registrar-side changes connect to Azure DNS
- validation confirms that the naming-ownership flow is correct
