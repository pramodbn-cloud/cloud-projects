# Cleanup

## Purpose of this file
This file defines how to leave the Security + Compliance lab in a clean and reusable state.

This module can create service connections, variable groups, test secrets, and security-related experiments. Cleanup should preserve the learning value while removing unsafe, duplicate, or confusing security objects.

## What should be removed
Remove or clean up:
- duplicate test service connections created by mistake
- badly named variable groups that add confusion
- placeholder secret values that are no longer needed
- overly broad experimental access that was granted only for testing
- unused secure files or draft security objects with no learning value

If something creates confusion or unnecessary exposure without strengthening the learning story, it should be removed or tightened.

## What can be retained
The following should usually be kept:
- the main intended variable group
- one clear service connection example
- the documented least-privilege reasoning
- the secret-handling pattern used in the lab
- notes on resource sharing and governance decisions

These will support future modules, especially operational automation and later Azure/AKS security-related workflows.

## Cleanup sequence

1. Review whether multiple security objects were created by mistake  
2. Keep only the main intended service connection and variable group  
3. Remove duplicate or badly named security resources  
4. Ensure test secrets are placeholders only and not real long-term credentials  
5. Re-check resource access scope and narrow it where appropriate  
6. Confirm that the project is ready for the next module without security clutter  

## Cost awareness note
This module is more about trust, exposure, and governance than direct infrastructure cost, but unmanaged service connections or careless secret objects can create real operational risk.

The main cleanup goal here is controlled clarity and safer reuse.

## Post-cleanup validation
After cleanup:
- one main security pattern should remain
- the service connection should still be understandable
- the variable group strategy should remain clear
- the learner should feel ready to connect security-aware delivery with operational visibility and automation

## Final note
This lab is fully complete only when:
- the security workflow has been practiced
- validation is complete
- trust boundaries and secret handling are understood
- unnecessary security clutter has been removed
- the project is clean enough to support Folder 08
