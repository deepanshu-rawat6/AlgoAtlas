# Valid Anagram (LC 242)

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`.
An anagram uses the same characters in the same frequencies, just rearranged.

## Approaches

### 1. Sort — O(n log n) time, O(1) space
Sort both strings and compare. Anagrams produce identical sorted strings.

**Why it works:** Sorting is a canonical form — all anagrams of a word sort to the same string.

### 2. Character Count — O(n) time, O(1) space
Use a 26-element array. Increment for each char in `s`, decrement for each char in `t`. All zeros means balanced.

**Why it works:** Anagrams have identical character frequencies. Incrementing and decrementing simultaneously cancels out if and only if the strings are anagrams.

## Key Insight
Anagram ↔ identical character frequency profile. A single 26-element array captures this in O(1) space.

## Edge Cases
- Different lengths → immediately `false`
- Empty strings → both empty is `true`
- Single character strings
- Strings with all identical characters (e.g., `"aaa"` vs `"aaa"`)
