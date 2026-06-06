# LC 784 — Letter Case Permutation

Given a string `s` with letters and digits, generate all strings by transforming each letter to lowercase or uppercase. Digits remain unchanged.

## Approaches

### 1. DFS / Backtracking
- **Time:** O(2ˡ × n) where l = number of letters | **Space:** O(2ˡ × n)
- At each index: if digit, move to next unchanged. If letter, branch into two recursive calls — one with lowercase, one with uppercase. When index reaches end, add the current string to results.

## Key Insight

Only letters create branching (2 choices each); digits are deterministic (1 choice). The total number of results is `2^(number of letters)`. The DFS naturally builds all combinations by exploring both case options at each letter position. Building the string character by character avoids the overhead of string mutation.

## Edge Cases

- All digits (e.g., `"123"`): Only one result — the original string.
- All letters (e.g., `"abc"`): `2³ = 8` results.
- Mixed (e.g., `"a1b2"`): `2² = 4` results.
- Empty string: Return `[""]`.
- Note: The solution stub in `solution.py` has `pass` — the approach is described above.
