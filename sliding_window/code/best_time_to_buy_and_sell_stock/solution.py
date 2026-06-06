from typing import List


class Solution:
    """
    ## 121. Best Time to Buy and Sell Stock

    You are given an array `prices` where `prices[i]` is the price of a given stock on
    the `i`-th day. You want to maximize your profit by choosing a single day to buy one
    stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot
    achieve any profit, return `0`.

    ### Examples

    ```text
    Input:  prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price=1), sell on day 5 (price=6), profit = 6-1 = 5.

    Input:  prices = [7, 6, 4, 3, 1]
    Output: 0
    Explanation: No profitable transaction possible.
    ```

    ### Constraints

    - `1 <= prices.length <= 10^5`
    - `0 <= prices[i] <= 10^4`
    """

    def maxProfit_brute(self, prices: List[int]) -> int:
        # Try every buy-sell pair — O(n^2)
        # O(n^2) time, O(1) space
        max_p = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_p = max(max_p, prices[j] - prices[i])
        return max_p

    def maxProfit(self, prices: List[int]) -> int:
        # Track the minimum price seen so far as the best buy day
        # At each price, compute profit if we sold today; update best
        # O(n) time, O(1) space
        min_price, max_p = float("inf"), 0
        for price in prices:
            min_price = min(min_price, price)
            max_p = max(max_p, price - min_price)
        return max_p


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([1, 2]) == 1
    assert sol.maxProfit_brute([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit_brute([7, 6, 4, 3, 1]) == 0
    print("All tests passed.")
