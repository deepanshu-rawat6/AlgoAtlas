# LC 190 — Reverse Bits

Reverse the bits of a 32-bit unsigned integer.

## Approaches

### 1. Bit-by-Bit
- **Time:** O(32) | **Space:** O(1)
- For each of 32 iterations: shift result left by 1, OR in the lowest bit of `n`, shift `n` right by 1.

### 2. Divide and Conquer (Bit Manipulation)
- **Time:** O(1) | **Space:** O(1)
- Swap 16-bit halves, then 8-bit groups, then 4-bit groups, then 2-bit groups, then individual bits using masks. Five operations total.

## Key Insight

The divide-and-conquer approach treats the 32-bit integer as a sequence of groups and swaps them at each level. The masks isolate alternating groups: `0xFF00FF00` selects the upper bytes of each 16-bit half, etc. This is O(1) in the sense that it's a fixed number of operations regardless of input, making it faster than the 32-iteration loop for hardware implementations.

## Edge Cases

- `n = 0`: All bits are 0, result is 0.
- `n = 0xFFFFFFFF`: All bits are 1, result is 0xFFFFFFFF.
- `n = 1` (bit 0 set): Result has bit 31 set = 2147483648.
- Python's arbitrary precision integers require masking with `0xFFFFFFFF` at the end.
