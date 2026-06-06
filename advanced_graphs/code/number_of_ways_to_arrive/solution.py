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
