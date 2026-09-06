# Initial live smoke results

## Scope

Payload: `7d6bcf7e6930279bbba7debb0737e047f128d22c`, skill v0.1.0. The skill itself was not changed after these trials.

- Hermes v0.21.0, upstream `52cf39c9`; configured provider/model `openai-codex/gpt-6-astra`.
- OMP v18.1.10; event metadata confirms `openai-codex/gpt-6-astra`.
- Default profiles only. Same three-file payload verified byte-for-byte in both installations.
- Six offline structural checks pass. These checks are not behavioral evaluation.

Two fictional, self-contained prompts were run in fresh sessions on each host. Both requested the installed skill and its linked reference/template, prohibited execution/outreach/writes, and supplied enough facts for a provisional brief without follow-up questions. This tests explicit invocation, not automatic natural-language triggering or interactive questioning.

## Observed decisions

| Scenario | Hermes | OMP |
|---|---|---|
| No customers or validated workflow; one operator reachable; five hours; no hardware budget; goal is reliable SMB outcomes | Chose a bounded operator workflow-diagnosis cycle; deferred kernels, local serving, and broad n8n learning. | Same priority; five-hour diagnosis cap, baseline sheet, operator confirmation, and specific revisit triggers. |
| Paying client; validated extraction workflow; authorized samples; agreed baseline/error threshold; signed offline constraint; existing adequate hardware; one day | Chose entirely offline local feasibility testing; rejected cloud and deferred general interviews. | Same reversal; verify isolation and compliant dependencies before samples; test quality/net benefit and stop on compliance failure. |

All four captured briefs contain a goal, causal blocker, alternatives, one Now action, proposed owner, timebox, artifact, acceptance/stop criteria, and review/reversal conditions. They distinguish hypotheses from known facts and do not claim customer implementation succeeded. The core choice and safety reasoning meet these smoke checks; this is not a claim that every full-suite rubric item or all ten scenarios passed.

OMP JSON tool events confirm successful reads of `SKILL.md`, `references/smb-ai-example.md`, and `templates/priority-brief.md` from its installed skill directory. Only read tools executed in those captures.

## Invocation and capture

Hermes used `hermes chat --oneshot -Q -s mind-debug --max-turns 8 --run-budget 180 -q '<scenario>'`.

OMP used `omp -p --mode=json --no-session --no-title --no-extensions --no-rules --no-lsp --tools=read --skills=mind-debug --max-time=180 '/skill:mind-debug <scenario>'`.

The OMP tool filter limits built-in tools to reads. Hermes used its configured tools, with a read-only instruction in the prompt; this is not an equivalent tool-enforced sandbox. Both hosts retained existing provider configuration. OMP's configured continuation/advisor behavior was present, so this is a host integration trial, not an isolated measurement of the skill alone.

## Runtime caveats

- Initial OMP text-mode captures contained only short closing verification messages, not the substantive briefs. One initial OMP process timed out. Those attempts were not counted as complete brief evidence.
- JSON retries captured complete substantive briefs, successful skill/reference reads, and `agent_end` events. The host also emitted a continuation message and closing summary. Agent completion and OS-process termination are separate; the outer runner imposed a timeout because OMP did not exit promptly. Do not call this a clean CLI end-to-end pass.
- Standalone `omp read skill://mind-debug` reported no skills, while fresh agent-session discovery and reads succeeded. Do not use that standalone command as the sole installation check.
- Hermes warned that existing gateways may still use pre-update modules. No update or gateway restart was performed; these tests used new CLI processes.

Raw transcripts and the local runner remain in ignored `evals/runs/`; they are not published. This report contains only fictional-scenario summaries, no client data or private runtime metadata.

## Still untested

The remaining eight scenarios, interactive follow-up behavior, automatic triggering, live desktop command selection, other models/profiles, and clean OMP process termination. The skill is usable for a manual review session; these are the boundaries of the evidence, not hidden passes.
