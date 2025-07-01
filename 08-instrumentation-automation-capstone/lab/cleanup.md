# Cleanup

## Purpose of this file
This file defines how to leave the Instrumentation + Automation + Capstone lab in a clean and reusable state.

This module can create dashboards, trial widgets, alerting ideas, and automation experiments. Cleanup should preserve the learning value while removing noisy or confusing visibility objects.

## What should be removed
Remove or clean up:
- duplicate dashboards created during testing
- low-value widgets that do not support meaningful visibility
- experimental notification setups that create confusion
- unused or unclear service-hook experiments
- temporary capstone notes that were only draft-level and no longer needed

If something creates noise without strengthening understanding, it should be removed or simplified.

## What can be retained
The following should usually be kept:
- the main capstone dashboard
- the most useful widgets
- one clear notification scenario
- one clear service-hook or webhook automation story
- the final capstone explanation of the foundation phase

These will support the transition into the AKS phase and keep the Azure DevOps base understandable.

## Cleanup sequence

1. Review whether multiple dashboards were created by mistake  
2. Keep only the main intended dashboard for the foundation phase  
3. Remove unnecessary widgets and keep the dashboard focused  
4. Keep only useful notification or event-driven examples  
5. Remove unclear automation experiments with no lasting learning value  
6. Confirm that the capstone explanation is saved clearly for future reference  

## Cost awareness note
This module is more about visibility quality and operational clarity than infrastructure cost, but cluttered dashboards and noisy automation patterns can reduce usefulness and make later review harder.

The main cleanup goal here is readability and operational focus.

## Post-cleanup validation
After cleanup:
- one main dashboard should remain
- the signal set should still be easy to explain
- the capstone story should remain clear
- the learner should feel ready to begin the AKS phase with a strong Azure DevOps foundation

## Final note
This lab is fully complete only when:
- the visibility and automation workflow has been practiced
- validation is complete
- the capstone understanding is strong
- unnecessary monitoring and automation clutter has been removed
- the project is clean enough to support Folder 09
