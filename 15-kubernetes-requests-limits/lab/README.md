# Lab Guide — Kubernetes Requests + Limits

## Lab objective
The objective of this lab is to help the learner understand and configure CPU and memory requests and limits in AKS so that workloads behave more predictably and the cluster scheduler has meaningful resource information to work with.

This lab focuses on scheduler expectations, container runtime boundaries, and the difference between “what a workload needs” and “what a workload is allowed to consume.” The goal is not to tune a highly optimized production application yet, but to make the learner comfortable with the core resource-governance model used in Kubernetes.

## What you will build or configure
In this lab, you will deploy or review a sample workload, observe it with minimal or no explicit resource controls, then define CPU and memory requests and limits and compare the resulting scheduling and runtime behavior.

This creates the first true workload-resource-discipline workflow in the course.

## Why this lab matters
In real AKS environments, requests and limits are one of the strongest foundations for predictable cluster behavior. They influence scheduling decisions, reduce resource ambiguity, and help prevent individual workloads from consuming resources in uncontrolled ways.

Kubernetes documents that requests inform scheduling and that limits cap resource use, while AKS best-practice guidance recommends defining requests and limits on all pods and notes that quota-enforced clusters may reject workloads that omit them.

## Estimated time
50 to 65 minutes

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
- a practical understanding of requests and limits
- one workload with explicit CPU and memory resource settings
- a clear explanation of how scheduling and runtime behavior change
- confidence in explaining why this is a production-readiness topic

## Skills gained
- Understanding CPU and memory requests in scheduling terms
- Understanding limits as runtime guardrails
- Thinking about workloads as resource citizens inside a shared cluster
- Preparing for quotas, namespaces, and autoscaling later

## Real-world relevance
In real AKS platforms, poor resource definitions often lead to difficult operational problems: unschedulable pods, unstable workloads, noisy-neighbor behavior, and weak capacity planning. Clear requests and limits are one of the most basic but most important workload hygiene practices.

## Completion standard
A learner should not mark this lab complete until:
- the difference between requests and limits is clear
- the workload uses explicit resource definitions
- scheduler/runtime behavior can be explained clearly
- validation confirms the resource-governance pattern end to end
