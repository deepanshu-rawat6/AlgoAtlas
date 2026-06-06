# LC 268 — Missing Number

Given an array of `n` distinct numbers in range `[0, n]`, find the one missing number.

## Approaches

### 1. Sum Formula
- **Time:** O(n) | **Space:** O(1)
- Expected sum of `[0, n]` is `n*(n+1)/2`. Subtract the actual sum to get the missing number.

### 2. XOR
- **Time:** O(n) | **Space:** O(1)
- XOR all indices `0..n` with all values in `nums`. Pairs cancel out (a XOR a = 0), leaving only the missing number.

## Key Insight

Both approaches exploit the fact that every number except one appears exactly once. The sum approach uses arithmetic: the difference between expected and actual sum is the missing value. The XOR approach uses the property that XOR is its own inverse: pairing each index with its corresponding value cancels them, leaving the unpaired index (the missing number).

## Edge Cases

- Missing `0`: Both approaches handle this correctly.
- Missing `n` (the largest): Also handled correctly.
- `nums = [0]`: Missing 1. `n = 1`, XOR: `1 ^ 0 ^ 0 = 1`. ✓
- Single element `[1]`: Missing 0.
