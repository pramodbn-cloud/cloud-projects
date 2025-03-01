# Learning Path

This file explains the best way to move through the repository so that learning stays structured, practical, and high-value.

The goal is not just to finish modules.  
The goal is to build a deep, explainable, reusable understanding.

---

## Core Learning Principle

Every module in this repository should be approached in the same order:

1. Understand the topic
2. Understand why it matters
3. Understand where it fits in the larger workflow
4. Perform the hands-on lab
5. Validate results
6. Troubleshoot actively if needed
7. Clean up properly
8. Summarize the module in your own words

This repeated learning pattern is what creates long-term understanding.

---

## How to Study Each Module

## Step 1 — Read the module overview
Start with the module `README.md`.

At this stage, focus on:
- what the topic is
- why it matters
- what you are expected to learn
- how it connects to previous and next modules

Do not rush into the lab immediately.

## Step 2 — View the module visual
Open the image in `post-assets/`.

This helps create a visual memory of the workflow before implementation.

## Step 3 — Read the lab landing file
Open `lab/README.md`.

This tells you:
- the objective
- what you will build
- estimated effort
- lab file reading order
- expected final outcome

## Step 4 — Understand the architecture flow
Read `lab/architecture-flow.md`.

This is where you connect actions to system behavior.

## Step 5 — Check prerequisites
Read `lab/prerequisites.md`.

Confirm that:
- tools are ready
- permissions are sufficient
- dependent setup is already complete
- naming choices are clear

## Step 6 — Follow implementation carefully
Use `lab/implementation-steps.md`.

Move slowly and validate checkpoints during the lab instead of waiting until the end.

## Step 7 — Validate properly
Use `lab/validation-checks.md`.

Do not assume success.  
Always confirm what changed and why the outcome is considered correct.

## Step 8 — Use troubleshooting when needed
If anything behaves unexpectedly, go to `lab/troubleshooting.md`.

The purpose of troubleshooting is not only fixing.  
It is also understanding failure patterns.

## Step 9 — Perform cleanup
Always finish with `lab/cleanup.md`.

This matters for:
- cost control
- environment discipline
- readiness for the next module

## Step 10 — Capture proof of execution
After cleanup, update `lab/proof-of-execution.md` with:
- commands used
- key outputs
- screenshots or evidence links
- short validation notes

This turns each module into reviewable, portfolio-grade evidence.

---

## How to Take Notes

For every module, write down:

- what problem this module solves
- what service or feature was used
- what was built
- how validation was done
- what issues appeared
- what you learned from the troubleshooting
- how you would explain this in an interview or real project

This turns the repository into a portfolio-grade learning asset.

---

## How to Treat Foundation Modules

For modules 1 to 8:

- focus on delivery workflow clarity
- understand traceability and collaboration
- learn how builds, releases, approvals, and security connect together
- build confidence in explaining the DevOps lifecycle

These modules create the mental model for everything later.

---

## How to Treat Advanced Modules

For modules 9 to 23:

- think in architecture layers
- connect networking, security, deployment, and operations together
- understand dependencies between ingress, DNS, SSL, registry, identity, scaling, and cluster design
- avoid treating each topic as isolated

These modules should be studied more slowly and more deeply.

---

## Learning Standard to Aim For

After each module, you should be able to answer these questions clearly:

- What is this topic?
- Why is it needed?
- What problem does it solve?
- Where does it sit in the workflow?
- What did I configure or build?
- How did I validate it?
- What common issues can happen?
- How would I explain this to another engineer?

If you can answer these well, the module is truly learned.

---

## Revision Strategy

A strong revision approach:

- revise after every 3 modules
- summarize phase 1 before starting phase 2
- review advanced dependencies before production-grade design
- maintain one running note of key architecture lessons

---

## End Goal of the Learning Path

The goal is to reach a point where you can confidently explain:

- how teams plan work
- how code is reviewed
- how builds and releases happen
- how images are stored and deployed
- how traffic reaches AKS workloads
- how DNS and TLS secure exposure
- how permissions control access
- how autoscaling supports reliability
- how all of this becomes a production-aware delivery system

That is the real success condition for this repository.
