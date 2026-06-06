# LC 66 — Plus One

Given a large integer represented as a digit array (most significant first), increment it by one and return the result as a digit array.

## Approaches

### 1. Carry Propagation from End
- **Time:** O(n) | **Space:** O(1) extra (O(n) for result in worst case)
- Iterate from the last digit. If `digit < 9`, increment and return. If `digit == 9`, set it to 0 and continue (carry propagates). If all digits were 9, prepend 1.

## Key Insight

Adding 1 only propagates a carry when the current digit is 9 (becomes 10, write 0 carry 1). The loop can exit early as soon as a non-9 digit is found. The only case requiring a new digit is when all digits are 9 (e.g., `[9, 9, 9]` → `[1, 0, 0, 0]`), handled by prepending 1 after the loop.

## Edge Cases

- `[9]`: Returns `[1, 0]`.
- `[9, 9, 9]`: Returns `[1, 0, 0, 0]`.
- `[1, 2, 3]`: Returns `[1, 2, 4]` (no carry).
- `[1, 9, 9]`: Returns `[2, 0, 0]` (carry propagates through two 9s).
