# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the Ingress Context Path Routing lab.

The goal is to create one ingress entry point that routes traffic to multiple backend services according to URL paths.

---

## Step 1 — Understand the routing goal
Before applying any routing manifests, understand what this module is trying to teach.

This lab is not about exposing multiple services in different random ways. It is about showing that one ingress entry layer can make traffic decisions based on request paths.

At the end of this lab, you should have:
- multiple backend applications
- multiple internal Services
- one ingress resource with multiple path rules
- one clear explanation of how the path determines the backend

## Step 2 — Confirm cluster, controller, and current ingress state
Use kubectl to confirm that:
- the AKS cluster context is correct
- nodes are healthy
- the ingress-controller strategy from Folder 09 is still active
- the ingress layer is stable enough to add multi-service rules

This step matters because path-routing troubleshooting becomes harder if the base ingress path is already unstable.

## Step 3 — Deploy or confirm multiple backend applications
Deploy or reuse at least two simple backend applications inside the cluster.

Keep them easy to distinguish so validation becomes obvious later.

Examples:
- app1 returns an `app1` response
- app2 returns an `app2` response

The goal is not business logic complexity. The goal is route clarity.

## Step 4 — Create or confirm one Service per backend
Each backend application should have its own Kubernetes Service.

Validate that:
- each Service selects the correct pods
- the ports are correct
- the applications are independently reachable through their Services in an internal validation pattern

This is critical because ingress path rules do not target pods directly. They target Services.

## Step 5 — Validate the backends internally first
Before applying the multi-path ingress resource, confirm that each backend is healthy on its own.

Do not use ingress as the first point of diagnosis. If one backend is already misconfigured internally, the path-routing test will produce misleading results.

At this stage, verify:
- backend A works behind Service A
- backend B works behind Service B

## Step 6 — Design the path map
Now define the routing story clearly.

For a clean learning lab, use a simple pattern such as:
- `/app1` → service A
- `/app2` → service B

This step matters because readable paths make both validation and later troubleshooting much easier.

## Step 7 — Create the ingress resource with multiple path rules
Define one ingress resource that includes multiple path rules.

Keep the design simple:
- one shared ingress entry point
- one ingress class
- two backend services
- clear path mappings

Use the current class field style with `spec.ingressClassName` as aligned with the updated course guidance for ingress modules.

## Step 8 — Apply the ingress and inspect its state
Apply the ingress resource and inspect:
- whether the object is accepted by the cluster
- whether the rule set is visible as expected
- whether the ingress controller recognizes the multi-path design

Do not test externally yet if the rule set itself looks incomplete or unclear.

## Step 9 — Confirm the ingress endpoint is stable
Because the lab is now adding complexity to the ingress path, confirm that:
- the shared ingress endpoint still resolves correctly
- controller reconciliation has completed
- no obvious error exists before external testing begins

This is an important operator habit: validate controller and endpoint state before blaming routing logic.

## Step 10 — Test each path externally
Now test the ingress endpoint with the defined paths.

For example:
- request the shared endpoint with `/app1`
- request the shared endpoint with `/app2`

Validate that:
- the path is recognized
- the intended backend responds
- the responses differ in the expected way

This is the most important technical validation moment in the module.

## Step 11 — Compare multi-service ingress to multiple public services
Now reflect on the design.

Ask:
- why is one shared ingress endpoint often more manageable than exposing every workload separately?
- how does this pattern help when many services exist?
- how does this prepare the cluster for later DNS and TLS patterns?

This step helps the learner move into real platform reasoning instead of stopping at successful routing.

## Step 12 — Review the request-selection logic end to end
Now explain the routing chain in plain language:

- the client sends a request to the shared ingress endpoint
- the request path is inspected
- the ingress controller matches the correct path rule
- the rule points to the correct Service
- the Service forwards traffic to the correct backend pods
- the response comes back through the same ingress layer

If the learner can explain this chain clearly, the module is doing its real job.

## Step 13 — Reflect on path routing as a traffic-control layer
Pause and think beyond the manifest.

In this module, path-based routing means:
- one front door can serve multiple workloads
- external traffic structure can be centralized
- backend services remain independent internally
- later domain and TLS logic now have a stronger traffic-management base

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- multiple backend workloads are running
- each backend has its own Service
- one ingress resource defines multiple path rules
- the shared ingress endpoint is stable
- each external path reaches the intended backend
- the learner understands path-based backend selection

## Step 14 — Prepare for DNS and naming strategy
Before moving to the next module, understand what changes next.

The next module begins **Domain Delegation to Azure DNS**. That means the learner will move from path-based differentiation to domain ownership and DNS-managed naming, which is a major step toward more production-like external exposure.

This is the bridge from route structure into DNS-driven ingress identity.

---

## Implementation notes
- keep the first path-routing lab simple and deterministic
- always validate backends before ingress rules
- prefer very clear path names during learning
- treat the ingress endpoint as shared infrastructure, not only a manifest target
- focus on route selection logic before later security and naming layers

## End-of-implementation summary
In this lab, you:
- confirmed cluster and ingress-controller readiness
- deployed or reused multiple backend workloads
- exposed each workload with its own Service
- created one ingress resource with multiple path rules
- validated multi-service routing behind one ingress endpoint
- practiced the first real multi-application traffic-engineering pattern in the AKS phase

You are now ready to validate whether the context-path routing lifecycle is clean, correct, and explainable.
