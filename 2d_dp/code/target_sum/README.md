# LC 494 — Target Sum

Given `nums` and a `target`, assign `+` or `-` to each number and count the number of expressions that evaluate to `target`.

## Approaches

### 1. Brute Force DFS
- **Time:** O(2ⁿ) | **Space:** O(n)
- Explore all 2ⁿ sign assignments recursively. At each index, branch into adding or subtracting the current number.

### 2. DP with Hash Map
- **Time:** O(n × sum) | **Space:** O(sum)
- `dp` maps current sum → number of ways to reach it. For each number, create a new map by adding and subtracting the number from every existing sum. Final answer is `dp[target]`.

## Key Insight

The hash map DP avoids the exponential blowup by grouping all paths that reach the same intermediate sum. Instead of tracking individual paths, we track how many ways each sum is reachable. This is equivalent to a 2D DP table `dp[i][sum]` but uses a dictionary to handle negative sums naturally without offset arithmetic.

## Edge Cases

- `target` outside `[-sum(nums), sum(nums)]`: Return 0.
- All zeros with `target = 0`: Every assignment works, return `2ⁿ`.
- Single element: Return 1 if `nums[0] == abs(target)`, else 0.
- `nums = [1], target = 2`: Impossible, return 0.
