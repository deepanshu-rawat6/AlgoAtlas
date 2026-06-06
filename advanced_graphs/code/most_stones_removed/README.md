# LC 947 - Most Stones Removed with Same Row or Column

Remove the maximum number of stones where a stone can be removed if it shares a row or column with another stone. Return max removable count.

## Approach: Union-Find — O(n)
Group stones that share a row or column into the same component. From each component of size `k`, you can remove `k-1` stones (always keep one). Answer = `total_stones - num_components`.

## Key Insight
Union rows and columns together using a shared namespace (offset columns by 10001 to avoid collision). Two stones in the same row or column end up in the same component transitively. Each component can be reduced to exactly 1 stone.

## Edge Cases
- Single stone → can't remove any → answer is 0
- All stones in same row → one component → remove all but 1
- No two stones share row or column → each is its own component → answer is 0

## Example
```
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
All 6 stones form one connected component (via shared rows/cols)
Can remove 6-1 = 5 stones
Output: 5
```
