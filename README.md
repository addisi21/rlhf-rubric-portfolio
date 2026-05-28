# RLHF Rubric Portfolio

This repository demonstrates public-facing rubric structures for RLHF, SFT, prompt evaluation, side-by-side model comparison, and AI response quality review. The rubrics are based on real evaluation experience but rewritten for public use.

## Core Rubric Dimensions

| Dimension | What It Checks |
| --- | --- |
| Instruction adherence | Whether the response follows the user request and constraints |
| Factual accuracy | Whether claims are supported, precise, and not hallucinated |
| Helpfulness | Whether the response solves the user's actual need |
| Safety | Whether the response avoids harmful, policy-violating, or risky guidance |
| Formatting | Whether the output follows required structure, schema, or presentation rules |
| Verbosity | Whether the response is appropriately concise or detailed |
| UX quality | Whether the response feels usable, clear, and context-aware |

## Evaluation Workflow

1. Read the prompt and identify explicit and implied requirements.
2. Check whether the response satisfies all hard constraints.
3. Score high-risk dimensions first: safety, factuality, and instruction adherence.
4. Compare competing responses when doing side-by-side evaluation.
5. Write short, evidence-based feedback.
6. Flag recurring patterns for calibration.

## Included Files

- `rubric-template.md`: a reusable model-response evaluation rubric
- `side-by-side-review.md`: an example structure for comparing two AI responses
- `evaluated-response-examples.md`: completed public examples with Response A/B scoring, preferred response decisions, and reviewer rationale

## Confidentiality Standard

No platform-specific internal rubrics, private prompts, screenshots, or real task outputs are included.
