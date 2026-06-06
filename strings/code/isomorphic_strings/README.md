# LC 205 — Isomorphic Strings

## Problem
Two strings `s` and `t` are isomorphic if characters in `s` can be replaced
to get `t`, with each character mapping to exactly one other character and no
two characters mapping to the same character (bijection).

**Example:**
- `s="egg"`, `t="add"` → `True`  (e→a, g→d)
- `s="foo"`, `t="bar"` → `False` (o cannot map to both a and r)
- `s="paper"`, `t="title"` → `True`

**Constraints:** `1 <= s.length <= 5*10^4`, `s` and `t` have equal length.

---

## Approach — Two Hash Maps  `O(n)` time · `O(1)` space*

Maintain two dictionaries:
- `s_to_t`: maps each character in `s` to its corresponding character in `t`
- `t_to_s`: maps each character in `t` back to `s`

At each position, check consistency in both directions. If either map already
has a conflicting entry, return `False`.

*Space is O(1) because the alphabet is fixed (at most 256 ASCII chars).

**Why two maps?** A single map `s→t` catches "one s-char maps to two t-chars"
but misses "two s-chars map to the same t-char". The reverse map `t→s` catches
the latter, together enforcing a true bijection.

---

## Key Insight
Isomorphism requires a **bijective** mapping. One map only enforces injection
in one direction. You need both `s→t` and `t→s` to guarantee no two source
characters share the same target.

---

## Edge Cases
| s | t | Result | Reason |
|---|---|--------|--------|
| `"a"` | `"b"` | True | trivial single-char mapping |
| `"ab"` | `"aa"` | False | two s-chars map to same t-char |
| `"aa"` | `"ab"` | False | one s-char maps to two t-chars |
| `"a"` | `"a"` | True | identity mapping |

---

## Complexity
- **Time:** O(n) — single pass through both strings
- **Space:** O(1) — maps bounded by alphabet size (constant)
