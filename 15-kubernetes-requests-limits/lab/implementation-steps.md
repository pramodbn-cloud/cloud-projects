# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the Kubernetes Requests + Limits lab.

The goal is to create one clear workload-resource-governance path where the learner can observe how explicit CPU and memory requests and limits improve scheduling clarity and runtime control.

---

## Step 1 — Understand the resource-governance goal
Before changing any manifests, understand what this module is trying to teach.

This lab is not only about adding numeric values to YAML. It is about making the workload tell the cluster:

- what it expects to need
- how much it should be allowed to consume
- how it should behave inside a shared environment

At the end of this lab, you should have:
- one sample workload
- one explicit set of requests and limits
- one clear explanation of scheduler versus runtime control

## Step 2 — Reconfirm cluster and node readiness
Use kubectl to confirm that:
- the AKS cluster context is correct
- nodes are healthy
- the cluster has enough available capacity for the sample workload
- the environment is stable enough to observe scheduling behavior

This step matters because resource-related reasoning becomes misleading if the cluster itself is already unhealthy.

## Step 3 — Deploy or review the sample workload without strong resource definitions
Start with a simple workload that either:
- has no explicit requests/limits, or
- has intentionally incomplete resource definitions for comparison

This establishes the “before” state.

At this stage, the learner should observe that Kubernetes can still run the workload, but the resource contract is weaker and less explicit.

## Step 4 — Review the workload from a scheduler perspective
Now think about what the scheduler actually knows at this point.

Ask:
- how much CPU does the pod say it needs?
- how much memory does it say it needs?
- if those values are missing or weak, how predictable is scheduling?

This is one of the first major learning moments in the module. Requests are primarily scheduler-facing signals. Kubernetes official docs make this distinction very clearly.

## Step 5 — Define CPU and memory requests
Now update the workload to include clear requests.

These values should represent:
- the amount of CPU the workload regularly needs
- the amount of memory the workload regularly needs

The learner should understand that requests are not maximums. They are the scheduler-facing contract for expected need.

## Step 6 — Define CPU and memory limits
Now define clear limits for the same workload.

These values should represent:
- the upper bound of CPU the workload may use
- the upper bound of memory the workload may consume

The learner should understand that limits are different from requests. Limits are runtime guardrails. Kubernetes docs are explicit that containers cannot use more than their configured CPU or memory limits.

## Step 7 — Apply the updated workload
Apply the workload with the new requests and limits.

At this stage, inspect:
- whether the updated workload is accepted cleanly
- whether the pod is scheduled successfully
- whether the workload description now clearly shows the resource contract

This is where the resource-governance model becomes visible.

## Step 8 — Review the scheduled outcome
Now inspect the pod or deployment and review what changed.

The learner should focus on:
- how the workload now presents explicit resource expectations
- how this affects confidence in scheduling
- how this would scale better in a shared multi-team environment than leaving the workload undefined

This is the core scheduler-awareness moment of the module.

## Step 9 — Review runtime protection thinking
Now step beyond placement and think about runtime containment.

Ask:
- what happens if this workload suddenly tries to consume far more than expected?
- why is a limit useful in a shared cluster?
- how do limits reduce the chance that one workload harms others?

This is where the learner starts thinking like a platform operator, not only a workload deployer.

## Step 10 — Compare the “before” and “after” states
Now compare the original state and the updated state.

The learner should be able to explain:
- before: the workload gave the cluster weak resource information
- after: the workload gives both a scheduling contract and a runtime boundary

This comparison is one of the most important conceptual outputs of the module.

## Step 11 — Connect requests and limits to later policy controls
Now connect this module to later governance patterns.

Explain that:
- namespaces can carry policy and boundary meaning
- LimitRanges can enforce defaults or constraints
- ResourceQuotas can control aggregate namespace consumption

Kubernetes documentation explicitly connects requests/limits with namespace-level policy tools like LimitRange and ResourceQuota.

This makes requests and limits feel like part of a broader governance system rather than isolated numbers.

## Step 12 — Review AKS best-practice expectations
Now step back and connect this to AKS-specific guidance.

AKS best-practice documentation recommends defining pod requests and limits on all pods, and notes that without them the scheduler lacks important placement information and quota-enforced clusters may reject deployments.

The learner should understand that this is not “extra polish.” It is expected workload hygiene.

## Step 13 — Explain the resource-governance lifecycle end to end
Now explain the flow in plain language:

- a workload is defined
- requests tell the scheduler what the workload needs
- the scheduler places it where that need can fit
- limits define how far the workload may grow at runtime
- the cluster becomes more predictable and safer for shared use

If the learner can explain this clearly, the module is doing its real job.

## Step 14 — Reflect on workload discipline as production readiness
Pause and think beyond the YAML.

In this module, requests and limits mean:
- applications become more predictable citizens of the cluster
- the scheduler has meaningful information to work with
- runtime overuse is better controlled
- shared clusters become easier to operate safely

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- a sample workload is deployed
- explicit CPU and memory requests are defined
- explicit CPU and memory limits are defined
- the scheduler-visible contract is clearer than before
- runtime boundary thinking is present
- the learner understands why unmanaged resource usage is risky

## Step 15 — Prepare for namespace-level governance
Before moving to the next module, understand what changes next.

The next module is **Kubernetes Namespaces**. That means the learner will now move from per-workload resource discipline into logical isolation and policy boundaries, which naturally extend this resource-governance model.

This is the bridge from workload contract into namespace-level governance.

---

## Implementation notes
- keep the first resource-governance lab simple and deterministic
- do not tune for perfection; tune for understanding
- separate scheduling logic from runtime-limit logic clearly
- compare before and after explicitly
- focus on predictability and safety, not only “cluster acceptance”

## End-of-implementation summary
In this lab, you:
- reconfirmed cluster readiness
- observed a workload before strong resource controls
- added CPU and memory requests
- added CPU and memory limits
- reviewed scheduler-facing and runtime-facing effects
- connected requests/limits to later policy controls
- practiced the first true internal workload-governance pattern in the AKS phase

You are now ready to validate whether the requests-and-limits lifecycle is clean, correct, and explainable.
