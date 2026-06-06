# Count Substrings with Exactly K Distinct Characters

## Problem
Given a string `s` and integer `k`, count the number of substrings that
contain **exactly** `k` distinct characters.

**Example:**
- `s="aba"`, `k=2` → `3`  ("ab", "ba", "aba")
- `s="aaa"`, `k=1` → `6`  (all 6 substrings)
- `s="abc"`, `k=2` → `2`  ("ab", "bc")

**Constraints:** `1 <= s.length <= 10^4`, `1 <= k <= 26`.

---

## Approach — Sliding Window with atMost Trick  `O(n)` time · `O(k)` space

Directly counting "exactly k distinct" with a sliding window is hard because
the window can't simply expand/shrink to maintain exactly k. Instead, use:

```
exactly(k) = atMost(k) - atMost(k - 1)
```

`atMost(k)` counts substrings with **at most** k distinct characters, which
is easy with a sliding window:
- Expand right, add character to frequency map.
- If distinct count exceeds k, shrink from left until it's ≤ k.
- At each right position, `right - left + 1` valid substrings end here.

Subtracting `atMost(k-1)` removes substrings with fewer than k distinct chars,
leaving exactly k.

---

## Key Insight
`exactly(k) = atMost(k) - atMost(k-1)` is a universal trick for sliding
window problems where "exactly" is hard but "at most" is easy. The same
pattern appears in LC 992 (subarrays with k different integers).

---

## Edge Cases
| s | k | Output | Reason |
|---|---|--------|--------|
| `"a"` | `1` | `1` | Single char |
| `"ab"` | `3` | `0` | k > distinct chars |
| `"aaa"` | `1` | `6` | All substrings valid |
| `"abc"` | `1` | `3` | Only single chars |

---

## Complexity
- **Time:** O(n) — two linear passes (atMost called twice)
- **Space:** O(k) — frequency map holds at most k+1 entries
