# LC 43 — Multiply Strings

Given two non-negative integers as strings `num1` and `num2`, return their product as a string. No built-in BigInteger or direct integer conversion allowed.

## Approaches

### 1. Grade-School Multiplication
- **Time:** O(m × n) | **Space:** O(m + n)
- Allocate a result array of size `m + n`. For each digit pair `(i, j)`, the product contributes to positions `i + j` (carry) and `i + j + 1` (digit). After all multiplications, convert the array to a string, stripping leading zeros.

## Key Insight

The product of `num1[i]` and `num2[j]` (0-indexed from the right) contributes to position `i + j + 1` in the result (with carry to `i + j`). This position mapping is the core insight: it avoids the need to shift intermediate results. Processing all digit pairs and accumulating into the position array, then propagating carries, mirrors how long multiplication works on paper.

## Edge Cases

- Either input is `"0"`: Return `"0"` immediately.
- Single-digit inputs: Standard multiplication.
- Large inputs (up to 200 digits each): The O(m × n) approach handles this within constraints.
- Result has leading zeros in the position array: Strip with `lstrip('0')`.
