# Kosaraju's Algorithm - Strongly Connected Components

Find all Strongly Connected Components (SCCs) in a directed graph. An SCC is a maximal set of nodes where every node is reachable from every other.

## Approach: Two-Pass DFS — O(V+E)
1. **Pass 1**: DFS on original graph, push nodes to stack in **finish order**
2. **Transpose**: reverse all edges
3. **Pass 2**: Pop from stack, DFS on transposed graph — each DFS tree is one SCC

## Key Insight
Nodes finishing last in Pass 1 belong to "source" SCCs (no incoming edges from other SCCs). In the transposed graph, these become "sink" SCCs — DFS from them can only reach nodes within the same SCC. The finish-order stack ensures we process SCCs in reverse topological order of the condensation DAG.

## Edge Cases
- Single node with self-loop → one SCC of size 1
- DAG (no cycles) → every node is its own SCC
- Fully connected directed graph → one SCC containing all nodes

## Example
```
n=5, edges=[[0,1],[1,2],[2,0],[1,3],[3,4]]
0→1→2→0 form a cycle → SCC {0,1,2}
3→4, no back edges → SCCs {3} and {4}
Output: [[0,1,2],[3],[4]]
```
