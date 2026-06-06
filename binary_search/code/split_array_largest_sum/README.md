# Split Array Largest Sum (LC 410)

Split `nums` into `k` non-empty subarrays to minimize the largest subarray sum.

## Approaches

### 1. Dynamic Programming
- **Time:** O(n² × k) | **Space:** O(n × k)
- `dp[i][j]` = minimum possible largest sum when splitting the first `i` elements into `j` parts.
- For each split point `m`: `dp[i][j] = min(dp[i][j], max(dp[m][j-1], prefix[i] - prefix[m]))`.

### 2. Binary Search on Answer
- **Time:** O(n × log(sum(nums))) | **Space:** O(1)
- Search space: `[max(nums), sum(nums)]`.
- For each candidate max-sum `mid`, greedily check if we can split into ≤ k parts where no part exceeds `mid`.
- If feasible, try smaller (`hi = mid`); else try larger (`lo = mid + 1`).

## Key Insight

This is the same pattern as LC 1011 (Capacity to Ship Packages). The feasibility function is monotone: if we can split with max-sum `c`, we can also split with any larger cap. Binary search on the answer avoids the O(n²k) DP. The greedy check works because we always want to pack as much as possible into each subarray before starting a new one.

## Edge Cases

- `k == 1`: answer is `sum(nums)` (one subarray, no split).
- `k == len(nums)`: answer is `max(nums)` (each element its own subarray).
- Single element: answer is that element.
- All zeros: answer is 0.
