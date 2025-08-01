# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the AKS Ingress Basics lab.

In this module, the most common failures usually come from misunderstanding the controller requirement, misconfiguring the Service target, using the wrong ingress class pattern, or testing the ingress before the endpoint is actually ready. The goal is to strengthen runtime traffic reasoning, not only fix manifests.

---

## Common issue 1 — Ingress resource exists, but traffic does not work

### Symptoms
- the ingress object is present in the cluster
- external requests fail or do not reach the application
- the learner assumes ingress is broken
- the path from ingress to backend is unclear

### Likely cause
The most common cause is that the learner is treating ingress as self-executing. In reality, the ingress resource only defines intent; a controller must implement it.

### Fix
- confirm which ingress controller strategy is in use
- confirm the controller is healthy
- confirm the ingress class matches the controller expectation
- confirm the controller actually recognizes the ingress object

### Re-validation
After the fix:
- inspect the ingress again
- confirm that the controller and ingress class alignment is correct
- retest the external path

---

## Common issue 2 — The ingress controller is fine, but the Service target is wrong

### Symptoms
- ingress endpoint exists
- requests appear to reach the ingress layer
- backend response fails or times out
- the application is still unreachable

### Likely cause
The Service may be pointing to the wrong pods, wrong ports, or mismatched selectors.

### Fix
- inspect the Service definition carefully
- verify labels and selectors
- verify service port and targetPort alignment
- verify that the backend pods are actually serving on the expected port

### Re-validation
After the fix:
- validate the Service internally first
- only then retest through ingress

---

## Common issue 3 — Deprecated ingress-class pattern causes confusion

### Symptoms
- the ingress exists but is not being handled as expected
- the learner used old annotation-only class style
- examples from older Kubernetes material behave differently

### Likely cause
The ingress class pattern may be outdated. The StackSimplify course update specifically calls out the move away from deprecated annotation-only style and toward `spec.ingressClassName`.

### Fix
- inspect the ingress definition
- use `spec.ingressClassName` correctly
- verify the actual ingress classes present in the cluster
- align the ingress object with the controller implementation

### Re-validation
After the fix:
- confirm the ingress class is recognized
- confirm the controller now processes the ingress as expected

---

## Common issue 4 — External endpoint is tested too early

### Symptoms
- the learner applies the ingress and immediately tests it
- traffic fails even though the manifests look correct
- the endpoint or address is not yet stable

### Likely cause
Ingress readiness often depends on controller reconciliation and underlying load balancer or endpoint provisioning. This is real infrastructure behavior, not only YAML behavior.

### Fix
- inspect ingress status carefully
- confirm the controller has reconciled the resource
- wait for the external endpoint to become ready
- retest only when the endpoint is actually provisioned

### Re-validation
After the fix:
- confirm endpoint readiness explicitly
- retry the request against the correct address

---

## Common issue 5 — The learner understands the steps but not why ingress matters

### Symptoms
- the learner completes the lab but still sees ingress as only another resource object
- the value of centralized traffic entry feels weak
- the advanced-track transition does not feel meaningful

### Likely cause
The learner may still be thinking in deployment terms only, not platform-entry terms.

### Fix
Reframe ingress like this:
- Services expose applications inside the cluster
- ingress creates a controlled entry layer for external HTTP/HTTPS traffic
- this layer becomes the base for path routing, domain routing, TLS, and traffic governance
- ingress is a platform boundary, not just a Kubernetes object

### Re-validation
After the fix:
- confirm the learner can explain one strong reason to prefer ingress over exposing every workload individually with separate external services

---

## Troubleshooting mindset
While debugging this module, always ask:
- is the backend healthy first?
- is the Service correct?
- is there an ingress controller implementing the rule?
- is the ingress class aligned correctly?
- is the endpoint actually ready?
- do I understand the traffic chain from client to pod?

## Escalation rule
If the ingress path still feels broken:
1. validate pods  
2. validate Service  
3. validate controller presence  
4. validate ingress class alignment  
5. validate endpoint readiness  
6. retest only after each lower layer is confirmed  
7. prioritize traffic-path reasoning over YAML guessing  
