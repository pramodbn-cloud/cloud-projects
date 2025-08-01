# Validation Checks

## Purpose of this file
This file confirms whether the AKS Ingress Basics lab is complete and correct.

The goal is not only to verify that an ingress object exists, but to confirm that the learner understands the real runtime traffic path from external entry to backend workload.

## Validation approach
For this lab, validation is based on:
- workload readiness
- service readiness
- ingress-controller readiness
- ingress-object correctness
- external traffic success
- learner explanation ability

## Check 1 — The backend workload is healthy
Confirm that:
- the application pods are running
- the deployment is stable
- the application responds correctly when tested through internal service validation

This proves that the backend is not the source of failure.

## Check 2 — The Kubernetes Service is correct
Confirm that:
- the Service exists
- it selects the correct pods
- ports and target mapping are correct
- the Service is the intended internal target for ingress

This proves that the middle layer of the traffic chain is healthy.

## Check 3 — The ingress controller path is available
Confirm that:
- an ingress-controller strategy is present in the cluster
- the learner understands which controller is implementing the ingress
- the ingress class relationship is correct

In AKS, ingress only becomes real when a controller implements it. Current course updates specifically emphasize the ingress class field in these sections.

## Check 4 — The ingress resource is correct
Confirm that:
- the ingress object exists
- the backend service reference is correct
- the ingress class is set correctly
- the rule structure matches the intended simple exposure model

This proves that the ingress definition itself is not malformed.

## Check 5 — The ingress endpoint becomes externally usable
Confirm that:
- the ingress receives an address or endpoint as expected
- the learner can identify where external traffic should arrive
- readiness timing is understood as part of the real runtime lifecycle

This proves that infrastructure and controller reconciliation have completed successfully.

## Check 6 — External traffic reaches the intended backend
Confirm that:
- a request to the ingress endpoint succeeds
- the intended application responds
- the learner can verify that the correct service path was used

This is the core technical success signal for the module.

## Check 7 — The learner can explain the request path
Confirm that the learner can clearly explain:
- client to ingress endpoint
- ingress controller to Service
- Service to pod
- response path back outward

This proves that the learner understands ingress as a traffic system, not only as a YAML object.

## Check 8 — The learner can explain why ingress matters
This is the most important validation for this module.

The learner should now be able to explain:
- why ingress exists
- why a Service alone is not the same thing as ingress
- why a controller is required
- why ingress is a better platform base for later routing, DNS, and TLS patterns
- why this is the correct starting point for the advanced AKS track

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the backend is healthy
- the Service is correct
- the ingress rule is implemented by the correct controller
- external traffic reaches the application successfully
- the learner understands ingress as a platform layer

## If validation fails
If any validation step fails:
- validate the backend first
- validate the Service next
- verify ingress class and controller alignment
- review endpoint readiness and reconciliation timing
- use `troubleshooting.md` for common ingress issues
