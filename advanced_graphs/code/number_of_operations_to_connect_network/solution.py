"""
# LC 1319: Number of Operations to Make Network Connected

Find the minimum number of cable moves needed to connect all `n` computers. A
cable can be reused from any redundant connection. Return -1 if impossible.

## Examples
```text
Input: n=4, connections=[[0,1],[0,2],[1,2]]
Output: 1
# Edge (1,2) is redundant; move it to connect the isolated computer 3.
```

## Constraints
- Union-Find — O(n + e)
- If len(connections) < n-1 → return -1 (not enough cables)
- Answer = number_of_components - 1
"""
from typing import List

class Solution:
    # Union-Find: count components and redundant edges
    # Need (components-1) moves; possible only if redundant_edges >= components-1
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1  # not enough edges to connect n nodes

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False  # redundant edge
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        components = n
        for u, v in connections:
            if union(u, v):
                components -= 1  # merged two components

        return components - 1  # need this many moves to connect remaining components


if __name__ == "__main__":
    sol = Solution()

    # Example from README: one redundant edge, one isolated node
    assert sol.makeConnected(4, [[0, 1], [0, 2], [1, 2]]) == 1

    # LC example 2: two redundant edges cover two extra components
    assert sol.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]) == 2

    # Not enough cables to ever connect n nodes
    assert sol.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]) == -1

    # Already fully connected → no moves needed
    assert sol.makeConnected(1, []) == 0

    print("All tests passed.")
