# LC 678 — Valid Parenthesis String

Given a string with `(`, `)`, and `*` (which can be `(`, `)`, or empty), return `true` if the string is valid.

## Approaches

### 1. Two-Pass Greedy
- **Time:** O(n) | **Space:** O(1)
- Left pass: treat `*` as `(`. If open count goes negative, return `False`.
- Right pass (reversed): treat `*` as `)`. If close count goes negative, return `False`.
- Both passes passing means a valid assignment exists.

### 2. Range Tracking [lo, hi]
- **Time:** O(n) | **Space:** O(1)
- Track the range `[lo, hi]` of possible open-paren counts. `(` increases both, `)` decreases both, `*` widens the range (`lo -= 1, hi += 1`). If `hi < 0`, return `False`. Clamp `lo = max(lo, 0)`. Valid if `lo == 0` at the end.

## Key Insight

The range `[lo, hi]` represents all possible open-paren counts given the `*` choices made so far. `hi` is the maximum (treating all `*` as `(`); `lo` is the minimum (treating all `*` as `)`). If `hi < 0`, even the most optimistic interpretation fails. If `lo == 0` at the end, there's at least one valid assignment.

## Edge Cases

- Empty string: Valid (return `True`).
- All `*`: Valid (treat all as empty).
- `"(*)"`: Valid — `*` can be empty or `)`.
- `")("`: Invalid — closing before opening.
- Unmatched `(` at the end: `lo > 0` catches this.
