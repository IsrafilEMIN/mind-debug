---
name: prioritization
description: "Use when choosing the next step toward a goal."
version: 0.1.0
author: IsrafilEMIN, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [priorities, decision-making, strategy]
    related_skills: []
---

# Prioritization

Find the shortest credible route from the user's actual goal to verified progress. Optimize against the user's values and constraints, not the agent's preferred technology or a default ambition to make money. Produce a decision and a bounded next action, not a comprehensive curriculum or implementation project.

## When to Use

- The user knows the direction but is unsure what to do next.
- Several attractive projects compete for attention.
- Preparation, research, tooling, or optimization may be displacing progress.
- New evidence, a missed milestone, or a changed constraint requires reprioritization.

Don't use for: executing an already agreed task with no material priority conflict, urgent incident response that already has a playbook, or replacing qualified legal/medical judgment.

## Prerequisites

No platform-specific dependency. Use the host agent's available search, file, calculation, and question tools when needed; do not invent tool names or capabilities. Read existing goals and decision records when supplied. Do not access unrelated private material to fill gaps.

## Procedure

### 1. Establish the destination

Restate the intended beneficiary, desired change, observable success measure, time horizon, and non-negotiable constraints. Distinguish the long-term direction from the next meaningful milestone. Include current baseline and capacity if known.

Retrieve accessible facts rather than asking the user to repeat them. Ask only missing questions whose answers could change the next action; group independent questions and sequence dependent ones. Do not force a numeric target where the user has not chosen one: propose it as provisional. If goals conflict, ask which governs or explicitly preserve the trade-off.

**Exit:** one outcome statement, with unknowns labeled. Do not invent a customer, budget, deadline, demand, or risk tolerance.

### 2. Find the current bottleneck

Work backward: outcome ← necessary milestone ← current blocker. Separate facts (with sources), user preferences, assumptions, and open questions. A hypothesis is not a proven bottleneck.

Ask: “If this activity succeeded tomorrow, what would still prevent the outcome?” Then ask: “If we skipped it, what specific failure would block the next milestone?” Skills, credentials, infrastructure, and research are prerequisites only when that causal link holds. Challenge sunk-cost justifications without belittling curiosity.

If demand, access, or feasibility is unknown, prioritize a bounded test of the most decision-changing uncertainty rather than pretending implementation is ready. Research must name the decision it will unlock, its evidence threshold, and a stopping time.

**Exit:** one bottleneck hypothesis, supporting evidence, and the observation that could disprove it.

### 3. Compare a small set of routes

Usually compare three to five plausible routes, including the user's favored activity, a direct route to the milestone, and a cheaper/manual/no-build alternative when relevant. Do not manufacture extra options for a trivial decision.

For each route record:
- Causal link to the goal and blocker removed.
- Evidence strength and the critical assumption.
- Time to useful evidence or value, including dependencies, review, deployment, and likely rework.
- Effort/cash, downside, reversibility, and opportunity cost.
- Whether it meets the minimum safety, quality, and reliability bar.

Use these rules in order:
1. Exclude options that violate hard constraints or lack necessary authorization.
2. Reject dominated routes: another route achieves the same relevant result with no greater burden or risk and less of at least one. State uncertainty where comparisons are not established.
3. Prefer the feasible route addressing the current blocker with the shortest credible time to meaningful evidence or value.
4. Under substantial uncertainty, favor a cheap reversible test with a result that can actually change the choice.
5. Break genuine ties using the user's values and strategic capability goals; do not default to easiest, most profitable, or most interesting.

Use qualitative judgments unless numerical inputs are defensible. If calculating, use a calculation tool, expose assumptions/ranges, and test whether plausible changes reverse the result. Do not disguise guesses in a weighted score.

**Exit:** a compact comparison, a recommended route, why the strongest alternative loses now, and the condition that would reverse the ranking.

### 4. Apply the diagnosis-before-tools check

For business/AI work, load [the SMB anchor](references/smb-ai-example.md). Diagnose efficiency gains, cost savings, revenue opportunities, and failure costs before selecting a stack. Compare conventional software, deterministic automation, AI, human judgment, and no change. If AI is a user-imposed constraint, state the trade-off rather than inventing a need for AI.

Separate discovery, prototype, controlled pilot, and production milestones. Never label a demo production-ready. A delivery action needs a risk-proportionate floor: representative tests/evaluations, permissions and data handling, failure/timeout behavior, human escalation, observability, rollback or manual recovery, and an accountable operator. Define measurable acceptance thresholds before live rollout; unknown thresholds are blockers to rollout, not to safe discovery. Avoid “bug-free” promises.

Do not reflexively defer infrastructure: verified offline, privacy, latency, cost, or scale requirements can make local inference the real prerequisite. Do not mandate enterprise infrastructure for a small reversible experiment.

**Exit:** the chosen route is justified by the problem, with an appropriate readiness bar and any delivery blockers explicit.

### 5. Commit attention, not an entire roadmap

Use [the priority brief](templates/priority-brief.md). Set exactly one **Now** action unless a real independent parallel obligation makes that impossible; explain any exception and protect the bottleneck work. Name its owner, first concrete step, timebox, observable artifact, acceptance criterion, and stop/pivot condition. If ownership is unknown, propose rather than assign another person.

List **Next** only where it is conditional on the Now result. Classify competing work as necessary prerequisite, later enabler, optional interest, or distraction relative to this goal. For each deferred item, record a reason and an evidence-based revisit trigger. Optional interests can have a user-chosen budget; they need not masquerade as business progress.

When evidence is insufficient, mark the recommendation provisional and make Now an information-gathering action. Do not force a build decision.

**Exit:** a brief the user can act on without another planning session. Writing the brief is not evidence of outcome progress.

### 6. Review and hand off

Set a review date or observable event, the evidence to inspect, and continue/pivot/stop thresholds. On review, compare actual results with the baseline; retain, revise, or abandon the bottleneck hypothesis. Reopen deferred work only when its trigger fires or the user changes the goal.

Return the brief in chat by default; save it only in an agreed workspace when requested. Prioritization does not authorize spending, outreach, publishing, deployment, or executing the selected work. Hand execution to a suitable workflow only with user authorization.

**Exit:** one clear next step and a falsifiable review rule—not an endless interview.

## Pitfalls

- **Goal substitution:** revenue is not mastery; mastery is not customer delivery. Do not silently exchange them.
- **Tool-first anchoring:** neither n8n nor local LLMs are inherently the right first step.
- **Premature optimization:** a real future need is not necessarily today's dependency.
- **Speed without reliability:** include expected rework, human review, support, and failure costs.
- **Analysis as avoidance:** stop when further answers would not change a safe, reversible next action.
- **Overconfident coaching:** challenge the causal claim, not the person's motives or character.
- **Universal prescriptions:** interviews are not always Now; existing customer evidence may make delivery or reliability the blocker.

## Verification

Before returning the brief, check:
- The outcome reflects the user's actual goal; facts and assumptions are separated.
- The bottleneck has a causal explanation and a disconfirming observation.
- Alternatives include a credible challenger; ranking respects constraints and opportunity cost.
- Now removes a blocker or tests a decision-changing uncertainty, with owner, timebox, artifact, and acceptance criterion.
- Safety and production requirements are neither bypassed nor overbuilt.
- Deferred work has reasons and revisit triggers; the strongest alternative has a reversal condition.
- Review criteria can change the recommendation; no execution or success is falsely claimed.
