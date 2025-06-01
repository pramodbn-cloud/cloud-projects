# Lab Guide — Azure Artifacts: Package Management Strategy

## Lab objective
The objective of this lab is to help the learner understand and configure a simple Azure Artifacts package workflow using a feed, a published package, and a basic consumption path.

This lab focuses on feed creation, package strategy, version awareness, internal reuse, and upstream source thinking. The goal is not to build a large enterprise package platform, but to make the learner comfortable with how reusable outputs are managed professionally inside Azure DevOps.

## What you will build or configure
In this lab, you will create or configure an Azure Artifacts feed, choose a simple package scenario, publish a package or reusable output into that feed, and review how it can be consumed in a controlled way.

You will also introduce package visibility, upstream source awareness, and versioning discipline so that the learner sees package management as a real delivery strategy rather than just storage.

## Why this lab matters
Pipeline artifacts are useful for one workflow run, but package management is about repeatable reuse across teams, services, and pipelines.

This lab matters because reusable engineering systems depend on clearly versioned, centrally managed components. Azure Artifacts feeds provide that structure and can also include upstream sources from public registries, which helps centralize dependency use.

## Estimated time
40 to 55 minutes

## Lab file reading order
Follow the files in this order:

1. `architecture-flow.md`
2. `prerequisites.md`
3. `implementation-steps.md`
4. `validation-checks.md`
5. `troubleshooting.md`
6. `cleanup.md`

## Expected final outcome
By the end of this lab, the learner should have:
- a working Azure Artifacts feed
- a clear understanding of package publishing and consumption flow
- a basic reusable package scenario
- awareness of versioning and upstream source strategy
- confidence in explaining why package management supports scalable delivery

## Skills gained
- Creating and understanding Azure Artifacts feeds
- Thinking in terms of reusable packages instead of only pipeline outputs
- Understanding package publishing and consumption flow
- Building early awareness of visibility, versioning, and upstream dependency strategy

## Real-world relevance
In real engineering teams, reusable packages often support shared libraries, templates, build tooling, deployment components, and internal standards. Azure Artifacts feeds allow teams to host packages, control access, and centralize dependency management across projects and organizations.

## Completion standard
A learner should not mark this lab complete until:
- a feed exists and is understandable
- the package flow is visible
- publishing and consumption logic are clear
- versioning and upstream thinking are understood
- validation confirms the workflow works correctly
