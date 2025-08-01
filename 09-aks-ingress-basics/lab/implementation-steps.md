# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the AKS Ingress Basics lab.

The goal is to create one clear ingress-based traffic path that takes an external request and delivers it to a backend application running inside AKS.

---

## Step 1 — Understand the ingress goal
Before applying any manifests, understand what this module is trying to teach.

This lab is not just about creating an ingress YAML file. It is about learning the runtime chain that makes ingress meaningful:

- a workload runs in pods
- a Service exposes it internally
- an ingress controller provides the traffic-entry implementation
- an ingress resource defines how external traffic reaches the service

At the end of this lab, you should have:
- one backend application
- one internal service
- one working ingress path
- one clear explanation of how traffic reaches the application

## Step 2 — Confirm cluster access and current state
Use kubectl to confirm that:
- the current cluster context is correct
- nodes are ready
- the target namespace is understood
- the cluster is healthy enough for the lab

This step matters because ingress troubleshooting becomes confusing if the cluster state itself is not stable.

## Step 3 — Confirm or choose the ingress-controller approach
Decide whether your lab is using:
- the AKS application routing add-on, or
- an unmanaged NGINX ingress-controller installation

For most current AKS learning flows, the managed application routing path is the preferred recommendation. AKS also documents unmanaged ingress-controller approaches for specific scenarios and troubleshooting contexts.

The important thing is that the learner understands one key truth:
an ingress resource does not route traffic by itself; a controller must exist to implement it.

## Step 4 — Deploy the sample application
Deploy a simple backend application into the cluster.

Keep the application straightforward. The goal of this lab is traffic architecture, not application complexity.

At this stage, focus on:
- successful pod creation
- predictable service port behavior
- simple HTTP response for validation later

This keeps the ingress behavior easy to verify.

## Step 5 — Create the internal Kubernetes Service
Create a Service for the application.

This service should provide internal access to the pods and should be stable enough for the ingress resource to target.

The learner must understand this clearly:
the ingress sends traffic to the Service, not directly to the pods.

This distinction becomes very important in later advanced routing and troubleshooting modules.

## Step 6 — Validate the application internally before using ingress
Before introducing ingress, verify that:
- the pods are healthy
- the Service resolves correctly inside the cluster context
- the backend application is actually serving traffic

Do not skip this step. If the backend is already broken, ingress troubleshooting will become misleading.

## Step 7 — Create the ingress resource
Now define the ingress resource that routes traffic to the internal service.

Use the current pattern with `spec.ingressClassName` rather than relying on deprecated annotation-only ingress class style, matching the updated course guidance for the ingress sections.

At this stage, keep the ingress definition simple:
- one backend service
- one predictable rule
- minimal complexity

The goal is to validate the basic chain, not advanced routing yet.

## Step 8 — Apply the ingress and inspect its state
Apply the ingress resource and inspect:
- ingress object creation
- associated address or external endpoint readiness
- whether the ingress controller has recognized the resource

Do not rush to browser testing immediately. First confirm that the cluster sees the ingress resource correctly.

## Step 9 — Wait for the ingress entry point to stabilize
Depending on the controller model, the ingress may need time for:
- controller reconciliation
- load balancer provisioning
- external endpoint readiness

Current AKS ingress implementations are still dependent on cluster networking and controller reconciliation, so this readiness phase is part of the real runtime behavior.

The learner should understand that ingress is not only declarative — it also has infrastructure readiness behavior underneath.

## Step 10 — Test the ingress path externally
Once the ingress endpoint is ready, test the application through the ingress layer.

Validate that:
- the external request reaches the ingress entry point
- the ingress forwards traffic correctly
- the intended service is reached
- the backend application responds as expected

This is one of the most important learning moments in the module because it confirms the full chain from external request to internal workload.

## Step 11 — Compare ingress flow to direct service exposure
Now reflect on why ingress is useful.

Ask:
- how is this different from exposing every application directly with a LoadBalancer service?
- why does a centralized ingress layer help later routing and TLS patterns?
- why is this a better foundation for multi-application traffic control?

This step helps the learner move from technical success into platform reasoning.

## Step 12 — Review the runtime path end to end
Now explain the flow in plain language:

- the client sends the request
- the ingress entry point receives it
- the ingress controller enforces the ingress rule
- traffic is forwarded to the Service
- the Service forwards traffic to the pods
- the application returns the response

If the learner can explain this chain clearly, the module is doing its real job.

## Step 13 — Reflect on ingress as a platform layer
Pause and think beyond the manifest.

In this module, ingress means:
- external application access is centralized
- routing logic is separated from application deployment
- services stay internal while traffic entry becomes managed
- later DNS and TLS layers now have a clean place to connect

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- a backend workload is running
- a Kubernetes Service exposes it internally
- an ingress controller strategy is active
- an ingress resource is applied correctly
- external traffic reaches the intended backend through ingress
- the learner understands the end-to-end request path

## Step 14 — Prepare for advanced routing
Before moving to the next module, understand what changes next.

The next module focuses on **Ingress Context Path Routing**. That means the learner will go from one simple ingress-to-service mapping into multi-service routing based on URL paths.

This is where ingress begins to evolve from an entry mechanism into a traffic-routing layer.

---

## Implementation notes
- keep the first ingress scenario simple and deterministic
- validate the backend before validating ingress
- never forget that a controller is required
- treat ingress readiness as both a Kubernetes and infrastructure event
- focus on traffic understanding first, optimization later

## End-of-implementation summary
In this lab, you:
- confirmed AKS cluster readiness
- deployed a simple backend workload
- created an internal Kubernetes Service
- introduced an ingress controller strategy
- created an ingress resource
- validated external-to-internal traffic flow
- practiced the first true runtime traffic architecture pattern in the course

You are now ready to validate whether the ingress lifecycle is clean, correct, and explainable.
