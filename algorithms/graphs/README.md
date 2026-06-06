# Graph Algorithms

## When to Use Which Algorithm

| Problem                                      | Algorithm              | Time           |
|----------------------------------------------|------------------------|----------------|
| Shortest path, unweighted graph              | BFS                    | O(V + E)       |
| Connected components, flood fill             | BFS or DFS             | O(V + E)       |
| Cycle detection                              | DFS                    | O(V + E)       |
| Topological ordering (DAG)                   | Kahn's or DFS post-order | O(V + E)     |
| Shortest path, weighted, non-negative        | Dijkstra               | O((V+E) log V) |
| Shortest path, negative weights              | Bellman-Ford           | O(VE)          |
| Shortest path with at most K edges           | Bellman-Ford (K-stops) | O(KE)          |
| Shortest path, all pairs                     | Floyd-Warshall         | O(V³)          |
| Minimum spanning tree                        | Prim's or Kruskal's    | O(E log V)     |
| Dynamic connectivity / union queries         | Union-Find (DSU)       | O(α(n)) ≈ O(1) |

## Graph Representations

```
Adjacency List  — best for sparse graphs (E << V²), most common in interviews
Adjacency Matrix — best for dense graphs, O(1) edge lookup
Edge List       — used in Kruskal's, Bellman-Ford
```

## Key Concepts

- **Directed vs Undirected**: cycle detection differs; topological sort only for DAGs
- **Weighted vs Unweighted**: BFS for unweighted, Dijkstra/Bellman-Ford for weighted
- **Connected vs Disconnected**: always iterate over all nodes as starting points
- **Negative weights**: Dijkstra fails; use Bellman-Ford
- **Negative cycles**: Bellman-Ford detects them; Dijkstra cannot handle them

## Files

- `bfs.py` — BFS on graph/grid, shortest path, multi-source BFS
- `dfs.py` — DFS recursive/iterative, cycle detection, connected components
- `dijkstra.py` — shortest path with non-negative weights, path reconstruction
- `bellman_ford.py` — negative weights, negative cycle detection, K-stops variant
- `topological_sort.py` — Kahn's (BFS) and DFS post-order
- `union_find.py` — DSU with path compression + union by rank
- `mst.py` — Prim's and Kruskal's minimum spanning tree
