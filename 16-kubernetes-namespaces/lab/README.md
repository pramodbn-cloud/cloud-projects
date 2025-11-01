# Lab Guide — Kubernetes Namespaces

## Lab objective
The objective of this lab is to help the learner understand and implement namespace-based workload organization in AKS so that multiple applications, teams, or environments can coexist with clearer boundaries inside one cluster.

This lab focuses on logical separation, namespace-scoped resource visibility, naming clarity, and the connection between namespaces and later governance controls such as quotas, limits, and RBAC. The goal is not to build a large enterprise cluster hierarchy yet, but to make the learner comfortable with the core namespace model used in Kubernetes platforms.

## What you will build or configure
In this lab, you will create one or more namespaces, deploy or move workloads into them, observe namespace-scoped behavior, and compare namespaced organization with flat cluster usage.

This creates the first true cluster-organization and boundary-design workflow in the course.

## Why this lab matters
Namespaces are often one of the first structural decisions that make a Kubernetes cluster feel organized rather than chaotic. They create cleaner separation, improve naming discipline, and become the natural scope for later policy enforcement.

Kubernetes documentation explains that namespaces provide a scope for names and are intended for use in environments with many users spread across multiple teams or projects. This makes them especially important in shared AKS platforms. 

## Estimated time
45 to 60 minutes

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
- one or more namespaces created intentionally
- workloads placed into meaningful namespace boundaries
- a clear explanation of why namespace structure improves cluster organization
- confidence in explaining how namespaces prepare the cluster for stronger governance later

## Skills gained
- Understanding namespace-based resource grouping in AKS
- Thinking in terms of cluster organization rather than only workload deployment
- Connecting namespace boundaries to future policy controls
- Preparing for more advanced multi-team and multi-environment AKS patterns

## Real-world relevance
In real AKS environments, namespaces are commonly used to separate teams, applications, or environments such as dev, test, and prod. They are also the natural boundary for many governance controls, which makes them essential for scalable operations. 

## Completion standard
A learner should not mark this lab complete until:
- the namespace concept is clear
- workloads are organized inside meaningful namespace boundaries
- namespace-scoped behavior is understandable
- validation confirms that the cluster-organization pattern is correct
