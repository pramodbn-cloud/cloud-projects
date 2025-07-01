# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the Security + Compliance lab.

The goal is to create one clear DevSecOps-oriented workflow that reviews permissions, introduces a safer service connection model, and improves variable and secret handling.

---

## Step 1 — Understand the security goal
Before configuring anything, understand what this module is trying to teach.

This lab is not about adding random security settings. It is about understanding the trust model behind your delivery workflow:

- who can access what
- what a pipeline can do
- how secrets are handled
- how external systems are trusted
- how delivery can stay safer without becoming unworkable

At the end of this lab, you should have:
- one understandable permission view
- one service connection example or review
- one safer variable/secret pattern
- one clear explanation of least-privilege thinking

## Step 2 — Review Azure DevOps project security at a high level
Open Project Settings and review the security-related areas available to you.

Focus on understanding that Azure DevOps uses access levels, roles, groups, and inheritance to shape what users can do. The learner does not need to master every permission yet, but should understand that not all users should have equal control.

Ask:
- who should manage pipelines?
- who should manage service connections?
- who should only consume the system?
- where would broad access create risk?

## Step 3 — Review the concept of least privilege
Now translate what you saw into one practical principle: give only the access that is needed.

This is the key mental model for the module. The learner should understand that giving too much permission may make work convenient at first, but increases risk significantly later.

Keep this principle in mind for the rest of the lab:
- narrow permissions where possible
- avoid broad admin rights unless truly needed
- treat automation identities and connections carefully

## Step 4 — Open the Service connections area
Go to Project Settings and open Service connections.

Service connections are how Azure Pipelines connect to external systems such as Azure subscriptions and other services. Azure DevOps documents service connections as the mechanism to create, view, edit, and use these trusted endpoints.

Spend a few minutes observing:
- available service connection types
- how they are named
- where permissions and usage scope matter

## Step 5 — Create or review one Azure Resource Manager service connection
Create or inspect a simple Azure Resource Manager service connection if your setup supports it.

Azure DevOps documents Azure Resource Manager service connections and supports workload identity federation for authentication, which is the modern pattern to reduce reliance on long-lived secrets.

At this stage, focus on:
- what the connection is for
- what target it can access
- why this connection should not be over-permissioned
- why naming and ownership clarity matter

If you cannot create one in your environment, model the design conceptually.

## Step 6 — Review service connection trust boundaries
Pause and think about the service connection as a trust boundary.

Ask:
- what could a pipeline do if it used this connection?
- is the scope larger than necessary?
- should all pipelines be able to use it?
- who should be allowed to edit or approve it?

This step matters because many delivery risks begin with overly trusted external connections.

## Step 7 — Open the Library / Variable groups area
Go to the pipeline Library area and open Variable groups.

Azure DevOps documents variable groups as a way to store values and secrets that can be passed into pipelines and shared across pipelines in a project.

This step introduces the learner to a safer shared-configuration pattern.

## Step 8 — Create a variable group
Create one simple variable group for this learning module.

Include:
- one non-secret variable, such as an environment label
- one secret variable, such as a placeholder credential value

Do not put a real sensitive production secret into a casual training environment. The point is to understand the control model, not to expose real credentials.

This step teaches the learner that configuration and secrets should be separated from hardcoded pipeline definitions.

## Step 9 — Review secret handling rules
Now review how Azure DevOps expects secrets to be handled.

Azure DevOps states that secret variables should not be stored in plain text inside `azure-pipelines.yml`, and recommends setting secret variables in the UI, in variable groups, or via Key Vault-backed variable groups.

The learner should understand:
- secret handling is different from normal variable handling
- centralizing secrets improves control
- masking and controlled access reduce accidental exposure risk

## Step 10 — Link the variable group idea back to the pipeline
Now think about how an existing pipeline from Folder 04 or 05 would use the variable group.

You do not need to build a large example here. The important point is that:
- pipeline values can come from a managed location
- secrets can be referenced without hardcoding them
- shared configuration can stay consistent across runs

This is one of the most important learning moments in the module.

## Step 11 — Review secure files at a high level
Now introduce secure files briefly.

Azure Pipelines library also supports secure files for protected file-based content used across project pipelines. This helps when the sensitive material is file-based rather than plain variable text.

The learner should understand:
- not everything sensitive is a string variable
- secure files address a different but related need
- pipeline permissions still matter around their usage

## Step 12 — Review pipeline permissions and restricted sharing
Now think about which pipelines should be allowed to use which resources.

Azure DevOps documentation notes that variable groups and secure files can be restricted to a small set of pipelines using pipeline permissions.

This introduces an important governance concept:
- not every shared secret should be available to every pipeline
- delivery safety improves when use is intentionally limited

## Step 13 — Reflect on DevSecOps as design, not decoration
Pause and think beyond the mechanics.

In this module, DevSecOps means:
- permissions shape delivery trust
- service connections are controlled trust bridges
- secrets should be managed safely and centrally
- pipelines should not have more access than they need
- governance is part of delivery design, not a late-stage extra

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- the learner understands that Azure DevOps security is layered through permissions and inheritance
- a service connection example exists or is clearly understood
- a variable group pattern has been introduced
- safe secret handling principles are understood
- least-privilege thinking is visible
- pipeline/resource governance has been introduced

## Step 14 — Prepare for instrumentation and operational flow
Before moving to the next module, understand the next workflow step.

The next module focuses on monitoring, automation, notifications, and capstone flow. Once the learner understands how delivery should be protected, the next logical step is to understand how delivery should be observed and coordinated operationally.

This is the bridge from secure delivery into visible and manageable delivery.

---

## Implementation notes
- keep the security model simple and practical in this module
- focus on high-value control points, not every permission checkbox
- do not use real sensitive production values casually
- treat service connections and secrets as trust boundaries
- always connect security decisions back to delivery workflow behavior

## End-of-implementation summary
In this lab, you:
- reviewed Azure DevOps security at a project level
- introduced least-privilege thinking
- created or reviewed a service connection
- created a variable group with secret/non-secret separation
- reviewed secret handling guidance
- introduced secure files and restricted resource use
- practiced the core DevSecOps mindset inside Azure DevOps

You are now ready to validate whether the security lifecycle is clean, correct, and explainable.
