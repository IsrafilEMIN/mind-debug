# Mind Debug

**Clarify the purpose. Attack the current bottleneck. Stop funding competing paths.**

An interview-first agent skill for establishing a direction and concentrating effort on it—not arranging every attractive activity into a plausible roadmap.

## Current revision

**v0.4.0** replaces the detailed procedure with a compact thinking frame: direction, starting position, causal priority, and justified exclusion. The conversation adapts to the uncertainty instead of following a checklist. Published under the new name `mind-debug`; default Hermes and OMP installations use this name.

Detailed scenarios stay in evaluations, not the default skill payload. The template and domain reference are optional reviewer aids, not required context. The [earlier smoke results](docs/smoke-results.md) concern v0.1.0 only; the compact revision has not been live-tested.

## How it works

Discover and confirm direction, reason from requirements and reality, and concentrate on the current constraint. Preserve necessary support while excluding competing pursuits. Interactive questions serve the reasoning, not a prescribed interview sequence.

The [SMB anchor](skills/mind-debug/references/smb-ai-example.md) distinguishes learning/evals/subscriptions used for applied-AI delivery from local-inference tinkering for speculative savings. Actual offline requirements can change the judgment; generic future usefulness cannot.

## Files

- [SKILL.md](skills/mind-debug/SKILL.md) — complete agent instructions.
- [Focus brief](skills/mind-debug/templates/priority-brief.md) — used after confirmation, not instead of interviewing.
- [Focus regressions](evals/focus-regressions.md) — new multi-turn test specifications, not passing results.
- [Original scenarios](evals/scenarios.md) — earlier coverage.
- [Inspiration](docs/inspiration.md) — source notes.

## Validation

```sh
python3 -m unittest discover -s tests -v
```

Structural checks verify packaging and explicit contract fields, not interviewing quality. Multi-turn behavioral evaluation of v0.4.0 remains pending.

## Installation and invocation

Use the current published skill; update installed snapshots explicitly when the repository changes.

Hermes, default profile:

```sh
hermes skills install IsrafilEMIN/mind-debug/skills/mind-debug --yes
```

For an existing installation: `hermes skills update mind-debug`.

In a new Hermes session: `/mind-debug <your situation>`.

OMP, default profile: copy the complete approved `skills/mind-debug` directory into `~/.omp/agent/skills/mind-debug`, preserving relative references and templates. Compare before overwriting an existing installation. In a new session: `/skill:mind-debug <your situation>`.

Installed copies are snapshots, not automatically synchronized with this repository. Other profiles may use different paths.

## Try the interview

> I keep getting pulled toward different possibilities and am not making progress on what matters. Help me clarify my purpose, choose what deserves my commitment, and decide what to stop.

Expect questions first, not a menu or immediate recommendation.

## Contributing and license

Bring a concrete failure scenario and the evidence that should change the agent's behavior. Preserve the user's values, distinguish necessary support from distractions, and keep client data, private briefs, and credentials out of the repository.

MIT. Copyright IsrafilEMIN. Developed with Hermes Agent. Conceptual inspiration includes Matt Pocock's skills; no endorsement is implied.
