# Count Subsequences with Sum K

Given an array `nums` and integer `k`, count all subsequences whose elements sum to `k`.

## Approaches

### 1. Recursion with Memoization
- **Time:** O(n × k) | **Space:** O(n × k)
- `dp(idx, remaining)` = count of subsequences from `nums[idx:]` that sum to `remaining`. At each index, either include or exclude the element. Memoize on `(idx, remaining)`.

### 2. Backtracking
- **Time:** O(2ⁿ) | **Space:** O(n) call stack
- Explore all 2ⁿ include/exclude combinations. At each leaf (all elements processed), check if the current sum equals `k`.

## Key Insight

The memoized approach avoids recomputing the same `(idx, remaining)` state. The key observation is that the count from position `idx` with remaining sum `r` is the same regardless of how we got there — this is the optimal substructure that makes memoization valid. The backtracking approach is simpler but exponential.

## Edge Cases

- `k = 0`: The empty subsequence counts. Return 1 (plus any subsets of zeros).
- All elements larger than `k`: Only the empty subsequence (if `k = 0`), else 0.
- Duplicate elements: Each occurrence is treated independently (e.g., `[1,1,1], k=2` → 3 ways).
- `nums = [1, 2, 1], k = 2`: Two ways — `[2]` and `[1, 1]`.
