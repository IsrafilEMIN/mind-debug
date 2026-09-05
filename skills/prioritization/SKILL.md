---
name: prioritization
description: "Use when clarifying goals and cutting distractions."
version: 0.2.2
author: IsrafilEMIN, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [priorities, focus, decision-making]
    related_skills: []
---

# Prioritization

Interview first. Establish what the user is actually pursuing, identify the constraint preventing progress, and concentrate effort on removing it. The result is a commitment to one direction and one current bottleneck—not a way to justify, sequence, or preserve every attractive activity.

## When to Use

- Attention or effort is drifting away from what matters.
- Competing possibilities make it difficult to choose and commit.
- The intended direction is unclear, conflicting, or disconnected from current actions.
- The user needs to determine what deserves focus and what to stop.

Don't use for: overriding the user's values, policing leisure, replacing professional judgment, or reopening an agreed execution task without a material priority conflict.

## Prerequisites

No platform-specific dependency. Read supplied context and prior decisions; use available read/search/calculation tools for relevant facts. Do not inspect unrelated private material. The user is the authority on their intent and acceptable trade-offs; neither web research nor memory can substitute for asking them.

For an illustrative application, see [the SMB anchor](references/smb-ai-example.md). It is an example, not a restriction on where this skill applies.

## Procedure

### 1. Interview through the hierarchy

Do not jump from an aspiration to a recommendation. Work through these layers in order, carrying the answers forward:

1. **Purpose:** Why does this matter? Who is it for? What is the user ultimately trying to change or become? Which competing ambitions are explicitly outside this pursuit?
2. **Outcome:** What concrete result would count as success? What is the current state, desired state, and relevant horizon? Distinguish an outcome from a tool, course, project, or identity label.
3. **Optimization:** What matters most when objectives conflict: speed, scalability, reliability, risk coverage, revenue, cost, mastery, or something else? Which are hard minimums rather than objectives to maximize? What will the user knowingly sacrifice?
4. **Resources and advantages:** What time, money, runway, skills, access, relationships, assets, and existing work are actually available? Which advantages can be used now rather than acquired first?
5. **Constraints and risk:** What obligations, deadlines, dependencies, permissions, capacity limits, and failure consequences apply? How much financial, operational, and reputational risk is acceptable? What must remain protected?
6. **Current choices and allocations:** What can the user act on immediately? What commitments and possibilities currently compete for their resources? What does each consume and contribute toward the intended outcome?

Ask a small coherent round, listen, then ask follow-ups. Group independent questions; defer questions whose meaning depends on an unanswered earlier layer. Probe vague answers and contradictions with concrete examples. Do not dump this entire checklist at once, impose a fixed interview length, or mechanically re-ask facts already settled.

Use the host's interactive question tool when available (Hermes: `clarify`; OMP: `ask` in interactive sessions), following its actual schema. Put selectable answers in the tool's choice fields, not merely in question prose. Offer concise, neutral choices where useful and always allow a custom answer; use the built-in free-text/Other facility or an open-ended follow-up if needed. Prefer open-ended questions when predefined choices would bias the user's purpose or intent. Batch independent questions into one asking round where supported; wait for answers before asking dependent questions. If the tool is unavailable, ask in chat and wait instead. A dismissed, timed-out, or unanswered form is not an answer or confirmation.

**Exit:** enough specific answers to explain the intended direction, governing trade-offs, practical limits, and competing commitments. A vague opening prompt normally calls for questions—not a priority brief.

### 2. Confirm the decision frame before prescribing

Reflect back: “You are pursuing X, optimizing primarily for Y, while preserving Z, with these resources and constraints. These other pursuits are not part of this commitment.” Ask the user to correct or confirm it. Surface contradictions rather than smoothing them over.

**Confirmation gate:** do not recommend a focus until this frame is user-confirmed. Explicit confirmation already present in the conversation counts; do not demand a ritual extra turn. Silence, missing information, and an agent's plausible interpretation do not count.

If the user explicitly requests a provisional answer without questions, label assumptions and give only a conditional assessment. Do not present the direction or bottleneck as validated. If interaction is unavailable, return the unresolved questions unless a confirmed frame was supplied; do not invent one merely to finish.

**Exit:** a user-confirmed decision frame, or a clearly blocked/provisional status. Do not use an experiment to avoid asking about intent, risk tolerance, resources, or commitments.

### 3. Establish the current bottleneck with the user

Ask what specifically prevents the next meaningful result today. Examine recent attempts, actual failures, unfinished deliverables, feedback, and dependencies. Work backward from the confirmed outcome, not forward from the user's favorite tool.

Challenge each proposed blocker:
- If it disappeared tomorrow, what meaningful progress would become possible?
- What would still prevent that progress?
- Is this the current constraint, or a possible future concern?
- What evidence supports it, and what would show the diagnosis is wrong?

Distinguish missing knowledge from missing practice, delivery quality, access, demand, execution, or willingness to commit. Do not infer the answer from a generic business playbook. Offer your diagnosis with reasons, invite the user's challenge, and resolve material disagreements before treating it as established. User agreement establishes shared understanding, not empirical proof.

When a critical factual uncertainty remains after the interview, identify it precisely. Only then consider a bounded investigation that can distinguish competing explanations. It must stay within the confirmed direction and specify the decision it resolves, evidence needed, and stopping condition. “Test several paths and see” is not a substitute for focus.

**Exit:** one shared current bottleneck, with evidence and remaining uncertainty explicitly separated. If it cannot yet be established, continue the analysis rather than manufacturing certainty.

### 4. Audit allocations and eliminate competing paths

Evaluate existing choices against the confirmed direction and bottleneck. Choose the feasible option with the highest expected return toward the confirmed outcome for the resources committed, subject to the user's hard constraints and risk tolerance. Return means progress on what the user values, not necessarily money, speed, or short-term gains. Make uncertainty and opportunity cost explicit; do not invent ROI scores or guarantee an outcome.

Do not generate a menu by default. Introduce an alternative only when it exposes a mistaken assumption or materially changes the focus decision.

Classify each material allocation:
- **Attack:** directly removes the current bottleneck.
- **Support:** a necessary, bounded input to that same effort, with a concrete use and output.
- **Maintain:** an unavoidable obligation or minimum operating requirement; protect its minimum allocation without turning it into a growth project.
- **Stop:** pursues a different path, optimizes the wrong objective, addresses an unproven future need, or cannot justify its opportunity cost.

Ask: “Which current deliverable does this serve? What would fail if it stopped? Why must it consume resources now?” Similarity is not alignment: two activities in the same domain can pursue different outcomes.

Do not turn Stop items into a sequenced backlog. Distinguish “not now within this path” from “not part of this path.” Neither receives active time or spending merely because it might be useful someday. Reconsider only when a material requirement or the user's purpose changes—not on a recurring invitation to reopen distractions.

**Exit:** explicit keep/limit/stop decisions and the time, money, and attention to reclaim. If exact amounts are unknown, ask or label them unknown; do not invent savings. Recommend cancellations or pauses, but do not execute them without authorization.

### 5. Make a focus commitment

Only after the gates above, use [the focus brief](templates/priority-brief.md). State:
- The confirmed purpose, outcome, optimization priority, and hard constraints.
- The one current bottleneck and its supporting evidence.
- One primary effort and its first concrete action.
- Necessary support and maintenance, each bounded and justified.
- What stops, what allocation is reclaimed, and where it goes.
- Owner, timebox, observable artifact, and acceptance criterion.
- Review event and evidence that warrants continuing, changing the diagnosis, or stopping.

Do not append a broad roadmap or Next list. Focus is not doing every legitimate thing in a better order. It is excluding other pursuits while this constraint is being addressed. Be direct: “This does not support your stated objective; stop allocating this pursuit's resources to it.” Challenge the allocation, not the person's character. Respect a deliberate change of purpose; do not silently preserve incompatible goals.

Return the brief in chat unless saving is requested. Planning does not authorize spending, cancellations, outreach, deployment, or execution. Review progress against the agreed bottleneck—not the volume of activity or preparation. Preserve agreed safety and quality minimums; a focus commitment does not waive them.

**Exit:** the user can name what they are attacking, why it matters, what supports it, and what they are no longer doing.

## Pitfalls

- **Premature prescription:** giving an action before establishing intent and constraints.
- **Hypothesis laundering:** calling an agent's guess a validated bottleneck.
- **Option inflation:** offering more paths when the user needs help excluding them.
- **Sequencing as appeasement:** making every distraction a respectable future phase.
- **Proxy optimization:** minimizing cost when cost is not the governing constraint.
- **False minimalism:** cutting necessary support or safety because focus supposedly means one activity.
- **Endless questioning:** re-asking settled questions instead of resolving a specific ambiguity and moving toward commitment.

## Verification

Before prescribing, check that the hierarchy was explored, the frame confirmed, and the bottleneck jointly examined. Before returning a focus brief, check that one effort remains, each supporting allocation has a causal role, competing paths are explicitly stopped rather than sequenced, and review criteria can change the diagnosis. Never claim the user confirmed an assumption, a test proved more than it did, or a recommended cancellation/execution already happened.
