from typing import List

class Solution:
    # Union-Find with lazy initialization - add land cells one by one
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        count = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            count -= 1  # merging two islands

        result = []
        for r, c in positions:
            cell = r * n + c
            if cell in parent:  # duplicate position
                result.append(count)
                continue

            parent[cell] = cell  # new island
            rank[cell] = 0
            count += 1

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                neighbor = nr * n + nc
                if 0 <= nr < m and 0 <= nc < n and neighbor in parent:
                    union(cell, neighbor)  # merge with adjacent land

            result.append(count)
        return result
