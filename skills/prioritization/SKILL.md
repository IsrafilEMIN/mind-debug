---
name: prioritization
description: "Use when clarifying goals and cutting distractions."
version: 0.3.0
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

Help discover direction rather than demand a finished ambition. The hierarchy is a reasoning dependency, not a questionnaire to recite. Gather concrete evidence where the user can supply it, synthesize its implications, and return to unresolved earlier layers.

1. **Purpose:** When direction is unclear, start from lived experiences, recurring frustrations, meaningful achievements, responsibilities, and what the user wants their work or life to make possible. Reflect patterns as tentative interpretations and invite correction. Uncertainty is a starting condition, not unwillingness to commit; the agent helps synthesize rather than outsourcing that synthesis to the user.
2. **Outcome:** Establish the enduring change or position the user wants to build toward, ordinarily over five to ten years for an open-ended life or career pursuit. This is a direction, not a forecast or a demand for precise distant targets. Distinguish the underlying purpose from an aspirational number or status label. Respect an already-set purpose and genuine external deadlines; execution timeboxes come later and do not define purpose.
3. **Optimization:** Ground trade-offs in what the desired future makes valuable and what must remain protected. Use concrete tensions from the user's context to establish which objective governs, rather than requiring abstract rankings detached from consequences.
4. **Resources and advantages:** Establish the starting position: assets, runway, relationships, access, experience, transferable strengths, and evidence of learning ability. Surface overlooked intellectual or practical advantages through examples of actual performance, not invented talent labels. Remember that current skills are a baseline, not a ceiling: distinguish usable strengths from capabilities that can be learned, practiced, acquired, or accessed through others, with realistic costs and uncertainty.
5. **Constraints and risk:** Separate hard limits and protected obligations from changeable conditions and untested assumptions. Include debt, financial commitments, health, dependencies, and failure consequences where relevant. Separate willingness to commit from practical capacity: commitment chooses the direction; actual obligations and capacity bound a sustainable execution plan. Quantify capacity when it changes feasibility or scope, not as a proxy for seriousness.
6. **Requirements and current allocations:** Work backward from that direction to the capabilities, access, evidence, and conditions it requires; compare these with the starting position. Distinguish essential gaps from speculative future needs and identify the nearest meaningful prerequisite. A feasible next step can build a missing capability rather than monetize an existing one. Inventory competing allocations without demanding that the user preselect what to abandon. Keep the dependency chain only as detailed as needed to locate the current constraint, not a comprehensive roadmap.

**Question-quality gate:** Every question must resolve a specific uncertainty in the developing decision frame, be answerable from the user's experience or considered preferences, and have an identifiable consequence for the analysis. If it asks the user to supply the conclusion the agent should help derive, break it into concrete evidence and synthesize together. Do not disguise a diagnosis or commitment demand as a neutral choice. When the user does not know, change the level of inquiry rather than repeating the abstraction. Near-term milestones must follow from requirements and reality; a desired number alone establishes neither feasibility nor a path.

Ask a small coherent round, listen, then ask follow-ups. Group independent questions; defer questions whose meaning depends on an unanswered earlier layer. Probe vague answers and contradictions with concrete examples. Do not dump this entire checklist at once, impose a fixed interview length, or mechanically re-ask facts already settled.

Use the host's interactive question tool when available (Hermes: `clarify`; OMP: `ask` in interactive sessions), following its actual schema. Put selectable answers in the tool's choice fields, not merely in question prose. Offer concise, neutral choices where useful and always allow a custom answer; use the built-in free-text/Other facility or an open-ended follow-up if needed. Prefer open-ended questions when predefined choices would bias the user's purpose or intent. Batch independent questions into one asking round where supported; wait for answers before asking dependent questions. If the tool is unavailable, ask in chat and wait instead. A dismissed, timed-out, or unanswered form is not an answer or confirmation.

**Exit:** enough specific answers to explain the intended direction, governing trade-offs, practical limits, and competing commitments. A vague opening prompt normally calls for questions—not a priority brief.

### 2. Confirm the decision frame before prescribing

Reflect back the discovered long-term direction, why it matters, governing trade-offs, starting position, and distinction between hard limits and learnable gaps. Ask the user to correct or confirm this frame; do not bundle agreement with premature exclusions. Surface contradictions rather than smoothing them over.

**Confirmation gate:** do not recommend a focus until this frame is user-confirmed. Explicit confirmation already present in the conversation counts; do not demand a ritual extra turn. Silence, missing information, and an agent's plausible interpretation do not count.

If the user explicitly requests a provisional answer without questions, label assumptions and give only a conditional assessment. Do not present the direction or bottleneck as validated. If interaction is unavailable, return the unresolved questions unless a confirmed frame was supplied; do not invent one merely to finish.

**Exit:** a user-confirmed decision frame, or a clearly blocked/provisional status. Do not use an experiment to avoid asking about intent, risk tolerance, resources, or commitments.

### 3. Establish the current bottleneck with the user

Derive the next meaningful milestone from the confirmed direction's necessary conditions and the actual starting position. Examine recent attempts, failures, unfinished deliverables, feedback, and dependencies with the user to locate what prevents that milestone. The user need not know the bottleneck in advance. Separate a requirement inferred from the path from a blocker demonstrated by evidence; work backward from the confirmed outcome, not forward from a favorite tool or an arbitrary near-term target.

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

Exclusion follows causal analysis: explain how an allocation serves or competes with the confirmed direction, which scarce resource it consumes, and what it displaces before seeking agreement to stop it. Technical buildability or low implementation cost does not establish strategic value; include adoption, operation, maintenance, and attention costs where material. Invite correction of the reasoning rather than testing willingness to renounce possibilities.

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
- The confirmed long-term direction, purpose, optimization priority, and hard constraints.
- The derived next milestone, required capabilities, and relevant learnable gaps.
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

Before prescribing, check that direction was discovered from context rather than demanded, near-term milestones were derived rather than arbitrarily targeted, learnable gaps were distinguished from hard limits, the frame was confirmed, and the bottleneck jointly examined. Exclusions must follow causal analysis, not precede it. Before returning a focus brief, check that one effort remains, each supporting allocation has a causal role, competing paths are explicitly stopped rather than sequenced, and review criteria can change the diagnosis. Never claim the user confirmed an assumption, a test proved more than it did, or a recommended cancellation/execution already happened.
