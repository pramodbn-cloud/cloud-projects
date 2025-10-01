# Validation Checks

## Purpose of this file
This file confirms whether the Domain Name Based Routing lab is complete and correct.

The goal is not only to verify that host rules exist, but to confirm that the learner understands how DNS names and ingress host matching combine to route requests to the correct backend services.

## Validation approach
For this lab, validation is based on:
- backend readiness
- DNS readiness
- ingress rule correctness
- host-specific routing success
- controller/rule alignment
- learner explanation ability

## Check 1 — Multiple backends are healthy
Confirm that:
- all intended backend applications are running
- each Service maps correctly to its backend
- each backend can be reasoned about independently

This proves that backend instability is not the source of the routing problem.

## Check 2 — The Azure DNS hostnames are correct
Confirm that:
- each hostname exists inside the delegated Azure DNS zone
- each hostname is intended for the correct application
- each hostname points to the ingress-facing endpoint as expected

This proves that the naming layer is correct before ingress host matching is blamed.

## Check 3 — ExternalDNS or DNS management alignment is correct
Confirm that:
- the DNS records were created as intended
- the learner understands whether the records were automated by ExternalDNS or managed by the chosen lab design
- the hostnames and ingress design are aligned

This proves that the DNS and ingress layers are not drifting apart.

## Check 4 — The ingress controller and host rules align correctly
Confirm that:
- the expected ingress controller is active
- the ingress object uses the correct class
- the host rules are readable and structurally correct
- each hostname points to the intended backend Service

This proves that the routing logic is being expressed correctly.

## Check 5 — Each hostname reaches the correct backend
Confirm that:
- requests to the first hostname reach backend A
- requests to the second hostname reach backend B
- the responses clearly indicate the expected routing outcome

This is the main technical success signal for the module.

## Check 6 — The learner can explain the hostname-routing chain
Confirm that the learner can clearly explain:
- public hostname resolution in Azure DNS
- ingress endpoint entry
- ingress host inspection
- Service selection
- pod-level request handling

This proves that the learner understands host-based routing as a combined DNS-and-ingress system.

## Check 7 — The learner can explain why hostname routing matters
Confirm that the learner can explain:
- why host-based routing often feels cleaner than path-based routing for public apps
- why application identity becomes clearer with distinct hostnames
- why this makes later TLS integration more natural

This proves that the learner is thinking in platform patterns, not only ingress syntax.

## Check 8 — You can explain why this module is the right step after ExternalDNS
This is the most important validation for this module.

The learner should now be able to explain:
- why DNS authority and DNS automation had to come first
- why hostnames now become meaningful routing keys
- how one ingress entry point can still front multiple hostnames
- why this pattern is more production-like than path-only separation in many cases

If the learner can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the backends are healthy
- the hostnames are correct in Azure DNS
- the ingress host rules are readable
- each hostname reaches the intended backend
- the learner understands host-based routing as a production-style exposure pattern

## If validation fails
If any validation step fails:
- validate each backend independently
- validate DNS records separately
- verify ingress host rules and service targets
- verify controller and ingress-class alignment
- use `troubleshooting.md` for common hostname-routing issues
