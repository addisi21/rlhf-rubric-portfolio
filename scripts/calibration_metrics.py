#!/usr/bin/env python3
"""Compute simple reviewer calibration metrics for public RLHF samples."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "calibration_reviews.json"


def cohen_kappa(gold: list[str], reviewer: list[str]) -> float:
    labels = sorted(set(gold) | set(reviewer))
    total = len(gold)
    observed = sum(1 for left, right in zip(gold, reviewer) if left == right) / total
    gold_counts = Counter(gold)
    reviewer_counts = Counter(reviewer)
    expected = sum((gold_counts[label] / total) * (reviewer_counts[label] / total) for label in labels)
    if expected == 1:
        return 1.0
    return round((observed - expected) / (1 - expected), 3)


def main() -> None:
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    items = payload["items"]
    gold = [item["gold_verdict"] for item in items]
    reviewer = [item["reviewer_verdict"] for item in items]
    exact = sum(1 for left, right in zip(gold, reviewer) if left == right)
    score_errors = [abs(item["gold_score"] - item["reviewer_score"]) for item in items]

    print("# RLHF Calibration Metrics")
    print()
    print("| Metric | Value |")
    print("| --- | ---: |")
    print(f"| Items reviewed | {len(items)} |")
    print(f"| Exact verdict agreement | {exact}/{len(items)} |")
    print(f"| Agreement rate | {round(exact / len(items) * 100, 1)}% |")
    print(f"| Cohen kappa | {cohen_kappa(gold, reviewer)} |")
    print(f"| Mean absolute score error | {round(sum(score_errors) / len(score_errors), 2)} |")
    print()
    print("## Calibration Flags")
    print()
    for item in items:
        if item["gold_verdict"] != item["reviewer_verdict"]:
            print(f"- **{item['id']}**: verdict mismatch. {item['notes']}")
        elif abs(item["gold_score"] - item["reviewer_score"]) >= 1:
            print(f"- **{item['id']}**: score calibration gap. {item['notes']}")


if __name__ == "__main__":
    main()
