from typing import List
import heapq
from collections import defaultdict


class Solution:
    """
    ## 787. Cheapest Flights Within K Stops

    There are `n` cities connected by some number of flights. You are given an array `flights`
    where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city
    `from_i` to city `to_i` with cost `price_i`.

    Given three integers `src`, `dst`, and `k`, return the **cheapest price** from `src` to `dst`
    with at most `k` stops. If there is no such route, return `-1`.

    ---

    ### Examples

    ```text
    Input:  n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src=0, dst=3, k=1
    Output: 700
    Explanation: 0 -> 1 -> 3 costs 700.

    Input:  n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1
    Output: 200

    Input:  n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=0
    Output: 500
    ```

    ---

    ### Constraints

    - `1 <= n <= 100`
    - `0 <= flights.length <= n * (n - 1) / 2`
    - `flights[i].length == 3`
    - `0 <= from_i, to_i < n`
    - `from_i != to_i`
    - `1 <= price_i <= 10^4`
    - There will not be any multiple flights between two cities.
    - `0 <= k <= n`
    """

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford with k+1 relaxation rounds (k stops = k+1 edges)
        # Use a copy of prices each round to prevent using more than one edge per round
        # O(k*E) — Bellman-Ford limited to k+1 relaxation rounds
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices[:]
            for u, v, w in flights:
                if prices[u] + w < tmp[v]:
                    tmp[v] = prices[u] + w
            prices = tmp

        return prices[dst] if prices[dst] < float('inf') else -1

    def findCheapestPrice_dijkstra(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # O(V*E) — modified Dijkstra tracking stops; heap entry: (cost, node, stops_used)
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # dist[node][stops] = min cost
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        heap = [(0, src, 0)]  # (cost, node, stops)

        while heap:
            cost, u, stops = heapq.heappop(heap)
            if u == dst:
                return cost
            if stops > k:
                continue
            for v, w in graph[u]:
                new_cost = cost + w
                if new_cost < dist[v][stops + 1]:
                    dist[v][stops + 1] = new_cost
                    heapq.heappush(heap, (new_cost, v, stops + 1))

        return -1


if __name__ == '__main__':
    s = Solution()
    assert s.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1) == 700
    assert s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) == 200
    assert s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0) == 500

    assert s.findCheapestPrice_dijkstra(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1) == 700
    assert s.findCheapestPrice_dijkstra(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) == 200
    assert s.findCheapestPrice_dijkstra(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0) == 500

    print("All tests passed.")
