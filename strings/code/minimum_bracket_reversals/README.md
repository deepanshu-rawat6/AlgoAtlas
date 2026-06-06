# Minimum Bracket Reversals

## Problem

Given a bracket expression containing only `{` and `}`, find the minimum number of reversals to make it balanced. Return -1 if impossible.

**Example:**
- `"}{"` → 2
- `"{{}}"`→ 0
- `"{{{"` → -1 (odd length)

## Approach: Stack

**Why stack?** A stack naturally cancels matched `{}` pairs. After processing, only unmatched brackets remain, always in the form `}}}...{{{` (all closes before all opens).

**Steps:**
1. If `len(s)` is odd → return -1 immediately
2. Use stack: push `{`; on `}`, pop if top is `{` (matched), else push `}`
3. Count remaining `close` (}s) and `open` ({s)
4. Answer: `ceil(close/2) + ceil(open/2)`

**Why ceil division?** Each pair of `}}` needs 1 reversal (flip one `}` to `{`). Same for `{{`.

**Complexity:** O(n) time, O(n) space

## Key Insight

After stack reduction, the string looks like `}^a {^b`. To fix `}}` → `{}` costs 1 reversal. To fix `{{` → `{}` costs 1 reversal. Odd counts round up.

## Edge Cases

- Odd length → always -1
- Already balanced → 0
- All same bracket → `ceil(n/2)` reversals (if even length)
