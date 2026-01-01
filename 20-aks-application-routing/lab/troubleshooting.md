# Troubleshooting

## Purpose of this file
This file helps the learner understand common issues that appear during the AKS Application Routing lab.

In this module, the most common failures usually come from following outdated HTTP Application Routing guidance, missing the managed-identity prerequisite, expecting the managed add-on to behave exactly like a self-managed ingress deployment, or misunderstanding the role of Azure DNS integration. The goal is to strengthen managed-platform reasoning, not only fix setup steps.

---

## Common issue 1 — The learner follows outdated HTTP Application Routing instructions

### Symptoms
- the learner finds older commands or documentation
- the platform behavior does not match current AKS guidance
- the learner becomes confused about what feature actually exists now

### Likely cause
The learner is using the retired HTTP Application Routing model instead of the current Application Routing add-on.

Microsoft’s lifecycle guidance states that the HTTP Application Routing add-on retired on March 3, 2025. Current AKS ingress guidance recommends the Application Routing add-on instead.

### Fix
- explicitly stop using retired HTTP Application Routing instructions
- switch to the modern Application Routing add-on model
- reinterpret the older course topic as historical context only

### Re-validation
After the fix:
- confirm the learner can clearly state which feature is current and which is retired

---

## Common issue 2 — The add-on cannot be used because the cluster does not meet prerequisites

### Symptoms
- the learner tries to enable the add-on
- the workflow does not behave as expected
- the setup path seems blocked or inconsistent

### Likely cause
The cluster may not satisfy the managed-identity requirement or other add-on assumptions.

### Fix
- inspect the cluster identity model
- confirm whether managed identity is in use
- do not continue assuming the add-on should work on an incompatible cluster

### Re-validation
After the fix:
- confirm the prerequisite is satisfied before retrying the add-on flow

---

## Common issue 3 — The learner expects the managed add-on to expose the same full ownership model as a self-managed controller

### Symptoms
- the learner looks for the same exact control surface as before
- the managed experience feels unfamiliar
- the learner sees differences as errors rather than design trade-offs

### Likely cause
The learner may not yet understand that the point of a managed add-on is to reduce some operator-owned controller lifecycle responsibility.

### Fix
Reframe the model like this:
- ingress concepts remain the same
- but AKS manages more of the controller lifecycle
- the operator gains convenience and Azure integration
- the operator may also accept some boundaries compared with a self-managed pattern

### Re-validation
After the fix:
- confirm the learner can explain one managed-ingress advantage and one self-managed-ingress advantage clearly

---

## Common issue 4 — Azure DNS integration value feels unclear

### Symptoms
- the routing works
- the learner still does not see why the add-on matters in Azure
- the DNS side feels disconnected from the routing side

### Likely cause
The learner may still be thinking only in terms of ingress exposure and not in terms of Azure-native operations.

### Fix
Reframe the integration like this:
- Azure-native routing is stronger when DNS management fits naturally into the same operational model
- the add-on supports Azure DNS public/private zone management
- this reduces some of the cross-tool friction of platform operations

### Re-validation
After the fix:
- confirm the learner can explain one concrete Azure-native operational advantage of the add-on

---

## Common issue 5 — The learner does not understand why this module appears after the earlier ingress modules

### Symptoms
- the learner thinks the course is repeating ingress
- the value of the sequence feels weak
- the managed add-on seems redundant

### Likely cause
The learner may not yet see that earlier modules taught fundamentals and ownership, while this module teaches managed-platform alternatives.

### Fix
Reframe the course progression like this:
- earlier modules taught ingress architecture deeply and explicitly
- this module teaches how AKS can manage more of that for you
- the sequence is correct because you can only judge a managed option well after learning the underlying system

### Re-validation
After the fix:
- confirm the learner can explain why learning self-managed ingress first makes the managed-routing lesson stronger

---

## Troubleshooting mindset
While debugging this module, always ask:
- am I using current Application Routing guidance or outdated HTTP Application Routing guidance?
- does the cluster meet the managed-identity requirement?
- am I expecting managed behavior or self-managed behavior?
- is the ingress route itself healthy?
- do I understand what operational burden AKS is taking over here?

## Escalation rule
If the managed-routing story still feels weak:
1. re-establish the retired-versus-current distinction  
2. confirm cluster prerequisites  
3. validate one simple ingress route only  
4. compare managed and self-managed models explicitly  
5. reconnect the Azure DNS value proposition  
6. prioritize platform trade-off reasoning over feature memorization  
