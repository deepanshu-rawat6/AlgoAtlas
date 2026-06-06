"""
LC 1137 — N-th Tribonacci Number
==================================

The Tribonacci sequence is defined as:
  T(0) = 0, T(1) = 1, T(2) = 1
  T(n) = T(n-1) + T(n-2) + T(n-3) for n >= 3

Return the value of T(n).

Examples
--------
```text
Input:  n = 4
Output: 4
Explanation: T(4) = T(3) + T(2) + T(1) = 2 + 1 + 1 = 4

Input:  n = 25
Output: 1389537
```

Constraints
-----------
- 0 <= n <= 37
"""


class Solution:
    # Approach 1: DP array — O(n) time, O(n) space
    def tribonacci(self, n: int) -> int:
        # dp[i] = dp[i-1] + dp[i-2] + dp[i-3]; base cases T(0)=0, T(1)=T(2)=1
        if n == 0:
            return 0
        if n <= 2:
            return 1
        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]

    # Approach 2: Space-optimized — O(n) time, O(1) space
    def tribonacci_opt(self, n: int) -> int:
        # Rolling three variables: a, b, c represent T(n-2), T(n-1), T(n)
        if n == 0:
            return 0
        if n <= 2:
            return 1
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c


if __name__ == "__main__":
    sol = Solution()
    assert sol.tribonacci(0) == 0
    assert sol.tribonacci(1) == 1
    assert sol.tribonacci(2) == 1
    assert sol.tribonacci(4) == 4
    assert sol.tribonacci(25) == 1389537
    assert sol.tribonacci_opt(4) == 4
    assert sol.tribonacci_opt(25) == 1389537
    print("All tests passed.")
