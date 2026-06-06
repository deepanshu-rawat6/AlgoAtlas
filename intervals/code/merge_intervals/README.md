# LC 56 — Merge Intervals

Given an array of intervals, merge all overlapping intervals and return the non-overlapping result.

## Approaches

### 1. Sort by Start + Linear Merge
- **Time:** O(n log n) | **Space:** O(n)
- Sort by start time. Maintain a result list. For each interval, if it overlaps with the last result interval (`start <= result[-1][1]`), extend the last interval's end. Otherwise, append as a new interval.

## Key Insight

Sorting by start time ensures that any interval overlapping with the current one must be adjacent in the sorted order. Two intervals overlap iff the later one's start ≤ the earlier one's end. The merge is done in-place on the result list by updating the last interval's end to `max(last_end, current_end)` — handles containment too.

## Edge Cases

- Single interval: Return it as-is.
- No overlaps: Return the sorted input.
- All intervals overlap: Return one merged interval.
- Containment (e.g., `[1,4]` and `[2,3]`): The `max` of ends handles this correctly.
- Adjacent intervals (e.g., `[1,4]` and `[4,5]`): Merged into `[1,5]` since `4 <= 4`.
