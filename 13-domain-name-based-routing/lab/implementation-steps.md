# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the Domain Name Based Routing lab.

The goal is to create one ingress layer that routes different hostnames to different backend services using Azure-controlled DNS and ingress host rules.

---

## Step 1 — Understand the hostname-routing goal
Before applying any manifests, understand what this module is trying to teach.

This lab is not only about changing path rules into host rules. It is about shifting the routing model so that:
- public DNS names represent application identity
- ingress uses the hostname to select the backend
- one shared ingress layer can still support multiple applications
- DNS and routing logic now work together more tightly

At the end of this lab, you should have:
- multiple backend applications
- multiple internal Services
- one or more ingress host rules
- one clear explanation of how hostname determines backend selection

## Step 2 — Reconfirm Azure DNS authority and ExternalDNS readiness
Before configuring ingress host rules, verify that:
- Azure DNS is authoritative for the delegated zone
- the chosen hostnames belong to that zone
- ExternalDNS is deployed or the DNS record management path is understood

This step matters because hostname routing is not only an ingress problem. It is also a DNS correctness problem.

## Step 3 — Deploy or confirm multiple backend applications
Deploy or reuse at least two simple backend applications inside the cluster.

As in Folder 10, keep them easy to distinguish.

Examples:
- app1 returns a clearly identifiable response
- app2 returns a clearly identifiable response

This keeps hostname-based validation unambiguous later.

## Step 4 — Create or confirm one Service per backend
Each backend application should have its own Service.

Validate that:
- each Service selects the correct pods
- ports are correct
- the backend applications are independently healthy behind their Services

As before, ingress will route to Services, not directly to pods.

## Step 5 — Define the hostname map
Now define the routing story clearly.

For a clean learning lab, use a pattern such as:
- `app1.apps.example.com` → service A
- `app2.apps.example.com` → service B

This makes the relationship between DNS name and backend very easy to validate and explain.

## Step 6 — Create the ingress resource with host rules
Define one ingress resource that contains multiple hostname rules.

Keep the design simple:
- one ingress class
- one ingress endpoint
- one hostname per backend
- minimal complexity

At this stage, focus on host-based separation rather than adding extra path complexity unless needed for a later extension.

## Step 7 — Apply the ingress and inspect cluster state
Apply the ingress resource and inspect:
- whether the object is accepted by the cluster
- whether the host rules are visible as expected
- whether the ingress controller recognizes the rule set

Do not jump immediately to browser validation if the ingress object itself is not healthy.

## Step 8 — Confirm DNS record creation or alignment
Now verify that the required DNS records exist for the chosen hostnames.

Depending on your lab design:
- ExternalDNS may create them automatically, or
- you may review the expected record state if the automation is modeled conceptually

At this stage, confirm:
- each hostname exists in Azure DNS
- each hostname points to the intended ingress-facing endpoint

This is the key bridge between DNS and ingress.

## Step 9 — Wait for resolution and endpoint readiness
Now allow for:
- ingress endpoint readiness if needed
- DNS propagation visibility if records were newly created or changed

The learner should understand that hostname-based routing depends on both routing rules and public naming state becoming visible together.

## Step 10 — Test each hostname externally
Now test the hostnames individually.

Validate that:
- requests to `app1.apps.example.com` reach backend A
- requests to `app2.apps.example.com` reach backend B
- the responses differ in the expected and clearly identifiable way

This is the most important technical validation moment in the module.

## Step 11 — Compare hostname routing to path routing
Now reflect on the design difference.

Ask:
- why might different public hostnames be cleaner than `/app1` and `/app2` for many applications?
- how does this affect user-facing identity and ownership?
- why does this make later TLS management more natural?

This step helps the learner move from pure routing success into real platform reasoning.

## Step 12 — Review the hostname-selection logic end to end
Now explain the flow in plain language:

- the client resolves the hostname in Azure DNS
- the request reaches the shared ingress endpoint
- the ingress controller inspects the requested host
- the matching host rule selects the correct Service
- the Service forwards traffic to the corresponding pods
- the response returns through the same ingress path

If the learner can explain this clearly, the module is doing its real job.

## Step 13 — Reflect on hostname routing as a production-style pattern
Pause and think beyond the manifests.

In this module, hostname-based routing means:
- applications gain clearer external identity
- routing becomes aligned with real DNS names
- TLS and certificate boundaries become cleaner later
- platform teams can separate apps logically while still centralizing ingress control

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- multiple backend workloads are running
- each workload has its own Service
- Azure DNS hostnames exist for each application
- one ingress resource contains host-based routing rules
- each hostname reaches the intended backend
- the learner understands how DNS and ingress combine to select the service

## Step 14 — Prepare for TLS
Before moving to the next module, understand what changes next.

The next module is **Ingress SSL with Let’s Encrypt**. That means the learner will now take the hostname-based routing layer and make it production-safer by enabling HTTPS and certificate automation.

This is the bridge from public naming into secure public exposure.

---

## Implementation notes
- keep the first hostname-routing lab simple and deterministic
- validate DNS correctness and ingress correctness separately
- prefer very clear hostnames during learning
- make backend responses visually or textually distinct
- focus on hostname-to-service selection before adding TLS complexity

## End-of-implementation summary
In this lab, you:
- reconfirmed Azure DNS authority and DNS automation readiness
- deployed or reused multiple backend workloads
- exposed each workload through its own Service
- created host-based ingress rules
- aligned hostnames with the ingress endpoint
- validated hostname-driven backend selection
- practiced the first production-style public identity routing pattern in the AKS phase

You are now ready to validate whether the domain-name-based routing lifecycle is clean, correct, and explainable.
