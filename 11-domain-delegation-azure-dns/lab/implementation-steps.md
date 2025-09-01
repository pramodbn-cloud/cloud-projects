# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the Domain Delegation to Azure DNS lab.

The goal is to create one clear DNS authority path that makes Azure DNS the authoritative home for a chosen domain or subdomain so later ingress-related records can be managed there.

---

## Step 1 — Understand the DNS delegation goal
Before creating anything in Azure, understand what this module is trying to teach.

This lab is not only about adding a DNS zone. It is about changing where DNS authority lives.

At the end of this lab, you should understand:
- why an Azure DNS zone alone is not enough
- how Azure DNS becomes authoritative
- how registrar or parent-zone delegation connects to Azure
- why this step must happen before ExternalDNS and hostname-based ingress automation

## Step 2 — Choose the delegation scope
Decide whether you are modeling:
- a full domain delegation, or
- a subdomain delegation

For learning and platform-isolation reasons, a subdomain is often the cleaner approach.

Example:
- keep `example.com` at the current provider
- delegate `apps.example.com` to Azure DNS

This makes later AKS naming easier while limiting blast radius.

## Step 3 — Create the Azure DNS public zone
Create the public DNS zone in Azure for the domain or subdomain chosen.

At this stage, focus on:
- zone name correctness
- resource-group placement
- visibility of the assigned Azure name servers

Azure DNS creates the authoritative zone structure, but Azure is not yet the live authority until delegation is updated at the registrar or parent zone. Microsoft’s custom domain guidance is explicit that delegation must happen first.

## Step 4 — Record the Azure-assigned name servers
After the zone is created, identify the authoritative Azure name servers assigned to the zone.

These name servers are the values that will be used in the delegation change.

This step is critical because the delegation handoff depends on using the exact authoritative name server set assigned by Azure.

## Step 5 — Identify the current DNS authority point
Now identify where the delegation must be changed.

This will usually be:
- the domain registrar, or
- the provider currently hosting the parent zone

The learner should understand this clearly:
Azure DNS does not “pull” authority automatically. The parent authority must be updated to point to Azure.

## Step 6 — Update the delegation at the registrar or parent zone
Now perform or model the actual delegation step.

This means:
- updating the domain’s or subdomain’s NS records at the current authority point
- replacing or configuring the authoritative name servers so they point to Azure’s assigned name servers

For a root domain, this is usually done at the registrar.  
For a subdomain, this may be done inside the parent DNS zone.

This is the real authority-transfer moment of the module.

## Step 7 — Understand propagation and authority transition
After the delegation update, allow time for DNS propagation and authority change to be visible.

The learner should understand that delegation is not always visible everywhere instantly. Public DNS caches and resolver behavior can affect when the new authority appears consistently.

This is a real operational characteristic of DNS, not a misconfiguration by default.

## Step 8 — Verify the delegated authority
Now verify whether Azure DNS is becoming authoritative for the delegated domain scope.

Use:
- portal review
- DNS lookup tools
- resolver checks
- name server authority checks if available

The goal is to confirm not only that the zone exists in Azure, but that the internet’s DNS chain now points to Azure for that delegated scope.

## Step 9 — Explain what Azure can do now that it could not do before
Now reflect on the difference between “zone exists in Azure” and “Azure DNS is authoritative.”

Ask:
- before delegation, could Azure DNS really answer live public queries for this domain scope?
- after delegation, can Azure now serve records that other systems can rely on?
- why does this matter for ingress hostnames and future automation?

This is one of the most important learning moments in the module.

## Step 10 — Connect delegation to future ingress records
Now connect the DNS authority story back to AKS.

Explain that later modules will use this delegated Azure DNS zone to:
- create records for ingress endpoints
- automate DNS record lifecycle
- support hostname-based routing
- support certificate and TLS flows

Without delegation, those later steps would not be authoritative in the live DNS chain.

## Step 11 — Reflect on subdomain delegation as a platform boundary
Now think about this in platform terms.

A delegated subdomain can create a clean separation such as:
- central domain remains with one team
- application subdomain is delegated to the platform team in Azure
- ingress-related automation operates safely within that delegated boundary

This is often more realistic than moving an entire corporate root domain for one AKS platform use case.

## Step 12 — Reflect on DNS ownership as part of platform engineering
Pause and think beyond the portal steps.

In this module, DNS delegation means:
- naming authority becomes explicit
- Azure becomes the trusted record owner for the delegated scope
- ingress-related naming can now be managed from Azure
- later automation has a real DNS authority layer to work against

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- an Azure DNS zone exists for the chosen domain or subdomain
- the Azure-assigned name servers are known
- the delegation point at the registrar or parent zone is understood
- delegation has been updated or modeled clearly
- the learner understands the difference between zone creation and DNS authority
- the learner can explain why later ingress automation depends on this step

## Step 13 — Prepare for ExternalDNS automation
Before moving to the next module, understand what changes next.

The next module is **ExternalDNS with Azure DNS**. That means the learner will now move from manual or conceptual DNS ownership into controller-driven DNS record lifecycle management inside the delegated Azure DNS zone.

This is the bridge from DNS authority into DNS automation.

---

## Implementation notes
- a subdomain delegation is often the cleanest learning path
- always record the exact Azure name servers carefully
- treat propagation as a real runtime characteristic
- keep the DNS authority model simple and unambiguous
- focus on ownership transfer before thinking about automation

## End-of-implementation summary
In this lab, you:
- chose a DNS delegation scope
- created an Azure DNS public zone
- captured Azure’s authoritative name servers
- identified the registrar or parent-zone delegation point
- updated or modeled the delegation handoff to Azure
- connected Azure DNS authority to future ingress-hostname automation

You are now ready to validate whether the DNS delegation lifecycle is clean, correct, and explainable.
