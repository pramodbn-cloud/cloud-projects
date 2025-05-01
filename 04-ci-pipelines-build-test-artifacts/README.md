# Folder 04 — CI Pipelines: Build + Test + Artifacts
![Week-4 Plan](../Posts/4.png)

## Overview
This module introduces Continuous Integration as the workflow that automatically validates code changes whenever development work is pushed into the shared repository. It helps the learner understand how source control and automation come together to create a reliable engineering system.

This is where the course starts moving from manual repository workflow into automated delivery discipline. The learner begins to see how builds, tests, and artifacts form the first layer of technical trust in a modern DevOps pipeline.

## Why this module matters
A repository alone is not enough to protect quality. Teams need a way to automatically check whether changes are buildable, whether basic verification succeeds, and whether usable outputs can be produced consistently.

Without CI, every code change depends too heavily on manual trust. That slows teams down, increases risk, and makes integration fragile. CI pipelines reduce that risk by ensuring every meaningful change goes through a repeatable validation path.

This module builds that automation mindset.

## What you will learn
- What a CI pipeline is and why it is essential in modern delivery
- How build, test, and artifact stages fit together in one workflow
- How repository changes can trigger automated validation
- Why CI is the foundation for safe and scalable release workflows

## Workflow position
This module builds directly on Folder 03, where the learner established repository, branch, commit, and pull request workflow. Now the learner moves from controlled code collaboration into automated code validation.

This module also prepares the learner for Folder 05, where the outputs created here will become part of release and deployment workflows.

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain the role of CI in a delivery lifecycle
- create a basic Azure DevOps pipeline connected to a repository
- understand how build and test steps work together
- produce and validate an artifact for later pipeline stages

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the trigger, build, test, and artifact flow carefully  
5. Do not move ahead until the pipeline lifecycle feels understandable end to end  

## Next module
The next module is **CD Pipelines: Deployments + Approvals + Rollback**.

That module will build on the outputs from CI and show how validated artifacts move into controlled deployment workflows. Once the learner understands how changes are automatically verified, the next step is to understand how those changes are promoted safely across environments.
