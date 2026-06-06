# LC 802 - Find Eventual Safe States

Return all nodes from which every path eventually leads to a terminal node (no cycle reachable).

## Approaches

**Approach 1: DFS 3-color — O(V+E)**
- `0` = unvisited, `1` = in current DFS path (potentially in cycle), `2` = confirmed safe
- If DFS reaches a node with state `1` → cycle detected → unsafe
- After all neighbors confirmed safe → mark current node as `2`

**Approach 2: Reverse graph + Kahn's topological sort — O(V+E)**
Reverse all edges. Terminal nodes (out-degree 0 in original) become sources. BFS from sources in reversed graph — all reachable nodes are safe.

## Key Insight
A node is safe iff it's **not part of a cycle and doesn't lead to one**. In the reversed graph, safe nodes are exactly those reachable from terminal nodes via topological order.

## Edge Cases
- Node with no outgoing edges → always safe (terminal)
- All nodes in one big cycle → return `[]`
- Disconnected graph → handle each component

## Example
```
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Nodes 5,6 are terminals. Node 4→5 (safe). Node 2→5 (safe).
Nodes 0,1,3 form a cycle → unsafe
Output: [2,4,5,6]
```
