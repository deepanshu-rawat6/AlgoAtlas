# Advanced Graphs — Pattern Notes

## Core Intuition

Advanced graph problems go beyond plain BFS/DFS. The key is recognizing **which algorithm fits the constraint**:

- Need shortest path with weights → Dijkstra (non-negative) or Bellman-Ford (negative edges / K-hops)
- Need minimum spanning tree → Prim's (dense) or Kruskal's (sparse, union-find)
- Need to traverse every edge exactly once → Euler path (Hierholzer's)
- Need topological order from implicit constraints → build graph from rules, then topo sort
- Need connectivity / cycle detection in undirected graph → Union-Find
- Need all-pairs shortest paths → Floyd-Warshall (O(V³), ok for small V)
- Need strongly connected components → Kosaraju's or Tarjan's

### Dijkstra
Single-source shortest path with **non-negative** edge weights. Greedy: always relax the cheapest unvisited node next. Uses a min-heap so each node is finalized once. Fails with negative edges (a later cheaper path can invalidate an already-finalized node).

### Bellman-Ford
Relax **all edges V−1 times**. Correct with negative edges. An extra (V-th) relaxation pass that still changes any distance means a **negative cycle** is reachable. Also useful when you need exactly K-hop shortest paths — copy the dist array before each round to prevent chaining.

### Floyd-Warshall
All-pairs shortest path in O(V³). For each intermediate node k, update `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`. Works with negative edges as long as there are no negative cycles. Practical only for small V (≤ ~300).

### Union-Find (Disjoint Set Union)
Answers connectivity queries in near-O(1) with path compression + union by rank. Core operations: `find(x)` returns the representative of x's component; `union(x, y)` merges two components (returns false if already same). Powers Kruskal's MST and cycle detection in undirected graphs.

### Topological Sort
Valid only on a DAG. Two approaches: Kahn's (BFS: decrement in-degree; nodes with 0 in-degree enter queue) and DFS (post-order, reverse). If any node never reaches 0 in-degree (Kahn's) or is revisited in the visiting state (DFS), there is a cycle.

### Minimum Spanning Tree
Kruskal's: sort all edges by weight, add an edge if it connects two different components (union-find). Best for sparse graphs. Prim's: greedily extend a growing tree by the cheapest edge to an unvisited node (min-heap). Better for dense graphs or when edges are implicit (like grid problems).

---

## Java Idioms

### Weighted adjacency list
```java
Map<Integer, List<int[]>> graph = new HashMap<>();
// each int[] is {neighbor, weight}
for (int[] e : edges) {
    graph.computeIfAbsent(e[0], k -> new ArrayList<>()).add(new int[]{e[1], e[2]});
}
```

### Dijkstra
```java
int[] dist = new int[n];
Arrays.fill(dist, Integer.MAX_VALUE);
dist[src] = 0;
// min-heap sorted by distance: (distance, node)
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
pq.offer(new int[]{src, 0});
while (!pq.isEmpty()) {
    int[] cur = pq.poll();
    int u = cur[0], d = cur[1];
    if (d > dist[u]) continue;           // stale entry
    for (int[] nb : graph.getOrDefault(u, List.of())) {
        int v = nb[0], w = nb[1];
        if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
            pq.offer(new int[]{v, dist[v]});
        }
    }
}
```

### Bellman-Ford
```java
int[] dist = new int[n];
Arrays.fill(dist, Integer.MAX_VALUE);
dist[src] = 0;
for (int i = 0; i < n - 1; i++) {
    for (int[] edge : edges) {           // edge = {u, v, w}
        int u = edge[0], v = edge[1], w = edge[2];
        if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v])
            dist[v] = dist[u] + w;
    }
}
// negative cycle check: one more pass
for (int[] edge : edges) {
    int u = edge[0], v = edge[1], w = edge[2];
    if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v])
        // negative cycle reachable
}
```

### Floyd-Warshall
```java
int[][] dist = new int[n][n];
// initialize: dist[i][i]=0, dist[i][j]=weight or INF
for (int k = 0; k < n; k++)
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (dist[i][k] != INF && dist[k][j] != INF)
                dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
```

### Union-Find (path compression + union by rank)
```java
int[] parent, rank;

int find(int x) {
    return parent[x] == x ? x : (parent[x] = find(parent[x]));
}

boolean union(int x, int y) {
    int px = find(x), py = find(y);
    if (px == py) return false;
    if (rank[px] < rank[py]) { int t = px; px = py; py = t; }
    parent[py] = px;
    if (rank[px] == rank[py]) rank[px]++;
    return true;
}
```

### Kahn's topological sort
```java
int[] inDegree = new int[n];
List<List<Integer>> adj = new ArrayList<>();
for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
// populate adj and inDegree from edges
Queue<Integer> q = new LinkedList<>();
for (int i = 0; i < n; i++)
    if (inDegree[i] == 0) q.offer(i);
List<Integer> order = new ArrayList<>();
while (!q.isEmpty()) {
    int u = q.poll();
    order.add(u);
    for (int v : adj.get(u))
        if (--inDegree[v] == 0) q.offer(v);
}
// cycle exists if order.size() < n
```

---

## Algorithm Skeletons (Python)

### Dijkstra
```python
import heapq
from collections import defaultdict

def dijkstra(graph, src, n):
    # graph: {u: [(v, w), ...]}
    dist = [float('inf')] * n
    dist[src] = 0
    heap = [(0, src)]          # (distance, node)
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue           # stale entry
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```

### Union-Find (path compression + rank)
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True
```

### Kahn's topological sort
```python
from collections import deque

def kahn_topo(adj, n):
    # adj: {u: [v, ...]}; n = number of nodes
    in_degree = [0] * n
    for u in adj:
        for v in adj[u]:
            in_degree[v] += 1
    q = deque(i for i in range(n) if in_degree[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    return order if len(order) == n else []   # empty = cycle
```

---

## Decision Guide

| Constraint | Algorithm |
|---|---|
| Weighted shortest path, no negatives | Dijkstra |
| Negative edges or exact K hops | Bellman-Ford |
| All-pairs shortest path, small V | Floyd-Warshall |
| MST, sparse graph | Kruskal's + Union-Find |
| MST, dense / implicit edges | Prim's |
| Visit every edge exactly once | Hierholzer's (Euler path) |
| Ordering from implicit constraints | Topological sort (Kahn's or DFS) |
| Connectivity / cycle in undirected | Union-Find |
| Strongly connected components | Kosaraju's / Tarjan's |
| Bridges / articulation points | Tarjan's with discovery + low time |

---

## Per-Problem Notes

| Problem | Key Insight | Tricky Part | Common Mistakes | Time | Space |
|---|---|---|---|---|---|
| Network Delay Time (LC 743) | Dijkstra from source k; answer = max of all dist values | 1-indexed nodes — size array n+1 | Not checking all nodes reached; returning early | O((V+E) log V) | O(V+E) |
| Path with Min Effort (LC 1631) | Modified Dijkstra on grid; cost = max(path cost so far, grid[r][c]) | Cost function is max not sum | Using plain BFS (unweighted); not taking max | O(mn log mn) | O(mn) |
| Swim in Rising Water (LC 778) | Dijkstra where dist to cell = max(current dist, grid[r][c]); answer at (n-1,n-1) | Same max-based cost as min effort | Using BFS; not tracking max over path | O(n² log n) | O(n²) |
| Cheapest Flights K Stops (LC 787) | Bellman-Ford for exactly K+1 hops; copy dist each round | Must copy dist before each round to prevent same-round chaining | Using Dijkstra (can't cap hops); in-place update | O(K·E) | O(V) |
| Number of Ways to Arrive (LC 1976) | Dijkstra tracking both shortest dist and count of paths achieving it | Count paths modulo 1e9+7; update count when equal dist found | Not resetting count on strictly shorter path | O((V+E) log V) | O(V+E) |
| Find City Smallest Neighbors (LC 1334) | Floyd-Warshall all-pairs; then count reachable cities within threshold per node | Tie-break: largest index wins | Off-by-one on threshold check; wrong tie-break | O(V³) | O(V²) |
| Min Cost Connect All Points (LC 1584) | MST: Prim's (implicit edges) or Kruskal's (build all O(n²) edges first) | Prim's avoids materializing all edges — better in practice | Building explicit edge list for Prim's (wastes memory) | O(n² log n) | O(n²) |
| Most Stones Removed (LC 947) | Stones sharing row or col are connected; Union-Find on (row, col); removed = n - components | Use offset trick: col ID = col + max_row to avoid collision with row ID | Not offsetting col keys; counting components wrong | O(n α(n)) | O(n) |
| Number of Ops to Connect Network (LC 1319) | Need n-1 edges for n nodes; count extra edges (redundant cables); need (components-1) extras | If total edges < n-1 at all → impossible | Not checking feasibility first | O(E α(V)) | O(V) |
| Number of Islands II (LC 305) | Union-Find: on each land addition, union with adjacent land cells | Track island count incrementally; decrement on each successful union | Rebuilding from scratch per query | O(k α(mn)) | O(mn) |
| Reconstruct Itinerary (LC 332) | Euler path on directed graph; sort adjacency lists lexicographically; Hierholzer's DFS | Post-order push then reverse; must use all edges | Not sorting; not reversing result | O(E log E) | O(E) |
| Alien Dictionary (LC 269) | Extract char ordering from adjacent word pairs; topological sort on char graph | Prefix longer than next word with matching prefix → return "" | Missing cycle detection; not initializing all chars in in-degree | O(C) | O(1) — 26 chars |
| Build Matrix with Conditions (LC 2392) | Two independent topological sorts: one for rows, one for cols; both must be acyclic | Must detect cycles in each separately | Conflating row and col graphs; not detecting cycles | O(k² + k) | O(k²) |
| Bridges in Graph / Critical Connections (LC 1192) | Tarjan's bridge algorithm: bridge when low[v] > disc[u] | Distinguish parent edge from back edge (use parent ID not visited flag) | Using visited flag instead of parent tracking with multiple edges | O(V+E) | O(V+E) |
| Articulation Points | Tarjan's: articulation if low[v] >= disc[u] (root needs 2+ children) | Root node is special: it's articulation only if it has 2+ DFS tree children | Forgetting root special case | O(V+E) | O(V+E) |
| Find Critical & Pseudo-Critical Edges (LC 1489) | For critical: MST increases without it. For pseudo: MST achievable with it forced in | Two MST runs per edge; use Union-Find + Kruskal's | Not distinguishing critical from pseudo-critical correctly | O(E² α(V)) | O(V) |
| Greatest Common Divisor Traversal (LC 2709) | Group nodes by prime factors (sieve); connect nodes sharing a prime factor; check connectivity | Naive O(n²) edge building TLEs; group by prime factors instead | Building edges between all pairs | O(n√M) | O(n+M) |
| Kosaraju's Algorithm | Two-pass DFS: first pass fills finish-time stack on original graph; second pass DFS on reversed graph | Must reverse graph for second pass; process nodes in reverse finish order | Using same graph for both passes | O(V+E) | O(V+E) |
| Making a Large Island (LC 827) | Label each island with an ID; store sizes; for each 0-cell, sum sizes of distinct adjacent islands + 1 | Must track distinct island IDs to avoid double-counting | Double-counting same island when 0-cell touches it from two sides | O(n²) | O(n²) |
| Shortest Path in Binary Matrix (LC 1091) | BFS on 8-directional grid of 0-cells; path length = number of cells visited | Start or end cell being 1 → return -1 immediately | Not handling blocked start/end; counting path length off by 1 | O(n²) | O(n²) |

---

## Edge Cases to Watch

1. **Disconnected graph in Dijkstra**: nodes unreachable from the source remain at `float('inf')` / `Integer.MAX_VALUE`. Always check all nodes are reachable before returning an answer (e.g., Network Delay Time returns -1).

2. **Negative cycle detection in Bellman-Ford**: after V−1 relaxation passes, do one more pass. If any distance still decreases, a negative cycle is reachable. Guard against overflow: check `dist[u] != INF` before computing `dist[u] + w`.

3. **Integer overflow in Dijkstra / Bellman-Ford**: when `dist[u]` is `Integer.MAX_VALUE` and you compute `dist[u] + w`, it overflows to a negative number. Use `Long` for distances, or guard with `if (dist[u] == INF) continue`.

4. **Self-loops in Union-Find**: `union(x, x)` must return `false` (already same component). The standard implementation handles this via `find(x) == find(y)` check, but self-loops in the input graph can cause issues if not filtered before union calls.

5. **Cycle in topological sort**: after Kahn's, if `len(order) < n`, at least one cycle exists. Nodes with non-zero in-degree are part of a cycle. The DFS approach detects cycles via a "currently visiting" state (color 1). For Alien Dictionary, a cycle means no valid ordering → return `""`.

6. **Modified Dijkstra with max-based cost** (Path with Min Effort, Swim in Rising Water): the cost to reach a cell is `max(current_best, edge_weight)`, not a sum. BFS does not work here because the cost function is not monotonically additive — you need the heap to process min-cost states first.

7. **Directed vs undirected**: Union-Find detects cycles only in **undirected** graphs. For directed graphs, use DFS with 3-state coloring or Kahn's (cycle if order is incomplete). Kruskal's MST applies to undirected graphs; for directed MST you need Edmonds' algorithm.

8. **Kruskal's on sparse vs Prim's on dense**: Kruskal's requires materializing and sorting all edges — O(E log E). For grid problems or complete graphs where E = O(V²), Prim's with a lazy heap avoids building the full edge list and can be faster in practice.

9. **Euler path existence**: a valid Euler path in an undirected graph requires exactly 0 or 2 nodes of odd degree. In a directed graph, exactly one node has out-degree − in-degree = 1 (start) and one has in-degree − out-degree = 1 (end). If the graph is also disconnected, no Euler path exists even with correct degrees.

10. **Union-Find island problems with coordinate encoding**: when merging row and column nodes (Most Stones), use an offset (e.g., col + 10001) so row and column IDs do not collide. Forgetting this silently merges unrelated components.
