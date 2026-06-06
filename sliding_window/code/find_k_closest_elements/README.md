# Find K Closest Elements (LC 658)

Given a sorted array `arr`, integers `k` and `x`, return the `k` closest integers to `x`
in sorted order. Ties broken by smaller value.

## Approaches

### 1. Sort by Distance — O(n log n) time, O(n) space
Sort all elements by `|a - x|` (then by value for ties), take first `k`, re-sort.

**Why it works:** Directly ranks by closeness. Extra sort at the end restores ascending order.

### 2. Binary Search on Window Start — O(log n + k) time, O(1) space
Binary search for the left boundary of the k-element window. Compare `x - arr[mid]` vs `arr[mid+k] - x`. If the left edge is farther from `x` than the right edge, shift the window right.

**Why it works:** The answer is always a contiguous window of size `k` in the sorted array. Binary search finds the optimal left boundary by comparing which edge is closer to `x`.

## Key Insight
The answer is a contiguous window of size `k`. Binary search on the window's left boundary in range `[0, n-k]` finds it in O(log n).

## Edge Cases
- `x` smaller than all elements → window starts at index 0
- `x` larger than all elements → window ends at last index
- Tie in distance → smaller value wins (handled by `x - arr[mid] > arr[mid+k] - x` comparison)
- `k == len(arr)` → return entire array
