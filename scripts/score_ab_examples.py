#!/usr/bin/env python3
"""Score reconstructed A/B RLHF examples and print a markdown summary."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "ab_evaluations.json"


def avg(scores: dict[str, int]) -> float:
    return round(sum(scores.values()) / len(scores), 2)


def main() -> None:
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))

    print("# RLHF A/B Evaluation Summary")
    print()
    print("| Example | Category | Avg A | Avg B | Preferred | Decision Gap |")
    print("| --- | --- | ---: | ---: | --- | ---: |")

    for item in payload["examples"]:
        avg_a = avg(item["scores"]["A"])
        avg_b = avg(item["scores"]["B"])
        gap = round(avg_a - avg_b, 2)
        print(
            f"| {item['id']} | {item['category']} | {avg_a} | {avg_b} | "
            f"{item['preferred']} | {gap} |"
        )

    print()
    print("## Reviewer Rationale")
    print()
    for item in payload["examples"]:
        print(f"- **{item['id']}**: {item['rationale']}")


if __name__ == "__main__":
    main()
