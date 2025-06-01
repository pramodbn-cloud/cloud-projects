# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the CD Pipelines lab.

The goal is to create one clear deployment workflow that takes a validated artifact and moves it through a simple, controlled release path with visibility into approvals and rollback thinking.

---

## Step 1 — Understand the CD goal
Before creating the deployment flow, understand what this module is trying to teach.

This lab is not about building a complex production release platform. It is about understanding the delivery logic that sits after CI:

- take a validated artifact
- choose a target environment
- promote it in a controlled way
- protect the process with stage discipline
- stay ready to recover if the deployment is not acceptable

At the end of this lab, you should have:
- one understandable deployment workflow
- one or more stages or environments
- approval awareness
- rollback reasoning

## Step 2 — Review the CI artifact that will feed the release flow
Open the successful CI run from Folder 04 and review the artifact.

Ask:
- what exactly is being handed off?
- is it clearly named?
- is it suitable for downstream use?
- can it represent a deployable package in this learning flow?

This step matters because CD should never start from unclear outputs.

## Step 3 — Define the release scenario
Choose a simple release story for this lab.

Recommended example:
- deploy the validated artifact into a Dev stage
- optionally promote it into a Test stage after review

Even if the target is simplified, the learner should think in terms of environment progression, not only “run deployment.”

## Step 4 — Open Azure Pipelines and choose the deployment approach
Go to Azure Pipelines and decide how you want to model the CD workflow in your learning setup.

The important thing is not the exact product mode. The important thing is that the workflow contains:
- artifact input
- deployment stage logic
- stage visibility
- controlled progression

Keep the design easy to explain.

## Step 5 — Create the first deployment stage
Define the first stage, such as `Deploy_Dev`.

This stage should represent the first environment where the artifact is promoted after CI.

At this stage, focus on:
- stage naming clarity
- artifact linkage
- the concept of environment-specific delivery

Even if the deployment action is simple, the stage boundary itself is the learning objective.

## Step 6 — Define the deployment action
Now define what the deployment stage actually does.

For a learning repo, this can be simplified. The key is that the artifact is being used in a deployment-oriented action, such as:
- unpacking or preparing files for a target
- simulating an environment deployment step
- running a release-oriented script
- copying validated output to a destination pattern

The exact target can remain lightweight as long as the release logic is real.

## Step 7 — Add a second stage if appropriate
If your learning setup supports it well, add a second logical stage such as `Deploy_Test`.

This helps teach promotion flow:
- artifact first enters Dev
- only after that should it move further
- later stages represent increased delivery confidence

Do not overcomplicate the flow. One clear additional stage is enough to teach the concept.

## Step 8 — Introduce approval thinking
Before promoting into the next stage, introduce an approval checkpoint concept.

If your setup supports actual approval gates, configure one.  
If not, document the approval boundary clearly and simulate the logic.

The learner should understand:
- approvals are not only about permission
- approvals create deliberate pause and review before higher-risk deployment
- release discipline becomes stronger when promotion is intentional

## Step 9 — Run the deployment workflow
Save the deployment flow and execute it.

Observe:
- how the artifact is picked up
- how stages are shown
- where a stage succeeds or pauses
- how approval or progression appears
- what the release history looks like

This is one of the most important learning moments in the module.

## Step 10 — Review the stage progression
Once the run completes or reaches a review point, inspect the stage view carefully.

Ask:
- did the artifact move as expected?
- is the stage order understandable?
- is the release history visible?
- can I explain what happened at each point?

This step helps the learner read delivery systems instead of only running them.

## Step 11 — Review rollback thinking
Even if no failure occurred, now introduce rollback reasoning.

Ask:
- what would we do if this deployment failed?
- what would we do if the deployment succeeded technically but was still not acceptable?
- how would we return to the last known good state?
- which stage should include this recovery awareness?

The goal is to treat rollback as part of design, not as panic after failure.

## Step 12 — Document a simple rollback approach
For this lab, define a simple rollback story.

Examples:
- redeploy the last successful artifact
- stop promotion to the next stage
- restore the previously accepted version
- keep rollback documentation tied to stage history

This step matters because mature delivery includes both forward movement and safe retreat.

## Step 13 — Reflect on delivery discipline
Pause and think beyond the mechanics.

In this module, CD means:
- deployment is a controlled promotion process
- environments create risk boundaries
- approvals improve release confidence
- rollback protects operational safety

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- the CI artifact is being used as deployment input
- at least one deployment stage exists
- environment or stage logic is visible
- approval thinking is included
- rollback thinking has been documented clearly
- the learner understands the difference between build validation and delivery promotion

## Step 14 — Prepare for package and reuse thinking
Before moving to the next module, understand the next workflow step.

The next module focuses on Azure Artifacts and package management strategy. Once the learner sees how build outputs and deployment flow work, the next logical question is how reusable outputs can be stored, versioned, and consumed consistently across teams and pipelines.

This is the bridge from release flow into package strategy.

---

## Implementation notes
- keep the release path simple in this module
- focus on delivery logic, not environment complexity
- make stage names and responsibilities obvious
- treat approvals as meaningful control points
- make rollback part of the design conversation, not an afterthought

## End-of-implementation summary
In this lab, you:
- reviewed the CI artifact
- defined a deployment scenario
- created one or more release stages
- introduced environment progression
- included approval thinking
- documented rollback awareness
- observed a full release-oriented workflow

You are now ready to validate whether the CD lifecycle is clean, correct, and explainable.
