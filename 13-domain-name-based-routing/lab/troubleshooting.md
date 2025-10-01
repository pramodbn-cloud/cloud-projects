# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Domain Name Based Routing lab.

In this module, the most common failures usually come from DNS and ingress being validated together instead of separately, hostnames pointing outside the delegated zone, incorrect host-rule-to-service mapping, or assuming that host-based routing is working when DNS is actually the layer that is broken. The goal is to strengthen combined DNS-and-routing reasoning, not only fix manifests.

---

## Common issue 1 — The ingress looks correct, but the hostname does not resolve

### Symptoms
- the ingress object exists
- the host rules look correct
- requests by hostname fail before reaching the application
- the learner assumes ingress is broken

### Likely cause
The most common cause is that DNS is not yet correct:
- the hostname record may not exist
- the record may point to the wrong endpoint
- the hostname may not belong inside the delegated zone
- propagation may not be complete yet

### Fix
- validate Azure DNS records independently
- confirm the hostname belongs to the delegated zone
- confirm the record target points to the ingress-facing endpoint
- separate DNS-layer validation from ingress-layer validation

### Re-validation
After the fix:
- confirm the hostname resolves correctly
- only then retest ingress-based application routing

---

## Common issue 2 — The hostname resolves, but the wrong backend is returned

### Symptoms
- DNS works
- the request reaches the ingress layer
- the response comes from the wrong backend
- multiple hostnames appear to serve the same application unexpectedly

### Likely cause
The host-rule mapping may be wrong, or the backend responses may not be distinct enough to validate confidently.

### Fix
- inspect each host rule carefully
- verify that each hostname maps to the correct Service
- make backend responses clearly distinct
- retest each hostname individually

### Re-validation
After the fix:
- confirm that each hostname now produces a clearly correct backend-specific response

---

## Common issue 3 — ExternalDNS created records, but the routing still feels inconsistent

### Symptoms
- DNS records exist
- the learner sees automation working
- traffic results still feel unstable or confusing

### Likely cause
The learner may be mixing DNS success with ingress success. ExternalDNS can create correct records while the ingress rule set is still wrong, or the ingress endpoint may still be reconciling.

### Fix
- validate DNS creation separately
- validate ingress rule correctness separately
- verify that the ingress endpoint itself is healthy
- test each layer independently before combining them

### Re-validation
After the fix:
- confirm that both DNS and ingress rule layers are individually healthy before judging end-to-end behavior

---

## Common issue 4 — Hostnames are outside the intended Azure DNS scope

### Symptoms
- the learner uses hostnames that feel reasonable
- DNS automation or DNS lookup does not behave as expected
- some names appear structurally unrelated to the delegated zone

### Likely cause
The hostname pattern may not actually fall under the Azure-controlled delegated scope from Folder 11.

### Fix
- compare every hostname to the delegated zone carefully
- keep the first learning scenario fully inside one clear Azure-controlled naming boundary
- avoid mixing in unrelated or higher-level domain names

### Re-validation
After the fix:
- confirm that every application hostname is a child of the delegated Azure DNS zone

---

## Common issue 5 — The learner still does not understand why hostname routing is more production-like

### Symptoms
- the technical flow works
- the learner still prefers to think only in terms of paths
- the architectural value of host-based routing feels weak

### Likely cause
The learner may still be thinking at small-demo scale rather than public application scale.

### Fix
Reframe hostname routing like this:
- different applications often deserve different public identities
- certificates align more naturally to distinct hostnames
- ownership and user-facing clarity improve
- DNS, TLS, and routing all become easier to reason about together

### Re-validation
After the fix:
- confirm the learner can explain one clear real-world advantage of `app1.apps.example.com` and `app2.apps.example.com` over only using `/app1` and `/app2`

---

## Troubleshooting mindset
While debugging this module, always ask:
- does the hostname resolve first?
- does the hostname belong in the delegated zone?
- does the record point to the correct ingress-facing endpoint?
- does the ingress host rule map to the correct Service?
- are backend responses distinct enough to validate clearly?
- am I separating DNS problems from ingress-routing problems?

## Escalation rule
If the routing still feels broken:
1. validate backend A  
2. validate backend B  
3. validate Service A  
4. validate Service B  
5. validate DNS record A  
6. validate DNS record B  
7. validate ingress host rules  
8. retest one hostname at a time  
9. prioritize DNS-and-ingress layer separation over repeated YAML edits  
