# Validation Checks

## Purpose of this file
This file confirms whether the AKS Application Routing lab is complete and correct.

The goal is not only to verify that the add-on works, but to confirm that the learner understands why the old HTTP Application Routing topic had to be modernized, how the new add-on behaves, and how it compares to earlier self-managed ingress patterns.

## Validation approach
For this lab, validation is based on:
- platform-currency correctness
- cluster prerequisite correctness
- add-on correctness
- ingress-path correctness
- managed-versus-self-managed understanding
- learner explanation ability

## Check 1 — The learner understands the modernization from HTTP Application Routing to Application Routing
Confirm that:
- the learner knows the original HTTP Application Routing add-on is retired
- the learner knows the modern replacement is the Application Routing add-on
- the learner can explain why the course must use the current model now

This is one of the most important course-quality validation points.

## Check 2 — The cluster meets the add-on prerequisites
Confirm that:
- the AKS cluster uses managed identity
- the learner understands this as a hard prerequisite
- the environment is actually compatible with the add-on model

Microsoft documents managed identity as required for Application Routing.

## Check 3 — The Application Routing add-on is active or clearly validated
Confirm that:
- the add-on is enabled or correctly reviewed
- the learner can identify the managed ingress-controller layer created by AKS
- the learner understands that this is a managed NGINX-based pattern

Microsoft documents managed NGINX ingress as part of the add-on.

## Check 4 — A sample ingress route works through the managed path
Confirm that:
- the ingress resource is recognized
- the workload is exposed correctly
- the learner can see that routing still works conceptually the same, even though controller ownership differs

This is the main technical success signal for the module.

## Check 5 — Azure DNS integration value is understood
Confirm that:
- the learner understands that the add-on supports Azure DNS zone integration
- the learner can explain why that matters operationally
- the learner sees this as part of the Azure-native value proposition

This proves that the learner understands more than traffic entry alone.

## Check 6 — Managed versus self-managed ingress trade-offs are understood
Confirm that the learner can explain:
- what AKS manages here that earlier modules required the team to manage more directly
- why managed routing can reduce operational burden
- why self-managed ingress may still remain useful in some scenarios

This is the main platform-architecture understanding check.

## Check 7 — Add-on constraints are understood
Confirm that:
- the learner understands the add-on has prerequisites and boundaries
- the learner knows this is a design choice, not a universal default for every scenario

This proves operational realism.

## Check 8 — You can explain why this module matters in production
This is the most important validation for this module.

The learner should now be able to explain:
- why this topic had to be modernized from the retired add-on
- what the Application Routing add-on does
- how it differs operationally from self-managed ingress
- why Azure-native teams may choose it
- why this module belongs after the earlier manual ingress/DNS lessons

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the modernized topic is understood correctly
- the add-on is working or clearly validated
- the ingress route is exposed through the managed path
- the learner understands the trade-off between managed and self-managed ingress
- the learner is ready to move into AKS identity and RBAC governance

## If validation fails
If any validation step fails:
- revisit the retirement-versus-modernization distinction
- re-check cluster managed-identity readiness
- re-check the add-on status
- re-check the sample ingress route
- use `troubleshooting.md` for common managed-routing issues
