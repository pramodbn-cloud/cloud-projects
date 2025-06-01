# Validation Checks

## Purpose of this file
This file confirms whether the Azure Artifacts lab is complete and correct.

The goal is not only to verify that a feed exists, but to confirm that the learner understands how reusable, versioned components are managed, published, and consumed in a disciplined way.

## Validation approach
For this lab, validation is based on:
- feed creation verification
- package visibility verification
- version identity verification
- consumption flow understanding
- upstream source awareness
- learner explanation ability

## Check 1 — Feed exists and is understandable
Confirm that:
- a feed exists in Azure Artifacts
- the feed name is clear
- the learner can explain the purpose of the feed

This proves that package management now has a defined home inside the project or organization.

## Check 2 — Package scenario is meaningful
Confirm that:
- the learner selected a reusable package scenario
- the package represents something that could realistically be reused
- the learner can explain why it belongs in a feed instead of being treated as a one-time artifact

This proves that the module has moved into package lifecycle thinking.

## Check 3 — Package publication is visible or clearly modeled
Confirm that:
- a package was published into the feed, or
- the publish flow was modeled clearly enough to explain step by step
- the package is visible with a recognizable identity

This proves that the feed is being used as a managed package source.

## Check 4 — Version identity is present and understood
Confirm that:
- the package has a visible version
- the learner can explain why version identity matters
- the package lifecycle can be discussed in terms of evolution over time

This proves that reuse is being handled with discipline.

## Check 5 — Consumption path is understandable
Confirm that:
- the learner can explain how a consumer would connect to the feed
- the publish-consume loop is clear
- the learner understands how a project or pipeline would retrieve the package

This proves that package management is being understood end to end.

## Check 6 — Upstream source strategy is understood
Confirm that:
- the learner understands what upstream sources are
- the learner can explain why an organization might enable them
- the learner knows that consumed upstream packages can be saved in the feed

This proves that dependency centralization thinking is present.

## Check 7 — Feed visibility and sharing mindset are understood
Confirm that:
- the learner understands that feeds have scope and visibility settings
- the learner has basic awareness of feed views or controlled sharing
- package exposure is being thought of as governed, not accidental

This proves that package management includes access and sharing control.

## Check 8 — You can explain the package lifecycle in your own words
This is the most important validation for this module.

You should now be able to explain:
- what Azure Artifacts is
- what a feed is
- why packages need versions
- how publishing and consumption relate
- how upstream sources help centralize dependencies
- how package reuse differs from pipeline artifact usage

If you can explain this clearly, the module is truly understood.

## Expected success indicators
The strongest success signals for this lab are:
- the feed exists and is clear
- package identity is visible
- consumption flow is understandable
- upstream and visibility strategy are understood
- the learner feels ready to move into security and compliance thinking

## If validation fails
If any validation step fails:
- revisit the feed structure
- simplify the package scenario
- re-check version naming
- review consumption guidance again
- use `troubleshooting.md` for common package-management issues
