"""
LC 343 — Integer Break
=======================

Given an integer `n`, break it into the sum of k positive integers (k >= 2),
and maximize the product of those integers. Return the maximum product.

Examples
--------
```text
Input:  n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 * 1 = 1

Input:  n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 * 3 * 4 = 36
```

Constraints
-----------
- 2 <= n <= 58
"""


class Solution:
    # Approach 1: DP — O(n^2) time, O(n) space
    def integerBreak(self, n: int) -> int:
        # dp[i] = max product from breaking i; try all splits j and (i-j)
        # Either keep (i-j) as-is or break it further: max(i-j, dp[i-j])
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

    # Approach 2: Math (greedy with 3s) — O(n) time, O(1) space
    def integerBreak_math(self, n: int) -> int:
        # Greedy: break into 3s as much as possible (3s maximize product)
        # Handle remainders 2 and 4 specially
        if n == 2:
            return 1
        if n == 3:
            return 2
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        return product * n


if __name__ == "__main__":
    sol = Solution()
    assert sol.integerBreak(2) == 1
    assert sol.integerBreak(10) == 36
    assert sol.integerBreak(3) == 2
    assert sol.integerBreak_math(2) == 1
    assert sol.integerBreak_math(10) == 36
    assert sol.integerBreak_math(3) == 2
    print("All tests passed.")
