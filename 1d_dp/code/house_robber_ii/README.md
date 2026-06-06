# LC 213 — House Robber II

All houses are arranged in a **circle**, so the first and last houses are adjacent. You cannot rob two adjacent houses. Return the maximum amount you can rob.

## Approaches

### 1. Two Linear Passes (Exclude First or Last)
- **Time:** O(n) | **Space:** O(1)
- The circular constraint means you can't rob both house 0 and house n-1. Run the linear House Robber on `nums[0..n-2]` and `nums[1..n-1]` separately, then take the max of both results.

## Key Insight

Breaking the circle into two linear subproblems is the key reduction. By fixing that either the first or the last house is excluded, we guarantee the circular adjacency constraint is satisfied. The answer is the better of the two linear solutions. This reuses the O(n) linear robber as a subroutine.

## Edge Cases

- Single house: Return `nums[0]` directly (can't split into two ranges).
- Two houses: Return `max(nums[0], nums[1])`.
- Three houses: Can only rob one of the three.
- All equal values: The DP picks every other house optimally.
