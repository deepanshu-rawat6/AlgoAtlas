from typing import List

class Solution:
    # Union-Find: group stones sharing row or col. Each group can be reduced to 1 stone.
    # Answer = total_stones - number_of_groups
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for r, c in stones:
            # offset col by 10001 to avoid collision with row indices
            union(r, c + 10001)

        # count distinct components among stones
        components = len({find(r) for r, c in stones})
        return len(stones) - components
