# LC 1851 — Minimum Interval to Include Each Query

Given intervals and queries, for each query find the size (`end - start + 1`) of the smallest interval containing the query point. Return -1 if none exists.

## Approaches

### 1. Sort + Sweep with Min-Heap
- **Time:** O((n + q) log n) | **Space:** O(n + q)
- Sort intervals by start. Sort queries with original indices. Sweep queries in order:
  1. Push all intervals with `start <= query` into a min-heap keyed by size.
  2. Pop intervals from the heap that have already ended (`end < query`).
  3. The heap top is the smallest valid interval for this query.

## Key Insight

By processing queries in sorted order, we can incrementally add intervals as their start becomes ≤ the current query. The min-heap by size ensures we always find the smallest containing interval efficiently. Lazy deletion (popping expired intervals when they're at the top) avoids the cost of removing them eagerly.

## Edge Cases

- Query point before all intervals: Return -1.
- Query point after all intervals: Return -1.
- Multiple intervals of the same size: Any one is valid (heap returns one).
- Query exactly at interval boundary: Interval contains the query (`start <= query <= end`).
- Duplicate query values: Each is answered independently.
