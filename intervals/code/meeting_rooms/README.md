# LC 252 — Meeting Rooms

Given meeting time intervals `[start, end]`, return `true` if a person can attend all meetings (no two meetings overlap).

## Approaches

### 1. Sort and Check Adjacent
- **Time:** O(n log n) | **Space:** O(1)
- Sort intervals by start time. Check each consecutive pair: if `intervals[i][0] < intervals[i-1][1]`, there's an overlap — return `False`.

## Key Insight

After sorting by start time, two meetings can only overlap if the later meeting starts before the earlier one ends. Checking only adjacent pairs is sufficient because if any two meetings overlap, the one that starts later will be adjacent to the one that starts earlier after sorting.

## Edge Cases

- Empty list: Return `True` (no meetings to conflict).
- Single meeting: Return `True`.
- Back-to-back meetings (e.g., `[1,5]` and `[5,10]`): Valid — end time equals start time, not an overlap (`<` not `<=`).
- Completely overlapping meetings (e.g., `[1,10]` and `[2,3]`): Return `False`.
