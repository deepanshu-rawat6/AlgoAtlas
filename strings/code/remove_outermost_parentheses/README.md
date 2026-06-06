# LC 1021 — Remove Outermost Parentheses

## Problem
Given a valid parentheses string `s`, decompose it into primitive valid strings
(cannot be split further). Remove the outermost parentheses of each primitive
and return the result.

**Example:**
- `s = "(()())(())"` → `"()()()"`
- `s = "(()())(())(()(()))"` → `"()()()()(())"`
- `s = "()()"` → `""`

**Constraints:** `1 <= s.length <= 10^5`, `s` is a valid parentheses string.

---

## Approach — Depth Counter  `O(n)` time · `O(n)` space

Use an integer `depth` to track nesting level as we scan left to right.

- On `(`: if `depth > 0` it is NOT the outermost open paren → keep it.
  Then increment depth.
- On `)`: decrement depth first. If `depth > 0` it is NOT the outermost
  close paren → keep it.

**Why it works:** A primitive starts when depth goes 0 → 1 and ends when
depth goes 1 → 0. Those two boundary characters are the outermost pair we
want to discard. Every character in between (depth ≥ 1 after the open,
depth ≥ 1 before the close) belongs to the inner content.

---

## Key Insight
Skip a character only at the exact moment depth transitions through 0↔1.
All other characters are inner content and should be kept.

---

## Edge Cases
| Input | Output | Reason |
|-------|--------|--------|
| `"()"` | `""` | Single primitive, both chars are outermost |
| `"()()"` | `""` | Two primitives, both stripped |
| `"((()))"` | `"(())"` | One primitive, strip one layer |
| Very long string | — | O(n) handles 10^5 comfortably |

---

## Complexity
- **Time:** O(n) — single pass
- **Space:** O(n) — result list (output itself is O(n) in worst case)
