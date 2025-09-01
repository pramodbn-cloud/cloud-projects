# Validation Checks

## Purpose of this file
This file confirms whether the ExternalDNS with Azure DNS lab is complete and correct.

The goal is not only to verify that a record appears in Azure DNS, but to confirm that the learner understands the full automation chain from Kubernetes intent to public DNS state.

## Validation approach
For this lab, validation is based on:
- Azure DNS authority correctness
- controller identity correctness
- permission-scope correctness
- source-object correctness
- Azure DNS record creation success
- public resolution success
- learner explanation ability

## Check 1 — Azure DNS authority is correct
Confirm that:
- the correct Azure DNS zone exists
- Azure is authoritative for the intended delegated scope
- the chosen hostname belongs inside that delegated zone

This proves the controller is working against the correct DNS ownership boundary.

## Check 2 — The ExternalDNS authentication model is clear
Confirm that:
- the learner knows whether Service Principal or Managed Identity is being used
- the identity being used is the one intended for DNS updates
- the learner can explain why that identity exists

This proves that DNS automation is not being treated as anonymous or magical.

## Check 3 — Azure permissions are present and appropriately scoped
Confirm that:
- the chosen identity has the required Azure DNS modification rights
- the scope is aligned to the intended DNS zone or appropriate resource boundary
- the learner can explain why over-permissioning would be risky

This proves that the automation is both functional and governed.

## Check 4 — ExternalDNS is healthy and watching the correct source type
Confirm that:
- the ExternalDNS controller is running
- it is watching the intended resource type, such as ingress
- it can observe the hostname-bearing Kubernetes resource correctly

This proves that the controller side of the automation chain is healthy.

## Check 5 — The source ingress or service is correct
Confirm that:
- the Kubernetes resource expresses the intended hostname
- the hostname belongs inside the delegated Azure DNS scope
- the object is otherwise healthy enough to be a valid automation source

This proves that the automation intent is being expressed correctly inside the cluster.

## Check 6 — The Azure DNS record is created or updated automatically
Confirm that:
- the record appears in Azure DNS
- the name matches the expected hostname
- the target matches the expected ingress-facing endpoint or service exposure pattern

This is the main technical success signal for the module.

## Check 7 — Public DNS resolution reflects the automated state
Confirm that:
- the hostname resolves publicly
- the resolution points to the intended destination
- the learner can explain how the record got there without manual record entry

This proves the automation chain is externally visible and real.

## Check 8 — The learner can explain why ExternalDNS matters
This is the most important validation for this module.

The learner should now be able to explain:
- why DNS authority had to come first
- what ExternalDNS watches
- how Kubernetes intent becomes Azure DNS state
- why Azure permissions matter
- why this is better than frequent manual DNS updates in a scalable platform

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- Azure DNS authority is correct
- the ExternalDNS controller has the right identity and permissions
- a hostname-bearing Kubernetes resource triggers record creation
- the record is visible in Azure DNS and resolves publicly
- the learner understands DNS automation as a platform maturity step

## If validation fails
If any validation step fails:
- re-check Azure DNS authority first
- re-check the identity and permission scope
- re-check the source ingress/service object
- re-check controller health and reconciliation behavior
- use `troubleshooting.md` for common ExternalDNS issues
