# LC 1614 — Maximum Nesting Depth of the Parentheses

## Problem
Given a valid parenthesized string `s` (a VPS), return the nesting depth —
the maximum number of open parentheses that are simultaneously open at any point.

**Example:**
- `s="(1+(2*3)+((8)/4))+1"` → `3`
- `s="(1)+((2))+(((3)))"` → `3`
- `s="1+(2*3)/(2-1)"` → `1`

**Constraints:** `1 <= s.length <= 100`, `s` is a valid parenthesized string.

---

## Approach — Single Pass Counter  `O(n)` time · `O(1)` space

Maintain a running `depth` counter:
- Increment on `(`, then update `max_depth`.
- Decrement on `)`.

Ignore all other characters (digits, operators). The maximum value `depth`
ever reaches is the answer.

**Why it works:** `depth` at any position equals the number of unmatched
open parentheses seen so far, which is exactly the nesting level at that point.

---

## Key Insight
You don't need a stack. A single integer tracks the current depth because
parentheses are always balanced (VPS guarantee). The maximum of this counter
over the entire string is the answer.

---

## Edge Cases
| Input | Output | Reason |
|-------|--------|--------|
| `"1"` | `0` | No parentheses |
| `"()"` | `1` | Single pair |
| `"(())"` | `2` | Nested pair |
| `"()()"` | `1` | Sequential, not nested |
| `"((()))"` | `3` | Triple nesting |

---

## Complexity
- **Time:** O(n) — single pass
- **Space:** O(1) — two integer variables
