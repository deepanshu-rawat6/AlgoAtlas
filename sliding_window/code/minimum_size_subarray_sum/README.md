# Minimum Size Subarray Sum (LC 209)

Given an array of positive integers `nums` and positive integer `target`, return the
minimal length of a contiguous subarray with sum ≥ `target`. Return 0 if none exists.

## Approaches

### 1. Brute Force — O(n²) time, O(1) space
For each start index, expand right until sum ≥ target. Track the minimum length found.

**Why it works:** Correct but redundantly recomputes sums from each start.

### 2. Sliding Window — O(n) time, O(1) space
Expand right to grow the sum. While `sum >= target`, record the window length and shrink from the left. Each element is added and removed at most once.

**Why it works:** All values are positive, so shrinking the window always decreases the sum. This monotonicity makes the two-pointer approach valid — we can greedily shrink whenever the constraint is met.

## Key Insight
Positive values only → shrinking always decreases sum. This monotonicity is what makes the sliding window valid here.

## Edge Cases
- No subarray reaches `target` → return 0
- Single element ≥ target → return 1
- Entire array needed → return `len(nums)`
- All elements are 1 and target is large
