# Search in Rotated Sorted Array (LC 33)

Given a sorted array rotated at an unknown pivot (distinct values), find the index of a target in O(log n), or return -1.

## Approaches

### 1. Linear Scan
- **Time:** O(n) | **Space:** O(1)

### 2. Binary Search with Half-Identification
- **Time:** O(log n) | **Space:** O(1)
- At each step, determine which half is **properly sorted** by comparing `nums[lo]` to `nums[mid]`.
- If `nums[lo] <= nums[mid]`: left half is sorted. Check if target falls in `[nums[lo], nums[mid])` → search left; else search right.
- Otherwise: right half is sorted. Check if target falls in `(nums[mid], nums[hi]]` → search right; else search left.

## Key Insight

In a rotated array, at least one half is always sorted. By identifying the sorted half, we can check in O(1) whether the target is in it. If yes, narrow to that half; if no, the target must be in the other half. This preserves the O(log n) guarantee despite the rotation.

## Edge Cases

- Not rotated: `nums[lo] <= nums[mid]` always holds → behaves like standard binary search.
- Single element: `lo == hi`, one comparison.
- Target not present: loop exits with `lo > hi`, return -1.
- Target at the pivot boundary: the range checks `nums[lo] <= target < nums[mid]` handle this correctly.
