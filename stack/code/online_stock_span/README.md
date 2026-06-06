# Online Stock Span (LC 901)

Design a data structure that returns the **span** of a stock's price for the current day — the number of consecutive days (going backwards, including today) where the price was ≤ today's price.

## Approaches

### 1. Brute Force — Linear Scan
- **Time:** O(n) per call | **Space:** O(n)
- Store all prices; on each `next()`, scan backwards until a higher price is found.
- Simple but degrades to O(n²) total for n calls.

### 2. Monotonic Stack (Optimal)
- **Time:** O(1) amortized per call | **Space:** O(n)
- Stack stores `(price, span)` pairs. When a new price arrives, pop all entries with price ≤ current and accumulate their spans.
- Each element is pushed and popped at most once → O(1) amortized.
- The accumulated span collapses dominated days into a single entry, so future queries skip them entirely.

## Key Insight

Instead of re-scanning dominated days on every call, we **collapse** them into a single `(price, span)` entry. A day is "dominated" if its price ≤ the current price — it can never be the answer for any future query either, so it's safe to merge it.

## Edge Cases

- First call always returns span = 1 (no previous days).
- Strictly decreasing prices → every span is 1, stack grows to n entries.
- Strictly increasing prices → each call pops the entire stack, span = total days so far.
- Equal prices count as part of the span (condition is `<=`).
