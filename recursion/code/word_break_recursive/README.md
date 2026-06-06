# Word Break (LC 139) — Recursive

## Problem Statement
Given string `s` and a list of words `wordDict`, return `True` if `s` can be
segmented into a space-separated sequence of dictionary words.

**Example:** s="leetcode", wordDict=["leet","code"] → True

---

## Approach: Recursion with Memoization — O(n²) time, O(n) space

For each starting index `start`, try every prefix `s[start:end]`.
If the prefix is in the dictionary, recursively check `s[end:]`.
Cache the result for each `start` index to avoid recomputation.

**Why memoization is essential:** Without it, the recursion is O(2^n) — the
same suffix can be reached via many different prefix splits, causing exponential
recomputation. Memoizing by `start` index ensures each suffix is solved once.

**Why try all prefixes:** We don't know which split is valid in advance, so we
must try all. The first valid split that leads to a full segmentation returns True.

---

## Key Insight
The problem has **overlapping subproblems**: `wordBreak(s, start)` may be
called multiple times with the same `start` from different parent calls.
Memoizing by `start` converts O(2^n) to O(n²) (n starting positions × n
prefix lengths each).

---

## Edge Cases
- Single word that matches exactly → True.
- String that can't be segmented at all → False (all paths exhausted).
- Repeated words in dict: using a set avoids duplicate lookups.
- Empty string `s=""` → True (base case: start == len(s)).

---

## Complexity Summary
| Metric | Value  |
|--------|--------|
| Time   | O(n²)  |
| Space  | O(n) memo + O(n) stack |
