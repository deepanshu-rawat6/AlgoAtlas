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
