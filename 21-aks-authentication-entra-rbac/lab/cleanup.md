# Cleanup

## Purpose of this file
This file defines how to leave the AKS Authentication with Microsoft Entra ID and Kubernetes RBAC lab in a clean and reusable state.

This module can create roles, bindings, and identity access patterns that affect real cluster governance. Cleanup should preserve the learning value while removing over-broad or confusing access definitions that could interfere with later modules.

## What should be removed
Remove or clean up:
- duplicate Roles or RoleBindings created during testing
- overly broad experimental bindings that are no longer part of the final intended design
- user-specific bindings that were created only for trial purposes and do not reflect the final group-based pattern
- notes or manifests that mix namespace-scoped and cluster-scoped access confusingly

If something creates access-governance confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final narrow Role or ClusterRole example
- the final binding pattern used for the lab
- the final namespace-scoped access design
- the validated explanation of authentication versus authorization

These will support later governance topics and stronger production-cluster access reasoning.

## Cleanup sequence

1. Review whether duplicate or conflicting RBAC objects were created during testing  
2. Keep only the objects that match the final intended least-privilege design  
3. Remove overly broad or misleading experimental bindings  
4. Prefer retaining one clear group-based example over many ad hoc user examples  
5. Confirm that the retained access model is readable and intentional  
6. Ensure the environment is ready for Folder 22 without RBAC clutter  

## Cost awareness note
RBAC objects are lightweight technically, but access clutter creates real governance risk. The main cleanup goal here is not cost. It is access clarity and avoiding accidental permission confusion.

## Post-cleanup validation
After cleanup:
- one clean RBAC example should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the access-governance model clearly
- the environment should feel ready for AKS autoscaling

## Final note
This lab is fully complete only when:
- the authentication and RBAC workflow has been practiced
- validation is complete
- least-privilege access design is understood clearly
- unnecessary RBAC clutter has been removed
- the environment is clean enough to support Folder 22
