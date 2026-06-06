# LC 371 — Sum of Two Integers

Return the sum of two integers `a` and `b` without using `+` or `-` operators.

## Approaches

### 1. XOR + AND Carry Loop
- **Time:** O(32) | **Space:** O(1)
- `a ^ b` gives the sum without carry. `(a & b) << 1` gives the carry. Repeat until no carry remains. Mask to 32 bits to handle Python's arbitrary precision integers.

## Key Insight

Binary addition works bit by bit: XOR gives the sum bit (1+0=1, 0+1=1, 0+0=0, 1+1=0 with carry), and AND gives the carry bit (1+1=carry 1). Shifting the carry left by 1 aligns it with the next bit position. Repeating until carry is 0 completes the addition. Python requires a 32-bit mask because its integers are arbitrary precision (negative numbers don't naturally wrap around).

## Edge Cases

- `a = 0` or `b = 0`: No carry, result is the other number.
- `a = -1, b = 1`: Result is 0. The carry propagation handles this.
- Both negative: The mask and sign extension handle Python's representation.
- `a = b`: Result is `2a` (left shift by 1).
