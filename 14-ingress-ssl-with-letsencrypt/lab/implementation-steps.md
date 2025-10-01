# Implementation Steps

## Purpose of this file
This file contains the practical execution flow for the Ingress SSL with Let’s Encrypt lab.

The goal is to create one clear certificate automation path where a hostname-based ingress route is secured with a trusted HTTPS certificate issued through Let’s Encrypt and managed by cert-manager.

---

## Step 1 — Understand the TLS goal
Before deploying certificate resources, understand what this module is trying to teach.

This lab is not only about making the browser show a lock icon. It is about learning the full trust lifecycle:

- the hostname must resolve correctly
- the ingress must be reachable
- cert-manager must request the certificate
- Let’s Encrypt must validate domain control
- the certificate must be stored and attached correctly
- HTTPS must then be served successfully

At the end of this lab, you should have:
- one working hostname
- one certificate issuer path
- one TLS secret
- one HTTPS-enabled ingress route

## Step 2 — Reconfirm DNS and ingress readiness
Before introducing TLS, verify that:
- the hostname resolves correctly in public DNS
- the ingress route already works over HTTP
- the backend application responds correctly

Do not skip this step. Certificate challenge failures often come from trying to secure a hostname that is not yet reachable properly.

## Step 3 — Install or review cert-manager
Deploy cert-manager into the cluster or confirm that it is already installed and healthy.

At this stage, focus on:
- controller readiness
- webhook readiness
- namespace and deployment health

cert-manager is the lifecycle engine for certificate issuance and renewal. Microsoft’s AKS guidance for HTTPS with application routing also centers on cert-manager for certificate automation scenarios. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/aks/app-routing-dns-ssl?utm_source=chatgpt.com))

## Step 4 — Choose the Let’s Encrypt environment
Now decide whether you will begin with:
- Let’s Encrypt staging, or
- Let’s Encrypt production

For safe learning, staging is often the cleaner first step because it avoids unnecessary production issuance mistakes and rate-limit issues while the learner validates the workflow.

The important point is that the issuer configuration should clearly reflect which CA environment is being used.

## Step 5 — Create the Issuer or ClusterIssuer
Now define the certificate authority configuration that cert-manager will use.

For a cluster-wide learning pattern, a ClusterIssuer is often simpler.  
For more scoped learning, an Issuer may be enough.

At this stage, focus on:
- Let’s Encrypt endpoint selection
- email/contact configuration
- solver strategy for HTTP-01
- ingress-class alignment

This is the trust-definition layer of the workflow.

## Step 6 — Review the HTTP-01 challenge path
Now understand how Let’s Encrypt will validate the hostname.

For this lab, the learner should treat the challenge flow as a real runtime request path:
- Let’s Encrypt must reach the hostname
- the challenge response must be served correctly through ingress
- if the HTTP path is not reachable, issuance will fail

This is one of the most important learning moments in the module because it shows that certificate issuance is not only a control-plane action; it depends on the actual networked ingress path.

## Step 7 — Update the ingress for TLS
Now update the hostname-based ingress resource so it includes TLS configuration and references the intended TLS secret.

The ingress should now express:
- which hostname is being secured
- which secret will hold the certificate
- which issuer path is expected to satisfy the certificate request

Keep the first scenario simple:
- one hostname
- one certificate
- one ingress route
- no unnecessary rule complexity

## Step 8 — Apply the issuer and ingress changes
Apply the ClusterIssuer or Issuer and the TLS-aware ingress changes.

At this stage, inspect:
- whether the resources were accepted cleanly
- whether cert-manager is reacting to the request
- whether certificate and challenge resources begin to appear

Do not jump directly to HTTPS testing before the certificate lifecycle has visibly started.

## Step 9 — Observe certificate issuance behavior
Now inspect the certificate flow carefully.

The learner should look for:
- certificate request creation
- ACME challenge or order resources
- solver behavior
- TLS secret creation once issuance succeeds

This is the core lifecycle moment of the module.

## Step 10 — Verify the TLS secret
Once issuance succeeds, verify that:
- the TLS secret exists
- it is the intended secret referenced by ingress
- the secret represents the issued certificate material

This proves that cert-manager has completed the issuance flow successfully.

## Step 11 — Test HTTPS externally
Now test the hostname over HTTPS.

Validate that:
- HTTPS connects successfully
- the certificate is trusted as expected for the chosen CA path
- the application responds correctly over the secure connection
- the ingress route still reaches the intended backend

This is the main technical success signal for the module.

## Step 12 — Review TLS termination at the ingress layer
Now reflect on where the security is actually being applied.

The learner should understand:
- the certificate is attached at the ingress layer
- the ingress terminates TLS for the public connection
- backend service routing can remain independent underneath
- the secure public entry layer is now part of platform design

This is important because later platform security reasoning depends on knowing where trust is terminated.

## Step 13 — Compare manual certificate handling to cert-manager lifecycle management
Now reflect on why cert-manager matters.

Ask:
- how would this process look if certificates had to be requested and renewed manually?
- what operational burden does cert-manager remove?
- why is certificate renewal as important as initial certificate issuance?

This step moves the learner from HTTPS enablement into lifecycle thinking.

## Step 14 — Explain the certificate lifecycle end to end
Now explain the flow in plain language:

- the hostname resolves to ingress
- cert-manager requests a certificate for that hostname
- Let’s Encrypt validates control of the hostname through the challenge path
- cert-manager stores the issued certificate in a TLS secret
- the ingress uses that secret to serve HTTPS

If the learner can explain this clearly, the module is doing its real job.

## Step 15 — Reflect on TLS as a platform trust layer
Pause and think beyond the manifests.

In this module, ingress TLS means:
- public application access becomes encrypted
- client trust is based on a real certificate lifecycle
- hostnames, DNS, and routing are now tied to trust
- cert-manager turns HTTPS into an operational process instead of a manual task

This mindset is the real objective of the module.

---

## Checkpoint
At this point, the following should already be true:

- the hostname resolves correctly
- the ingress route is already healthy
- cert-manager is running
- an Issuer or ClusterIssuer exists
- a certificate request has succeeded
- a TLS secret exists
- HTTPS works for the intended hostname
- the learner understands the end-to-end certificate lifecycle

## Step 16 — Prepare for workload resource governance
Before moving to the next module, understand what changes next.

The next module is **Kubernetes Requests + Limits**. That means the learner will now shift from public edge security into internal workload resource discipline, which is another critical production-readiness concern.

This is the bridge from secure exposure into runtime resource control.

---

## Implementation notes
- always validate DNS and HTTP reachability before starting certificate issuance
- keep the first certificate scenario simple and deterministic
- use staging first if the environment is still being proven
- treat challenge validation as a real traffic path
- focus on lifecycle understanding, not only first-time success

## End-of-implementation summary
In this lab, you:
- reconfirmed DNS and ingress readiness
- installed or reviewed cert-manager
- created an Issuer or ClusterIssuer for Let’s Encrypt
- attached TLS configuration to ingress
- observed certificate issuance and secret creation
- validated HTTPS for the hostname
- practiced the first true trust-lifecycle automation pattern in the AKS phase

You are now ready to validate whether the ingress TLS lifecycle is clean, correct, and explainable.
