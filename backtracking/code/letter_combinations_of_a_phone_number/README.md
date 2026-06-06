# Letter Combinations of a Phone Number (LC 17)

Given a string of digits (2-9), return all possible letter combinations the digits could
represent, based on the standard phone keypad mapping.

## Approaches

### 1. Backtracking (DFS)
**Complexity:** O(4ⁿ · n) time, O(n) space (n = digits length)

For each digit, try all mapped letters. Recurse to the next digit. Add to results when
all digits are processed.

**Why it works:** Each digit independently maps to 3-4 letters. The total combinations
are the Cartesian product of all letter sets. DFS builds each combination character by
character.

### 2. Iterative BFS
**Complexity:** O(4ⁿ · n) time, O(4ⁿ) space

Start with `['']`. For each digit, expand every existing partial combination by
appending each mapped letter. The queue grows level by level.

**Why it works:** BFS builds combinations level by level (one digit at a time). Each
level multiplies the number of combinations by the number of letters for that digit.

## Key Insight

This is a Cartesian product problem. Both DFS and BFS enumerate all combinations; DFS
uses less memory (O(n) stack vs O(4ⁿ) queue). The phone mapping is a fixed lookup table.

## Edge Cases

- Empty input — return `[]`.
- Single digit — return its mapped letters.
- Digit `'1'` — not on the keypad (problem guarantees digits 2-9).
- `'7'` and `'9'` map to 4 letters each; others map to 3.
