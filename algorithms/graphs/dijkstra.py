"""
Dijkstra's Algorithm
====================
Strategy   : Greedy — always expand the unvisited node with smallest known distance.
             Uses a min-heap (priority queue).
Time       : O((V + E) log V)
Space      : O(V)

Constraints:
- Edge weights must be NON-NEGATIVE
- Fails with negative weights (use Bellman-Ford instead)

Use when:
- Single-source shortest path in weighted graph
- Network routing, GPS navigation
- Any "minimum cost to reach" problem with non-negative costs
"""

import heapq
from typing import Dict, List, Optional, Tuple


Graph = Dict[int, List[Tuple[int, int]]]   # node → [(neighbor, weight)]


def dijkstra(graph: Graph, start: int) -> Dict[int, float]:
    """Return shortest distances from start to all reachable nodes.
    
    graph[u] = [(v, weight), ...]
    Returns dist dict; unreachable nodes have dist = infinity.
    """
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]            # (distance, node)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:            # stale entry — skip
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist


def dijkstra_with_path(graph: Graph, start: int, end: int) -> Tuple[float, Optional[List[int]]]:
    """Return (shortest distance, path) from start to end.
    
    Returns (inf, None) if end is unreachable.
    """
    dist = {node: float('inf') for node in graph}
    prev: Dict[int, Optional[int]] = {node: None for node in graph}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        if u == end:
            break                  # early exit once target is settled
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

    if dist[end] == float('inf'):
        return float('inf'), None

    # Reconstruct path by following prev pointers
    path = []
    node: Optional[int] = end
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    return dist[end], path


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    #   0 --1-- 1 --2-- 3
    #   |       |
    #   4       1
    #   |       |
    #   2 --1-- 4
    graph: Graph = {
        0: [(1, 1), (2, 4)],
        1: [(0, 1), (3, 2), (4, 1)],
        2: [(0, 4), (4, 1)],
        3: [(1, 2)],
        4: [(1, 1), (2, 1)],
    }

    dist = dijkstra(graph, 0)
    print("Distances from 0:", dist)

    cost, path = dijkstra_with_path(graph, 0, 3)
    print(f"Shortest path 0→3: cost={cost}, path={path}")

    cost, path = dijkstra_with_path(graph, 0, 2)
    print(f"Shortest path 0→2: cost={cost}, path={path}")
