"""
# 309. Best Time to Buy and Sell Stock with Cooldown

## Problem
You are given an array `prices` where `prices[i]` is the price of a given stock on
the i-th day. Find the maximum profit you can achieve. You may complete as many
transactions as you like with the following restrictions:
- After you sell your stock, you cannot buy stock on the next day (cooldown of 1 day).
- You may not engage in multiple transactions simultaneously (must sell before buying).

## Examples
```text
Input:  prices = [1,2,3,0,2]
Output: 3
Explanation: Buy on day 0 (price=1), sell on day 1 (price=2),
             cooldown on day 2, buy on day 3 (price=0), sell on day 4 (price=2).
             Profit = (2-1) + (2-0) = 3

Input:  prices = [1]
Output: 0
```

## Constraints
- 1 <= prices.length <= 5000
- 0 <= prices[i] <= 1000
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # States: holding, sold (cooldown), idle
        # holding: max(prev_holding, prev_idle - price)
        # sold: prev_holding + price
        # idle: max(prev_idle, prev_sold)
        # Time: O(n), Space: O(1)
        # States: hold (own stock), sold (just sold, next day is cooldown), rest (cooldown/idle)
        hold, sold, rest = -float('inf'), 0, 0
        for p in prices:
            hold, sold, rest = max(hold, rest - p), hold + p, max(rest, sold)
        return max(sold, rest)


if __name__ == '__main__':
    s = Solution()
    assert s.maxProfit([1,2,3,0,2]) == 3
    assert s.maxProfit([1]) == 0
    assert s.maxProfit([2,1]) == 0
    assert s.maxProfit([1,2]) == 1
    print("All tests passed.")
