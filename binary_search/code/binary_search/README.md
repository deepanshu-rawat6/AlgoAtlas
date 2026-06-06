# Binary Search (LC 704)

Given a sorted array of unique integers and a target, return the target's index or -1 if not found.

## Approaches

### 1. Linear Scan
- **Time:** O(n) | **Space:** O(1)
- Iterate through the array and return the index when the value matches.

### 2. Binary Search
- **Time:** O(log n) | **Space:** O(1)
- Maintain `lo` and `hi` pointers. At each step, compare `nums[mid]` to target.
- If equal, return `mid`. If less, search right half (`lo = mid + 1`). If greater, search left half (`hi = mid - 1`).
- Return -1 if the loop ends without finding the target.

## Key Insight

Each comparison eliminates half the remaining search space. The invariant is: if target exists, it's always within `[lo, hi]`. When `lo > hi`, the target is absent. This is the foundational binary search template — all other binary search problems build on this pattern.

## Edge Cases

- Single element array: works correctly (lo == hi == 0, one comparison).
- Target smaller than all elements: `hi` drops below 0, return -1.
- Target larger than all elements: `lo` exceeds last index, return -1.
- Target at first or last position: handled by the standard loop.
