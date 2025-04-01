# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the Azure DevOps foundation setup lab.

The goal is to establish a clean starting environment that will support every later module in the repository.

---

## Step 1 — Understand the setup goal
Before creating anything, take a moment to understand what this module is trying to achieve.

This module is not about pipelines, deployments, or Kubernetes. It is about creating the base environment where those things can be learned later without setup-related confusion.

At the end of this lab, you should have:
- Azure DevOps access
- a working organization and project
- a prepared local machine
- enough confidence to continue into actual workflow modules

## Step 2 — Sign in to Azure DevOps
Open Azure DevOps in your browser and sign in using your Microsoft or work account.

Once you sign in, observe the interface calmly. Do not rush ahead. The aim here is to become familiar with the platform at a basic level.

At this stage, confirm that:
- the portal opens properly
- your account signs in successfully
- you can navigate the home screen without access errors

## Step 3 — Create or confirm an Azure DevOps organization
If you do not already have an organization, create one.

Choose a clean and professional name. Keep it simple and reusable. Do not overcomplicate naming at this stage.

If an organization already exists and you are intentionally reusing it for this course, confirm that:
- it is accessible
- you have working control inside it
- it is suitable for repeated practice

The purpose of this step is to establish the top-level working boundary for the rest of the course.

## Step 4 — Create the working project
Inside the organization, create a new project for this repository journey.

Use a name that clearly reflects the learning purpose. Keep it easy to identify later.

Examples:
- Azure-DevOps-Foundation
- Azure-DevOps-AKS-Learning
- Job-Ready-DevOps-AKS

While creating the project, pay attention to:
- project name
- description
- visibility choice
- version control option
- work item process option

The goal is not to optimize every setting yet. The goal is to create a clean, usable project space for future modules.

## Step 5 — Explore the core Azure DevOps services at a high level
Once the project is created, open the main service areas and observe them:

- Boards
- Repos
- Pipelines
- Artifacts
- Project Settings

You do not need to configure everything now. You only need to become comfortable with the fact that this one platform will later support planning, code, builds, releases, and package management.

This step matters because many beginners feel lost simply due to lack of interface familiarity.

## Step 6 — Prepare the local machine
Now move to the local environment.

Open your terminal and confirm that the following are installed and working:

- Git
- Azure CLI
- editor access

You do not need advanced usage yet. Just confirm that the tools are available and can be invoked from the terminal.

This step is important because later modules will depend on local repo work, command execution, and cloud interaction.

## Step 7 — Create a local working folder for the course
On your machine, create a dedicated working directory for this full repository journey.

Example:
- `azure-devops-aks-job-ready`
- `ado-aks-learning`
- `azure-course-labs`

Inside that folder, you are not required to build the full repo yet for this lab, but you should establish the habit of working in a dedicated, organized space.

This improves repeatability and reduces confusion later.

## Step 8 — Document your chosen naming and setup decisions
Write down:
- organization name
- project name
- local root folder name
- chosen naming style
- any environment notes that may matter later

This may seem small, but it is extremely useful in later labs when multiple services and resources begin to appear.

## Step 9 — Review your current setup state
At this point, pause and review whether the foundation is truly ready.

Ask yourself:
- Can I access Azure DevOps properly?
- Do I have a working organization?
- Do I have a project created?
- Is my local terminal ready?
- Are my core tools installed?
- Do I understand where later modules will happen?

If the answer is yes, you are ready for validation.

---

## Checkpoint
At this point, the following should already be true:

- Azure DevOps is accessible
- a clean organization exists or is confirmed
- a working project is available
- the learner understands the purpose of Boards, Repos, Pipelines, and Artifacts at a high level
- the local environment is ready for future hands-on work

## Step 10 — Prepare for the next module
Before leaving this lab, make sure you are mentally ready for the next step in the course.

The next module moves into Agile Planning and Traceability. That means your project space should now feel real and usable, not just created for formality.

You are now ready to move from platform setup into work-structuring logic.

---

## Implementation notes
- Do not over-engineer the project settings in this module
- The focus is readiness, not feature depth
- Keep names simple and consistent
- Avoid creating multiple test organizations unless necessary
- Treat this module as the platform foundation for the full learning journey

## End-of-implementation summary
In this lab, you established the starting working environment for the repository by:
- accessing Azure DevOps
- creating or confirming the organization
- creating the learning project
- reviewing the major service areas
- preparing the local machine
- organizing the initial working space

You are now ready to validate that the foundation is complete.
