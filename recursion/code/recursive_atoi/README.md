# LC 8 Variant — Recursive atoi (String to Integer)

Implement `atoi` recursively: strip leading whitespace, read optional sign, then read digits until a non-digit is encountered. Clamp result to 32-bit signed integer range.

## Approaches

### 1. Recursive Digit Accumulation
- **Time:** O(n) | **Space:** O(n) call stack
- Strip whitespace and parse sign iteratively upfront. Then recurse: `recurse(idx, current) = recurse(idx+1, current*10 + digit)` while `s[idx]` is a digit. Base case: non-digit or end of string.

## Key Insight

The recursive structure mirrors the iterative digit-by-digit accumulation: `current = current * 10 + new_digit`. Each recursive call processes one digit and passes the accumulated value forward. The sign and whitespace are handled before recursion to keep the recursive function pure. Clamping to 32-bit range is applied to the final result.

## Edge Cases

- Leading whitespace: Stripped with `lstrip()` before recursion.
- Optional sign (`+` or `-`): Parsed before the recursive digit reading.
- Non-digit characters after digits (e.g., `"4193 with words"`): Recursion stops at the space.
- No digits after sign/whitespace (e.g., `"words and 987"`): Returns 0.
- Overflow: Clamp to `[-2³¹, 2³¹ - 1]`.
