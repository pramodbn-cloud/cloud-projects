# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the ACR with AKS lab.

The goal is to create one clear private-image supply path where an image is stored in ACR, AKS is authorized to pull it, and a workload runs successfully from that source.

---

## Step 1 — Understand the image-supply goal
Before building or pushing anything, understand what this module is trying to teach.

This lab is not only about creating a registry and pushing an image. It is about creating a trusted runtime supply path:

- the image has a controlled home
- AKS knows how to authenticate to that home
- workloads can start reliably from that private source
- registry trust becomes part of the platform design

At the end of this lab, you should have:
- one private registry
- one image stored there
- one AKS integration path
- one workload running from that image

## Step 2 — Reconfirm AKS cluster identity model
Before touching the registry, inspect the AKS identity posture.

The learner should understand:
- AKS commonly uses managed identity
- the kubelet/agent-pool identity is the one that normally needs pull access
- registry pull success depends on that identity being authorized correctly

Microsoft’s AKS integration docs describe AcrPull assignment to the managed identity when you attach ACR.

## Step 3 — Create or review the ACR registry
Create a new ACR registry or review an existing one for the lab.

At this stage, focus on:
- registry naming clarity
- whether the registry is the intended trusted source for the cluster
- how the image repositories inside it will be named

This is where the registry becomes part of the platform supply chain.

## Step 4 — Build or select the sample image
Now prepare a lightweight sample image.

Keep the first scenario simple and deterministic:
- one small application
- one repository path
- one clear tag

This keeps validation easy and makes image-pull troubleshooting much cleaner.

## Step 5 — Log in to ACR and push the image
Now authenticate to ACR and push the sample image.

At this stage, confirm that:
- the image exists in ACR
- the repository path is correct
- the tag is readable and intentional

Azure’s ACR authentication docs describe `az acr login` for registry access, and Azure best-practices guidance emphasizes clear repository/tagging discipline.

## Step 6 — Attach ACR to AKS or confirm equivalent role assignment
Now integrate the cluster with the registry.

Recommended standard path:
- attach the ACR to AKS using the supported attach-acr workflow, or
- confirm that the kubelet/managed identity already has AcrPull on the registry

Microsoft’s AKS integration docs explain that attach-acr configures the appropriate AcrPull role for the managed identity.

This is one of the most important learning moments in the module because it is the actual trust bridge between cluster and registry.

## Step 7 — Verify the image reference format
Now construct the image reference exactly as the workload will use it.

At this stage, verify:
- login server / registry endpoint correctness
- repository path correctness
- tag correctness

The learner should understand that many pull failures are really image-reference failures, not AKS failures.

## Step 8 — Create or update the workload to use the ACR image
Now create or update a deployment so that the pod uses the private image from ACR.

Keep the first scenario simple:
- one namespace
- one deployment
- one clearly referenced image

The goal is to validate the trust path, not introduce unrelated deployment complexity.

## Step 9 — Apply the workload and inspect startup behavior
Apply the workload and inspect:
- whether the deployment is accepted
- whether the pod schedules successfully
- whether image pull succeeds
- whether the container starts cleanly

Do not assume success only because the deployment exists. Validate actual runtime image retrieval.

## Step 10 — Review the pod events if needed
Now inspect pod status and events carefully.

The learner should focus on:
- whether the image was pulled
- whether authentication to ACR worked
- whether any image reference errors exist

This is the key runtime visibility moment in the module.

## Step 11 — Compare private-registry-backed execution to unmanaged public sourcing
Now reflect on why this matters.

Ask:
- why is a private trusted registry stronger than ad hoc image sourcing?
- why does managed-identity-based pull feel cleaner than distributing pull secrets?
- how does this help platform governance and supply-chain trust?

This step moves the learner from technical success into platform reasoning.

## Step 12 — Review tagging and image-version discipline
Now look beyond the first successful pull.

Azure’s ACR best-practices guidance emphasizes tagging and versioning strategy for clean registry usage. The learner should understand:
- image tags influence rollout clarity
- ambiguous tags increase operational risk
- reliable deployment depends on reliable image identity

## Step 13 — Explain the image-supply lifecycle end to end
Now explain the flow in plain language:

- the image is built
- the image is pushed to ACR
- AKS is authorized to pull from ACR
- the deployment references the private image
- the cluster pulls it through its identity
- the pod starts successfully

If the learner can explain this clearly, the module is doing its real job.

## Step 14 — Reflect on ACR as supply-chain trust
Pause and think beyond the registry object.

In this module, ACR with AKS means:
- workload images come from a governed private source
- AKS uses identity-based authorization rather than fragile manual secrets
- image identity becomes part of deployment quality
- runtime success depends on a clean registry-to-cluster trust path

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- an ACR registry exists and contains the sample image
- AKS is integrated with that registry or has equivalent AcrPull authorization
- the workload references the ACR image correctly
- the pod can pull and start successfully
- the learner understands identity-based registry access

## Step 15 — Prepare for pipeline-driven deployment
Before moving to the next module, understand what changes next.

The next module is **Azure DevOps with AKS**. That means the learner will now connect build, push, and deploy into one pipeline-driven lifecycle where ACR becomes the registry handoff point between CI and runtime.

This is the bridge from trusted image supply into end-to-end deployment automation.

---

## Implementation notes
- keep the first ACR scenario simple and deterministic
- validate registry presence and identity access separately
- use clear tags and avoid confusing image naming
- inspect pod events rather than guessing at pull failures
- focus on supply-chain trust, not just successful image storage

## End-of-implementation summary
In this lab, you:
- reviewed the AKS identity model
- created or reviewed an ACR registry
- built and pushed a sample image
- integrated AKS with ACR using the supported trust path
- deployed a workload from the private image
- validated runtime image pull behavior
- practiced the first true private-image supply-chain pattern in the AKS phase

You are now ready to validate whether the ACR-to-AKS lifecycle is clean, correct, and explainable.
