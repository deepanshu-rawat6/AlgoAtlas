"""
Minimum Spanning Tree (MST)
============================
A spanning tree of a connected undirected graph that connects all V nodes
with exactly V-1 edges and minimum total weight.

Two classic algorithms:

┌──────────────┬──────────────────┬──────────────────────────────────────────┐
│ Algorithm    │ Time             │ Best for                                 │
├──────────────┼──────────────────┼──────────────────────────────────────────┤
│ Prim's       │ O((V+E) log V)   │ Dense graphs (E close to V²)             │
│ Kruskal's    │ O(E log E)       │ Sparse graphs, edge list already sorted  │
└──────────────┴──────────────────┴──────────────────────────────────────────┘

Both produce the same MST weight (may differ in edge selection for equal weights).
"""

import heapq
from typing import Dict, List, Tuple

Edge = Tuple[int, int, int]                         # (weight, u, v)
Graph = Dict[int, List[Tuple[int, int]]]            # node → [(neighbor, weight)]


# ─── Prim's Algorithm (min-heap, greedy) ─────────────────────────────────────

def prim(graph: Graph, start: int = 0) -> Tuple[int, List[Edge]]:
    """Find MST using Prim's algorithm.
    
    Grows the MST one vertex at a time by always picking the cheapest edge
    that connects a new vertex to the current tree.
    
    Returns (total_weight, list of MST edges).
    """
    visited = set()
    heap = [(0, start, -1)]         # (weight, node, parent)
    total = 0
    mst_edges = []

    while heap and len(visited) < len(graph):
        w, u, parent = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        total += w
        if parent != -1:
            mst_edges.append((parent, u, w))
        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(heap, (weight, v, u))

    return total, mst_edges


# ─── Kruskal's Algorithm (sort edges + Union-Find) ───────────────────────────

def kruskal(n: int, edges: List[Edge]) -> Tuple[int, List[Edge]]:
    """Find MST using Kruskal's algorithm.
    
    Sorts all edges by weight, then greedily adds the cheapest edge that
    doesn't form a cycle (checked via Union-Find).
    
    Args:
        n: number of nodes (0 to n-1)
        edges: list of (weight, u, v)
    
    Returns (total_weight, list of MST edges).
    """
    # Union-Find (inline for self-containment)
    parent = list(range(n))
    rank   = [0] * n

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> bool:
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True

    edges_sorted = sorted(edges)    # sort by weight (first element of tuple)
    total = 0
    mst_edges = []

    for w, u, v in edges_sorted:
        if union(u, v):             # add edge only if it doesn't form a cycle
            total += w
            mst_edges.append((u, v, w))
            if len(mst_edges) == n - 1:
                break               # MST complete

    return total, mst_edges


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    #     2       3
    # 0 ─── 1 ─── 3
    # │     │
    # 6     8
    # │     │
    # 2 ─── 4
    #     5
    graph: Graph = {
        0: [(1, 2), (2, 6)],
        1: [(0, 2), (3, 3), (4, 8)],
        2: [(0, 6), (4, 5)],
        3: [(1, 3)],
        4: [(1, 8), (2, 5)],
    }
    edge_list: List[Edge] = [
        (2, 0, 1), (6, 0, 2), (3, 1, 3), (8, 1, 4), (5, 2, 4)
    ]

    prim_weight, prim_edges = prim(graph)
    print("Prim's MST  — weight:", prim_weight, "| edges:", prim_edges)

    kruskal_weight, kruskal_edges = kruskal(5, edge_list)
    print("Kruskal MST — weight:", kruskal_weight, "| edges:", kruskal_edges)
