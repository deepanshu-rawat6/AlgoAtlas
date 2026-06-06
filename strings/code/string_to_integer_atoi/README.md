# LC 8 — String to Integer (atoi)

## Problem
Implement `myAtoi(s)` which converts a string to a 32-bit signed integer.

Rules (in order):
1. Skip leading whitespace.
2. Read optional `+` or `-` sign.
3. Read digits until a non-digit or end of string.
4. Clamp result to `[-2^31, 2^31 - 1]`.

**Example:**
- `"   -42"` → `-42`
- `"4193 with words"` → `4193`
- `"words and 987"` → `0`
- `"-91283472332"` → `-2147483648`

**Constraints:** `0 <= s.length <= 200`, ASCII characters.

---

## Approach — Sequential Parsing  `O(n)` time · `O(1)` space

Process the string in four sequential steps matching the problem rules:
1. Advance index past whitespace.
2. Capture sign if present.
3. Accumulate digits into an integer (stop at first non-digit).
4. Multiply by sign, then clamp with `max(INT_MIN, min(INT_MAX, result))`.

No regex, no state machine needed — the rules map directly to sequential
index manipulation.

---

## Key Insight
Clamp **after** building the full number. Clamping digit-by-digit is error-prone.
`max(INT_MIN, min(INT_MAX, result))` is the cleanest one-liner clamp.

---

## Edge Cases
| Input | Output | Reason |
|-------|--------|--------|
| `""` | `0` | Empty string |
| `"  "` | `0` | Only spaces |
| `"+-12"` | `0` | Two signs → stop at `+` |
| `"+0 123"` | `0` | Stop at space after `0` |
| `"2147483648"` | `2147483647` | Overflow clamped |
| `"-2147483649"` | `-2147483648` | Underflow clamped |

---

## Complexity
- **Time:** O(n) — single pass
- **Space:** O(1) — no extra data structures
