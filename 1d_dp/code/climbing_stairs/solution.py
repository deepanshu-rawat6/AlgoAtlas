"""
LC 70 — Climbing Stairs
=======================

You are climbing a staircase. It takes `n` steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Examples
--------
```text
Input:  n = 2
Output: 2
Explanation: 1+1, 2

Input:  n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1
```

Constraints
-----------
- 1 <= n <= 45
"""

from functools import lru_cache


class Solution:
    # Approach 1: Recursion with memoization — O(n) time, O(n) space
    def climbStairs(self, n: int) -> int:
        # dp(i) = ways to reach step i = dp(i-1) + dp(i-2) (Fibonacci-like)
        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            if i <= 1:
                return 1
            return dp(i - 1) + dp(i - 2)
        return dp(n)

    # Approach 2: Bottom-up DP — O(n) time, O(n) space
    def climbStairs_dp(self, n: int) -> int:
        # Bottom-up: fill table[i] = table[i-1] + table[i-2]
        if n <= 1:
            return 1
        table = [0] * (n + 1)
        table[0], table[1] = 1, 1
        for i in range(2, n + 1):
            table[i] = table[i - 1] + table[i - 2]
        return table[n]

    # Approach 3: Space-optimized — O(n) time, O(1) space
    def climbStairs_opt(self, n: int) -> int:
        # Space-optimized: only keep last two values
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    sol = Solution()
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(5) == 8
    assert sol.climbStairs_dp(3) == 3
    assert sol.climbStairs_opt(3) == 3
    print("All tests passed.")
