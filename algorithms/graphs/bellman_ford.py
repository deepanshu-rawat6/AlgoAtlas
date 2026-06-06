"""
Bellman-Ford Algorithm
======================
Strategy   : Relax ALL edges V-1 times. A Vth relaxation indicates a negative cycle.
Time       : O(V * E)
Space      : O(V)

Use when:
- Graph has NEGATIVE edge weights
- Need to detect negative cycles
- Shortest path with at most K edges (K-stops variant)

vs Dijkstra:
- Bellman-Ford handles negative weights; Dijkstra does not
- Dijkstra is faster: O((V+E) log V) vs O(VE)
- Use Dijkstra when all weights >= 0
"""

from typing import Dict, List, Optional, Tuple

Edge = Tuple[int, int, int]   # (u, v, weight)


def bellman_ford(n: int, edges: List[Edge], start: int) -> Tuple[Dict[int, float], bool]:
    """Shortest distances from start using Bellman-Ford.
    
    Args:
        n: number of nodes (0 to n-1)
        edges: list of (u, v, weight) directed edges
        start: source node
    
    Returns:
        (dist dict, has_negative_cycle)
        dist[v] = shortest distance from start to v (inf if unreachable)
    """
    dist = [float('inf')] * n
    dist[start] = 0

    # Relax all edges V-1 times
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break               # early termination if no updates

    # Vth relaxation: if any edge still relaxes, there's a negative cycle
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    return {i: dist[i] for i in range(n)}, has_negative_cycle


# ─── K-stops variant (LeetCode 787: Cheapest Flights Within K Stops) ─────────

def cheapest_flights_k_stops(
    n: int,
    flights: List[Tuple[int, int, int]],
    src: int,
    dst: int,
    k: int
) -> int:
    """Find cheapest price from src to dst with at most k stops (k+1 edges).
    
    Key: use a COPY of dist from previous iteration to avoid using edges
    added in the same round (ensures at-most-k-edges constraint).
    """
    dist = [float('inf')] * n
    dist[src] = 0

    for _ in range(k + 1):          # at most k+1 edges = k stops
        temp = dist[:]              # snapshot: only use distances from prev round
        for u, v, w in flights:
            if dist[u] != float('inf') and dist[u] + w < temp[v]:
                temp[v] = dist[u] + w
        dist = temp

    return dist[dst] if dist[dst] != float('inf') else -1


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    # Graph with negative edge (no negative cycle)
    #  0 --4--> 1 --(-1)--> 2
    #  |                    ^
    #  +--------2-----------+
    edges = [(0, 1, 4), (0, 2, 2), (1, 2, -1)]
    dist, neg_cycle = bellman_ford(3, edges, 0)
    print("Distances from 0:", dist)
    print("Negative cycle  :", neg_cycle)   # False

    # Graph with negative cycle
    neg_edges = [(0, 1, 1), (1, 2, -3), (2, 0, 1)]
    _, neg_cycle = bellman_ford(3, neg_edges, 0)
    print("Negative cycle  :", neg_cycle)   # True

    # K-stops: LeetCode 787
    flights = [(0,1,100),(1,2,100),(0,2,500)]
    print("\nCheapest 0→2 with 1 stop:", cheapest_flights_k_stops(3, flights, 0, 2, 1))  # 200
    print("Cheapest 0→2 with 0 stops:", cheapest_flights_k_stops(3, flights, 0, 2, 0))  # 500
