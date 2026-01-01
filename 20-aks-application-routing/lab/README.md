# Lab Guide — AKS Application Routing

## Lab objective
The objective of this lab is to help the learner understand and implement the AKS Application Routing add-on as a managed ingress-controller option, and to compare it with the more explicit ingress-controller patterns covered earlier in the course.

This lab focuses on managed ingress behavior, Azure DNS integration, ingress exposure through the add-on, and platform trade-off reasoning. The goal is not to replace the learner’s understanding of ingress internals, but to show how AKS can provide a managed path that reduces operational ownership in some scenarios.

## What you will build or configure
In this lab, you will enable or review the AKS Application Routing add-on, inspect the managed ingress-controller behavior, connect it to a sample ingress scenario, and validate how it exposes traffic through the managed pattern.

This creates the first true managed-ingress comparison point in the course.

## Why this lab matters
A strong AKS engineer should understand both:
- how ingress works when you manage the controller yourself, and
- how ingress works when AKS provides a managed add-on experience.

Microsoft documents the Application Routing add-on as the recommended ingress-controller path in AKS and states that it provides managed NGINX ingress plus Azure DNS integration. It also uses a CRD called `NginxIngressController` for configuration and requires managed identity.

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
- a clear understanding of the AKS Application Routing add-on
- a configured or reviewed managed ingress path
- a comparison model between managed and self-managed ingress approaches
- confidence in explaining when this approach makes sense operationally

## Skills gained
- Understanding managed ingress in AKS
- Comparing operational responsibilities between managed and self-managed ingress
- Thinking about Azure-integrated routing options as platform design choices
- Preparing for more production-grade governance decisions

## Real-world relevance
In real AKS environments, teams often have to choose between managing ingress components directly or using a managed add-on. The Application Routing add-on exists precisely to reduce operational burden in supported scenarios, while still offering Azure DNS integration and managed NGINX behavior.

## Completion standard
A learner should not mark this lab complete until:
- the managed-routing concept is clear
- the add-on behavior is understandable
- the learner can compare it to earlier ingress patterns
- validation confirms the managed-platform trade-off reasoning end to end
