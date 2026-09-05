# Prioritization

**Clarify the purpose. Attack the current bottleneck. Stop funding competing paths.**

An interview-first agent skill for establishing a direction and concentrating effort on it—not arranging every attractive activity into a plausible roadmap.

## Current revision

**v0.2.0 is a local review draft.** It has not replaced the installed Hermes/OMP copies and has not been live-tested. The [earlier smoke results](docs/smoke-results.md) concern v0.1.0 only. One-shot recommendation tests missed a real-use failure: the agent could rationalize distractions instead of clarifying intent and enforcing focus.

## How it works

1. Interview in dependent rounds: purpose → outcome → optimization → resources/advantages → constraints/risk → current choices and allocations.
2. Obtain confirmation of the decision frame before prescribing.
3. Establish the current bottleneck with the user, grounded in actual attempts and evidence.
4. Classify allocations as **Attack, Support, Maintain, or Stop**. Exclude competing paths rather than scheduling them for later.
5. Apply learning to the target work. Several necessary resources can support one effort; unrelated practice projects do not become aligned just because they teach something.
6. Produce a focus commitment only when the preceding gates are satisfied.

The [SMB anchor](skills/prioritization/references/smb-ai-example.md) distinguishes learning/evals/subscriptions used for applied-AI delivery from local-inference tinkering for speculative savings. Actual offline requirements can change the judgment; generic future usefulness cannot.

## Files

- [SKILL.md](skills/prioritization/SKILL.md) — complete agent instructions.
- [Focus brief](skills/prioritization/templates/priority-brief.md) — used after confirmation, not instead of interviewing.
- [Focus regressions](evals/focus-regressions.md) — new multi-turn test specifications, not passing results.
- [Original scenarios](evals/scenarios.md) — earlier coverage.
- [Inspiration](docs/inspiration.md) — source notes.

## Validation

```sh
python3 -m unittest discover -s tests -v
```

Structural checks verify packaging and explicit contract fields, not interviewing quality. Multi-turn behavioral evaluation of v0.2.0 is pending review.

## Installation and invocation

The published/installed version remains v0.1.0 until this review draft is approved and distributed.

Hermes, default profile:

```sh
hermes skills install IsrafilEMIN/prioritization/skills/prioritization --yes
```

In a new Hermes session: `/prioritization <your situation>`.

OMP, default profile: copy the complete approved `skills/prioritization` directory into `~/.omp/agent/skills/prioritization`, preserving relative references and templates. Compare before overwriting an existing installation. In a new session: `/skill:prioritization <your situation>`.

Installed copies are snapshots, not automatically synchronized with this repository. Other profiles may use different paths.

## Try the interview

> I want to scale applied AI, but my time is split between evals, courses, local LLM work, and side projects. Help me clarify what I am actually pursuing and what needs to stop. Do not infer my bottleneck before asking about my intent and circumstances.

Expect questions first, not a menu or immediate recommendation.

## Contributing and license

Bring a concrete failure scenario and the evidence that should change the agent's behavior. Preserve the user's values, distinguish necessary support from distractions, and keep client data, private briefs, and credentials out of the repository.

MIT. Copyright IsrafilEMIN. Developed with Hermes Agent. Conceptual inspiration includes Matt Pocock's skills; no endorsement is implied.
