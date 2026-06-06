# LC 1976 - Number of Ways to Arrive at Destination

Count the number of shortest paths from node `0` to node `n-1` in a weighted undirected graph. Return count modulo 10⁹+7.

## Approach: Dijkstra + Path Count — O((V+E) log V)
Run Dijkstra. Maintain a `ways[]` array alongside `dist[]`:
- If a shorter path to `v` is found: `dist[v] = new_dist`, `ways[v] = ways[u]`
- If an equally short path is found: `ways[v] += ways[u]`

## Key Insight
Dijkstra processes nodes in order of increasing distance. When we first pop a node, we have its final shortest distance. The count propagation mirrors how we'd count paths in a DAG — the shortest-path DAG is implicitly constructed during Dijkstra.

## Edge Cases
- Only one path exists → answer is 1
- Multiple roads between same cities → handled naturally
- Apply modulo at every addition to prevent overflow

## Example
```
n=7, roads connect cities with various weights
Dijkstra finds shortest dist to node 6
4 different paths achieve that minimum distance
Output: 4
```
