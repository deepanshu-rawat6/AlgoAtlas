# LC 918 — Maximum Sum Circular Subarray

Given a circular integer array `nums`, return the maximum possible sum of a non-empty subarray (the end wraps around to the beginning).

## Approaches

### 1. Kadane's for Max and Min Subarray
- **Time:** O(n) | **Space:** O(1)
- Two cases:
  1. **Non-wrapping**: Standard Kadane's for max subarray.
  2. **Wrapping**: The wrapping subarray's sum = `total - min_subarray_sum`. Use Kadane's variant to find the minimum subarray.
- Answer is `max(max_sum, total - min_sum)`, with a special case when all elements are negative.

## Key Insight

A wrapping subarray is the complement of some non-wrapping subarray. Maximizing the wrapping sum is equivalent to minimizing the non-wrapping sum (since `total` is fixed). Running Kadane's twice — once for max, once for min — covers both cases in O(n). The all-negative edge case must be handled separately: `total - min_sum = 0` would be wrong (empty subarray not allowed).

## Edge Cases

- All negative numbers: `total - min_sum = 0` is invalid (empty subarray). Return `max_sum` (the least negative element).
- Single element: Return that element.
- All positive: The entire array is the answer (non-wrapping case).
- Wrapping case: e.g., `[5, -3, 5]` → wrapping sum = 10 (5 + 5).
