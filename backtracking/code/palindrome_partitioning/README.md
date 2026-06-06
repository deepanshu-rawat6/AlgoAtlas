# Palindrome Partitioning (LC 131)

Given a string `s`, return all possible ways to partition it such that every substring
in the partition is a palindrome.

## Approaches

### 1. Backtracking with Palindrome Check
**Complexity:** O(n · 2ⁿ) time, O(n) space

At each position, try all prefixes. If a prefix is a palindrome, add it to the current
partition and recurse on the remaining suffix. Add the complete partition to results
when the entire string is consumed.

**Why it works:** Every partition corresponds to a unique way of splitting the string.
Checking palindromes at each step prunes invalid splits early. The recursion naturally
enumerates all valid partitions.

## Key Insight

The backtracking structure mirrors subset generation: at each position, we decide where
to "cut". The palindrome check is the constraint that filters valid cuts. For better
performance, precompute a palindrome DP table to make each check O(1) instead of O(n).

## Edge Cases

- Single character — always a palindrome; return `[["a"]]`.
- All same characters — every partition is valid (e.g., `"aaa"` → `[["a","a","a"],["a","aa"],["aa","a"],["aaa"]]`).
- No palindrome partition longer than 1 — return all single-character partitions.
- Empty string — return `[[]]`.
