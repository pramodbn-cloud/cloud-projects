# Folder 06 — Azure Artifacts: Package Management Strategy
![Week-6 Plan](../Posts/6.png)

## Overview
This module introduces Azure Artifacts as the package management layer of the delivery ecosystem. It helps the learner understand that modern engineering teams do not only build and deploy applications — they also create, version, store, share, and consume reusable packages in a controlled way.

This is where the course moves from pipeline-produced build outputs into a more mature understanding of reusable delivery assets. The learner begins to see how feeds, package versions, consumption patterns, and upstream sources support scale, consistency, and team-wide reuse.

## Why this module matters
In real engineering environments, teams rarely rebuild everything from scratch every time. They reuse internal libraries, shared components, deployment bundles, and common dependencies. Without a package management strategy, this reuse becomes inconsistent, difficult to govern, and hard to scale.

Azure Artifacts gives teams a structured way to host and manage packages through feeds, control package visibility, and consume both internal packages and upstream packages from trusted public sources. This makes delivery more consistent and reduces dependency chaos.

This module builds that reuse mindset.

## What you will learn
- What Azure Artifacts is and how feeds support package management
- Why internal package reuse matters in scalable delivery workflows
- How package publishing and consumption work at a high level
- Why upstream sources and package visibility are important in team environments

## Workflow position
This module builds on Folder 04 and Folder 05, where the learner understood build outputs, artifacts, and controlled delivery flow. Now the learner moves from one-time pipeline outputs into reusable package strategy.

This module also prepares the learner for security, compliance, and later advanced delivery patterns by introducing package governance and dependency control thinking early.

## Included in this folder
- Module overview
- Post image
- Hands-on lab
- Validation guide
- Troubleshooting guide
- Cleanup guide

## Expected outcome
By the end of this module, the learner should be able to:
- explain the difference between pipeline artifacts and managed packages
- understand what an Azure Artifacts feed is
- create a simple package publishing and consumption flow
- explain why package versioning and upstream sources matter in real projects

## Recommended approach
1. Read this overview fully  
2. Review the post image inside `post-assets/`  
3. Complete the lab files in order  
4. Validate the feed, package, and consumption flow carefully  
5. Do not move ahead until the package lifecycle feels clear and reusable  

## Next module
The next module is **Security + Compliance: DevSecOps Basics**.

That module will build on package management by showing how secure delivery depends not only on code and pipelines, but also on permissions, secrets, service connections, dependency trust, and delivery governance.
