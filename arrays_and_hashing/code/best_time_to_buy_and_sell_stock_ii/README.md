# Best Time to Buy and Sell Stock II (LC 122)

Given a `prices` array where `prices[i]` is the stock price on day `i`, find the maximum
profit. You may buy and sell on the same day and hold at most one share at a time.

## Approaches

### 1. Recursive DFS — O(2ⁿ) time, O(n) stack space
At each day, decide to buy, sell, or skip. Explores all decision paths.

**Why it works:** Correct but exponential — illustrates the decision tree without memoization.

### 2. Greedy — O(n) time, O(1) space
Sum up every positive day-over-day price difference: `sum(max(prices[i] - prices[i-1], 0))`.

**Why it works:** Any upward price movement can be captured as profit. Buying and selling on every consecutive rising day is equivalent to holding through the entire rise — the math is identical.

## Key Insight
Capture every upward tick. `profit(day1→day3) = profit(day1→day2) + profit(day2→day3)`, so summing adjacent positive differences equals the optimal multi-transaction profit.

## Edge Cases
- Strictly decreasing prices → profit is 0
- Single element → profit is 0
- All prices equal → profit is 0
- Prices rise then fall → only capture the rising portion
