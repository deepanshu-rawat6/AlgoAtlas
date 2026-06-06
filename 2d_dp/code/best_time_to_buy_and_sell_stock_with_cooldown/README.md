# LC 309 — Best Time to Buy and Sell Stock with Cooldown

Given stock prices, find the maximum profit. After selling, you must wait one day (cooldown) before buying again. You may not hold multiple positions simultaneously.

## Approaches

### 1. State Machine DP
- **Time:** O(n) | **Space:** O(1)
- Three states: `hold` (own stock), `sold` (just sold, next day is cooldown), `rest` (cooldown or idle).
  - `hold = max(hold, rest - price)` — buy only from rest state
  - `sold = hold + price` — sell from hold state
  - `rest = max(rest, sold)` — rest after cooldown or stay resting

## Key Insight

Modeling the problem as a state machine with three states eliminates the need for a 2D DP table. The transitions enforce the cooldown: you can only buy from the `rest` state (not immediately after selling). Each state tracks the maximum profit achievable when entering that state on the current day.

## Edge Cases

- Single price: No transaction possible, return 0.
- Monotonically decreasing prices: Never buy, return 0.
- Two prices: Buy on day 0, sell on day 1 if profitable (no cooldown issue with just 2 days).
- Prices `[2, 1]`: Return 0 (buying at 2 and selling at 1 is a loss).
