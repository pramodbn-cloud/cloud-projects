# Cleanup

## Purpose of this file
This file defines how to leave the AKS Application Routing lab in a clean and reusable state.

This module can create managed add-on state, sample ingress routes, and test routing configurations. Cleanup should preserve the learning value while removing confusion between retired and current routing models or between managed and self-managed ingress experiments.

## What should be removed
Remove or clean up:
- outdated HTTP Application Routing notes or manifests that no longer match the current platform
- duplicate sample ingress resources created only for comparison experiments
- abandoned managed-routing test objects that no longer support the final learning path
- notes that mix self-managed and managed-routing behavior without clear distinction

If something creates platform-model confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final managed-routing example
- the final comparison notes between managed and self-managed ingress
- the final explanation of why the old topic was modernized
- the validated explanation of Azure-native routing integration

These will support future governance and production-cluster design discussions.

## Cleanup sequence

1. Review whether outdated retired-feature guidance is still mixed into the lab materials  
2. Keep only the modern Application Routing add-on flow  
3. Remove duplicate comparison ingress examples that are no longer needed  
4. Keep one clear explanation of managed versus self-managed ingress trade-offs  
5. Confirm the retained example is readable and operationally intentional  
6. Ensure the environment is ready for Folder 21 without routing-model confusion  

## Cost awareness note
Managed add-ons and routing resources can create real platform state. Even in a learning environment, confusion between deprecated and current models can create more operational risk than cost, especially when later modules depend on correct platform assumptions.

The main cleanup goal here is model clarity and readiness for cluster access governance.

## Post-cleanup validation
After cleanup:
- one clean managed-routing example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the modernization and trade-offs clearly
- the environment should feel ready for AKS identity and RBAC work

## Final note
This lab is fully complete only when:
- the managed-routing workflow has been practiced
- validation is complete
- the retired-versus-current distinction is understood clearly
- unnecessary routing-model clutter has been removed
- the environment is clean enough to support Folder 21
