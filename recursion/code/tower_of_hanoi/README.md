# Tower of Hanoi

## Problem Statement
Transfer `n` disks from `src` peg to `dest` peg using `aux` as helper.
Rules: move one disk at a time; never place a larger disk on a smaller one.
Return the list of moves as strings like `"A->C"`.

**Example:** n=2, src=A, dest=C, aux=B → ["A->B", "A->C", "B->C"]

---

## Approach: Recursion — O(2^n) time, O(n) stack space

Three steps:
1. Move n-1 disks from `src` to `aux` (using `dest` as helper).
2. Move the nth (largest) disk from `src` to `dest`.
3. Move n-1 disks from `aux` to `dest` (using `src` as helper).

**Why this works:** The largest disk can only move when all smaller disks are
out of the way (on `aux`). After placing it on `dest`, we reconstruct the
tower of n-1 disks on top of it.

**Why recursion is natural here:** The problem is self-similar — moving n disks
reduces to moving n-1 disks twice plus one direct move.

---

## Key Insight
The recurrence `T(n) = 2·T(n-1) + 1` solves to `T(n) = 2^n - 1`.
This is the **minimum** number of moves possible — no algorithm can do better.

---

## Edge Cases
- `n=1`: single move `src->dest`.
- Large n: 2^n - 1 moves grow exponentially; n=30 requires ~1 billion moves.

---

## Complexity Summary
| Metric | Value     |
|--------|-----------|
| Time   | O(2^n)    |
| Space  | O(n) stack|
| Moves  | 2^n - 1   |
