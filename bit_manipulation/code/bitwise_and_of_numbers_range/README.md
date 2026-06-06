# LC 201 — Bitwise AND of Numbers Range

Given `[left, right]`, return the bitwise AND of all numbers in the range.

## Approaches

### 1. Right-Shift Until Equal (Common Prefix)
- **Time:** O(32) | **Space:** O(1)
- Right-shift both `left` and `right` until they're equal, counting shifts. Left-shift the result back. This finds the common binary prefix of all numbers in the range.

### 2. Brian Kernighan — Strip Lowest Set Bit
- **Time:** O(32) | **Space:** O(1)
- Repeatedly clear the lowest set bit of `right` (`right &= right - 1`) until `right <= left`. The result is `right`.

## Key Insight

Any bit that differs between `left` and `right` will be 0 in the AND of the entire range (because the range contains both a number with that bit set and one with it cleared). Only the common prefix of `left` and `right` survives. The right-shift approach finds this prefix directly. Brian Kernighan's trick strips the differing low bits from `right` until it matches `left`.

## Edge Cases

- `left == right`: AND of a single number is itself.
- `left = 0`: Result is always 0 (0 ANDed with anything is 0).
- `left = 1, right = 2147483647`: All bits differ, result is 0.
- Powers of 2 range: The common prefix may be just the leading bit.
