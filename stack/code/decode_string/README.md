# Decode String (LC 394)

Given an encoded string like `"3[a2[c]]"`, decode it by repeating each `encoded_string` inside brackets `k` times. Brackets can be nested.

## Approaches

### 1. Iterative Stack
- **Time:** O(n) | **Space:** O(n)
- Track `cur_str` (current string being built) and `cur_num` (current repeat count).
- On `[`: save `(cur_num, cur_str)` to stack, reset both.
- On `]`: pop `(num, prev_str)`, set `cur_str = prev_str + cur_str * num`.
- On digit: accumulate multi-digit numbers with `cur_num = cur_num * 10 + digit`.
- On letter: append to `cur_str`.

### 2. Recursive Descent
- **Time:** O(n) | **Space:** O(n) call stack
- Parse with an index pointer. On a digit, read the full number, skip `[`, recurse for the inner string, skip `]`, repeat.
- Returns `(decoded_string, next_index)` so the caller knows where to continue.

## Key Insight

Nesting is the core challenge. The stack approach handles it by **saving state** at each `[` and **restoring** it at `]` — exactly like a call stack. The recursive approach makes this explicit. Multi-digit numbers (e.g., `100[a]`) require accumulating digits before the `[`.

## Edge Cases

- Multi-digit repeat counts: `10[a]` → `aaaaaaaaaa`.
- Nested brackets: `3[a2[c]]` → inner `2[c]` = `cc`, then `3[acc]` = `accaccacc`.
- No brackets: plain letters pass through unchanged.
- Repeat count of 1: `1[abc]` → `abc`.
