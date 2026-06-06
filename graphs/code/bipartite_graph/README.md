# LC 785 - Is Graph Bipartite?

A graph is bipartite if its nodes can be split into two groups such that every edge connects nodes from different groups (i.e., it's 2-colorable, contains no odd-length cycles).

## Approaches

**Approach 1: BFS Coloring — O(V+E)**
Assign color 0 to start node. For each neighbor, assign opposite color. If a neighbor already has the same color as current node → not bipartite.

**Approach 2: DFS Coloring — O(V+E)**
Same logic recursively. Return false immediately on color conflict.

## Key Insight
A graph is bipartite iff it has **no odd-length cycles**. 2-coloring detects this: if you ever need to assign two colors to the same node, an odd cycle exists. Must handle **disconnected components** by iterating over all unvisited nodes.

## Edge Cases
- Disconnected graph: check each component independently
- Self-loop: immediately not bipartite
- Empty graph / single node: bipartite

## Example
```
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Node 0 connects to 1,2,3 → color 0 gets color A
Nodes 1,2,3 get color B
But edge (1,2): both are color B → conflict → false
```
