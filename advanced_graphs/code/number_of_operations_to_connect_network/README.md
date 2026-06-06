# LC 1319 - Number of Operations to Make Network Connected

Find the minimum number of cable moves to connect all `n` computers. A cable can be taken from any redundant connection (where both endpoints are already connected).

## Approach: Union-Find — O(n + e)
1. If `len(connections) < n-1` → impossible, return `-1`
2. Union-Find all connections, count components
3. Answer = `components - 1` (need that many cables to bridge them)

## Key Insight
To connect `k` components into 1, you need exactly `k-1` cables. You can always find enough redundant cables as long as `total_edges >= n-1` (pigeonhole: with n-1+ edges among n nodes, at least one component has a cycle → redundant edge available).

## Edge Cases
- `connections < n-1` → return `-1` (not enough cables even if optimally placed)
- Already connected → return `0`
- n=1 → return `0` (single computer)

## Example
```
n=4, connections=[[0,1],[0,2],[1,2]]
Edge (1,2) is redundant (0,1,2 already connected)
Components: {0,1,2} and {3} → need 1 move
Output: 1
```
