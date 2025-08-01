# Cleanup

## Purpose of this file
This file defines how to leave the Ingress Context Path Routing lab in a clean and reusable state.

This module creates multiple workloads, multiple Services, and a shared ingress rule set. Cleanup should preserve the learning value while removing duplicate or confusing route objects that would interfere with later DNS- and hostname-based ingress modules.

## What should be removed
Remove or clean up:
- duplicate or abandoned backend workloads
- incorrect or test-only Services that no longer support the final route map
- extra ingress rules created during failed experiments
- path names or route patterns that are unclear or no longer needed
- namespace clutter that makes later hostname-based routing harder to understand

If something creates route confusion without strengthening learning, it should be removed or renamed clearly.

## What can be retained
The following should usually be kept:
- the final clean multi-service workload set
- one Service per backend
- one ingress resource with the intended path rules
- notes describing the path-to-service map
- the validated explanation of the multi-service request path

These will support the next advanced modules, especially DNS, hostname-based routing, and TLS work.

## Cleanup sequence

1. Review whether multiple redundant workloads were created by mistake  
2. Keep only the backend set used in the final validated path-routing example  
3. Remove duplicate or misnamed Services  
4. Keep one clean ingress object with the intended path rules  
5. Confirm that the path map remains readable and intentional  
6. Ensure the cluster is ready for Folder 11 without route clutter  

## Cost awareness note
Multi-service ingress labs can leave behind more cluster objects and public-exposure dependencies than simple ingress labs. Even in a learning environment, unnecessary retained resources can create both operational confusion and infrastructure overhead.

The main cleanup goal here is routing clarity and readiness for DNS-focused modules.

## Post-cleanup validation
After cleanup:
- one clean multi-service ingress example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the path-routing design clearly
- the cluster should feel ready for DNS and naming work

## Final note
This lab is fully complete only when:
- the path-routing workflow has been practiced
- validation is complete
- the multi-service traffic path is understood clearly
- unnecessary route clutter has been removed
- the cluster is clean enough to support Folder 11
