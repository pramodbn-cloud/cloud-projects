# Validation Checks

## Purpose of this file
This file confirms whether the Zero-Trust AKS Security with mTLS + Azure API Management lab is complete and correct.

The goal is not only to verify that APIM is in front of AKS, but to confirm that the learner understands the trust chain and why this architecture is stronger than normal ingress exposure.

## Validation approach
For this lab, validation is based on:
- API edge architecture clarity
- client-to-APIM trust clarity
- APIM-to-backend mTLS clarity
- Key Vault and identity understanding
- comparison reasoning
- learner explanation ability

## Check 1 — The learner understands APIM as more than a proxy
Confirm that:
- the learner can explain APIM as a security and governance layer
- the learner understands that APIM is shaping API posture, not just forwarding requests

Microsoft’s APIM guidance supports this understanding strongly.

## Check 2 — The learner understands client-to-APIM trust
Confirm that:
- the learner can explain client certificate validation or equivalent edge trust controls
- the learner understands why zero-trust starts at the entry layer

This proves gateway-edge trust understanding.

## Check 3 — The learner understands APIM-to-backend mutual TLS
Confirm that:
- the learner can explain how APIM authenticates to the backend with a certificate
- the learner understands why the backend can be restricted to trust a known caller

This is one of the most important technical checks in the module.

## Check 4 — The learner understands Key Vault and managed identity in the trust model
Confirm that:
- the learner can explain why certificate and secret hygiene matters
- the learner understands why managed identity and Key Vault strengthen the design

This proves secure resource-access maturity.

## Check 5 — The learner can compare this with ordinary ingress + TLS
Confirm that:
- the learner can explain what a normal ingress design provides
- the learner can explain what this design adds
- the learner can explain why this is a specialty-grade upgrade rather than a routine change

This proves architecture-level comparison maturity.

## Check 6 — The learner understands identity and certificate roles separately
Confirm that:
- the learner can explain that certificates and tokens solve different trust concerns
- the learner can explain how APIM can combine them in a stronger API security posture

This proves deep security understanding.

## Check 7 — The learner understands why this module follows Folder 26
Confirm that:
- the learner can explain why a private enterprise platform is a strong base for this architecture
- the learner sees Folder 27 as the premium API edge security layer on top of Folder 26

This proves full-course coherence.

## Check 8 — You can explain why this is the strongest final module
This is the most important validation for this module.

The learner should now be able to explain:
- why APIM belongs in front of AKS in this pattern
- how mTLS is used in the architecture
- why Key Vault and managed identity matter
- why this is a zero-trust design
- why this is a benchmark-grade end module

If the learner can explain this clearly, the module is truly understood.