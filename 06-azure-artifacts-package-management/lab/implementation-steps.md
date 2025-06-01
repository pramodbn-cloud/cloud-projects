# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the Azure Artifacts lab.

The goal is to create one clear package management workflow that uses a feed, a reusable package, version identity, and a basic consumption model.

---

## Step 1 — Understand the package management goal
Before creating the feed, understand what this module is trying to teach.

This lab is not about uploading a random file into Azure DevOps. It is about learning the purpose of managed package reuse:

- create a reusable component
- publish it into a controlled feed
- version it clearly
- consume it consistently from a known source

At the end of this lab, you should have:
- one feed
- one package publishing flow
- one consumption understanding path
- one clear explanation of why this differs from CI artifacts

## Step 2 — Choose the package scenario
Decide what kind of package flow you want to model.

For a learning repo, choose a simple scenario. Examples:
- a small internal npm-style utility
- a simple NuGet-style reusable library
- a Universal Package style shared bundle
- a generic internal reusable component story

The goal is not package complexity. The goal is to understand the lifecycle.

## Step 3 — Open Azure Artifacts
Go to Azure DevOps and open the Artifacts area.

Spend a few minutes observing:
- feed selection
- package listing behavior
- settings area
- feed connection options
- package visibility model

Azure Artifacts uses feeds as the core management boundary for packages. Feeds can be project-scoped or organization-scoped, and can optionally include upstream sources from common public registries.

## Step 4 — Create the feed
Create a new feed for this learning module if one does not already exist.

While creating it, pay attention to:
- feed name
- visibility
- scope
- whether to include upstream sources

Azure Artifacts feed creation includes choices around visibility and scope, and you can enable packages from common public sources when creating the feed.

Keep the feed name clear and professional.

## Step 5 — Decide the visibility and reuse intention
Before publishing anything, define what this feed is meant to represent.

Ask:
- is this a team-internal reusable feed?
- is it only for this project?
- should it centralize dependencies from public sources?
- is it intended as a trusted internal package source?

This step matters because package management is as much about governance as it is about storage.

## Step 6 — Prepare the package or reusable output
Now prepare the simple package scenario selected earlier.

Keep it lightweight. The goal is to have something that can logically be published and later consumed.

At this stage, focus on:
- what the package represents
- why it would be reused
- how version identity will matter

This is the moment where the learner moves from raw project files into a reusable delivery asset mindset.

## Step 7 — Define the package version
Assign a version to the package.

This is important because package reuse depends on version identity. Without version discipline, teams lose clarity about what exactly they are consuming.

Use a simple versioning pattern that is easy to explain in the learning repository.

## Step 8 — Publish the package into the feed
Publish the package into the Azure Artifacts feed.

The exact publish mechanism may depend on the package type, but the important point is that the package becomes visible inside the feed as a managed, versioned entity.

Azure Artifacts provides package-type-specific publishing flows, including official guidance for NuGet, npm, Python, and Universal Packages.

After publishing, confirm that:
- the package appears in the feed
- the version is visible
- the feed now behaves like a reusable package source

## Step 9 — Review feed connection options
Open the feed connection guidance and observe how a consumer would connect to this feed.

This is one of the most important learning moments in the module because it shows that package management is not only about publishing. It is about standardized consumption.

Azure Artifacts provides feed connection guidance for supported ecosystems so projects can consume the feed correctly.

## Step 10 — Simulate or perform package consumption
Now review or perform a simple consumption path.

Examples:
- connect a sample project to the feed
- review how a package source would be added
- restore or download the package
- explain how a pipeline would later consume the same package

The goal is to make the publish-consume loop visible.

## Step 11 — Review upstream source strategy
Now introduce upstream source thinking.

If enabled, upstream sources allow packages from public registries or other Azure feeds to be available through the feed and be saved there when consumed. This helps centralize dependency management and improve reliability of package access.

For this lab, the learner should understand:
- why an organization might want public dependencies routed through its feed
- how that helps centralize dependency behavior
- why internal package strategy and upstream strategy can work together

## Step 12 — Review feed views and sharing mindset
Now introduce feed views at a high level.

Feed views help control which subset of packages is visible for broader sharing, which supports promotion and controlled exposure of package versions.

The learner should understand that package management includes visibility control, not only storage.

## Step 13 — Reflect on package strategy
Pause and think beyond the mechanics.

In this module, package management means:
- reusable outputs should be centrally managed
- packages should have clear identity and versioning
- teams need controlled publishing and consumption
- public dependencies can be centralized through upstream strategy
- feeds support scale and consistency better than ad hoc reuse

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- a feed exists and is understandable
- a simple package scenario has been chosen
- a package has been published or clearly modeled
- version identity is visible
- consumption flow is understood
- upstream source and visibility thinking have been introduced

## Step 14 — Prepare for security and compliance thinking
Before moving to the next module, understand the next workflow step.

The next module focuses on security and compliance. Once the learner understands feeds, packages, and dependency flow, the next logical question is how to protect delivery through permissions, secret handling, connection governance, and safe dependency practices.

This is the bridge from package reuse into DevSecOps thinking.

---

## Implementation notes
- keep the package scenario simple in this module
- focus on reuse and lifecycle, not package complexity
- make feed purpose and package purpose easy to explain
- treat versioning as identity, not decoration
- use upstream sources as a governance concept, not only a convenience feature

## End-of-implementation summary
In this lab, you:
- opened Azure Artifacts
- created or reviewed a feed
- defined a reusable package scenario
- assigned version identity
- published a package or modeled package publication
- reviewed package consumption flow
- introduced upstream source and visibility strategy
- practiced the full package management lifecycle at a learning scale

You are now ready to validate whether the package lifecycle is clean, correct, and explainable.
