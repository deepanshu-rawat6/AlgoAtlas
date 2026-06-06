"""
Union-Find (Disjoint Set Union — DSU)
======================================
Strategy   : Maintain a forest of trees where each tree = one connected component.
             Path compression + union by rank keeps operations nearly O(1).
Time       : O(α(n)) per operation — inverse Ackermann, effectively O(1)
Space      : O(n)

Use when:
- Dynamic connectivity queries: "are u and v connected?"
- Counting connected components
- Cycle detection in undirected graphs
- Kruskal's MST algorithm
- Grouping/merging problems (accounts merge, friend circles)
"""

from typing import List


class UnionFind:
    def __init__(self, n: int):
        """Initialize n disjoint sets {0}, {1}, ..., {n-1}."""
        self.parent = list(range(n))    # parent[i] = i means i is a root
        self.rank   = [0] * n           # rank = upper bound on tree height
        self.count  = n                 # number of connected components

    def find(self, x: int) -> int:
        """Return root of x's component. Path compression flattens the tree."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Merge components of x and y. Returns True if they were different sets."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False                # already in same component
        # Union by rank: attach smaller tree under larger tree
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# ─── Connected components ────────────────────────────────────────────────────

def count_components(n: int, edges: List[List[int]]) -> int:
    """Count connected components in undirected graph. LeetCode 323."""
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.count


# ─── Cycle detection in undirected graph ─────────────────────────────────────

def has_cycle(n: int, edges: List[List[int]]) -> bool:
    """Detect cycle in undirected graph using Union-Find.
    
    If both endpoints of an edge are already in the same component,
    adding that edge creates a cycle.
    """
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):      # union returns False if already connected
            return True
    return False


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    # Basic operations
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    print("Components:", uf.count)                  # 3: {0,1,2}, {3,4}, {5}
    print("0 and 2 connected:", uf.connected(0, 2)) # True
    print("0 and 3 connected:", uf.connected(0, 3)) # False

    uf.union(2, 3)
    print("After union(2,3):", uf.count)            # 2: {0,1,2,3,4}, {5}

    # Connected components
    edges = [[0,1],[1,2],[3,4]]
    print("\nComponent count:", count_components(5, edges))  # 2

    # Cycle detection
    no_cycle = [[0,1],[1,2],[2,3]]
    with_cycle = [[0,1],[1,2],[2,0]]
    print("Has cycle (no)  :", has_cycle(4, no_cycle))    # False
    print("Has cycle (yes) :", has_cycle(3, with_cycle))  # True
