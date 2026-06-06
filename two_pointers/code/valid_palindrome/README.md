# Valid Palindrome (LC 125)

A phrase is a palindrome if, after lowercasing and removing non-alphanumeric characters,
it reads the same forward and backward. Return `true` if `s` is a palindrome.

## Approaches

### 1. Filter + Reverse — O(n) time, O(n) space
Build a filtered lowercase list of alphanumeric characters, then compare it to its reverse.

**Why it works:** Reduces the problem to a simple equality check on the cleaned string.

### 2. Two Pointers — O(n) time, O(1) space
Left and right pointers move inward. Skip non-alphanumeric characters from both ends. Compare the characters; mismatch means not a palindrome.

**Why it works:** Checking from both ends simultaneously avoids building a new string. Skipping non-alphanumeric chars in-place achieves O(1) space.

## Key Insight
Two pointers from both ends: skip non-alphanumeric characters in-place rather than building a cleaned copy. Saves O(n) space.

## Edge Cases
- String with only spaces or punctuation → `true` (empty after filtering)
- Single alphanumeric character → `true`
- Mixed case (e.g., `"A"` vs `"a"`) → must lowercase before comparing
- Numbers in the string (alphanumeric includes digits)
