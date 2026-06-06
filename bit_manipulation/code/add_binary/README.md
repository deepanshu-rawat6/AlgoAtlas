# LC 67 — Add Binary

Given two binary strings `a` and `b`, return their sum as a binary string.

## Approaches

### 1. Simulate Binary Addition with Carry
- **Time:** O(max(m, n)) | **Space:** O(max(m, n))
- Iterate from the rightmost digits of both strings simultaneously, adding digits and carry. Append `total % 2` to result and set `carry = total // 2`. Reverse the result at the end.

## Key Insight

Binary addition is identical to decimal addition but in base 2. The carry propagates left just like in decimal. Using `ord(c) - 48` converts a digit character to its integer value without `int()`. Building the result in reverse and joining at the end is more efficient than string concatenation.

## Edge Cases

- Different lengths: The shorter string is treated as having leading zeros (handled by the `i >= 0` / `j >= 0` checks).
- Carry after the last digit: The `while carry` condition handles this (e.g., `"1" + "1"` = `"10"`).
- `"0" + "0"` = `"0"`.
- One string is `"0"`: Return the other string.
