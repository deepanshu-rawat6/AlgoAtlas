# LC 435 — Non-overlapping Intervals

Given an array of intervals, return the minimum number of intervals to remove to make the rest non-overlapping.

## Approaches

### 1. Greedy — Sort by End Time
- **Time:** O(n log n) | **Space:** O(1)
- Sort by end time. Greedily keep intervals with the earliest end. When an overlap is detected (`start < prev_end`), remove the current interval (increment `removed`). Otherwise, update `prev_end`.

## Key Insight

This is the classic Activity Selection Problem. Sorting by end time and greedily keeping the interval that ends earliest maximizes the number of non-overlapping intervals we can keep. When two intervals overlap, we always remove the one with the later end time (the current one, since we sorted by end) — it leaves more room for future intervals.

The answer is `n - (max non-overlapping intervals kept)`.

## Edge Cases

- No overlaps: Return 0.
- All intervals identical: Remove `n - 1`.
- `[[1,2],[2,3]]`: No overlap (touching endpoints are not overlapping), return 0.
- `[[1,3],[1,3],[1,3]]`: Remove 2, return 2.
- Single interval: Return 0.
