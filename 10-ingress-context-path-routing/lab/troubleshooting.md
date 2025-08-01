# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the Ingress Context Path Routing lab.

In this module, the most common failures usually come from broken backend services, ambiguous or incorrect path rules, controller-class mismatches, or assuming the ingress object itself is enough without checking how the controller is interpreting the rules. The goal is to strengthen traffic-routing reasoning, not only fix YAML.

---

## Common issue 1 — One path works, but another path does not

### Symptoms
- `/app1` works but `/app2` fails
- only one backend appears reachable
- the learner assumes the ingress layer is partially broken

### Likely cause
The most common cause is that one backend service or one path target is configured incorrectly. Path routing exposes backend asymmetry quickly.

### Fix
- validate the failing backend independently through its Service
- confirm the Service selector and port mapping
- inspect the ingress rule for the failing path
- verify the path-to-service mapping carefully

### Re-validation
After the fix:
- test the failing path again
- confirm both paths now route to their intended backends

---

## Common issue 2 — All paths return the same backend unexpectedly

### Symptoms
- different paths appear to hit the same application
- the routing logic feels ignored
- the learner cannot tell whether the rule set is being interpreted correctly

### Likely cause
The ingress rule order or backend references may be incorrect, or the backends may not be visually distinguishable enough to validate properly.

### Fix
- make backend responses clearly different
- inspect the ingress rules carefully
- verify each path points to the intended Service
- retest with unambiguous backend responses

### Re-validation
After the fix:
- confirm that each path now produces a distinct backend-specific response

---

## Common issue 3 — Path rule exists, but controller does not appear to honor it

### Symptoms
- the ingress object is present
- the shared endpoint exists
- path routing behavior does not match the manifest
- the learner suspects a controller issue

### Likely cause
The ingress class may not align with the controller, or the controller may not be responsible for the ingress resource being used.

### Fix
- inspect the ingress class field
- verify which controller is active
- confirm that the controller is intended to process this ingress object
- align the ingress object with the actual controller strategy

### Re-validation
After the fix:
- inspect the ingress again
- retest path behavior against the same shared endpoint

---

## Common issue 4 — The learner is troubleshooting ingress before validating the backends

### Symptoms
- path tests fail
- the learner repeatedly edits ingress rules
- backend or Service validation was skipped

### Likely cause
The learner is diagnosing at the wrong layer. Ingress depends on healthy Services and backends underneath it.

### Fix
- stop editing ingress rules temporarily
- validate backend A directly
- validate backend B directly
- validate Service A and Service B
- only return to the ingress layer once the lower layers are confirmed

### Re-validation
After the fix:
- reapply attention to the ingress rule only after each lower layer is known-good

---

## Common issue 5 — The learner completes the lab but still does not understand why path routing is important

### Symptoms
- the technical steps are complete
- the learner still sees path rules as only a manifest pattern
- the advanced-track shift still feels shallow

### Likely cause
The learner may still be thinking about “getting traffic in” rather than “designing shared traffic entry.”

### Fix
Reframe path routing like this:
- one public entry point can front multiple services
- route structure becomes a platform concern
- teams can centralize access and reduce endpoint fragmentation
- this pattern is a bridge toward DNS-based and TLS-based exposure patterns

### Re-validation
After the fix:
- confirm the learner can explain one concrete operational advantage of path-based routing over exposing multiple separate public services

---

## Troubleshooting mindset
While debugging this module, always ask:
- are all backends healthy independently?
- are all Services correct?
- are the paths clearly and intentionally designed?
- does the ingress class match the controller?
- are the backend responses distinct enough to validate correctly?
- do I understand how the controller is choosing the target service?

## Escalation rule
If the routing still feels broken:
1. validate backend A  
2. validate backend B  
3. validate Service A  
4. validate Service B  
5. validate ingress class alignment  
6. validate path-to-service mapping  
7. retest one path at a time  
8. prioritize route-chain reasoning over repeated manifest guessing  
