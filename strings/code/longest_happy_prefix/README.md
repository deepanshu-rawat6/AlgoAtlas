# Longest Happy Prefix — LC 1392

## Problem

A "happy prefix" is a non-empty prefix that is also a suffix (but not the whole string). Return the longest happy prefix, or `""` if none exists.

**Examples:**
- `"level"` → `"l"`
- `"ababab"` → `"abab"`
- `"leetcodeleet"` → `"leet"`

## Approach 1: KMP LPS Array

**Why KMP?** The LPS (Longest Proper Prefix = Suffix) array is exactly what we need. `LPS[n-1]` gives the length of the longest proper prefix of `s` that is also a suffix.

**Steps:**
1. Compute LPS array for `s` (standard KMP preprocessing)
2. Return `s[:lps[-1]]`

**Complexity:** O(n) time and space

## Approach 2: Rolling Hash

Build prefix hash left→right and suffix hash right→left simultaneously. Track the largest `k` (excluding full string) where they match.

**Complexity:** O(n) time, O(1) extra space (probabilistic)

## Key Insight

This is a direct application of KMP's LPS array — no search phase needed. The LPS value at the last index is the answer length.

## Edge Cases

- Single character → no proper prefix → return `""`
- No prefix = suffix → return `""`
- Entire string is a repeated unit (e.g., `"aaaa"`) → LPS[-1] = n-1, return `s[:-1]`
