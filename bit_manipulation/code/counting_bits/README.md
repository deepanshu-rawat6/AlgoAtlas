# LC 338 — Counting Bits

Given `n`, return an array of length `n+1` where `ans[i]` is the number of 1-bits in the binary representation of `i`.

## Approaches

### 1. Naive (Brian Kernighan per number)
- **Time:** O(n × 32) | **Space:** O(n)
- For each number, count its set bits independently using `n &= n-1`.

### 2. DP with Right-Shift
- **Time:** O(n) | **Space:** O(n)
- `dp[i] = dp[i >> 1] + (i & 1)`. Right-shifting `i` removes the last bit; `i & 1` adds it back. This reuses already-computed results.

## Key Insight

`i >> 1` is `i` with its least significant bit removed — a number we've already processed. The number of 1-bits in `i` equals the number of 1-bits in `i >> 1` plus the value of `i`'s last bit (`i & 1`). This gives an O(n) DP where each value is computed in O(1) from a previously computed value.

## Edge Cases

- `n = 0`: Return `[0]`.
- `n = 1`: Return `[0, 1]`.
- Powers of 2: `dp[2^k] = 1` (only one set bit).
- `2^k - 1` (all ones): `dp[2^k - 1] = k`.
