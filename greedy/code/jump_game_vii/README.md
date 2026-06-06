# LC 1871 — Jump Game VII

Given a binary string `s` and integers `minJump`, `maxJump`, starting at index 0 (which is `'0'`), return `true` if you can reach the last index. You can jump from index `i` to any `j` where `i + minJump ≤ j ≤ i + maxJump` and `s[j] == '0'`.

## Approaches

### 1. DP with Sliding Window Prefix Sum
- **Time:** O(n) | **Space:** O(n)
- `reach[i] = True` if index `i` is reachable. For each `i`, count reachable positions in the window `[i - maxJump, i - minJump]` using a sliding window prefix sum (`prefix`). If `prefix > 0` and `s[i] == '0'`, then `reach[i] = True`.

## Key Insight

A naive DP would be O(n × (maxJump - minJump)) — too slow. The sliding window prefix sum reduces this to O(n): instead of checking every position in the jump range, maintain a running count of reachable positions in the current window. Add `reach[i - minJump]` when it enters the window and subtract `reach[i - maxJump - 1]` when it leaves.

## Edge Cases

- `s[-1] == '1'`: Last index is `'1'`, can never land there, return `False`.
- `minJump == maxJump`: Fixed jump size; only specific positions are reachable.
- `s = "00"` with `minJump = maxJump = 1`: Jump from 0 to 1, return `True`.
- Long string of `'1'`s after index 0: No reachable `'0'` positions, return `False`.
