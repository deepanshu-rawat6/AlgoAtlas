# Generate All Balanced Parentheses (LC 22)

## Problem Statement
Given `n` pairs of parentheses, generate all combinations of well-formed
(balanced) parentheses strings.

**Example:** n=3 → ["((()))", "(()())", "(())()", "()(())", "()()()"] (5 strings)

---

## Approach: Recursion with Open/Close Counters — O(4^n / √n) time

Track how many `(` and `)` have been placed so far.
- Add `(` if `open_count < n` — still have opening brackets available.
- Add `)` if `close_count < open_count` — can only close what's been opened.
- Base case: string length == 2n → record it.

**Why this works:** The two constraints enforce validity at every step:
- Never more `(` than n ensures we don't exceed the budget.
- Never more `)` than `(` ensures the string is always valid as we build it.

**Why not backtracking with validity check at the end:** Pruning invalid states
early (via the two counters) avoids generating and discarding invalid strings.
Every leaf in the recursion tree is a valid result.

---

## Key Insight
The number of valid combinations equals the nth Catalan number: C(n) = C(2n,n)/(n+1).
For n=3, C(3)=5; for n=4, C(4)=14. The recursive structure naturally enumerates
exactly these combinations without duplicates.

---

## Edge Cases
- n=1 → ["()"] (only one valid string).
- n=0 → [""] (empty string, one valid combination).

---

## Complexity Summary
| Metric | Value          |
|--------|----------------|
| Time   | O(4^n / √n)    |
| Space  | O(n) stack     |
| Count  | nth Catalan number |
