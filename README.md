# Prioritization

**Choose the shortest credible path to the outcome—not the most interesting detour.**

An agent skill for turning a direction into a defensible next priority. It helps people distinguish meaningful progress, necessary preparation, useful experiments, and distractions. Speed means time to a verified outcome, including likely rework and operational risk—not time to a flashy demo.

## The problem

Knowing where you want to go is not the same as knowing what to do next. A technically impressive activity can be unrelated to your current bottleneck. A quick-to-sell tool can also be unrelated to what a customer actually needs.

The skill asks:

1. What outcome matters, to whom, and how will we recognize it?
2. What currently prevents that outcome?
3. What is the smallest credible action that removes that blocker or resolves a decision-changing uncertainty?
4. What should we explicitly defer—and what evidence would make it relevant?

It does not impose income, speed, or productivity as everyone's goal. If your goal is research, mastery, enjoyment, or resilience, prioritize against that goal instead.

## Anchoring example: applied AI for small and medium businesses

Suppose you want to serve SMBs with applied AI engineering but do not know where to start.

- **Infrastructure-first detour:** study kernels, build local inference infrastructure, or buy hardware before identifying a customer constraint that requires it.
- **Tool-first shortcut:** learn n8n and assume connecting services is a business offer.
- **Outcome-first route:** find an accessible business workflow, establish its cost or missed-revenue baseline, identify who owns it and can authorize change, and diagnose the appropriate intervention. It may be conventional software, automation, an AI component, human judgment, or no change.

Then deliver a narrow end-to-end pilot with representative evaluation, safe permissions, human escalation, monitoring, recovery, and a responsible owner. Measure business improvement after review and operating costs—not merely model accuracy or a successful demo.

This is not an argument against local LLMs or n8n. Local deployment can become the priority when verified privacy, offline, latency, or economic constraints require it. n8n can be an appropriate implementation component. Neither gets to define the problem in advance.

Read the [worked example](skills/prioritization/references/smb-ai-example.md).

## Use

The portable entry point is [`skills/prioritization/SKILL.md`](skills/prioritization/SKILL.md). Supporting references and the output template live beside it. No paid API, package installation, or platform-specific tools are required by the skill itself.

For a manual trial, give an agent the skill file and access to its linked files, then say:

> Use Prioritization. I want to serve small businesses with applied AI engineering. I'm considering learning local inference, learning n8n, or interviewing operators. Help me find the current bottleneck, choose one next action, and define what would change your recommendation. Do not assume I already have a customer or validated demand.

Expected output: an outcome statement, evidence and assumptions, bottleneck, compact option comparison, **one Now action**, stop/defer list, and a review trigger. Ask only questions that could change the immediate recommendation.

## Repository

- `skills/prioritization/SKILL.md` — agent procedure and decision rules.
- `skills/prioritization/templates/priority-brief.md` — reusable decision record.
- `skills/prioritization/references/smb-ai-example.md` — worked anchor and reversal conditions.
- `docs/inspiration.md` — source links and what was adapted conceptually.
- `evals/scenarios.md` — behavioral cases for later agent trials.
- `tests/test_repository.py` — offline structural checks, not proof of agent behavior.

## Validation and status

```sh
python3 -m unittest discover -s tests -v
```

**Initial draft, v0.1.0.** Structural tests cover packaging and required decision-contract fields. Behavioral scenarios are specified but have not been run in Hermes or OMP. Installation, runtime discovery, and cross-agent behavioral testing are deliberately deferred. No install-command compatibility is claimed yet.

## Design influences

Inspired by the user's SMB applied-engineering example and Matt Pocock's [skills repository](https://github.com/mattpocock/skills), particularly `grilling`, `triage`, and `to-tickets`. The likely reference behind “Grid Me” is `grill-me`. This repository contains an original synthesis, not a copy of those skills. See [source notes](docs/inspiration.md).

## Contributing

Prefer changes that alter a concrete decision over adding productivity terminology. Include a scenario showing where the current skill makes the wrong call and what evidence should reverse that call. Preserve the anchor without making it a universal business prescription. Do not commit client data, credentials, or personal decision briefs.

## License

MIT. Copyright IsrafilEMIN. Developed with Hermes Agent.
