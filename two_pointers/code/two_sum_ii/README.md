# Two Sum II - Input Array Is Sorted (LC 167)

Given a 1-indexed sorted array `numbers`, find two numbers that add up to `target`.
Return their 1-based indices. Must use O(1) extra space.

## Approaches

### 1. Brute Force — O(n²) time, O(1) space
Check all pairs. Ignores the sorted property.

**Why it works:** Correct but doesn't exploit the sorted order.

### 2. Binary Search — O(n log n) time, O(1) space
For each element, binary search for its complement in the remaining array.

**Why it works:** Sorted array enables O(log n) complement lookup instead of O(n) scan.

### 3. Two Pointers — O(n) time, O(1) space
Left pointer at start, right at end. If sum < target, move left right. If sum > target, move right left. Stop when sum == target.

**Why it works:** The sorted order guarantees that moving left right increases the sum and moving right left decreases it. The two pointers converge to the unique solution.

## Key Insight
Sorted array + two pointers: the sum is monotonically controllable. Move the pointer that will bring the sum closer to target.

## Edge Cases
- Two-element array → only one possible pair
- Negative numbers (handled naturally)
- Target is negative
- Exactly one solution guaranteed — no need to handle zero solutions
