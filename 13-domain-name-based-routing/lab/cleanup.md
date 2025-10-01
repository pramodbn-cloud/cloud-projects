# Cleanup

## Purpose of this file
This file defines how to leave the Domain Name Based Routing lab in a clean and reusable state.

This module creates multiple hostnames, multiple backend services, and host-based ingress rules. Cleanup should preserve the learning value while removing duplicate or confusing naming and routing objects that could interfere with the TLS module that follows.

## What should be removed
Remove or clean up:
- duplicate backend workloads created during testing
- incorrect or duplicate Services
- hostnames in Azure DNS that no longer match the intended final route design
- abandoned ingress rules created during trial routing attempts
- mixed path-and-host experiments that no longer support the intended hostname-routing scenario

If something creates naming or routing confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final clean backend workload set
- one Service per backend
- one ingress resource with the intended host rules
- the Azure DNS records for the intended application hostnames
- the validated explanation of the DNS-to-ingress-to-service request path

These will directly support the next module, which introduces TLS and certificate automation.

## Cleanup sequence

1. Review whether redundant workloads or Services were created by mistake  
2. Keep only the backend set used in the final validated hostname-routing example  
3. Remove duplicate or misleading DNS records  
4. Keep one clean ingress object with the intended host rules  
5. Confirm that the retained hostnames are readable and intentional  
6. Ensure the environment is ready for Folder 14 without naming or routing clutter  

## Cost awareness note
Hostname-based routing often creates more persistent public-facing DNS state than path-only routing. Even in a learning environment, unnecessary retained records or host rules can create operational confusion and make later TLS validation harder.

The main cleanup goal here is hostname clarity and readiness for secure ingress.

## Post-cleanup validation
After cleanup:
- one clean hostname-based ingress example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for TLS
- the learner should still be able to explain the hostname-routing design clearly
- the environment should feel ready for certificate and HTTPS work

## Final note
This lab is fully complete only when:
- the hostname-routing workflow has been practiced
- validation is complete
- the DNS-and-ingress routing path is understood clearly
- unnecessary naming and route clutter has been removed
- the environment is clean enough to support Folder 14
