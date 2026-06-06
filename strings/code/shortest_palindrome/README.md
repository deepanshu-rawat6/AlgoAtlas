# Shortest Palindrome — LC 214

## Problem

Given string `s`, add characters to the **front** to make it a palindrome. Return the shortest such palindrome.

**Example:** `s="aacecaaa"` → `"aaacecaaa"`

## Approach 1: KMP on `s + '#' + reverse(s)`

**Why this works?** The longest palindromic prefix of `s` tells us the minimum characters to prepend. If `s[:k]` is a palindrome, we only need to prepend `reverse(s[k:])`.

**Finding the longest palindromic prefix:**
- Build `t = s + '#' + reverse(s)`
- Compute LPS array for `t`
- `lps[-1]` = length of longest palindromic prefix of `s`

**Why '#' separator?** Without it, the LPS could span across `s` and `reverse(s)`, giving a value larger than `len(s)`.

**Answer:** `reverse(s)[: len(s) - lps[-1]] + s`

**Complexity:** O(n) time and space

## Approach 2: Rolling Hash

Simultaneously compute forward hash (left→right) and backward hash (right→left). Largest `k` where both hashes match → `s[:k]` is a palindrome.

**Complexity:** O(n) time, O(1) extra space (probabilistic correctness)

## Key Insight

The problem reduces to: find the longest palindromic prefix. KMP's LPS on the concatenated string solves this in O(n).

## Edge Cases

- Empty string → return `""`
- Already a palindrome → return `s` unchanged
- Single character → return `s`
