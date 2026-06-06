# Find Minimum in Rotated Sorted Array (LC 153)

Given a sorted array rotated at an unknown pivot, find the minimum element in O(log n).

## Approaches

### 1. Linear Scan
- **Time:** O(n) | **Space:** O(1)
- Return `min(nums)`.

### 2. Binary Search
- **Time:** O(log n) | **Space:** O(1)
- Compare `nums[mid]` to `nums[hi]`.
- If `nums[mid] > nums[hi]`: the rotation point (minimum) is in the right half → `lo = mid + 1`.
- Otherwise: the minimum is in the left half including `mid` → `hi = mid`.
- Loop until `lo == hi`; return `nums[lo]`.

## Key Insight

In a rotated sorted array, one half is always "properly sorted" and the other contains the rotation point (minimum). Comparing `nums[mid]` to `nums[hi]` tells us which half has the minimum: if `mid > hi`, the right half is out of order (minimum is there); otherwise the left half is out of order or `mid` itself is the minimum.

Using `nums[hi]` (not `nums[lo]`) as the pivot avoids ambiguity when `lo == mid`.

## Edge Cases

- Not rotated (e.g., `[1, 2, 3, 4]`) → `nums[mid] <= nums[hi]` always → `hi` converges to 0 → minimum is `nums[0]`.
- Rotated by 1 position: minimum is at the last index.
- Single element: `lo == hi` immediately, return `nums[0]`.
- All elements unique (guaranteed by constraints).
