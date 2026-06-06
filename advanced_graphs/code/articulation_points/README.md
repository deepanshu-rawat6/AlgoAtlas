# Articulation Points (Tarjan's Algorithm)

Find all vertices whose removal increases the number of connected components.

## Approach: Tarjan's with disc/low — O(V+E)
Same `disc[]`/`low[]` framework as bridges, but the condition differs:
- **Non-root node `u`** is AP if any child `v` has `low[v] >= disc[u]` (v can't bypass u)
- **Root node** is AP if it has **2 or more children** in the DFS tree

## Key Insight
The root condition is special: the root has no parent, so `low[v] >= disc[root]` is always true. Instead, count DFS tree children — if root has 2+ children, removing it disconnects them. For non-root, `low[v] >= disc[u]` (not `>` like bridges) because even reaching `u` itself isn't enough to bypass it.

## Edge Cases
- Root with 1 child → not an AP (even if low[child] >= disc[root])
- Node in a cycle → not an AP (low of children < disc of node)
- Bridge endpoint → usually an AP (but not always — check the condition)

## Example
```
n=5, edges=[[0,1],[1,2],[2,0],[1,3],[3,4]]
Node 1: removing it disconnects {0,2} from {3,4} → AP
Node 3: removing it disconnects {4} → AP
Output: [1,3]
```
