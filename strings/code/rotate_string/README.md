# LC 796 — Rotate String

## Problem
Given strings `s` and `goal`, return `True` if `s` can become `goal` after
some number of left-shift rotations (moving the first character to the end).

**Example:**
- `s="abcde"`, `goal="cdeab"` → `True` (rotate 2 times)
- `s="abcde"`, `goal="abced"` → `False`

**Constraints:** `1 <= s.length, goal.length <= 100`, lowercase English letters.

---

## Approach 1 — Try All Rotations  `O(n^2)` time · `O(n)` space

Generate each of the n rotations `s[i:] + s[:i]` and compare to `goal`.
Simple but quadratic due to string slicing inside the loop.

---

## Approach 2 — Substring Check on `s+s`  `O(n)` time · `O(n)` space

Concatenate `s` with itself. Every possible rotation of `s` appears as a
contiguous substring of `s+s` of length `n`. So just check `goal in s+s`
(Python's `in` uses an optimised algorithm, effectively O(n)).

```
s = "abcde"
s+s = "abcdeabcde"
         ^^^^^ "cdeab" found at index 2
```

Also guard: lengths must be equal (a rotation preserves length).

---

## Key Insight
`s+s` is a neat trick that encodes all n rotations without explicitly
generating them. The same idea appears in circular buffer problems.

---

## Edge Cases
| s | goal | Result | Reason |
|---|------|--------|--------|
| `""` | `""` | True | empty strings |
| `"a"` | `"a"` | True | no rotation needed |
| `"aa"` | `"a"` | False | different lengths |
| `"abc"` | `"abc"` | True | 0 rotations |
| `"abc"` | `"cab"` | True | rotate once |

---

## Complexity
- **Approach 1 — Time:** O(n²) · **Space:** O(n)
- **Approach 2 — Time:** O(n) · **Space:** O(n) for the concatenated string
