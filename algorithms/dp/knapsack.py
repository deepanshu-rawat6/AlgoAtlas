"""
Knapsack Dynamic Programming
=============================
Classic DP problems built on the knapsack recurrence.

0/1 Knapsack:
  Each item used at most once.
  dp[i][w] = max value using first i items with capacity w
  Recurrence: dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]] + val[i])
  Time: O(n*W), Space: O(n*W) → O(W) with rolling array

Unbounded Knapsack:
  Each item can be used unlimited times.
  dp[w] = max(dp[w], dp[w - wt[i]] + val[i])  (iterate items inside)
  Time: O(n*W), Space: O(W)

Variants covered:
  - Subset Sum: can we partition into target sum?
  - Coin Change: minimum coins to make amount
  - Coin Change II: number of ways to make amount
  - Partition Equal Subset Sum
"""

from typing import List, Optional


# ─── 0/1 Knapsack ─────────────────────────────────────────────────────────────

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Space-optimized 0/1 knapsack using 1D dp array.
    CRITICAL: iterate capacity in REVERSE to avoid using same item twice.
    """
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        # reverse iteration ensures dp[w - weights[i]] is from previous item
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


def knapsack_01_with_items(weights: List[int], values: List[int], capacity: int):
    """Returns (max_value, selected_item_indices) using full 2D table for backtracking."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # backtrack to find selected items
    selected, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected[::-1]


# ─── Unbounded Knapsack ───────────────────────────────────────────────────────

def knapsack_unbounded(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Each item can be picked unlimited times.
    CRITICAL: iterate capacity FORWARD so dp[w - weights[i]] already includes
    current item (allowing reuse).
    """
    dp = [0] * (capacity + 1)
    for w in range(1, capacity + 1):
        for i in range(len(weights)):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


# ─── Subset Sum ───────────────────────────────────────────────────────────────

def subset_sum(nums: List[int], target: int) -> bool:
    """Can any subset of nums sum to target? O(n*target) time, O(target) space."""
    dp = [False] * (target + 1)
    dp[0] = True   # empty subset sums to 0

    for num in nums:
        for w in range(target, num - 1, -1):   # reverse: 0/1 style
            dp[w] = dp[w] or dp[w - num]

    return dp[target]


# ─── Coin Change (minimum coins) ──────────────────────────────────────────────

def coin_change(coins: List[int], amount: int) -> int:
    """
    Minimum number of coins to make amount. Unbounded (reuse allowed).
    Returns -1 if impossible.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for w in range(coin, amount + 1):   # forward: unbounded
            dp[w] = min(dp[w], dp[w - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# ─── Coin Change II (number of ways) ─────────────────────────────────────────

def coin_change_ways(coins: List[int], amount: int) -> int:
    """
    Number of combinations (not permutations) to make amount.
    Outer loop over coins ensures each combination counted once.
    """
    dp = [0] * (amount + 1)
    dp[0] = 1   # one way to make 0: use no coins

    for coin in coins:
        for w in range(coin, amount + 1):
            dp[w] += dp[w - coin]

    return dp[amount]


# ─── Partition Equal Subset Sum ───────────────────────────────────────────────

def can_partition(nums: List[int]) -> bool:
    """
    Can nums be split into two subsets with equal sum?
    Equivalent to: can any subset sum to total//2?
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    return subset_sum(nums, total // 2)


if __name__ == "__main__":
    # 0/1 Knapsack
    weights = [2, 3, 4, 5]
    values  = [3, 4, 5, 6]
    cap     = 8
    print("0/1 Knapsack max value:", knapsack_01(weights, values, cap))  # 10
    val, items = knapsack_01_with_items(weights, values, cap)
    print(f"  Items selected: {items}, value: {val}")

    # Unbounded Knapsack
    print("\nUnbounded Knapsack:", knapsack_unbounded([1, 3, 4], [1, 4, 5], 7))  # 9

    # Subset Sum
    print("\nSubset sum [3,1,5,9,12] → 20:", subset_sum([3, 1, 5, 9, 12], 20))  # True (3+5+12)
    print("Subset sum [3,1,5,9,12] → 21:", subset_sum([3, 1, 5, 9, 12], 21))  # True (9+12)
    print("Subset sum [3,1,5,9,12] → 22:", subset_sum([3, 1, 5, 9, 12], 22))  # False

    # Coin Change
    print("\nMin coins [1,5,6,9] → 11:", coin_change([1, 5, 6, 9], 11))  # 2 (5+6)
    print("Min coins [2] → 3:", coin_change([2], 3))                     # -1

    # Coin Change II
    print("\nWays [1,2,5] → 5:", coin_change_ways([1, 2, 5], 5))  # 4

    # Partition
    print("\nCan partition [1,5,11,5]:", can_partition([1, 5, 11, 5]))  # True
    print("Can partition [1,2,3,5]:", can_partition([1, 2, 3, 5]))     # False
