"""
# 133. Clone Graph

## Problem
Given a reference of a node in a connected undirected graph, return a deep copy (clone)
of the graph. Each node in the graph contains a value (`int`) and a list of its neighbors.

```text
class Node {
    public int val;
    public List<Node> neighbors;
}
```

## Examples
```text
Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: 4 nodes, node 1 connects to 2 and 4, node 2 connects to 1 and 3, etc.
```

```text
Input:  adjList = [[]]
Output: [[]]
Explanation: Single node with no neighbors.
```

```text
Input:  adjList = []
Output: []
Explanation: Empty graph.
```

## Constraints
- The number of nodes in the graph is in the range `[0, 100]`
- `1 <= Node.val <= 100`
- `Node.val` is unique for each node
- There are no repeated edges and no self-loops
- The graph is connected (all nodes can be visited starting from the given node)
"""

from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph_dfs(self, node: Optional['Node']) -> Optional['Node']:
        # O(V+E) time, O(V) space — DFS with visited map
        if not node:
            return None
        visited = {}

        def dfs(n):
            if n in visited:
                return visited[n]
            clone = Node(n.val)
            visited[n] = clone
            for nb in n.neighbors:
                clone.neighbors.append(dfs(nb))
            return clone

        return dfs(node)

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS/DFS with a visited map: old_node -> new_node clone
        # For each node, clone it if not seen, then clone all its neighbors
        # O(V+E) time, O(V) space — BFS with visited map
        if not node:
            return None
        visited = {node: Node(node.val)}
        q = deque([node])
        while q:
            curr = q.popleft()
            for nb in curr.neighbors:
                if nb not in visited:
                    visited[nb] = Node(nb.val)
                    q.append(nb)
                visited[curr].neighbors.append(visited[nb])
        return visited[node]


def build_graph(adj: list) -> Optional[Node]:
    if not adj:
        return None
    nodes = [Node(i+1) for i in range(len(adj))]
    for i, neighbors in enumerate(adj):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    return nodes[0]

def graph_to_adj(node: Optional[Node]) -> list:
    if not node:
        return []
    visited, result = {}, {}
    q = deque([node])
    visited[node.val] = node
    while q:
        curr = q.popleft()
        result[curr.val] = sorted(nb.val for nb in curr.neighbors)
        for nb in curr.neighbors:
            if nb.val not in visited:
                visited[nb.val] = nb
                q.append(nb)
    return [result[i] for i in sorted(result)]


if __name__ == '__main__':
    s = Solution()
    adj = [[2,4],[1,3],[2,4],[1,3]]
    g = build_graph(adj)
    assert graph_to_adj(s.cloneGraph_dfs(g)) == [[2,4],[1,3],[2,4],[1,3]]
    assert graph_to_adj(s.cloneGraph(build_graph(adj))) == [[2,4],[1,3],[2,4],[1,3]]
    assert s.cloneGraph(None) is None
    print("All tests passed.")
