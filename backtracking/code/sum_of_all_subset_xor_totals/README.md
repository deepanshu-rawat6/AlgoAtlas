# Sum of All Subset XOR Totals (LC 1863)

Given an array `nums`, return the sum of XOR totals for every subset. The XOR total of
a subset is the XOR of all its elements (0 for empty subset).

## Approaches

### 1. Brute Force (Bitmask)
**Complexity:** O(2ⁿ · n) time, O(1) space

Enumerate all 2ⁿ subsets using bitmasks. For each subset, compute its XOR and add to
the total.

**Why it works:** Directly computes the answer by definition. Correct but slow for
large `n`.

### 2. Bit Manipulation (O(n))
**Complexity:** O(n) time, O(1) space

OR all elements together, then multiply by `2^(n-1)`.

**Why it works:** For each bit position, a bit contributes to the XOR total of a subset
iff an odd number of elements in the subset have that bit set. By symmetry, exactly
half of all subsets (2^(n-1)) will have an odd count for any bit that appears in at
least one element. The OR of all elements identifies which bits appear at all.
So each such bit contributes `2^(n-1)` to the total sum.

## Key Insight

The mathematical insight: each bit that appears in **any** element contributes exactly
`2^(n-1)` to the total sum (half of all subsets have that bit set in their XOR).
OR-ing all elements identifies the active bits; multiplying by `2^(n-1)` gives the answer.

## Edge Cases

- Single element — sum = element (only non-empty subset is the element itself).
- All zeros — sum = 0.
- `n = 12` (max) — `2^11 = 2048` multiplier.
