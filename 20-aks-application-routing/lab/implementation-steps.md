# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the AKS Application Routing lab.

The goal is to create one clear managed-ingress path using the AKS Application Routing add-on and to understand how that differs from earlier self-managed ingress patterns.

---

## Step 1 — Understand the managed-routing goal
Before enabling any add-on, understand what this module is trying to teach.

This lab is not only about turning on an AKS feature. It is about understanding a shift in platform ownership:

- earlier ingress modules taught how routing works in depth
- this module teaches how AKS can manage more of that ingress-controller lifecycle for you
- the goal is to understand when that trade-off is useful

At the end of this lab, you should have:
- one managed-routing path
- one sample ingress scenario
- one clear comparison between managed and self-managed ingress approaches

## Step 2 — Reconfirm current platform reality
Before doing any setup, explicitly acknowledge the current platform direction:

- the old HTTP Application Routing add-on is retired
- the modern pattern is the Application Routing add-on
- AKS now documents Application Routing as the recommended ingress-controller path

This step matters because course quality depends on using the current platform model rather than outdated implementation patterns.

## Step 3 — Reconfirm cluster managed-identity readiness
Now inspect the AKS cluster and confirm that it uses managed identity.

Microsoft documents managed identity as a prerequisite for the Application Routing add-on. Do not continue until this is clear.

## Step 4 — Enable or review the Application Routing add-on
Enable the Application Routing add-on on the AKS cluster, or review an already-enabled configuration intended for the lab.

At this stage, focus on:
- whether the add-on is active
- what system components it creates
- how the managed ingress-controller path appears in the cluster

The learner should treat this as a platform capability, not only as a namespace object list.

## Step 5 — Inspect the managed ingress-controller layer
Now inspect the cluster resources created for application routing.

Microsoft documents that the Application Routing add-on uses managed NGINX ingress and also supports configuration through the `NginxIngressController` CRD.

At this stage, the learner should observe:
- what AKS is managing on their behalf
- where the controller system lives
- how this differs from an explicitly self-installed ingress controller

## Step 6 — Review Azure DNS integration potential
Now revisit the DNS side of the story.

The learner should understand:
- the add-on can integrate with Azure DNS
- this is one of the operational advantages of the managed model
- DNS support is part of what makes the add-on valuable in Azure-native platform design

Microsoft documents Azure DNS public/private zone management as part of the Application Routing add-on capability set.

## Step 7 — Create or review a sample ingress resource
Now deploy or review a simple ingress resource that will use the managed routing layer.

Keep the first scenario simple:
- one backend workload
- one service
- one ingress path or hostname
- minimal complexity

The goal is to validate the managed-routing behavior, not to create a complicated traffic map.

## Step 8 — Apply the ingress and inspect behavior
Apply the ingress resource and inspect:
- whether the managed controller recognizes it
- whether the ingress object becomes active
- whether routing behavior appears healthy

Do not jump directly to browser testing until the cluster-side behavior looks stable.

## Step 9 — Validate external exposure
Now validate the exposure path.

Confirm:
- the ingress endpoint is reachable
- the backend service is being routed correctly
- the learner can identify where the managed routing layer is adding value operationally

This is the main technical success signal for the module.

## Step 10 — Compare the operational ownership model
Now compare:
- the earlier self-managed ingress-controller pattern
- the managed Application Routing pattern

The learner should focus on:
- who owns controller lifecycle
- who owns configuration surface
- where Azure integration is stronger
- where flexibility may be different

This is the core platform-engineering reasoning moment of the module.

## Step 11 — Review add-on constraints and fit
Now think about where this add-on fits well and where it may not.

Microsoft documents specific boundaries such as:
- managed identity requirement
- Azure DNS zone count limits
- some configuration and customization boundaries in the managed model

The learner should understand that managed routing is a design choice, not a universal answer.

## Step 12 — Explain the managed-routing lifecycle end to end
Now explain the flow in plain language:

- AKS enables the Application Routing add-on
- AKS manages the ingress-controller layer
- the learner applies an ingress resource
- the managed routing layer exposes the backend workload
- Azure-native integrations such as DNS fit more naturally into this model

If the learner can explain this clearly, the module is doing its real job.

## Step 13 — Reflect on managed routing as a platform choice
Pause and think beyond the feature enablement.

In this module, Application Routing means:
- ingress remains conceptually the same
- but controller ownership shifts more toward AKS
- Azure integration becomes more direct
- the platform operator chooses between flexibility and managed convenience deliberately

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- the learner understands that HTTP Application Routing is retired
- the Application Routing add-on is enabled or clearly understood
- the cluster’s managed-identity requirement is satisfied
- a sample ingress route works through the managed path
- the learner can compare managed and self-managed ingress meaningfully

## Step 14 — Prepare for cluster access governance
Before moving to the next module, understand what changes next.

The next module is **AKS Authentication with Azure AD and Kubernetes RBAC**. That means the learner will now shift from runtime traffic-management options into cluster access and authorization governance.

This is the bridge from managed routing choice into identity and access control at the cluster layer.

---

## Implementation notes
- treat this module as a modernization of an older course topic
- keep the routing scenario simple so the comparison stays clear
- focus on operational ownership differences
- do not lose the ingress fundamentals already learned earlier
- think in terms of managed platform components, not only add-on enablement

## End-of-implementation summary
In this lab, you:
- updated the older HTTP Application Routing concept to the current Application Routing add-on model
- reconfirmed the managed-identity prerequisite
- enabled or reviewed the managed routing add-on
- applied a sample ingress scenario through the managed path
- validated external exposure
- compared managed and self-managed ingress operationally
- practiced the first true AKS-managed routing pattern in the course

You are now ready to validate whether the managed-routing lifecycle is clean, correct, and explainable.
