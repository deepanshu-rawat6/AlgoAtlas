# LC 1192 - Critical Connections in a Network (Bridges)

Find all edges whose removal increases the number of connected components (bridges).

## Approach: Tarjan's Bridge Algorithm — O(V+E)
Maintain `disc[]` (discovery time) and `low[]` (lowest disc reachable via subtree).
- `low[v]` = min of: `disc[v]`, `disc` of back-edge neighbors, `low` of DFS children
- Edge `(u,v)` is a bridge if `low[v] > disc[u]` (v can't reach u or above without this edge)

## Key Insight
`low[v] > disc[u]` means the subtree rooted at `v` has no back edge reaching `u` or any ancestor of `u`. Removing `(u,v)` would disconnect `v`'s subtree. Pass `parent` to avoid treating the tree edge back to parent as a back edge.

## Edge Cases
- Multiple edges between same pair (multigraph): track parent edge index, not just parent node
- Single node → no bridges
- Tree (no cycles) → every edge is a bridge

## Example
```
n=4, connections=[[0,1],[1,2],[2,0],[1,3]]
0-1-2 form a cycle → no bridge among them
Edge (1,3): low[3]=disc[3] > disc[1] → bridge
Output: [[1,3]]
```
