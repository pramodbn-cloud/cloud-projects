# Validation Checks

## Purpose of this file
This file confirms whether the Domain Delegation to Azure DNS lab is complete and correct.

The goal is not only to verify that an Azure DNS zone exists, but to confirm that the learner understands and can validate the transfer of DNS authority to Azure.

## Validation approach
For this lab, validation is based on:
- zone creation correctness
- authoritative name server awareness
- delegation-point correctness
- authority-transition understanding
- future ingress-use readiness
- learner explanation ability

## Check 1 — The Azure DNS zone exists and is correct
Confirm that:
- the public DNS zone exists in Azure
- the zone name matches the intended domain or subdomain
- the learner can explain why this specific zone scope was chosen

This proves that the Azure-side DNS home has been created properly.

## Check 2 — The Azure authoritative name servers are known
Confirm that:
- the learner has identified the exact Azure-assigned name servers
- the learner understands that these are the delegation targets
- the learner can explain why these values matter

This proves that the delegation handoff information is complete.

## Check 3 — The correct delegation point is understood
Confirm that:
- the learner knows where the NS delegation change must occur
- the learner understands the difference between registrar-level root-domain delegation and parent-zone subdomain delegation
- the delegation point matches the chosen scope correctly

This proves that the authority-transfer logic is structurally correct.

## Check 4 — The delegation has been changed or modeled correctly
Confirm that:
- the NS update has been performed, or
- the delegation design has been modeled accurately if the lab is conceptual
- the learner can describe the exact authority transfer path

This proves that the module has moved beyond zone creation into real ownership logic.

## Check 5 — Azure DNS authority is understood as distinct from simple zone presence
Confirm that the learner can clearly explain:
- why creating a zone in Azure does not automatically make it authoritative
- why delegation is required
- what changes after delegation completes

This is one of the most important technical understanding checks in the module. Microsoft’s documentation is explicit that delegation is required before using Azure DNS for custom domain records.

## Check 6 — Delegation propagation is understood
Confirm that:
- the learner understands that delegation may not appear everywhere instantly
- propagation and resolver behavior are part of real DNS operations
- the learner would not immediately misdiagnose normal propagation delay as configuration failure

This proves operational maturity.

## Check 7 — Future ingress integration is understood
Confirm that:
- the learner can explain how this delegated Azure DNS zone will later support ingress-related records
- the learner can explain why ExternalDNS and hostname routing depend on this step
- the learner understands that DNS authority and ingress routing are different but connected layers

This proves that the platform story is coherent.

## Check 8 — You can explain the DNS delegation lifecycle in your own words
This is the most important validation for this module.

The learner should now be able to explain:
- what an Azure DNS zone is
- why delegation is required
- how registrar or parent-zone NS changes work
- when Azure becomes authoritative
- why this must happen before automated DNS and hostname-based ingress work

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the Azure DNS zone is correct
- the authoritative name servers are known
- the delegation path is clear
- the learner understands authority transfer clearly
- the learner is ready to move into ExternalDNS automation

## If validation fails
If any validation step fails:
- re-check the zone scope
- re-check the Azure name server values
- re-check the exact delegation point
- separate “zone exists” from “authority transferred”
- use `troubleshooting.md` for common DNS-delegation issues
