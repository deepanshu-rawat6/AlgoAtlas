# Group Anagrams (LC 49)

Given an array of strings `strs`, group all anagrams together and return the groups
in any order.

## Approaches

### 1. Sort Key — O(n · k log k) time, O(n · k) space
Sort each string to get a canonical key. Group strings by their sorted form.

**Why it works:** All anagrams of a word produce the same sorted string, making it a perfect grouping key.

### 2. Frequency Tuple Key — O(n · k) time, O(n · k) space
Build a 26-element character count array per word and use it as the dict key (as a tuple).

**Why it works:** Anagrams share identical character frequencies. The count tuple is a canonical key without the O(k log k) sorting cost.

## Key Insight
Canonical key = the thing all anagrams have in common. Sorted string works; character-count tuple is faster.

## Edge Cases
- Empty string `""` — groups with other empty strings
- Single-character strings
- All strings are anagrams of each other → one group
- No two strings are anagrams → each string in its own group
