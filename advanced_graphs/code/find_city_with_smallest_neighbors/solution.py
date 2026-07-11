"""
# LC 1334: Find the City With the Smallest Number of Neighbors at a Threshold Distance

Find the city that has the fewest other cities reachable within
`distanceThreshold`. On a tie, return the city with the largest index.

## Examples
```text
Input: n=4, edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold=4
Output: 3
# City 3 reaches {1,2} (2 cities), the smallest count.
```

## Constraints
- Weighted undirected graph; use Floyd-Warshall all-pairs shortest paths — O(n^3)
- Tie-break toward the larger index (use <= when comparing counts)
- Unreachable pairs remain at infinity
"""
from typing import List

class Solution:
    # Floyd-Warshall: compute all-pairs shortest paths, then count reachable cities
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0  # distance to self is 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # relax all pairs through intermediate node k
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # find city with fewest reachable neighbors within threshold
        # tie-break: pick the city with larger index
        best_city, min_count = -1, INF
        for i in range(n):
            count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            if count <= min_count:  # <= ensures we pick larger index on tie
                min_count = count
                best_city = i

        return best_city


if __name__ == "__main__":
    sol = Solution()

    # Example from README
    assert sol.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4) == 3

    # LC classic example: threshold 2 → city 0 has fewest, tie broken by larger index
    assert sol.findTheCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2) == 0

    # Two isolated cities, threshold 0 → each reaches nobody, pick larger index
    assert sol.findTheCity(2, [], 0) == 1

    print("All tests passed.")
