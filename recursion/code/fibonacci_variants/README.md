# Fibonacci Variants

## Problem Statement
1. Compute the nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1).
2. Count the number of ways to climb n stairs taking 1 or 2 steps at a time.

**Example:** fib(10) → 55, climbStairs(5) → 8

---

## Approach 1: Naive Recursion — O(2^n) time, O(n) space
`fib(n) = fib(n-1) + fib(n-2)` with base cases fib(0)=0, fib(1)=1.

**Why it's slow:** The same subproblems are recomputed exponentially many times.
`fib(5)` calls `fib(3)` twice; `fib(3)` calls `fib(1)` multiple times, etc.

---

## Approach 2: Memoized Recursion — O(n) time, O(n) space
Cache each result in a dict. Before computing, check if already solved.

**Why preferred over naive:** Converts exponential to linear by ensuring each
subproblem is solved exactly once. Retains the recursive structure for clarity.

---

## Approach 3: Iterative — O(n) time, O(1) space
Use two variables `a, b` and slide forward: `a, b = b, a + b`.

**Why preferred in production:** No recursion overhead, no stack risk for large
n, minimal memory. Trades elegance for efficiency.

---

## Key Insight
Fibonacci has **overlapping subproblems** — the defining property that makes
memoization (and DP) applicable. The climb-stairs problem has the identical
recurrence: `ways(n) = ways(n-1) + ways(n-2)` because the last step is either
1 or 2 stairs.

---

## Edge Cases
- n=0 → 0, n=1 → 1 (base cases).
- climbStairs(1) → 1, climbStairs(2) → 2.
- Large n: naive recursion will hit Python's recursion limit; use memoized or iterative.

---

## Complexity Summary
| Approach   | Time   | Space  |
|------------|--------|--------|
| Naive      | O(2^n) | O(n)   |
| Memoized   | O(n)   | O(n)   |
| Iterative  | O(n)   | O(1)   |
