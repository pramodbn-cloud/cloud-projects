# Cleanup

## Purpose of this file
This file defines how to leave the Azure Artifacts lab in a clean and reusable state.

This module can create feeds, package entries, and trial publishing attempts. Cleanup should preserve the learning value while removing unclear or duplicate package-management clutter.

## What should be removed
Remove or clean up:
- duplicate feeds created by mistake
- badly named trial feeds
- test package versions that add confusion without teaching value
- abandoned publish attempts that no longer represent the intended scenario
- unnecessary upstream experiments that make the feed harder to understand

If something creates confusion without strengthening the learning story, it should be removed or renamed clearly.

## What can be retained
The following should usually be kept:
- the main intended feed
- the clean package publishing example
- the version pattern used in the lab
- the documented consumption flow
- the upstream and visibility notes if they support future learning

These will support the next modules, especially security and governance thinking.

## Cleanup sequence

1. Review whether multiple feeds were created by mistake  
2. Keep only the main intended feed for the learning repo  
3. Remove or ignore unclear test feeds with no lasting value  
4. Keep one clean package example and one clear version pattern  
5. Ensure the feed settings remain understandable  
6. Confirm that the project is ready for the next module without package clutter  

## Cost awareness note
This module is more about governance and clarity than infrastructure cost, but unmanaged package clutter can reduce understanding and make future reuse confusing.

The main cleanup goal here is feed clarity and lifecycle readability.

## Post-cleanup validation
After cleanup:
- one main feed should remain
- the package example should still be easy to explain
- version identity should remain clear
- the learner should feel ready to connect package strategy with security and compliance controls

## Final note
This lab is fully complete only when:
- the package workflow has been practiced
- validation is complete
- feed and versioning logic are understood
- unnecessary package clutter has been removed
- the project is clean enough to support Folder 07
