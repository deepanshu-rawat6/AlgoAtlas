"""
LC 322 — Coin Change
=====================

You are given an integer array `coins` representing coins of different denominations
and an integer `amount` representing a total amount of money.
Return the fewest number of coins needed to make up that amount.
If that amount cannot be made up, return -1.
You may assume you have an infinite number of each coin.

Examples
--------
```text
Input:  coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 5 + 5 + 1 = 11

Input:  coins = [2], amount = 3
Output: -1

Input:  coins = [1], amount = 0
Output: 0
```

Constraints
-----------
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""

from typing import List
from functools import lru_cache


class Solution:
    # Approach 1: Top-down memoization — O(amount * n) time, O(amount) space
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp(rem) = 1 + min(dp(rem-c) for each coin c); base: dp(0)=0
        @lru_cache(maxsize=None)
        def dp(rem: int) -> int:
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            return min(1 + dp(rem - c) for c in coins)

        result = dp(amount)
        return result if result != float('inf') else -1

    # Approach 2: Bottom-up DP — O(amount * n) time, O(amount) space
    def coinChange_dp(self, coins: List[int], amount: int) -> int:
        # dp[i] = min coins to make amount i; try each coin and take minimum
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0
    assert sol.coinChange([1, 5, 11], 11) == 1
    assert sol.coinChange_dp([1, 2, 5], 11) == 3
    assert sol.coinChange_dp([2], 3) == -1
    print("All tests passed.")
