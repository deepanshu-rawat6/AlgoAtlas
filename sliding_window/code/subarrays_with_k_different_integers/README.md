# Subarrays with K Different Integers (LC 992)

Given an integer array `nums` and integer `k`, return the number of good subarrays —
subarrays with exactly `k` different integers.

## Approaches

### 1. atMost(k) - atMost(k-1) — O(n) time, O(k) space
`exactly(k) = atMost(k) - atMost(k-1)`. Each `atMost(limit)` counts subarrays with at most `limit` distinct integers using a sliding window.

**Why it works:** Exact-count problems on distinct values can't be solved directly with a single sliding window (the window can't maintain "exactly k"). Decomposing into two at-most problems sidesteps this — each at-most is a standard shrink-when-violated window.

## Key Insight
`exactly(k) = atMost(k) - atMost(k-1)` — the fundamental trick for exact-count sliding window problems. A single window can't enforce "exactly k" but two at-most windows can.

## Edge Cases
- `k == 1` → count subarrays with exactly one distinct integer
- `k > number of distinct values` → 0
- All elements identical → subarrays of any length have 1 distinct value; answer is 0 unless `k == 1`
- Array of length 1 → 1 if `k == 1`, else 0
