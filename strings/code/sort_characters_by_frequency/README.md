# LC 451 — Sort Characters By Frequency

## Problem
Given a string `s`, sort it so that characters with higher frequency come first.
If two characters have the same frequency, their relative order doesn't matter.

**Example:**
- `s="tree"` → `"eert"` or `"eetr"` (e appears twice)
- `s="cccaaa"` → `"cccaaa"` or `"aaaccc"`
- `s="Aabb"` → `"bbAa"` or `"bbaA"` (case-sensitive)

**Constraints:** `1 <= s.length <= 5*10^5`, ASCII characters.

---

## Approach 1 — Counter + Sort  `O(n log n)` time · `O(n)` space

1. Count character frequencies with `Counter`.
2. Use `most_common()` which returns chars sorted by frequency descending.
3. Repeat each character by its count and join.

Straightforward and readable. The bottleneck is the sort step O(k log k)
where k ≤ n is the number of distinct characters.

---

## Approach 2 — Bucket Sort  `O(n)` time · `O(n)` space

Since frequency is bounded by `len(s)`, create an array of `n+1` buckets
where `buckets[f]` holds all characters that appear exactly `f` times
(already repeated). Iterate buckets in reverse order to get descending
frequency output.

**Why O(n)?** No comparison sort; indexing into buckets is O(1) per character.

---

## Key Insight
Bucket sort eliminates the log factor by exploiting the bounded frequency
range [1, n]. This is the same idea as counting sort.

---

## Edge Cases
| Input | Note |
|-------|------|
| Single char `"a"` | Returns `"a"` |
| All same `"aaaa"` | Returns `"aaaa"` |
| All distinct `"abcd"` | Any permutation valid |
| Mixed case `"Aa"` | `'A'` and `'a'` are distinct |

---

## Complexity
- **Approach 1 — Time:** O(n log n) · **Space:** O(n)
- **Approach 2 — Time:** O(n) · **Space:** O(n)
