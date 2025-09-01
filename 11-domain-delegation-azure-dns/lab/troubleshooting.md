# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Domain Delegation to Azure DNS lab.

In this module, the most common failures usually come from confusing zone creation with authority transfer, updating the wrong delegation point, using the wrong name server values, or misreading propagation behavior. The goal is to strengthen DNS ownership reasoning, not only fix records.

---

## Common issue 1 — The Azure DNS zone exists, but Azure is not actually authoritative

### Symptoms
- the zone is visible in Azure
- the learner assumes the domain is now using Azure DNS
- public resolution still does not behave through Azure as expected
- the next steps feel blocked or inconsistent

### Likely cause
The most common cause is that the learner created the Azure DNS zone but did not actually change delegation at the registrar or parent zone.

### Fix
- confirm where the current authority for the domain or subdomain lives
- verify whether the Azure name servers were actually configured there
- separate “zone exists in Azure” from “delegation changed publicly”

### Re-validation
After the fix:
- confirm the delegation point is updated to Azure’s name servers
- re-check public DNS behavior after propagation

---

## Common issue 2 — The wrong delegation point was updated

### Symptoms
- the learner updated something in DNS, but authority still does not behave correctly
- the change was made at a provider that is not actually the correct parent authority
- the lab feels structurally correct but does not work

### Likely cause
The learner may have misunderstood whether the change belongs at:
- the registrar for a root domain, or
- the parent DNS zone for a subdomain

### Fix
- re-evaluate the chosen scope carefully
- identify whether this is full-domain delegation or subdomain delegation
- update the true parent authority location only

### Re-validation
After the fix:
- confirm the NS change exists at the correct parent level
- validate authority flow again

---

## Common issue 3 — Azure name servers were copied incorrectly

### Symptoms
- delegation was updated, but resolution still fails or behaves inconsistently
- the learner is unsure whether the Azure NS values are correct
- the error feels random

### Likely cause
The assigned Azure name server values may have been copied incompletely, mistyped, or mixed with values from another zone.

### Fix
- return to the Azure DNS zone
- re-copy the exact authoritative name server set
- verify every value carefully
- ensure the registrar or parent-zone update uses the exact assigned values

### Re-validation
After the fix:
- confirm the delegation values exactly match the Azure zone’s assigned name servers
- re-check authority behavior after propagation

---

## Common issue 4 — Propagation delay is mistaken for configuration failure

### Symptoms
- the learner updates delegation and immediately expects uniform global behavior
- some lookups reflect the change, while others do not
- the learner assumes the configuration is broken

### Likely cause
DNS delegation changes propagate through caching layers and recursive resolvers over time. This is normal operational behavior and not necessarily a sign of a bad configuration.

### Fix
- verify that the configuration change is structurally correct first
- allow time for propagation
- test from more than one resolver view if possible
- do not repeatedly change the delegation while propagation is still in progress

### Re-validation
After the fix:
- re-check resolution after appropriate time
- confirm that authority becomes consistent rather than changing settings prematurely

---

## Common issue 5 — The learner still does not understand why DNS delegation matters before ExternalDNS

### Symptoms
- the learner sees delegation as a registrar task only
- the connection to ingress feels weak
- the platform-engineering significance of the module feels low

### Likely cause
The learner may still be thinking about DNS as record entry rather than authority.

### Fix
Reframe delegation like this:
- ExternalDNS can automate records only inside a zone Azure controls
- hostname-based ingress patterns need authoritative DNS names
- certificate workflows also depend on stable authoritative naming
- delegation gives Azure the right to answer for that domain scope publicly

### Re-validation
After the fix:
- confirm the learner can explain one clear reason this module must come before ExternalDNS and domain-based routing

---

## Troubleshooting mindset
While debugging this module, always ask:
- did I only create the zone, or did I actually transfer authority?
- am I changing the correct parent authority point?
- are the Azure NS values exact?
- is this a real configuration problem or normal propagation timing?
- do I understand how this delegated scope will be used later for ingress hostnames?

## Escalation rule
If the DNS authority flow still feels broken:
1. confirm the exact zone scope  
2. confirm the exact Azure name server set  
3. confirm the exact parent delegation point  
4. confirm the NS change was applied there  
5. allow for propagation  
6. retest authority rather than changing multiple things at once  
7. prioritize authority-chain reasoning over trial-and-error edits  
