# Validation Checks

## Purpose of this file
This file confirms whether the Ingress Context Path Routing lab is complete and correct.

The goal is not only to verify that path rules exist, but to confirm that the learner understands how a single ingress entry point can deterministically route multiple requests to different services.

## Validation approach
For this lab, validation is based on:
- backend readiness
- service correctness
- ingress rule correctness
- controller/rule alignment
- path-specific routing success
- learner explanation ability

## Check 1 — Multiple backends are healthy
Confirm that:
- all intended backend applications are running
- pod health is stable
- each backend can be validated independently behind its own Service

This proves that the backends themselves are not causing the routing failure.

## Check 2 — Each Kubernetes Service is correct
Confirm that:
- each Service exists
- each Service selects the correct pods
- ports and target ports are aligned correctly
- the Services are the intended routing targets for the ingress rules

This proves that the internal routing destinations are healthy.

## Check 3 — The ingress controller and ingress class align correctly
Confirm that:
- the cluster has the expected ingress-controller strategy
- the ingress resource uses the correct ingress class
- the controller is responsible for implementing the routing rules

This is especially important because the updated course guidance emphasizes the modern ingress class field usage in these modules.

## Check 4 — The ingress rule set is structurally correct
Confirm that:
- the ingress object exists
- multiple path rules are present
- each path points to the intended backend service
- the rule structure is readable and deterministic

This proves that the routing logic is being expressed correctly.

## Check 5 — The shared ingress endpoint is externally usable
Confirm that:
- the ingress endpoint is ready
- external requests reach the ingress layer successfully
- the shared entry point is stable enough for multi-service routing

This proves that the infrastructure side of the route entry point is healthy.

## Check 6 — Each path reaches the correct backend
Confirm that:
- requests to `/app1` reach backend A
- requests to `/app2` reach backend B
- responses clearly indicate the correct routing outcome

This is the main technical success signal for the module.

## Check 7 — The learner can explain the route-selection chain
Confirm that the learner can clearly explain:
- one public entry point
- ingress controller path inspection
- path rule match
- Service selection
- pod-level request handling

This proves that the learner understands routing logic as a traffic system.

## Check 8 — The learner can explain why path routing matters
This is the most important validation for this module.

The learner should now be able to explain:
- why one ingress endpoint can front multiple services
- why path-based routing is useful before hostname-based routing
- why this pattern reduces fragmented exposure
- why it is a practical next step after ingress basics

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the backends are healthy
- the Services are correct
- the ingress rule set is readable
- the shared ingress endpoint routes correctly by path
- the learner understands context-path routing as a platform pattern

## If validation fails
If any validation step fails:
- validate each backend independently
- validate each Service next
- verify ingress rule targets and path mappings
- verify controller and ingress-class alignment
- use `troubleshooting.md` for common path-routing issues
