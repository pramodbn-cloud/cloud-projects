# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the CI Pipelines lab.

The goal is to create one clear CI workflow that connects repository changes to automated build, test, and artifact publishing behavior.

---

## Step 1 — Understand the CI goal
Before creating the pipeline, understand what this module is trying to teach.

This lab is not about building a highly advanced pipeline. It is about learning the purpose and structure of CI:

- detect change
- run validation
- produce output
- show visible result

At the end of this lab, you should have:
- one working pipeline
- one build flow
- one verification or test step
- one artifact output

## Step 2 — Review the repository that will feed the pipeline
Open the repository created in Folder 03 and decide what the CI pipeline will validate.

Keep it simple. Examples:
- validate repository structure
- build a small sample application
- run a small script
- package files into an artifact

This step matters because CI should always have a clear purpose, even in a learning repo.

## Step 3 — Open Azure Pipelines
Go to Azure DevOps and open the Pipelines area.

Spend a few minutes observing:
- pipeline creation options
- run history area
- logs and execution views
- artifact visibility area

Do not rush. First understand that this is the automation layer that sits on top of the repository workflow.

## Step 4 — Create a new pipeline connected to the repository
Start a new pipeline and connect it to the repository used in the previous module.

While doing this, pay attention to:
- repository selection
- branch context
- pipeline configuration method
- where the pipeline definition will live

The goal here is to create a strong link between the repository and the automation engine.

## Step 5 — Choose a simple pipeline definition approach
Use a clean and understandable pipeline structure.

For this module, the pipeline should contain the following logical sections:
- trigger
- build step
- test or verification step
- artifact publish step

Do not add too many extra stages yet. Keep the pipeline easy to explain.

## Step 6 — Define the trigger behavior
Decide how the pipeline will run.

Recommended approach:
- configure it to respond to changes on the main branch or relevant branch
- optionally run it manually first to confirm the structure works

This step teaches that CI pipelines are tied closely to repository activity.

## Step 7 — Add the build step
Now define the build portion of the pipeline.

Depending on the sample project, this could mean:
- preparing files
- running a simple install step
- validating syntax or content
- packaging the repo structure
- performing a lightweight build action

The important point is not the complexity of the build, but the fact that the pipeline is now automating preparation of code or repository content.

## Step 8 — Add a test or verification step
Add a simple validation step that proves the CI flow is doing more than only packaging.

Examples:
- run a small test command
- verify required files exist
- check formatting or structure
- run a basic script that exits successfully only when expected conditions are met

This step is important because CI should provide trust, not just movement.

## Step 9 — Add the artifact publishing step
Define an artifact output for the pipeline.

This could be:
- packaged application output
- a zipped project folder
- generated build output
- validated repository content prepared for downstream use

This step matters because CI should not only validate; it should also produce something reusable.

## Step 10 — Save and run the pipeline
Save the pipeline and run it.

For the first run, observe carefully:
- how the run starts
- what each step is doing
- where success or failure appears
- how logs are displayed
- whether the artifact is produced

The first run is one of the most important learning moments in the module.

## Step 11 — Review the run result in detail
Open the completed run and review:
- pipeline status
- duration
- step-level results
- any warnings or failures
- artifact publishing outcome

Do not just look for green success. Try to understand how the run tells its story.

## Step 12 — Trigger the pipeline through a repository change
Make a small, meaningful change in the repository and push it.

Then verify whether the CI pipeline responds according to the trigger rule you defined.

This step teaches the real value of CI: automation reacting to repository change.

## Step 13 — Observe artifact availability
Open the pipeline run and confirm that the artifact is present and understandable.

Ask:
- Is the artifact clearly named?
- Does it represent something usable?
- Could a later deployment stage consume it?

This thinking prepares the learner for the next module.

## Step 14 — Reflect on CI as a quality gate
Pause and think beyond the mechanics.

In this module, CI means:
- code changes are not trusted blindly
- validation is automated
- results are visible quickly
- reusable outputs are produced consistently

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- the pipeline is connected to the repository
- the pipeline can run successfully
- the build step is visible and understandable
- the test or verification step adds trust
- an artifact is published and visible
- repository changes can trigger the workflow

## Step 15 — Prepare for CD thinking
Before moving to the next module, understand the next workflow step.

The next module is about controlled deployment. That means the artifact produced here should now be seen as a candidate for promotion into later environments or release steps.

This is the bridge from automated validation into automated delivery.

---

## Implementation notes
- keep the pipeline readable and simple in this module
- do not overload it with advanced features yet
- make sure each step has a clear reason to exist
- treat logs as learning tools, not only error outputs
- think of artifacts as handoff outputs for downstream workflows

## End-of-implementation summary
In this lab, you:
- connected Azure Pipelines to the repository
- created a CI workflow
- defined trigger logic
- added build and validation behavior
- published an artifact
- observed a full pipeline run
- verified that repository change can feed automated validation

You are now ready to validate whether the CI lifecycle is clean, correct, and explainable.
