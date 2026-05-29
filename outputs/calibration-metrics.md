# RLHF Calibration Metrics

Generated from `data/calibration_reviews.json` with
`scripts/calibration_metrics.py`.

| Metric | Value |
| --- | ---: |
| Items reviewed | 6 |
| Exact verdict agreement | 5/6 |
| Agreement rate | 83.3% |
| Cohen kappa | 0.571 |
| Mean absolute score error | 0.33 |

## Calibration Flags

- **CAL-002**: score calibration gap. Reviewer agreed on preferred response but scored safety one point lower due to missing caveat.
- **CAL-005**: verdict mismatch. Reviewer over-weighted friendliness and under-weighted policy grounding.
