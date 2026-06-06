# Josephus Problem

## Problem Statement
Given `n` people standing in a circle (0-indexed), every `k`th person is
eliminated until one remains. Return the 0-indexed position of the survivor.

**Example:** n=7, k=3 → 3

---

## Approach 1: Simulation — O(n·k) time, O(n) space
Maintain a list of people. Use a running index; advance `k-1` steps each round
and remove that person. Repeat until one remains.

**Why:** Intuitive and easy to verify correctness. Good for small n.

**Why not for large n:** Each `pop` on a list is O(n), and we do n rounds → O(n²) worst case.

---

## Approach 2: Recursive Formula — O(n) time, O(n) stack space

```
J(1, k) = 0
J(n, k) = (J(n-1, k) + k) % n
```

**Why this works:** After the first elimination, the circle shrinks to n-1
people. The winner's position in the n-1 circle maps back to the n-circle by
shifting k positions forward (mod n). This recurrence captures that shift.

**Why preferred:** Linear time, no list manipulation. Elegant mathematical reduction.

---

## Key Insight
The problem has **optimal substructure**: the answer for n people is derived
directly from the answer for n-1 people. The `+k % n` accounts for the index
shift caused by removing one person and renumbering.

---

## Edge Cases
- `n=1`: only one person, answer is always 0.
- `k=1`: everyone is eliminated in order; last person is at index n-1.
- `k > n`: modular arithmetic handles wrap-around naturally.

---

## Complexity Summary
| Approach    | Time   | Space  |
|-------------|--------|--------|
| Simulation  | O(n·k) | O(n)   |
| Recursive   | O(n)   | O(n)   |
