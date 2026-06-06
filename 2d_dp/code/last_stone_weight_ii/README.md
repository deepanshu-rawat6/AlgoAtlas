# LC 1049 — Last Stone Weight II

You can smash any two stones together; if weights differ, the difference remains. Return the minimum possible weight of the last remaining stone (0 if all destroyed).

## Approaches

### 1. Subset Sum / Partition DP
- **Time:** O(n × sum) | **Space:** O(sum)
- Assign each stone a `+` or `-` sign. Minimize `|S1 - S2|` where `S1 + S2 = total`. This equals `total - 2 * best` where `best` is the largest subset sum ≤ `total / 2`. Use a set of reachable sums.

## Key Insight

Smashing stones is equivalent to assigning `+` or `-` to each stone and computing the absolute difference. Minimizing `|S1 - S2|` with `S1 + S2 = total` means maximizing `S1` subject to `S1 ≤ total / 2`. This reduces to the same subset-sum problem as Partition Equal Subset Sum (LC 416), but instead of checking equality, we find the closest achievable sum to `total / 2`.

## Edge Cases

- Single stone: Return its weight (can't smash anything).
- Two equal stones: Return 0.
- All stones equal: If even count, return 0; if odd, return one stone's weight.
- `total` is odd: The minimum difference is at least 1.
