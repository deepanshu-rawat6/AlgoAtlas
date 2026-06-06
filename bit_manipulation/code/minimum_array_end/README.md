# LC 3133 — Minimum Array End

Construct a strictly increasing array of `n` positive integers where the bitwise AND of all elements equals `x`. Return the minimum possible last element.

## Approaches

### 1. Embed (n-1) into Zero-Bits of x
- **Time:** O(64) | **Space:** O(1)
- The array must start at `x` (to preserve the AND). Each subsequent element must keep all bits of `x` set and differ only in the zero-bit positions of `x`. Embed the bits of `(n-1)` into the zero-bit positions of `x` to get the minimum last element.

## Key Insight

All elements must have every bit of `x` set (to maintain AND = x). The "free" bit positions are the zeros in `x`. To make the array strictly increasing with minimum last element, use the zero-bit positions to count from 0 to `n-1`. Embedding `(n-1)` into the zero-bits of `x` gives the smallest number that is ≥ x, has all bits of x set, and is the (n-1)-th such number.

## Edge Cases

- `n = 1`: Only one element needed, which is `x` itself.
- `x` has no zero bits (all 1s): The only valid array is `[x, x+1, ...]` but AND would lose bits — actually `x = 2^k - 1` means the zero-bits are above `x`, so we embed into higher bits.
- `n = 1, x = 1`: Return 1.
