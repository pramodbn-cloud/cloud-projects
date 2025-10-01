# Validation Checks

## Purpose of this file
This file confirms whether the Ingress SSL with Let’s Encrypt lab is complete and correct.

The goal is not only to verify that HTTPS works, but to confirm that the learner understands the full trust chain from DNS name to certificate issuance to ingress TLS termination.

## Validation approach
For this lab, validation is based on:
- DNS and ingress readiness
- cert-manager readiness
- issuer correctness
- challenge-path success
- TLS secret creation
- HTTPS success
- learner explanation ability

## Check 1 — The hostname and ingress are already healthy before TLS
Confirm that:
- the hostname resolves correctly
- the ingress route works correctly over HTTP
- the backend application is healthy

This proves that the base route is valid before certificate issuance is attempted.

## Check 2 — cert-manager is healthy
Confirm that:
- cert-manager is installed and running
- the relevant controller components are healthy
- the learner understands cert-manager’s role in the lifecycle

This proves that the certificate automation engine is ready.

## Check 3 — The Issuer or ClusterIssuer is correct
Confirm that:
- the correct Let’s Encrypt environment is chosen
- the issuer configuration is structurally correct
- the solver path is appropriate for the ingress model being used

This proves that the certificate authority integration is configured correctly.

## Check 4 — Challenge validation succeeds
Confirm that:
- the ACME challenge path is reachable
- cert-manager successfully progresses through the validation lifecycle
- the learner understands that challenge reachability is a real ingress/runtime dependency

This is one of the most important technical validations in the module.

## Check 5 — The TLS secret is created correctly
Confirm that:
- the TLS secret exists
- the ingress references the intended secret
- the learner understands that the secret is the certificate material output of the lifecycle

This proves that certificate issuance completed successfully.

## Check 6 — HTTPS works for the intended hostname
Confirm that:
- the application is reachable over HTTPS
- the certificate is presented correctly
- the backend application still routes correctly underneath the TLS layer

This is the main technical success signal for the module.

## Check 7 — The learner can explain ingress TLS termination
Confirm that the learner can clearly explain:
- where TLS is terminated
- why the ingress secret matters
- how the ingress keeps routing behavior and certificate behavior connected

This proves that the learner understands the edge-security model, not only certificate issuance.

## Check 8 — The learner can explain why cert-manager + Let’s Encrypt matters
This is the most important validation for this module.

The learner should now be able to explain:
- why hostname routing had to come first
- why DNS correctness matters for certificate issuance
- how cert-manager automates the lifecycle
- why Let’s Encrypt validation depends on real hostname reachability
- why automated renewal is a major operational advantage

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the hostname resolves correctly
- cert-manager is healthy
- certificate issuance succeeds
- the TLS secret is created
- HTTPS works for the intended hostname
- the learner understands TLS as a platform trust layer

## If validation fails
If any validation step fails:
- validate DNS first
- validate ingress HTTP reachability next
- validate cert-manager health
- validate issuer and solver configuration
- use `troubleshooting.md` for common TLS and challenge issues
