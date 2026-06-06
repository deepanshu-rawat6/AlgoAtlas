# Add Two Numbers (LC 2)

Two non-negative integers are stored in reverse order in linked lists. Add them and return the sum as a linked list (also in reverse order).

## Approaches

### 1. Digit-by-Digit Simulation
- **Time:** O(max(m, n)) | **Space:** O(max(m, n))
- Traverse both lists simultaneously, summing corresponding digits plus carry.
- `divmod(val, 10)` gives the new carry and the digit to store.
- Continue until both lists are exhausted **and** carry is 0.

## Key Insight

Storing digits in reverse order is actually convenient — the least significant digit is at the head, which is where we start adding. We don't need to reverse anything. The carry propagates naturally: after the last digit, if carry is still 1, we append one more node.

Using a dummy head simplifies the code by avoiding special-casing the first node.

## Edge Cases

- Different length lists: the shorter list contributes 0 for its missing digits.
- Final carry: `[9,9,9,9,9,9,9] + [9,9,9,9]` → result has 8 digits with a leading 1.
- Both lists are `[0]` → result is `[0]`.
- Single digit lists: `[5] + [5]` → `[0, 1]` (carry produces a second node).
