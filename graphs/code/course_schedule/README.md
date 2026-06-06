# Course Schedule (LC 207)

Given `numCourses` and `prerequisites` where `[a, b]` means take `b` before `a`, return
`true` if it's possible to finish all courses (i.e., no cycle exists in the dependency graph).

## Approaches

### 1. DFS Cycle Detection (3-color marking)
**Complexity:** O(V + E) time, O(V + E) space

Assign each node a state: 0 = unvisited, 1 = in-progress, 2 = done. DFS from each
unvisited node. If we revisit an in-progress node, a cycle exists.

**Why it works:** A back edge in DFS (reaching a node currently on the stack) indicates
a cycle. The 3-state system distinguishes "currently exploring" from "fully explored".

### 2. Kahn's BFS (Topological Sort)
**Complexity:** O(V + E) time, O(V + E) space

Compute in-degrees. Process nodes with in-degree 0 (no prerequisites). Decrement
neighbors' in-degrees; enqueue those reaching 0. If all nodes are processed, no cycle.

**Why it works:** If a cycle exists, the nodes in it will never reach in-degree 0 and
won't be processed. The count of processed nodes will be less than `numCourses`.

## Key Insight

Course completion is possible iff the prerequisite graph is a **DAG** (no cycles).
Both DFS and Kahn's detect cycles in O(V + E). Kahn's is often preferred for its
iterative nature and natural cycle detection via node count.

## Edge Cases

- No prerequisites — always `true`.
- Single course — always `true`.
- All courses in a single chain — `true` (linear DAG).
- Mutual dependency `[0,1],[1,0]` — `false`.
