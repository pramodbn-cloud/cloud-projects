# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the ExternalDNS with Azure DNS lab.

The goal is to create one clear automation path where a Kubernetes resource expresses DNS intent and Azure DNS is updated automatically by ExternalDNS.

---

## Step 1 — Understand the ExternalDNS goal
Before deploying anything, understand what this module is trying to teach.

This lab is not about manually adding records to Azure DNS. It is about shifting DNS record lifecycle into a controller-driven model:

- Kubernetes expresses naming intent
- ExternalDNS detects that intent
- Azure DNS is reconciled automatically
- public naming follows cluster state

At the end of this lab, you should have:
- one authoritative Azure DNS zone
- one Azure identity model for DNS updates
- one ExternalDNS controller path
- one Kubernetes resource that results in an automated DNS record

## Step 2 — Reconfirm Azure DNS authority from Folder 11
Before introducing automation, verify that:
- the correct Azure DNS zone exists
- the zone scope matches the hostname plan for the lab
- Azure is authoritative for the delegated scope

This step matters because ExternalDNS can only automate records inside the zone Azure actually controls.

## Step 3 — Choose the ExternalDNS source object pattern
Decide what Kubernetes resource ExternalDNS will watch for this lab.

The most common learning pattern is:
- an ingress with hostname-related annotations or host rules

You may also use services depending on your chosen design, but ingress-based hostname flows usually connect more naturally to the later hostname-routing and TLS modules.

## Step 4 — Choose the Azure authentication model
Now choose how ExternalDNS will authenticate to Azure DNS.

Keep the lab design simple and consistent:
- either Service Principal, or
- Managed Identity

The StackSimplify Azure AKS ExternalDNS guide explicitly discusses both options and presents managed identity as the preferred current direction there. The ExternalDNS Azure tutorial also documents managed-identity-based approaches. 

At this stage, focus on:
- what identity the controller will use
- what Azure scope that identity needs
- why over-permissioning is dangerous

## Step 5 — Grant Azure DNS permissions
Grant the chosen identity the ability to modify the Azure DNS zone.

This is one of the most important control points in the module because it determines whether ExternalDNS can actually reconcile DNS records.

The learner should understand:
- the permission should be scoped appropriately
- the controller should not receive more Azure power than it needs
- DNS automation is only trustworthy when permissions are narrowly and intentionally assigned

## Step 6 — Deploy or review the ExternalDNS controller
Deploy ExternalDNS into the cluster or review an existing deployment intended for this purpose.

At this stage, confirm that:
- the controller runs successfully
- the Azure provider configuration is correct
- the zone scope and source object pattern are aligned with the lab design

The ExternalDNS project documents Azure as a supported provider and the StackSimplify guide specifically frames the deployment around Azure DNS update permissions. 

## Step 7 — Create or update the source ingress
Now create or update an ingress resource that expresses hostname intent inside the delegated Azure DNS scope.

Use a hostname that clearly belongs to the delegated zone from Folder 11, such as:
- `app1.apps.example.com`

This step matters because the ingress is now acting as both:
- a traffic-routing object, and
- a DNS-intent source for ExternalDNS

## Step 8 — Apply the ingress and inspect cluster state
Apply the ingress or source object and inspect:
- whether the object is accepted cleanly
- whether the hostname intent is visible as expected
- whether the ingress endpoint is ready or known

Do not jump immediately to DNS validation if the source object itself is not healthy.

## Step 9 — Inspect ExternalDNS reconciliation behavior
Now inspect the ExternalDNS controller behavior.

At this stage, the learner should look for:
- whether ExternalDNS noticed the source object
- whether it identified the intended hostname
- whether it attempted to create or update the appropriate Azure DNS record

This is one of the most important learning moments in the module because it shows reconciliation rather than one-time scripting.

## Step 10 — Verify the record in Azure DNS
Now verify that the DNS record exists in the Azure DNS zone.

Confirm:
- record name correctness
- record type and target correctness
- that the record belongs to the intended delegated scope

This step proves that cluster intent has become Azure DNS state.

## Step 11 — Verify public resolution behavior
Now test the hostname through DNS lookup.

The learner should confirm:
- the hostname resolves
- the result reflects the intended ingress-facing endpoint
- public DNS behavior now matches what the cluster expressed

This is the key external proof that DNS automation is functioning.

## Step 12 — Compare automated DNS to manual DNS management
Now reflect on why this matters.

Ask:
- what manual step did ExternalDNS remove?
- how would this help when many ingress objects or frequent changes exist?
- why is this safer than manual DNS edits only when identity and scope are designed well?

This step helps the learner move from technical success into platform reasoning.

## Step 13 — Review reconciliation as an operating model
Now explain the lifecycle in plain language:

- the zone is authoritative in Azure
- the cluster exposes a hostname through a Kubernetes resource
- ExternalDNS detects that hostname intent
- ExternalDNS uses Azure permissions to update the zone
- the public hostname resolves according to cluster state

If the learner can explain this clearly, the module is doing its real job.

## Step 14 — Reflect on ExternalDNS as platform maturity
Pause and think beyond the manifests.

In this module, ExternalDNS means:
- DNS lifecycle becomes part of platform automation
- public naming can stay synchronized with cluster intent
- manual DNS drift is reduced
- ingress hostname design becomes much more scalable

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- Azure DNS authority is already in place
- an Azure identity model is chosen for DNS updates
- ExternalDNS is deployed or understood as the DNS controller
- a Kubernetes source object expresses hostname intent
- Azure DNS now contains an automatically managed record
- the learner understands the reconciliation path from cluster intent to public DNS

## Step 15 — Prepare for hostname-based routing
Before moving to the next module, understand what changes next.

The next module is **Domain Name Based Routing**. That means the learner will now move from path-based differentiation into hostname-based differentiation, using real DNS names that ExternalDNS can help manage at scale.

This is the bridge from DNS automation into hostname-driven ingress architecture.

---

## Implementation notes
- keep the first ExternalDNS scenario simple and deterministic
- ensure DNS authority is correct before adding automation
- keep Azure permissions narrow and intentional
- use one very clear hostname example for learning
- focus on reconciliation logic before optimization

## End-of-implementation summary
In this lab, you:
- reconfirmed Azure DNS authority
- chose an Azure authentication model for DNS updates
- scoped DNS permissions to the controller
- deployed or reviewed ExternalDNS
- used a Kubernetes resource as DNS intent
- validated automatic Azure DNS record creation
- practiced the first real DNS-lifecycle automation pattern in the AKS phase

You are now ready to validate whether the ExternalDNS lifecycle is clean, correct, and explainable.
