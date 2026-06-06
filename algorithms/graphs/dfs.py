"""
Depth-First Search (DFS)
========================
Strategy   : Explore as deep as possible before backtracking. Uses a stack (or recursion).
Time       : O(V + E)
Space      : O(V) — recursion stack or explicit stack

Use when:
- Cycle detection
- Topological sort (post-order DFS)
- Connected components
- Path existence (not shortest path)
- Backtracking problems
"""

from typing import Dict, List, Set, Tuple


# ─── DFS on adjacency list (recursive) ───────────────────────────────────────

def dfs_recursive(graph: Dict[int, List[int]], start: int, visited: Set[int] = None) -> List[int]:
    """Return nodes in DFS order (recursive)."""
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))
    return order


# ─── DFS on adjacency list (iterative) ───────────────────────────────────────

def dfs_iterative(graph: Dict[int, List[int]], start: int) -> List[int]:
    """Return nodes in DFS order (iterative, avoids recursion limit)."""
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        # Push neighbors in reverse so leftmost is processed first
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
    return order


# ─── DFS on grid ─────────────────────────────────────────────────────────────

def dfs_grid(grid: List[List[int]], r: int, c: int, visited: Set[Tuple]) -> int:
    """DFS flood fill on grid. Returns size of connected component from (r,c).
    
    grid[r][c] == 1: land, 0: water
    """
    rows, cols = len(grid), len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return 0
    if grid[r][c] == 0 or (r, c) in visited:
        return 0
    visited.add((r, c))
    size = 1
    for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        size += dfs_grid(grid, r + dr, c + dc, visited)
    return size


# ─── Connected components ────────────────────────────────────────────────────

def connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """Return list of connected components (each is a list of nodes)."""
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = dfs_recursive(graph, node, visited)
            components.append(component)
    return components


# ─── Cycle detection: undirected graph ───────────────────────────────────────

def has_cycle_undirected(graph: Dict[int, List[int]]) -> bool:
    """Detect cycle in undirected graph using DFS.
    
    Track parent to avoid treating the edge we came from as a back edge.
    """
    visited = set()

    def dfs(node: int, parent: int) -> bool:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:    # back edge found → cycle
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False


# ─── Cycle detection: directed graph ─────────────────────────────────────────

def has_cycle_directed(graph: Dict[int, List[int]]) -> bool:
    """Detect cycle in directed graph using DFS with 3-color marking.
    
    WHITE (0): unvisited, GRAY (1): in current path, BLACK (2): fully processed
    A back edge (to a GRAY node) indicates a cycle.
    """
    color = {node: 0 for node in graph}

    def dfs(node: int) -> bool:
        color[node] = 1             # mark as in-progress
        for neighbor in graph[node]:
            if color[neighbor] == 1:    # back edge → cycle
                return True
            if color[neighbor] == 0 and dfs(neighbor):
                return True
        color[node] = 2             # fully processed
        return False

    return any(dfs(node) for node in graph if color[node] == 0)


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [0, 3], 2: [0, 4], 3: [1], 4: [2], 5: [6], 6: [5]}
    print("Recursive DFS from 0:", dfs_recursive(graph, 0))
    print("Iterative DFS from 0:", dfs_iterative(graph, 0))
    print("Components:", connected_components(graph))

    cyclic   = {0: [1], 1: [2], 2: [0]}
    acyclic  = {0: [1], 1: [2], 2: []}
    print("\nUndirected cycle (0-1-2-0):", has_cycle_undirected({0:[1,2],1:[0,2],2:[1,0]}))
    print("Directed cycle  (0→1→2→0):", has_cycle_directed(cyclic))
    print("Directed acyclic(0→1→2)  :", has_cycle_directed(acyclic))

    grid = [[1,1,0],[1,0,0],[0,0,1]]
    visited: Set[Tuple] = set()
    print("\nIsland size from (0,0):", dfs_grid(grid, 0, 0, visited))
