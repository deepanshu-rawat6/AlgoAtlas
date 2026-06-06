"""
# 901. Online Stock Span

## Problem
Design an algorithm that collects daily price quotes for some stock and returns
the **span** of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of
consecutive days (starting from today and going backwards) for which the stock
price was less than or equal to today's price.

## Examples
```text
Input:
  ["StockSpanner","next","next","next","next","next","next","next"]
  [[],[100],[80],[60],[70],[60],[75],[85]]
Output:
  [null,1,1,1,2,1,4,6]

Explanation:
  next(100) -> 1  (no previous days)
  next(80)  -> 1  (80 < 100)
  next(60)  -> 1  (60 < 80)
  next(70)  -> 2  (70 >= 60, but 70 < 80)
  next(60)  -> 1
  next(75)  -> 4  (75 >= 60, 70, 60, but 75 < 80)
  next(85)  -> 6  (85 >= 75, 60, 70, 60, 80, but 85 < 100)
```

## Constraints
- `1 <= price <= 10^5`
- At most `10^4` calls will be made to `next`
"""


class StockSpanner:
    """Approach 1: Brute force — scan backwards on each call."""

    def __init__(self):
        # O(n) per call, O(n) space
        self.prices: list = []

    def next(self, price: int) -> int:
        # Collapse all previous days with price <= current into one span
        # Stack stores (price, span) pairs; accumulate spans of dominated days
        # O(n) time — linear scan back through history
        self.prices.append(price)
        span = 1
        i = len(self.prices) - 2
        while i >= 0 and self.prices[i] <= price:
            span += 1
            i -= 1
        return span


class StockSpannerOptimal:
    """Approach 2: Monotonic stack — O(1) amortized per call."""

    def __init__(self):
        self.stack: list = []  # (price, span)

    def next(self, price: int) -> int:
        # Collapse all previous days with price <= current into one span
        # Stack stores (price, span) pairs; accumulate spans of dominated days
        # O(1) amortized — collapse dominated entries into accumulated span
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


if __name__ == "__main__":
    for Cls in (StockSpanner, StockSpannerOptimal):
        sp = Cls()
        assert sp.next(100) == 1
        assert sp.next(80) == 1
        assert sp.next(60) == 1
        assert sp.next(70) == 2
        assert sp.next(60) == 1
        assert sp.next(75) == 4
        assert sp.next(85) == 6
    print("All tests passed.")
