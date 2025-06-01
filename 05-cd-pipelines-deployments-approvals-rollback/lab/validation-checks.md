# Validation Checks

## Purpose of this file
This file confirms whether the CD Pipelines lab is complete and correct.

The goal is not only to verify that a deployment flow exists, but to confirm that the learner understands how validated artifacts move into controlled release stages with appropriate delivery discipline.

## Validation approach
For this lab, validation is based on:
- artifact handoff verification
- stage flow verification
- environment or target clarity
- approval logic understanding
- rollback preparedness
- learner explanation ability

## Check 1 — The CI artifact is being used correctly
Confirm that:
- the deployment flow references the intended artifact from the CI pipeline
- the artifact is clearly identifiable
- the learner can explain why this artifact is suitable for promotion

This proves that CD is starting from validated output, not from undefined inputs.

## Check 2 — At least one deployment stage exists and is understandable
Confirm that:
- one deployment stage is configured
- the stage name is clear
- the learner can explain the purpose of the stage

This proves that delivery is being treated as an organized stage-based workflow.

## Check 3 — Stage progression is visible
If more than one stage exists, confirm that:
- the stage order is clear
- promotion logic is understandable
- the learner can explain why work should move in that sequence

If only one stage is used for simplicity, the learner should still be able to explain how stage progression would expand in a larger flow.

## Check 4 — Approval thinking is present
Confirm that:
- an approval checkpoint is configured or clearly documented
- the learner understands when approvals matter
- the learner can explain the value of pausing before promotion

This proves that release control is part of the workflow, not only automation speed.

## Check 5 — Deployment action is meaningful
Review the deployment action and confirm that:
- it performs a real release-oriented step
- the learner understands what it is doing
- it represents a delivery action, not only a renamed build step

This proves that the workflow has moved from CI into CD thinking.

## Check 6 — Rollback strategy is documented clearly
Confirm that:
- a simple rollback plan exists
- the learner can explain what would happen if deployment is not acceptable
- rollback is treated as an expected design concern

This proves that delivery safety has been considered.

## Check 7 — Release history or run visibility is understandable
Open the deployment run and confirm that the learner can explain:
- how the artifact entered the release flow
- what each stage did
- where approval would apply
- where recovery thinking would matter

This proves that the learner is reading the delivery lifecycle, not only running it.

## Check 8 — You can explain the CD lifecycle in your own words
This is the most important validation for this module.

You should now be able to explain:
- how CD differs from CI
- why environments and stages matter
- why approvals matter
- why rollback must be planned
- how artifacts move from validation into delivery

If you can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the artifact handoff is clear
- stage-based delivery is visible
- approval logic is understood
- rollback thinking is documented
- the learner feels ready to move into reusable package strategy and later advanced delivery patterns

## If validation fails
If any validation step fails:
- revisit the stage design
- confirm artifact linkage
- simplify the release flow if needed
- re-check approval assumptions
- use `troubleshooting.md` for common delivery issues
