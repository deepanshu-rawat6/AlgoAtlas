"""
LC 746 — Min Cost Climbing Stairs
==================================

You are given an integer array `cost` where `cost[i]` is the cost of the i-th step.
Once you pay the cost, you can climb one or two steps.
You can either start from index 0 or index 1.
Return the minimum cost to reach the top of the floor (beyond the last index).

Examples
--------
```text
Input:  cost = [10, 15, 20]
Output: 15
Explanation: Start at index 1, pay 15, climb 2 steps to the top.

Input:  cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
```

Constraints
-----------
- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999
"""

from typing import List
from functools import lru_cache


class Solution:
    # Approach 1: Top-down memoization — O(n) time, O(n) space
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp(i) = cost[i] + min(dp(i+1), dp(i+2)); can start at 0 or 1
        n = len(cost)

        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            if i >= n:
                return 0
            return cost[i] + min(dp(i + 1), dp(i + 2))

        return min(dp(0), dp(1))

    # Approach 2: Bottom-up DP — O(n) time, O(n) space
    def minCostClimbingStairs_dp(self, cost: List[int]) -> int:
        # dp[i] = min cost to reach step i from step i-1 or i-2
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]

    # Approach 3: Space-optimized — O(n) time, O(1) space
    def minCostClimbingStairs_opt(self, cost: List[int]) -> int:
        # Rolling two variables for O(1) space
        a, b = 0, 0
        for i in range(2, len(cost) + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b


if __name__ == "__main__":
    sol = Solution()
    assert sol.minCostClimbingStairs([10, 15, 20]) == 15
    assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert sol.minCostClimbingStairs_dp([10, 15, 20]) == 15
    assert sol.minCostClimbingStairs_opt([10, 15, 20]) == 15
    print("All tests passed.")
