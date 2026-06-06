"""
# 518. Coin Change II

## Problem
You are given an integer array `coins` representing coins of different denominations
and an integer `amount` representing a total amount of money. Return the number of
combinations that make up that amount. If that amount cannot be made up by any
combination of the coins, return 0. You may use each coin an unlimited number of times.

## Examples
```text
Input:  amount = 5, coins = [1,2,5]
Output: 4
Explanation: 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1

Input:  amount = 3, coins = [2]
Output: 0

Input:  amount = 10, coins = [10]
Output: 1
```

## Constraints
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- All values of coins are unique
- 0 <= amount <= 5000
"""
from typing import List


class Solution:
    def change_2d(self, amount: int, coins: List[int]) -> int:
        # Time: O(n*amount), Space: O(n*amount)
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i-1][j]
                if coins[i-1] <= j:
                    dp[i][j] += dp[i][j - coins[i-1]]
        return dp[n][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j] = ways to make amount j using first i coins
        # Either skip coin i or use it: dp[i][j] = dp[i-1][j] + dp[i][j-coin]
        # Time: O(n*amount), Space: O(amount)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]


if __name__ == '__main__':
    s = Solution()
    assert s.change(5, [1,2,5]) == 4
    assert s.change(3, [2]) == 0
    assert s.change(10, [10]) == 1
    assert s.change_2d(5, [1,2,5]) == 4
    print("All tests passed.")
