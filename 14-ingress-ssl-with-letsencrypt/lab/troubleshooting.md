# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Ingress SSL with Let’s Encrypt lab.

In this module, the most common failures usually come from trying to issue a certificate before DNS and HTTP routing are truly ready, misconfiguring the issuer or solver, misunderstanding challenge-path behavior, or assuming that a certificate secret should exist before the lifecycle has completed. The goal is to strengthen trust-lifecycle reasoning, not only fix manifests.

---

## Common issue 1 — Certificate issuance fails because the hostname path is not ready

### Symptoms
- cert-manager starts processing the request
- the certificate is not issued
- challenge resources appear to stall or fail
- the learner assumes cert-manager is broken

### Likely cause
The most common cause is that the hostname and ingress path were not truly ready:
- DNS may not resolve correctly yet
- the ingress route may not work properly over HTTP
- the challenge path may not be reachable through ingress

### Fix
- validate the hostname resolution first
- validate normal HTTP ingress reachability next
- confirm that the requested hostname matches the ingress route exactly
- treat the challenge path as a real networked path, not an internal-only detail

### Re-validation
After the fix:
- re-check challenge progression
- confirm the certificate lifecycle now advances successfully

---

## Common issue 2 — cert-manager is installed, but the Issuer or ClusterIssuer is wrong

### Symptoms
- cert-manager is healthy
- certificate requests fail
- the issuer is not usable
- the learner is unsure whether the problem is Kubernetes, ingress, or Let’s Encrypt

### Likely cause
The issuer may point to the wrong environment, use the wrong solver configuration, or be mismatched to the ingress/controller setup.

### Fix
- inspect the issuer configuration carefully
- confirm whether staging or production was intended
- confirm the solver path is aligned with ingress
- simplify to one hostname and one clean issuer path if needed

### Re-validation
After the fix:
- confirm the issuer is now healthy and usable
- retry the certificate request flow

---

## Common issue 3 — The TLS secret never appears

### Symptoms
- the ingress references a TLS secret
- the learner expects the secret to exist immediately
- no secret is visible yet
- the learner assumes ingress is broken

### Likely cause
The TLS secret is the output of successful certificate issuance. If the ACME lifecycle has not completed, the secret will not be available yet.

### Fix
- inspect the certificate request lifecycle
- inspect challenge and order progression
- confirm DNS and ingress challenge reachability
- treat the secret as the end-state output, not the starting state

### Re-validation
After the fix:
- confirm the certificate issuance completes
- verify that the TLS secret is then created

---

## Common issue 4 — HTTPS works, but the learner does not understand where TLS is actually applied

### Symptoms
- the endpoint is reachable over HTTPS
- the learner knows the feature works
- the trust model still feels vague
- the location of certificate usage is unclear

### Likely cause
The learner may be focusing on browser-level success rather than ingress-level architecture.

### Fix
Reframe the flow like this:
- Azure DNS resolves the hostname
- ingress receives the request
- ingress presents the certificate from the TLS secret
- TLS is terminated at ingress
- traffic is then routed to the backend Service

### Re-validation
After the fix:
- confirm the learner can explain where trust is applied and why the TLS secret belongs at the ingress boundary

---

## Common issue 5 — The learner sees TLS as “done once” rather than a lifecycle

### Symptoms
- the certificate was issued successfully
- the learner now sees the problem as solved permanently
- renewal and long-term operation are not considered

### Likely cause
The learner may still be thinking in static configuration terms rather than operational lifecycle terms.

### Fix
Reframe TLS like this:
- certificate issuance is only the beginning
- certificates expire
- cert-manager matters because it automates renewal and secret refresh
- the real value is not only obtaining the certificate, but sustaining trust over time

### Re-validation
After the fix:
- confirm the learner can explain one operational advantage of cert-manager beyond first-time issuance

---

## Troubleshooting mindset
While debugging this module, always ask:
- does the hostname resolve correctly?
- does the HTTP ingress route work before TLS?
- is cert-manager healthy?
- is the issuer configured correctly?
- is the ACME challenge path reachable?
- am I treating the TLS secret as a lifecycle output rather than a manual prerequisite?

## Escalation rule
If the TLS flow still feels broken:
1. validate DNS  
2. validate HTTP ingress  
3. validate cert-manager health  
4. validate issuer configuration  
5. validate challenge-path reachability  
6. validate secret creation only after issuance should have completed  
7. retest HTTPS only after lower layers are known-good  
8. prioritize trust-chain reasoning over repeated ingress edits  
