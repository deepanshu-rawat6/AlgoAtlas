"""
# LC 122: Best Time to Buy and Sell Stock II

You are given an integer array `prices` where `prices[i]` is the price of a
given stock on the i-th day. On each day, you may decide to buy and/or sell the
stock. You can only hold at most one share of the stock at any time. However,
you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

## Examples

```text
Input:  prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price=1), sell on day 3 (price=5), profit=4.
             Buy on day 4 (price=3), sell on day 5 (price=6), profit=3.
             Total profit = 7.

Input:  prices = [1,2,3,4,5]
Output: 4

Input:  prices = [7,6,4,3,1]
Output: 0
```

## Constraints
- 1 <= prices.length <= 3 * 10^4
- 0 <= prices[i] <= 10^4
"""
from typing import List


class Solution:
    def maxProfit_brute(self, prices: List[int]) -> int:
        """Recursion — O(2^n) time, O(n) stack space."""
        # Recursive DFS: at each day decide to buy, sell, or skip
        # Exponential without memoization — illustrates the decision tree
        def dfs(i: int, holding: bool) -> int:
            if i == len(prices):
                return 0
            # skip
            best = dfs(i + 1, holding)
            if holding:
                best = max(best, prices[i] + dfs(i + 1, False))
            else:
                best = max(best, -prices[i] + dfs(i + 1, True))
            return best
        return dfs(0, False)

    def maxProfit(self, prices: List[int]) -> int:
        """Greedy — O(n) time, O(1) space."""
        # Greedy: capture every upward price movement as profit
        # Equivalent to buying and selling on every consecutive rising day
        return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))


if __name__ == "__main__":
    s = Solution()

    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([1]) == 0

    print("All tests passed.")
