# Clone Graph (LC 133)

Given a reference to a node in a connected undirected graph, return a **deep copy** of
the entire graph. Each node has an integer value and a list of neighbors.

## Approaches

### 1. DFS with Visited Map
**Complexity:** O(V + E) time, O(V) space

Recursively clone each node. Use a `visited` dict mapping original → clone to handle
cycles and avoid infinite recursion.

**Why it works:** DFS naturally traverses all reachable nodes. The visited map ensures
each node is cloned exactly once and neighbor references point to the correct clones.

### 2. BFS with Visited Map (optimal)
**Complexity:** O(V + E) time, O(V) space

BFS from the start node. For each dequeued node, iterate its neighbors: clone them if
unseen, then append the clone to the current node's neighbor list.

**Why it works:** Same visited-map guarantee as DFS but avoids recursion stack overhead.
Neighbor wiring happens as each node is processed from the queue.

## Key Insight

The `visited` map (old node → new node) serves double duty: it prevents revisiting nodes
**and** provides the correct clone reference when wiring up neighbor lists.

## Edge Cases

- `None` input — return `None`.
- Single node with no neighbors — return a new node with empty neighbor list.
- Graph with self-loops — handled by the visited check before recursing.
