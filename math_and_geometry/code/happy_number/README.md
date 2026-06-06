# LC 202 — Happy Number

A happy number repeatedly replaces itself with the sum of squares of its digits until it reaches 1 (happy) or loops forever (not happy). Return `true` if `n` is happy.

## Approaches

### 1. Hash Set (Cycle Detection)
- **Time:** O(log n) per step | **Space:** O(log n)
- Apply the digit-square-sum transformation repeatedly. If we reach 1, return `True`. If we revisit a number (detected via a set), return `False`.

### 2. Floyd's Cycle Detection
- **Time:** O(log n) per step | **Space:** O(1)
- Use slow/fast pointers on the sequence. If `fast == 1`, it's happy. If `slow == fast` (cycle detected without reaching 1), it's not happy.

## Key Insight

Unhappy numbers always enter a cycle that includes 4 (a known fact). The sequence is bounded — for any n, the sum of digit squares is much smaller than n for large n, so the sequence eventually enters a small cycle. Floyd's algorithm detects this cycle in O(1) space by running two "pointers" at different speeds through the sequence.

## Edge Cases

- `n = 1`: Already happy, return `True`.
- `n = 4`: Enters the unhappy cycle immediately.
- Large `n`: The sequence quickly shrinks to a small number (< 1000) within a few steps.
