"""
# LC 547: Number of Provinces

Count connected components in an adjacency matrix where `isConnected[i][j] = 1`
means city `i` and city `j` are directly connected.

## Examples
```text
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

## Constraints
- A single city yields 1 province.
- If all cities are connected, the answer is 1.
- The identity matrix (no connections) yields `n`.
"""
from typing import List

class Solution:
    # Approach 1: DFS - treat adjacency matrix as graph, count connected components
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(node):
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                provinces += 1  # each unvisited node starts a new component
        return provinces

    # Approach 2: Union-Find
    def findCircleNum_uf(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            # union by rank
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        components = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    if union(i, j):
                        components -= 1  # merging two components
        return components


if __name__ == "__main__":
    s = Solution()
    assert s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
    assert s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3
    assert s.findCircleNum_uf([[1,1,0],[1,1,0],[0,0,1]]) == 2
    assert s.findCircleNum_uf([[1,0,0],[0,1,0],[0,0,1]]) == 3
    print("All tests passed.")
