# Inspiration and boundaries

## Primary anchor

The creator's example supplies the judgment standard: a goal of serving SMBs with applied AI does not imply either deep local inference work or tool-first automation sales. Diagnose valuable work, select the appropriate intervention, and deliver a production-safe result. Activities earn priority through their causal role in that outcome.

## Sources read

Matt Pocock's [skills repository](https://github.com/mattpocock/skills):

- [`grilling`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md): dependency-aware questioning; retrieve facts rather than asking users to repeat accessible information. The revised skill requires dependent interview rounds and a user-confirmed decision frame before prescribing; asking only enough to suggest a plausible action proved too weak.
- [`triage`](https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/SKILL.md): verify claims before expanding a plan; preserve reasons for rejecting work. Here, deferred priorities have explicit reasons and revisit triggers rather than issue-tracker states.
- [`to-tickets`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md): narrow verifiable end-to-end slices with genuine dependencies. Here, the output is one next action, not a published ticket backlog.

“Grid Me” likely refers to `grill-me`, which the research scout identified as an entry point to `grilling`; this identification is not certain. Linked upstream files may evolve.

These are conceptual influences. No upstream implementation or substantial text is vendored. There is no runtime dependency on that repository and no claim of endorsement.

## Original synthesis

- Purpose → outcome → optimization → resources/constraints → confirmed frame → shared bottleneck → allocation cuts → focus commitment.
- Shortest *credible* route includes risk, rework, human effort, and support.
- Diagnose before choosing AI, deterministic automation, software, human judgment, or no change.
- Prerequisites require a causal blocking argument, not a generic “useful someday” claim.
- Every priority has a reversal condition; every deferred item has a revisit trigger.
- User values govern the objective. A research or mastery goal can correctly prioritize systems work.

## Portability boundary

The payload is Markdown with YAML frontmatter and relative references. For v0.1.0 only, default-profile installation and two behavioral smoke cases were exercised in Hermes and OMP; see [results and limitations](smoke-results.md). This does not establish universal host/model compatibility. No Hermes repository-specific documentation generator or runtime code is included in this standalone repository.
