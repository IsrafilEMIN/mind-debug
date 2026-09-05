# v0.2.0 focus regression scenarios

Status: specified, not live-tested. Earlier smoke results apply only to v0.1.0 and supplied one-shot facts; they did not test the interview behavior that failed in actual use.

## K — Do not prescribe before intent

Opening prompt: “I want to scale applied AI. I have courses, subscriptions, local LLM experiments, and side projects. What should I do first?”

Required first response: ask a coherent purpose/outcome/optimization round, not a diagnosis or recommendation. Establish resources, constraints, advantages, risk tolerance, feasible choices, and allocations in subsequent dependent rounds. No broad options table or default customer-interview prescription.

Fail: infer a bottleneck and suggest an experiment before asking what the user actually means by success.

## L — Focus is exclusion, not sequencing

After interview and explicit confirmation: goal is reliable applied-AI delivery capacity; accessible validated workflow; failing representative evals; sufficient existing model budget; no offline or cost blocker. Current commitments include relevant eval study, one required model subscription, local-inference cost optimization, and an unrelated side project.

Required: jointly examine the evaluation failure bottleneck, concentrate work on the target workflow, justify bounded relevant learning and subscription use, stop local optimization and unrelated project allocation. State reclaimed resources only when amounts are supplied.

Fail: “First evals, then local inference, then the side project,” or give each a percentage of the goal's budget merely to preserve them.

## M — Practice on the path

Prompt after confirmation: “I need evaluation and production-delivery practice. I'll learn it by building a local-model runner first.”

Required: ask which target capability the runner develops and why target-work practice would not do it more directly. Reject the detour when no causal dependency is established; propose practice on the actual or representative delivery work, not a second pursuit.

Fail: accept vague transferable learning as sufficient justification.

## N — Several inputs, one direction

Prompt after confirmation: “Should focus mean canceling my model subscription and dropping the course even though I use both on the selected delivery work?”

Required: distinguish primary effort from bounded support. Keep resources justified by immediate use, relevant outputs, and constraints; cut redundant or unused inputs, not inputs simply because they are multiple.

Fail: reduce focus to one tool, one expense, or one kind of activity.

## O — Contradictory objectives

Opening: “I want fastest delivery, minimum spending, deep mastery, and zero risk.”

Required: expose trade-offs and ask which objective governs and which minimums are non-negotiable. Do not assume speed wins, fabricate feasible zero risk, or prescribe before confirmation.

## P — Noninteractive uncertainty

Prompt: “Prioritize my business,” with no confirmed frame and no opportunity for follow-up.

Required: return unresolved questions/blocked status. If explicitly asked to assume, provide a labeled conditional assessment without claiming confirmation.

Fail: substitute an invented purpose or an unrequested exploratory task just to output Now.

## Review protocol

Run in fresh sessions with the revised payload. Preserve the user's answers and the agent's question rounds; score confirmation and exclusion behavior, not just the final recommendation. Require transcript evidence for each pass. Do not feed expected answers to the evaluated agent or count a structural string check as behavioral success.
