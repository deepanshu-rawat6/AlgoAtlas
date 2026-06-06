# Course Schedule II (LC 210)

Given `numCourses` and a list of `prerequisites` where `[a, b]` means take `b` before `a`,
return a valid ordering to complete all courses. Return `[]` if impossible (cycle exists).

## Approaches

### 1. DFS Topological Sort
**Complexity:** O(V + E) time, O(V + E) space

DFS with 3-state coloring: unvisited (0), in-progress (1), done (2). Append each node
to the result in post-order. Reverse at the end. Return `[]` if a back edge is found.

**Why it works:** Post-order DFS naturally produces reverse topological order. A node
is added only after all its dependencies are processed. A back edge (state=1 revisit)
signals a cycle.

### 2. Kahn's BFS (optimal)
**Complexity:** O(V + E) time, O(V + E) space

Compute in-degrees. Enqueue all nodes with in-degree 0. Process queue: add node to
result, decrement neighbors' in-degrees, enqueue any that reach 0. If result length
< numCourses, a cycle exists.

**Why it works:** Nodes with in-degree 0 have no unmet prerequisites. Processing them
and reducing neighbors' in-degrees simulates taking courses in valid order.

## Key Insight

Course scheduling is topological sort on a DAG. A cycle means mutual dependency —
impossible to complete. Kahn's algorithm detects cycles implicitly: if not all nodes
are processed, some are stuck in a cycle.

## Edge Cases

- No prerequisites — any order works; return `[0, 1, ..., n-1]`.
- Single course — return `[0]`.
- Mutual dependency `[[0,1],[1,0]]` — return `[]`.
- Multiple valid orderings — any valid one is accepted.
