# Prioritization

**Clarify the purpose. Attack the current bottleneck. Stop funding competing paths.**

An interview-first agent skill for establishing a direction and concentrating effort on it—not arranging every attractive activity into a plausible roadmap.

## Current revision

**v0.2.1** generalizes the distraction triggers and removes the redundant learning/practice phase. The interview-first revision is ready for renewed user testing; its multi-turn behavior has not yet been validated. The [earlier smoke results](docs/smoke-results.md) concern v0.1.0 only. One-shot recommendation tests missed a real-use failure: the agent could rationalize distractions instead of clarifying intent and enforcing focus.

## How it works

1. Interview in dependent rounds: purpose → outcome → optimization → resources/advantages → constraints/risk → current choices and allocations.
2. Obtain confirmation of the decision frame before prescribing.
3. Establish the current bottleneck with the user, grounded in actual attempts and evidence.
4. Classify allocations as **Attack, Support, Maintain, or Stop**. Exclude competing paths rather than scheduling them for later.
5. Commit to one feasible option with the highest expected return toward the confirmed outcome, preserving constraints and necessary support.

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

Structural checks verify packaging and explicit contract fields, not interviewing quality. Multi-turn behavioral evaluation of v0.2.1 remains pending.

## Installation and invocation

Use the current published skill; update installed snapshots explicitly when the repository changes.

Hermes, default profile:

```sh
hermes skills install IsrafilEMIN/prioritization/skills/prioritization --yes
```

For an existing installation: `hermes skills update prioritization`.

In a new Hermes session: `/prioritization <your situation>`.

OMP, default profile: copy the complete approved `skills/prioritization` directory into `~/.omp/agent/skills/prioritization`, preserving relative references and templates. Compare before overwriting an existing installation. In a new session: `/skill:prioritization <your situation>`.

Installed copies are snapshots, not automatically synchronized with this repository. Other profiles may use different paths.

## Try the interview

> I keep getting pulled toward different possibilities and am not making progress on what matters. Help me clarify my purpose, choose what deserves my commitment, and decide what to stop.

Expect questions first, not a menu or immediate recommendation.

## Contributing and license

Bring a concrete failure scenario and the evidence that should change the agent's behavior. Preserve the user's values, distinguish necessary support from distractions, and keep client data, private briefs, and credentials out of the repository.

MIT. Copyright IsrafilEMIN. Developed with Hermes Agent. Conceptual inspiration includes Matt Pocock's skills; no endorsement is implied.
