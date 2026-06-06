# LC 191 — Number of 1 Bits (Hamming Weight)

Given a positive integer `n`, return the number of set bits (1s) in its binary representation.

## Approaches

### 1. Check Each Bit
- **Time:** O(32) | **Space:** O(1)
- Check each of the 32 bits with a mask, counting set bits.

### 2. Brian Kernighan's Algorithm
- **Time:** O(k) where k = number of set bits | **Space:** O(1)
- `n &= n - 1` clears the lowest set bit. Count how many times until `n = 0`.

## Key Insight

`n & (n-1)` clears the rightmost set bit of `n`. This is because subtracting 1 flips all bits from the rightmost set bit downward, and ANDing with the original clears that bit. This makes the algorithm run in O(k) time where k is the number of set bits — faster than O(32) when the number is sparse.

## Edge Cases

- `n = 0`: 0 set bits (though constraints say n ≥ 1).
- `n = 1`: 1 set bit.
- `n = 2147483647` (all 31 bits set): 31 set bits.
- Powers of 2: Exactly 1 set bit; Brian Kernighan terminates in 1 iteration.
