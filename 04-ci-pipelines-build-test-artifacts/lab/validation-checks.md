# Validation Checks

## Purpose of this file
This file confirms whether the CI Pipelines lab is complete and correct.

The goal is not only to confirm that a pipeline exists, but to verify that the learner has created a meaningful automation path from repository change to validated output.

## Validation approach
For this lab, validation is based on:
- pipeline existence verification
- repository linkage verification
- build and validation flow verification
- artifact publication verification
- trigger behavior verification
- learner explanation ability

## Check 1 — Pipeline exists and is connected to the correct repository
Confirm that:
- the pipeline is visible in Azure Pipelines
- the pipeline references the intended repository
- the learner can open and inspect its configuration

This proves that the automation layer is tied to the correct source control context.

## Check 2 — Pipeline run completes successfully
Confirm that:
- at least one run completed successfully
- the run history is visible
- the learner can inspect logs for the run

This proves that the pipeline is operational.

## Check 3 — Build step performs meaningful work
Review the build step and confirm that:
- it performs a real preparation or validation action
- it is not only decorative or empty
- the learner can explain why it exists

This proves that the CI flow includes an actual technical checkpoint.

## Check 4 — Test or verification step adds confidence
Confirm that:
- a test or validation step exists
- it contributes something meaningful to trust
- the learner understands what condition it is checking

This proves that the pipeline is not only moving content, but validating quality.

## Check 5 — Artifact is published and visible
Confirm that:
- the artifact exists after a successful run
- it has a clear purpose
- the learner can locate and review it in the pipeline run

This proves that the CI system is producing reusable outputs.

## Check 6 — Trigger behavior works as expected
Confirm that:
- a repository change can trigger the pipeline automatically if configured
- or the learner can clearly explain the trigger approach if using manual validation first
- the pipeline and repo relationship is clear

This proves that the pipeline is tied to source control activity properly.

## Check 7 — Pipeline logs are understandable at a basic level
Open a run and confirm that the learner can explain:
- where the run started
- what each step was doing
- where success or failure would appear
- where artifact publication occurred

This proves that the learner is not only clicking run, but interpreting automation behavior.

## Check 8 — You can explain the CI lifecycle in your own words
This is the most important validation for this module.

You should now be able to explain:
- why CI exists
- why it is connected to repository changes
- why build and validation are separate but related
- why artifacts are useful
- how this module prepares for deployment workflows later

If you can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the pipeline runs successfully
- the repository trigger path is clear
- build and validation steps have purpose
- artifact output is visible
- the learner feels ready to use CI output in the next module

## If validation fails
If any validation step fails:
- revisit the pipeline configuration
- re-check repository linkage
- review step definitions and ordering
- confirm artifact publication settings
- use `troubleshooting.md` for common pipeline issues
