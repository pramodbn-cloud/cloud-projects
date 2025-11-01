# Cleanup

## Purpose of this file
This file defines how to leave the Kubernetes Namespaces lab in a clean and reusable state.

This module can create multiple namespaces, duplicate workloads, and test-only organizational patterns. Cleanup should preserve the learning value while removing namespace sprawl or placement confusion that could interfere with later advanced modules.

## What should be removed
Remove or clean up:
- duplicate namespaces created during testing
- namespaces with no clear operational purpose
- workloads accidentally deployed into the wrong namespace
- abandoned namespace strategies that no longer match the final design
- notes or manifests that mix conflicting namespace models

If something creates cluster-organization confusion without strengthening learning, it should be removed or clearly separated.

## What can be retained
The following should usually be kept:
- the final clean namespace set
- the workloads intentionally placed inside those namespaces
- the namespace strategy notes explaining the chosen grouping model
- the final explanation of why namespace scope matters for governance

These will support future modules, especially when quotas, RBAC, and more advanced cluster design patterns are considered.

## Cleanup sequence

1. Review whether unnecessary namespaces were created during experimentation  
2. Keep only the namespaces that match the final intended strategy  
3. Remove duplicate or purposeless namespaces  
4. Ensure the retained workloads are in the correct namespace  
5. Keep one clean explanation of the namespace design choice  
6. Ensure the cluster is ready for the next module without namespace clutter  

## Cost awareness note
Namespaces themselves are logical objects, but namespace sprawl can still create real operational confusion and make later policy modules harder to reason about.

The main cleanup goal here is organizational clarity and readiness for more advanced execution and governance patterns.

## Post-cleanup validation
After cleanup:
- one clean namespace strategy should remain, if you are intentionally reusing it
- or the lab should be fully cleaned if you want a fresh start for the next module
- the learner should still be able to explain the namespace model clearly
- the cluster should feel ready for the next advanced topic

## Final note
This lab is fully complete only when:
- the namespace workflow has been practiced
- validation is complete
- logical isolation and governance scope are understood clearly
- unnecessary namespace clutter has been removed
- the environment is clean enough to support Folder 17
