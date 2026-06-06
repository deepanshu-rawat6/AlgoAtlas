# LC 1781 — Sum of Beauty of All Substrings

## Problem
The **beauty** of a string is `max_frequency - min_frequency` among all
characters that appear in it. Return the sum of beauty of all substrings of `s`.

**Example:**
- `s="aabcb"` → `5`
  - Substrings with non-zero beauty: "aab"(1), "aabc"(1), "aabcb"(2), "abcb"(1) = 5
- `s="aabcbaa"` → `17`

**Constraints:** `1 <= s.length <= 500`, lowercase English letters.

---

## Approach — Brute Force with Frequency Array  `O(n² × 26)` time · `O(26)` space

For every starting index `i`, maintain a frequency array of size 26 and
expand the right boundary `j` one character at a time:
1. Increment `freq[s[j]]`.
2. Compute beauty: filter out zero-frequency chars, then `max - min` in O(26).
3. Accumulate into total.

**Why not O(n³)?** By keeping a running frequency array as `j` expands, we
avoid recomputing frequencies from scratch for each substring. Each step is
O(26) instead of O(n), giving O(n² × 26) overall.

---

## Key Insight
Maintain a **running** frequency array as the right pointer expands. This
turns the inner beauty computation from O(n) to O(26) (constant), reducing
the naive O(n³) to O(n²).

---

## Edge Cases
| Input | Output | Reason |
|-------|--------|--------|
| `"a"` | `0` | Single char, max=min |
| `"aa"` | `0` | All same char |
| `"ab"` | `0` | Both freq=1, max=min |
| `"aab"` | `1` | "aab": max(a=2,b=1)-min=1 |

---

## Complexity
- **Time:** O(n² × 26) = O(n²) — n² substrings, O(26) beauty per substring
- **Space:** O(26) = O(1) — frequency array of fixed size
