# Check Palindrome (Recursive)

## Problem Statement
Given a string `s`, return `True` if it reads the same forwards and backwards,
`False` otherwise. Use recursion — no loops, no reversal.

**Example:** "racecar" → True, "abc" → False

---

## Approach: Compare Outer Characters, Recurse on Middle — O(n) time, O(n) space

```
isPalindrome("") = True
isPalindrome(s) of length 1 = True
isPalindrome(s) = s[0] == s[-1] and isPalindrome(s[1:-1])
```

**Why this works:** A string is a palindrome if and only if its first and last
characters match AND the inner substring is also a palindrome. We peel one
character from each end per call until the base case is reached.

**Why recursion is natural:** The problem has a clean self-similar structure —
checking a string of length n reduces to checking a string of length n-2.

**Space note:** Each recursive call creates a new string slice `s[1:-1]` in
Python, so space is O(n²) total for all slices, though stack depth is O(n).
An index-based approach avoids this.

---

## Key Insight
Base case `len(s) <= 1` handles both the empty string (trivially palindrome)
and single characters (always palindrome). The recursive case only needs to
check the outermost pair — the rest is delegated.

---

## Edge Cases
- Empty string `""` → True.
- Single character → True.
- Even-length palindrome `"abba"` → True (base case hits `""` at the end).
- All same characters `"aaaa"` → True.

---

## Complexity Summary
| Metric | Value  |
|--------|--------|
| Time   | O(n)   |
| Space  | O(n) stack + O(n²) slices |
