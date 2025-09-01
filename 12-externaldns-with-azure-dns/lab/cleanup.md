# Cleanup

## Purpose of this file
This file defines how to leave the ExternalDNS with Azure DNS lab in a clean and reusable state.

This module can create controller resources, Azure identity assignments, and public DNS records. Cleanup should preserve the learning value while removing duplicate automation patterns or confusing DNS entries that would interfere with later hostname-based routing and TLS modules.

## What should be removed
Remove or clean up:
- duplicate ExternalDNS deployments created during testing
- abandoned identity or permission experiments that are no longer part of the final model
- test hostnames or records that no longer match the intended naming pattern
- controller configurations that watch too broadly for the learning scenario
- notes or objects that mix multiple authentication strategies confusingly

If something creates DNS automation confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final ExternalDNS deployment
- the final Azure identity model used for DNS updates
- the delegated Azure DNS zone from Folder 11
- one or more clean hostname records created through the controller
- the validated explanation of the reconciliation flow from Kubernetes to Azure DNS

These will directly support the next modules, especially domain-based routing and TLS.

## Cleanup sequence

1. Review whether multiple ExternalDNS deployments or experiments were created by mistake  
2. Keep only the deployment and auth pattern that match the final design  
3. Remove duplicate or misleading DNS records from trial runs  
4. Confirm the retained hostnames belong to the intended naming strategy  
5. Keep the Azure permission scope clean and understandable  
6. Ensure the environment is ready for Folder 13 without DNS automation clutter  

## Cost awareness note
ExternalDNS interacts with public DNS state and Azure identity/governance surfaces. Even in a learning environment, unnecessary retained records or confused auth models can create real operational confusion.

The main cleanup goal here is automation clarity and readiness for hostname-based ingress work.

## Post-cleanup validation
After cleanup:
- one clean ExternalDNS automation pattern should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the automation lifecycle clearly
- the environment should feel ready for hostname-based ingress routing

## Final note
This lab is fully complete only when:
- the ExternalDNS workflow has been practiced
- validation is complete
- Azure DNS automation is understood clearly
- unnecessary automation clutter has been removed
- the environment is clean enough to support Folder 13
