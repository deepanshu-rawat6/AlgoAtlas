# Search Insert Position (LC 35)

Given a sorted array of distinct integers and a target, return its index if found, or the index where it would be inserted to maintain sorted order.

## Approaches

### 1. Linear Scan
- **Time:** O(n) | **Space:** O(1)
- Return the first index where `nums[i] >= target`, or `len(nums)` if target is larger than all.

### 2. Binary Search
- **Time:** O(log n) | **Space:** O(1)
- Standard binary search. When the target is not found, `lo` naturally converges to the correct insertion point.
- After the loop, `lo` is the leftmost index where `nums[lo] >= target` (or `len(nums)` if target is largest).

## Key Insight

The insertion point is exactly where `lo` lands when the binary search loop exits without finding the target. This works because `lo` always moves to `mid + 1` when `nums[mid] < target`, so it ends up at the first position where the value would be ≥ target. No special-casing needed — the same `lo` that would find the target also gives the insertion index.

## Edge Cases

- Target already in array → return its index (found during search).
- Target smaller than all elements → `lo` stays at 0 → insert at index 0.
- Target larger than all elements → `lo` ends at `len(nums)` → append at end.
- Single element array: works correctly.
