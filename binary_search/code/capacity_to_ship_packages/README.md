# Capacity To Ship Packages Within D Days (LC 1011)

Find the minimum ship capacity to ship all packages within `days` days, loading in order.

## Approaches

### 1. Linear Search
- **Time:** O(sum(weights) × n) | **Space:** O(1)
- Start at `max(weights)` and increment until the capacity is feasible.

### 2. Binary Search on Answer
- **Time:** O(n × log(sum(weights))) | **Space:** O(1)
- Search space: `[max(weights), sum(weights)]`.
  - Lower bound: must fit the heaviest package.
  - Upper bound: ship everything in one day.
- For each candidate capacity `mid`, simulate loading to count days needed.
- If `days_needed <= days`, try smaller (`hi = mid`); else try larger (`lo = mid + 1`).

## Key Insight

The feasibility function is monotone: if capacity `c` works, any capacity `> c` also works. This makes binary search on the answer valid. The simulation (`_days_needed`) greedily loads as much as possible each day — if adding the next package exceeds capacity, start a new day.

## Edge Cases

- `days == len(weights)`: minimum capacity is `max(weights)` (one package per day).
- `days == 1`: minimum capacity is `sum(weights)` (all in one day).
- Single package: capacity = that package's weight.
- All packages same weight: capacity = weight, days = ceil(n / days).
