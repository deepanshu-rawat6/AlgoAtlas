# Z-Function

## Problem

For string `s`, compute Z-array where `Z[i]` = length of the longest substring starting at `i` that matches a prefix of `s`.

**Example:** `s="aabxaa"` → `[0, 1, 0, 0, 2, 1]`

## Approach: Z-Array with Z-Box

**Why maintain a Z-box?** Without it, we'd recompute from scratch at each position → O(n²). The Z-box [l, r] represents the rightmost interval where `s[l..r] = s[0..r-l]`. For any `i ≤ r`, we already know `s[i..r] = s[i-l..r-l]`, so `Z[i] ≥ min(Z[i-l], r-i)`.

**Algorithm:**
1. For each `i` from 1 to n-1:
   - If `i ≤ r`: initialize `Z[i] = min(Z[i-l], r-i)`
   - Extend: while `s[Z[i]] == s[i+Z[i]]`, increment `Z[i]`
   - Update `[l, r]` if `i + Z[i] > r`

**Complexity:** O(n) — each character is compared at most twice

## Key Insight

The Z-box is the "memory" of the algorithm. Each position is extended at most once before becoming part of a Z-box, giving amortized O(1) per position.

## Pattern Matching with Z-Function

Build `t = pattern + '#' + text`. Positions where `Z[i] == len(pattern)` are match starts in text. The `#` separator ensures Z values don't exceed `len(pattern)`.

## Edge Cases

- Z[0] is undefined (whole string matches prefix); conventionally set to 0 or n
- Single character string → all Z values are 0
