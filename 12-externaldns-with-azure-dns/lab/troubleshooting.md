# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the ExternalDNS with Azure DNS lab.

In this module, the most common failures usually come from trying to automate against a zone Azure does not truly control, using the wrong Azure identity or permission scope, pointing ExternalDNS at the wrong source pattern, or assuming that record creation is immediate without checking reconciliation behavior. The goal is to strengthen controller-driven DNS reasoning, not only fix manifests.

---

## Common issue 1 — ExternalDNS runs, but no record appears in Azure DNS

### Symptoms
- the controller is running
- the ingress or service exists
- Azure DNS remains unchanged
- the learner assumes the controller is broken

### Likely cause
The most common cause is that one of the layers below the record action is missing:
- Azure DNS authority is not actually in place
- the source object does not express DNS intent correctly
- the controller does not have the right Azure permissions
- the controller is not watching the correct resource type

### Fix
- confirm the Azure zone is authoritative for the chosen hostname scope
- confirm the source object clearly expresses the intended hostname
- confirm the controller is watching the correct resource type
- confirm the Azure identity has DNS update permissions

### Re-validation
After the fix:
- inspect controller behavior again
- verify whether the expected record now appears in Azure DNS

---

## Common issue 2 — The wrong Azure identity is being used

### Symptoms
- ExternalDNS appears configured
- Azure API actions fail or do not affect the intended zone
- the learner is unsure which identity the controller is actually using

### Likely cause
The cluster may be using a different identity pattern than the learner expects, or the configured identity may not be the one granted access to the DNS zone.

### Fix
- explicitly identify the intended auth model
- verify whether the controller is using Service Principal or Managed Identity
- verify that the granted identity matches the configured identity exactly
- avoid mixing identity assumptions during troubleshooting

### Re-validation
After the fix:
- confirm the controller is operating with the intended identity
- verify that Azure DNS operations now succeed

---

## Common issue 3 — Azure permissions are too broad or too narrow

### Symptoms
- the controller cannot modify the zone, or
- the learner granted very broad Azure rights just to make it work
- the security model feels weak or confusing

### Likely cause
Permission scope may not have been designed intentionally.

### Fix
- identify the minimum Azure scope needed for DNS record updates
- grant that scope to the chosen identity
- avoid using excessive broad privileges as the default answer
- confirm the learner can explain the chosen scope

### Re-validation
After the fix:
- confirm record creation works
- confirm the permission design is still explainable and appropriately narrow

---

## Common issue 4 — Hostname is outside the delegated Azure DNS zone

### Symptoms
- the controller is healthy
- the zone exists
- the source object uses a hostname
- no useful DNS result appears where expected

### Likely cause
The hostname may not belong inside the delegated Azure DNS zone from Folder 11.

### Fix
- compare the source hostname to the delegated zone scope
- ensure the hostname is a child of the Azure-controlled domain or subdomain
- keep the first learning scenario inside one clear zone boundary

### Re-validation
After the fix:
- confirm the hostname now falls inside the delegated Azure DNS scope
- re-check record creation in the correct zone

---

## Common issue 5 — The learner understands the steps but not why ExternalDNS is a big platform step

### Symptoms
- the record was created successfully
- the learner still sees this as “just convenience”
- the strategic value of the module feels weak

### Likely cause
The learner may still be thinking in single-app or small-scale terms rather than platform-lifecycle terms.

### Fix
Reframe ExternalDNS like this:
- many ingress and hostname changes create repeated DNS work
- manual DNS updates slow teams and create drift
- ExternalDNS turns DNS state into something reconciled from cluster intent
- this becomes much more valuable as the platform grows

### Re-validation
After the fix:
- confirm the learner can explain one scaling advantage of ExternalDNS over frequent manual DNS management

---

## Troubleshooting mindset
While debugging this module, always ask:
- does Azure truly control the DNS zone?
- does the hostname belong inside that zone?
- is the controller using the intended Azure identity?
- does that identity have the correct DNS update scope?
- is the controller watching the right source objects?
- am I checking reconciliation rather than guessing?

## Escalation rule
If the automation still feels broken:
1. confirm Azure DNS authority  
2. confirm hostname scope  
3. confirm source object intent  
4. confirm identity model  
5. confirm permission scope  
6. confirm controller reconciliation behavior  
7. retest only after each lower layer is known-good  
8. prioritize lifecycle reasoning over repeated manifest edits  
