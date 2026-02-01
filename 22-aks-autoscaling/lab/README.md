# Lab Guide — AKS Autoscaling

## Lab objective
The objective of this lab is to help the learner understand and implement AKS autoscaling through a combination of Horizontal Pod Autoscaler and Cluster Autoscaler patterns.

This lab focuses on pod elasticity, node-pool elasticity, resource-driven scheduling pressure, and the relationship between workload demand and cluster capacity. The goal is not to tune a highly specialized production autoscaling policy yet, but to make the learner comfortable with the two main autoscaling layers that shape runtime elasticity in AKS.

## What you will build or configure
In this lab, you will deploy or review a sample workload, apply or review an HPA policy for it, enable or inspect Cluster Autoscaler settings on the node pool, and validate how the platform reacts as demand increases.

This creates the first true elastic-capacity workflow in the course.

## Why this lab matters
A mature AKS platform should not require constant manual resizing of replica counts and node pools. Instead, the platform should respond to changing demand in a controlled and observable way.

Kubernetes documents HPA as the mechanism that automatically changes the number of pods for a workload based on metrics. AKS documents Cluster Autoscaler as the mechanism that changes node-pool size when pending pods need capacity or nodes become underutilized. AKS also notes that HPA can continue to run even if cluster autoscaler is disabled, but pods may remain unscheduled if node resources are exhausted.

## Estimated time
60 to 75 minutes

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
- a clear understanding of pod autoscaling and node autoscaling
- one workload with an HPA pattern
- one AKS node-pool autoscaling pattern enabled or reviewed
- confidence in explaining how demand can propagate from load to pods to nodes

## Skills gained
- Understanding HPA in practical workload terms
- Understanding Cluster Autoscaler in node-pool terms
- Thinking about requests, scheduling, and scale as one system
- Preparing for stronger capacity, cost, and performance design later

## Real-world relevance
In real AKS platforms, workload elasticity is rarely solved at only one layer. HPA helps workloads expand horizontally, while Cluster Autoscaler ensures there is enough node capacity to host the additional pods. Microsoft’s performance and well-architected guidance recommends load testing and tuning both forms of autoscaling together.

## Completion standard
A learner should not mark this lab complete until:
- the HPA concept is clear
- the Cluster Autoscaler concept is clear
- the learner understands how they interact
- validation confirms the autoscaling chain end to end
