# LC 860 — Lemonade Change

Each lemonade costs $5. Customers pay with $5, $10, or $20 bills. Starting with no change, return `true` if you can give every customer correct change.

## Approaches

### 1. Greedy with Bill Tracking
- **Time:** O(n) | **Space:** O(1)
- Track counts of $5 and $10 bills. For $10: give back one $5. For $20: prefer giving $10 + $5 (saves $5 bills for future use); fall back to three $5 bills.

## Key Insight

$5 bills are the most versatile — they're needed as change for both $10 and $20 payments. When making $15 change for a $20 bill, always prefer using a $10 + $5 over three $5 bills. This greedy choice preserves $5 bills for future $10 payments where they're the only option. $20 bills are never useful as change.

## Edge Cases

- First customer pays $10 or $20: No $5 bills available, return `False`.
- All $5 bills: Always return `True` (no change needed).
- `[5, 5, 10, 10, 20]`: Second $10 payment fails — only one $5 left after first $10.
- Empty bills array: Return `True` (no customers).
