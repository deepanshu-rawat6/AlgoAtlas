# LC 1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance

Find the city that has the fewest cities reachable within `distanceThreshold`. On tie, return the city with the largest index.

## Approach: Floyd-Warshall — O(n³)
Compute all-pairs shortest paths. For each city, count how many other cities are reachable within the threshold. Return the city with the minimum count (largest index on tie).

## Key Insight
Floyd-Warshall is ideal here because n ≤ 100 (n³ = 10⁶ is fast) and we need **all-pairs** shortest paths. The tie-breaking rule (largest index) is handled by using `<=` instead of `<` when updating the best city.

## Edge Cases
- No city reachable within threshold → count = 0 for all, return largest index city
- All cities reachable → pick city with fewest connections
- Disconnected graph → unreachable pairs stay at `inf`

## Example
```
n=4, edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]], threshold=4
City 0: reaches {1,2,3} → 3 cities
City 3: reaches {1,2} → 2 cities (smallest)
Output: 3
```
