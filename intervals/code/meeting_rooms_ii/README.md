# LC 253 — Meeting Rooms II

Given meeting time intervals, return the minimum number of conference rooms required.

## Approaches

### 1. Min-Heap of End Times
- **Time:** O(n log n) | **Space:** O(n)
- Sort by start time. Use a min-heap of end times. For each meeting, if the earliest-ending room finishes before this meeting starts, reuse it (replace in heap). Otherwise, allocate a new room (push to heap). Heap size = rooms needed.

### 2. Chronological Ordering (Two Sorted Arrays)
- **Time:** O(n log n) | **Space:** O(n)
- Sort starts and ends separately. Use two pointers: if the next start < current earliest end, a new room is needed; otherwise, a room is freed (advance end pointer).

## Key Insight

The minimum rooms needed equals the maximum number of meetings happening simultaneously. The heap approach greedily reuses the room that frees up soonest. The two-pointer approach is equivalent but avoids the heap: it counts how many meetings have started but not yet ended at any point in time.

## Edge Cases

- Single meeting: Return 1.
- No overlapping meetings: Return 1.
- All meetings at the same time: Return `n`.
- Back-to-back meetings (end == start): The room is freed before the next meeting starts.
