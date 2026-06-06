# Best Time to Buy and Sell Stock (LC 121)

Given a `prices` array where `prices[i]` is the stock price on day `i`, find the maximum
profit from a single buy-sell transaction. Return 0 if no profit is possible.

## Approaches

### 1. Brute Force — O(n²) time, O(1) space
Try every buy-sell pair `(i, j)` where `i < j`. Track the maximum difference.

**Why it works:** Exhaustive search, but redundantly recomputes many pairs.

### 2. Sliding Window / One Pass — O(n) time, O(1) space
Track the minimum price seen so far. At each price, compute profit if sold today (`price - min_price`). Update the best profit.

**Why it works:** The optimal buy day is always the minimum price seen before the sell day. Tracking the running minimum ensures we always consider the best possible buy price for each sell day.

## Key Insight
Track the running minimum as the "best buy day so far." The answer is the maximum of `(current price - running minimum)` across all days.

## Edge Cases
- Strictly decreasing prices → profit is 0
- Single element → profit is 0
- All prices equal → profit is 0
- Maximum profit at the very last day
