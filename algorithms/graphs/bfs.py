"""
Breadth-First Search (BFS)
==========================
Strategy   : Explore all neighbors at current depth before going deeper.
             Uses a queue (FIFO).
Time       : O(V + E)
Space      : O(V)

Use when:
- Shortest path in an unweighted graph/grid
- Level-order traversal
- Finding all nodes within k hops
- Multi-source shortest distance (e.g., 0-1 matrix, rotting oranges)
"""

from collections import deque
from typing import Dict, List, Optional, Tuple


# ─── BFS on adjacency list ───────────────────────────────────────────────────

def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """Return nodes in BFS order from start."""
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> Optional[List[int]]:
    """Return shortest path from start to end (unweighted), or None if unreachable."""
    if start == end:
        return [start]
    visited = {start}
    queue = deque([[start]])        # queue of paths
    while queue:
        path = queue.popleft()
        node = path[-1]
        for neighbor in graph[node]:
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None


# ─── BFS on grid ─────────────────────────────────────────────────────────────

def bfs_grid(grid: List[List[int]], start: Tuple[int, int]) -> List[List[int]]:
    """Return distance grid from start. -1 = unreachable, 0 = wall (grid[r][c]==1).
    
    grid[r][c] == 0: passable, 1: blocked
    """
    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    sr, sc = start
    if grid[sr][sc] == 1:
        return dist
    dist[sr][sc] = 0
    queue = deque([(sr, sc)])
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return dist


# ─── Multi-source BFS ────────────────────────────────────────────────────────

def multi_source_bfs(grid: List[List[int]]) -> List[List[int]]:
    """Return distance from nearest 0-cell for each cell. -1 if unreachable.
    
    LeetCode 542: 01 Matrix — distance to nearest 0.
    Seed the queue with ALL source cells simultaneously.
    """
    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    queue = deque()

    # Seed all sources at once
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))

    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return dist


# ─── Level-order traversal ───────────────────────────────────────────────────

def bfs_levels(graph: Dict[int, List[int]], start: int) -> List[List[int]]:
    """Return nodes grouped by level (distance from start)."""
    visited = {start}
    queue = deque([start])
    levels = []
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        levels.append(level)
    return levels


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2],
    }
    print("BFS order from 0:", bfs(graph, 0))
    print("Shortest path 0→5:", shortest_path(graph, 0, 5))
    print("Levels from 0:", bfs_levels(graph, 0))

    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    print("\nGrid BFS from (0,0):")
    for row in bfs_grid(grid, (0, 0)):
        print(" ", row)

    matrix = [[0,0,0],[0,1,0],[1,1,1]]
    print("\nMulti-source BFS (01 Matrix):")
    for row in multi_source_bfs(matrix):
        print(" ", row)
