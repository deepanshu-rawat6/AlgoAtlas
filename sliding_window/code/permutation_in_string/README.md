# Permutation in String (LC 567)

Given strings `s1` and `s2`, return `true` if any permutation of `s1` is a substring of `s2`.

## Approaches

### 1. Brute Force — O(n · m log m) time, O(m) space
Sort each window of length `len(s1)` in `s2` and compare to sorted `s1`.

**Why it works:** Sorted strings are a canonical form for permutations. Slow due to sorting each window.

### 2. Fixed Sliding Window with Frequency Arrays — O(n) time, O(1) space
Build frequency arrays for `s1` and the first window of `s2`. Slide the window: add the new right character, remove the character that fell out. If frequency arrays match, a permutation is found.

**Why it works:** A permutation has the same character frequencies. A fixed-size window of `len(s1)` that matches `s1`'s frequencies is exactly a permutation. Sliding updates in O(1) per step.

## Key Insight
Fixed window size = `len(s1)`. Maintain frequency arrays and slide — no need to re-sort or re-count the entire window each step.

## Edge Cases
- `len(s1) > len(s2)` → impossible, return `false`
- `s1` is a single character → check if that character exists in `s2`
- `s1 == s2` → `true`
- Repeated characters in `s1`
