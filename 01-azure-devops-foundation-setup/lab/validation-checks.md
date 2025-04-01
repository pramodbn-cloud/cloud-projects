# Validation Checks

## Purpose of this file
This file confirms whether the Azure DevOps foundation setup lab is complete and correct.

Completing the setup steps is not enough by itself. Validation ensures that the environment is actually ready for the next modules.

## Validation approach
For this lab, validation is based on:
- portal verification
- project readiness verification
- local machine readiness verification
- workflow understanding verification

The goal is not just to see that something exists. The goal is to confirm that the learner can now work confidently inside the environment.

## Check 1 — Azure DevOps access works
Confirm that you can:
- open Azure DevOps in the browser
- sign in without errors
- navigate inside the platform successfully

This proves that your primary platform access is ready.

## Check 2 — Organization exists and is usable
Confirm that:
- your organization is visible
- you can open it
- you can access the working areas inside it

This proves that the top-level working boundary is established correctly.

## Check 3 — Project exists and is usable
Confirm that:
- your project is visible inside the organization
- you can open the project successfully
- you can navigate the major service sections inside the project

This proves that you now have a real working space for the rest of the course.

## Check 4 — Core service areas are visible
Open and review these areas inside the project:
- Boards
- Repos
- Pipelines
- Artifacts
- Project Settings

You do not need deep configuration yet, but you should be able to recognize that these areas are present and available.

This proves that the learning platform is ready for future module work.

## Check 5 — Local machine is ready
Confirm that your local machine can:
- open a terminal
- run Git
- run Azure CLI
- open the editor

This proves that the local execution side of the workflow is ready.

## Check 6 — Working directory is prepared
Confirm that you have a dedicated local folder for this repository journey.

This proves that your work will remain organized and repeatable.

## Check 7 — You can explain the setup in your own words
This is the most important validation for this module.

You should now be able to explain:
- what Azure DevOps is at a high level
- why an organization exists
- why a project exists
- why local tool readiness matters
- why this foundation comes before planning, repos, and pipelines

If you can explain these clearly, then the setup is not only done — it is understood.

## Expected success indicators
The strongest success signals for this lab are:
- Azure DevOps sign-in works
- organization is accessible
- project is created and visible
- local terminal tools are available
- the learner feels ready to move to structured Azure DevOps usage

## If validation fails
If any validation step fails:
- revisit the implementation sequence
- re-check access and permissions
- confirm tool installation
- verify that the correct organization and project were created
- use `troubleshooting.md` to identify likely causes
