# Check Subsequence with Sum K

Given an array `nums` and integer `k`, return `True` if any subsequence of `nums` sums to `k`.

## Approaches

### 1. Recursion with Early Termination
- **Time:** O(2ⁿ) worst case | **Space:** O(n) call stack
- At each index, try including or excluding the current element. If `remaining == 0`, return `True` immediately (early termination). Skip elements that would overshoot the target.

## Key Insight

This is the decision version of the subset-sum problem. The early termination on `remaining == 0` avoids exploring the rest of the tree once a valid subsequence is found. Pruning elements that exceed `remaining` reduces the search space when elements are non-negative. For a counting version, see `count_subsequences_with_sum_k`.

## Edge Cases

- `k = 0`: The empty subsequence sums to 0, return `True`.
- All elements larger than `k`: No valid subsequence, return `False`.
- Single element equal to `k`: Return `True`.
- `nums = [5], k = 3`: Return `False`.
