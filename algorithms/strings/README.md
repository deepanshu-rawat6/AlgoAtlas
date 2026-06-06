# String Algorithms

## Files

| File | Contents |
|------|----------|
| [`kmp.py`](kmp.py) | KMP pattern matching O(n+m), failure/prefix function, O(n+m) proof |
| [`rabin_karp.py`](rabin_karp.py) | Rolling hash O(n+m) avg, multiple pattern search, longest common substring |
| [`manacher.py`](manacher.py) | Longest palindromic substring O(n), transform trick, count palindromes |

---

## Complexity Comparison

| Algorithm | Time (avg) | Time (worst) | Space | Use Case |
|-----------|-----------|--------------|-------|----------|
| Naive search | O(nm) | O(nm) | O(1) | Short patterns, simple code |
| KMP | O(n+m) | O(n+m) | O(m) | Single pattern, guaranteed linear |
| Rabin-Karp | O(n+m) | O(nm) | O(1) | Multiple patterns, plagiarism detection |
| Manacher | O(n) | O(n) | O(n) | Palindrome problems only |

`n` = text length, `m` = pattern length

---

## When to Use What

**KMP**
- Single pattern search with guaranteed O(n+m) — no worst-case degradation
- When you need all occurrences (overlapping included)
- DNA/protein sequence matching, text editors, network packet inspection
- The failure function itself is useful: detect repeated patterns, string periods

**Rabin-Karp**
- Multiple pattern search simultaneously (hash all patterns, single pass over text)
- Plagiarism detection (many short patterns)
- 2D pattern matching (hash rows then columns)
- Longest common substring via binary search + hashing

**Manacher**
- Any problem involving palindromic substrings
- Longest palindromic substring (LeetCode 5)
- Count palindromic substrings (LeetCode 647)
- Palindrome partitioning preprocessing

---

## Key Insight: Why KMP is O(n+m)

The failure function `lps[i]` stores the length of the longest proper prefix
of `pattern[0..i]` that is also a suffix. When a mismatch occurs at position
`j` in the pattern, instead of restarting from 0, we jump to `lps[j-1]`.

The text pointer `i` never moves backward → at most `n` steps.
The pattern pointer `j` can decrease, but total decreases ≤ total increases ≤ n.
Combined with O(m) to build lps: **O(n+m) total**.

## Key Insight: Manacher's Transform

Inserting `#` between characters unifies odd and even palindromes:
```
"abba"  →  "^#a#b#b#a#$"
             0 1 2 3 4 5 6 7 8 9 10
```
The palindrome "abba" (even length 4) becomes "#a#b#b#a#" (odd length 9)
centered at index 5 (the middle `#`). Now a single algorithm handles both cases.

Sentinel characters `^` and `$` (not in alphabet) eliminate boundary checks.
