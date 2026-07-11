"""
# LC 1976: Number of Ways to Arrive at Destination

Count the number of shortest paths from node `0` to node `n-1` in a weighted
undirected graph. Return the count modulo 10^9 + 7.

## Examples
```text
Input: n=7, roads=[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],
                    [3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
# Four distinct paths achieve the minimum travel time.
```

## Constraints
- Dijkstra + path count — O((V+E) log V)
- Shorter path found → ways[v] = ways[u]; equal path → ways[v] += ways[u]
- Apply the modulo at every addition
"""
from typing import List
import heapq

class Solution:
    # Dijkstra + count: when we find a shorter path, reset count; equal path, add count
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1  # one way to reach source

        heap = [(0, 0)]  # (distance, node)
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue  # stale entry
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    ways[v] = ways[u]  # new shortest path found, inherit count
                    heapq.heappush(heap, (dist[v], v))
                elif dist[u] + w == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD  # another equally short path

        return ways[n - 1]


if __name__ == "__main__":
    sol = Solution()

    # LC classic example: 4 shortest paths from 0 to 6
    assert sol.countPaths(7, [
        [0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
        [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2],
    ]) == 4

    # Single edge → exactly one shortest path
    assert sol.countPaths(2, [[0, 1, 1]]) == 1

    # Two equal-length parallel routes 0->1->3 and 0->2->3
    assert sol.countPaths(4, [[0, 1, 1], [1, 3, 1], [0, 2, 1], [2, 3, 1]]) == 2

    print("All tests passed.")
