# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Zero-Trust AKS Security with mTLS + Azure API Management lab.

In this module, the most common failures usually come from confusing standard TLS with mTLS, treating APIM as a reverse proxy only, or failing to distinguish edge trust from backend trust. The goal is to strengthen zero-trust architecture reasoning, not only fix gateway settings.

---

## Common issue 1 — The learner confuses TLS with mutual TLS

### Symptoms
- the learner says the API is already secure because HTTPS exists
- mTLS seems redundant
- the zero-trust value feels unclear

### Likely cause
The learner may be treating all certificate-based transport as the same thing.

### Fix
Reframe the difference like this:
- TLS usually proves the server to the client
- mTLS adds client-side or caller-side certificate authentication into the relationship
- in this module, mTLS is used to strengthen trust, not only encrypt transport

### Re-validation
After the fix:
- confirm the learner can explain one trust difference between normal TLS and mutual TLS

---

## Common issue 2 — The learner sees APIM as only a forwarding layer

### Symptoms
- the architecture feels like “APIM in front of ingress”
- the governance and security value is weak
- the module feels like an extra hop rather than a stronger design

### Likely cause
The learner may not yet understand APIM as the API control plane.

### Fix
Reframe APIM like this:
- it validates access
- it applies policy
- it centralizes API governance
- it can secure both the incoming client path and the outgoing backend path

### Re-validation
After the fix:
- confirm the learner can explain one governance advantage and one backend trust advantage of APIM in this design

---

## Common issue 3 — The learner understands client mTLS but not backend mTLS

### Symptoms
- the gateway-side trust is clear
- the APIM-to-backend certificate path feels unnecessary or confusing
- backend protection feels incomplete

### Likely cause
The learner may still be thinking only about client exposure and not about service-to-service trust.

### Fix
Reframe backend mTLS like this:
- the backend should trust a known caller, not just any reachable caller
- APIM can present a client certificate to the backend
- backend mTLS makes the backend trust path explicit

### Re-validation
After the fix:
- confirm the learner can explain why backend mTLS is a stronger model than relying only on network path trust

---

## Common issue 4 — The learner treats Key Vault as optional decoration

### Symptoms
- APIM and certificates are configured conceptually
- Key Vault feels like a side integration
- certificate hygiene is weak

### Likely cause
The learner may still be thinking in one-time setup terms rather than lifecycle management terms.

### Fix
Reframe Key Vault like this:
- this module is about governed trust
- certificates and secrets are part of that trust lifecycle
- managed storage and managed access reduce unsafe handling patterns

### Re-validation
After the fix:
- confirm the learner can explain one reason Key Vault strengthens the architecture beyond simple certificate storage

---

## Common issue 5 — The learner does not understand why this is the final benchmark module

### Symptoms
- the module feels like “APIM plus AKS”
- its premium nature is not yet obvious
- the final capstone weight feels low

### Likely cause
The learner may still be thinking in product terms rather than architecture maturity terms.

### Fix
Reframe the course ending like this:
- earlier modules built runtime and delivery strength
- Folder 26 built private enterprise platform strength
- Folder 27 adds premium zero-trust API security above that foundation
- this is the strongest specialized trust and exposure pattern in the course

### Re-validation
After the fix:
- confirm the learner can explain why this module is a stronger benchmark than ordinary ingress or plain HTTPS setup

---

## Troubleshooting mindset
While debugging this module, always ask:
- am I clear on client trust vs backend trust?
- am I clear on TLS vs mTLS?
- do I understand APIM as security plane, not only proxy?
- do I understand why Key Vault and managed identity matter?
- can I explain why this design is zero-trust instead of only “secured”?

## Escalation rule
If the zero-trust story still feels weak:
1. separate the client-to-APIM and APIM-to-backend paths  
2. restate TLS versus mTLS  
3. restate APIM’s governance role  
4. restate Key Vault’s certificate-hygiene role  
5. compare with standard ingress again  
6. prioritize trust-chain reasoning over product configuration details