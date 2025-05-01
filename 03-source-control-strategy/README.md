# Folder 03 — Source Control Strategy
![Week-3 Plan](../Posts/3.png)

## Overview
This module introduces source control as the structured system that allows teams to manage code safely, collaborate without conflicts, and preserve delivery history with clarity. It helps the learner understand that repositories are not just storage locations for files, but the operational foundation for modern engineering collaboration.

This is the point where the course moves from planning into actual implementation workflow. The learner begins to see how work that was defined in Azure Boards can now be translated into controlled code activity through repositories, branches, commits, and pull requests.

## Why this module matters
In real delivery environments, multiple engineers work on the same codebase at different times and often on overlapping features. Without a disciplined source control strategy, changes collide, code quality drops, reviews become weak, and teams lose confidence in what is being merged into the main line.

Source control is not just a technical skill. It is a workflow discipline that protects team velocity, reduces chaos, and keeps delivery traceable. This module builds that discipline early, before the learner reaches CI/CD and deployment automation.

## What you will learn
- How Azure Repos supports team-based source control workflows
- Why branches are used and how branch strategy protects the codebase
- How commits and pull requests fit into the collaboration lifecycle
- Why source control strategy is essential before building pipelines and releases

## Workflow position
This module builds on Folder 02, where work was planned and structured inside Azure Boards. Now the learner moves from planned work into implementation workflow.

This module also prepares the learner for Folder 04, where code changes will start triggering CI pipelines. Without a clean repository and branching model, pipeline workflows become much harder to understand and manage.

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain the purpose of source control in modern engineering teams
- create and use a repository in Azure DevOps
- understand how branches support safe development
- create a basic pull request workflow with clear collaboration intent

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the repository and branch workflow carefully  
5. Do not move ahead until the repo flow feels natural and explainable  

## Next module
The next module is **CI Pipelines: Build + Test + Artifacts**.

That module will build directly on this repository workflow. Once the learner understands how code is stored, versioned, and reviewed, the next logical step is to automate validation of those changes through a CI pipeline.
