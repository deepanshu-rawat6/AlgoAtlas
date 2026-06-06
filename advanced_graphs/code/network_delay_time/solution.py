from typing import List
import heapq
from collections import defaultdict


class Solution:
    """
    ## 743. Network Delay Time

    You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`,
    a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source
    node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from
    source to target.

    We will send a signal from a given node `k`. Return the **minimum time** it takes for all
    the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive
    the signal, return `-1`.

    ---

    ### Examples

    ```text
    Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2

    Input:  times = [[1,2,1]], n = 2, k = 1
    Output: 1

    Input:  times = [[1,2,1]], n = 2, k = 2
    Output: -1
    ```

    ---

    ### Constraints

    - `1 <= k <= n <= 100`
    - `1 <= times.length <= 6000`
    - `times[i].length == 3`
    - `1 <= ui, vi <= n`
    - `ui != vi`
    - `0 <= wi <= 100`
    - All pairs `(ui, vi)` are unique.
    """

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra from source k; shortest path to each node = signal arrival time
        # Answer is max of all shortest paths; -1 if any node unreachable
        # O((V+E)logV) — Dijkstra's single-source shortest path
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))

        ans = max(dist.values())
        return ans if ans < float('inf') else -1

    def networkDelayTime_bellman_ford(self, times: List[List[int]], n: int, k: int) -> int:
        # O(V*E) — Bellman-Ford relaxing all edges V-1 times
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        ans = max(dist.values())
        return ans if ans < float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    assert s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert s.networkDelayTime([[1, 2, 1]], 2, 1) == 1
    assert s.networkDelayTime([[1, 2, 1]], 2, 2) == -1

    assert s.networkDelayTime_bellman_ford([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert s.networkDelayTime_bellman_ford([[1, 2, 1]], 2, 1) == 1
    assert s.networkDelayTime_bellman_ford([[1, 2, 1]], 2, 2) == -1

    print("All tests passed.")
