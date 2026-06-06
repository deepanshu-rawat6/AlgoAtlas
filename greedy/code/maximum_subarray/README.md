# LC 53 — Maximum Subarray

Given an integer array `nums`, find the contiguous subarray with the largest sum and return its sum.

## Approaches

### 1. Brute Force
- **Time:** O(n²) | **Space:** O(1)
- Try all O(n²) subarrays and track the maximum sum.

### 2. Kadane's Algorithm
- **Time:** O(n) | **Space:** O(1)
- `curr = max(x, curr + x)`: either extend the current subarray or start fresh at `x`. Track `best = max(best, curr)` throughout.

## Key Insight

Kadane's algorithm makes a greedy decision at each element: if the running sum becomes negative, it's better to start a new subarray from the current element than to carry the negative sum forward. A negative prefix can only hurt any future subarray. The `max(x, curr + x)` formulation elegantly captures this: if `curr < 0`, starting fresh at `x` is better.

## Edge Cases

- All negative numbers: Return the largest (least negative) single element.
- Single element: Return that element.
- All positive: Return the sum of the entire array.
- Mix of positive and negative: Kadane's handles this optimally.
