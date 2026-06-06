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
