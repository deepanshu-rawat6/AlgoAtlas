"""
Topological Sort
================
Strategy   : Order nodes of a DAG so every edge u→v has u before v.
Time       : O(V + E)
Space      : O(V)

Only valid for Directed Acyclic Graphs (DAGs).
If a cycle exists, topological sort is impossible.

Two approaches:
1. Kahn's (BFS) — process nodes with in-degree 0; intuitive, detects cycles easily
2. DFS post-order — add node to result AFTER all descendants are processed

Use when:
- Task scheduling with dependencies
- Build systems (compile order)
- Course prerequisites (LeetCode 207, 210)
- Detecting cycles in directed graphs
"""

from collections import deque
from typing import Dict, List, Optional


# ─── Kahn's Algorithm (BFS) ───────────────────────────────────────────────────

def topological_sort_kahn(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """Topological sort using Kahn's BFS algorithm.
    
    Returns sorted order, or None if graph has a cycle.
    """
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    # Start with all nodes that have no incoming edges
    queue = deque(node for node in in_degree if in_degree[node] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If not all nodes processed, there's a cycle
    return order if len(order) == len(graph) else None


# ─── DFS Post-order ───────────────────────────────────────────────────────────

def topological_sort_dfs(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """Topological sort using DFS post-order traversal.
    
    Returns sorted order, or None if graph has a cycle.
    Uses 3-color marking: 0=unvisited, 1=in-progress, 2=done.
    """
    color = {node: 0 for node in graph}
    result = []
    has_cycle = [False]

    def dfs(node: int) -> None:
        if has_cycle[0]:
            return
        color[node] = 1                     # mark in-progress
        for neighbor in graph[node]:
            if color[neighbor] == 1:        # back edge → cycle
                has_cycle[0] = True
                return
            if color[neighbor] == 0:
                dfs(neighbor)
        color[node] = 2                     # mark done
        result.append(node)                 # post-order: add after all descendants

    for node in graph:
        if color[node] == 0:
            dfs(node)

    if has_cycle[0]:
        return None
    result.reverse()                        # reverse post-order = topological order
    return result


# ─── Example ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    # Course prerequisites: 0→1 means course 0 must be taken before 1
    dag = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
        4: [],
    }
    print("Kahn's order :", topological_sort_kahn(dag))
    print("DFS order    :", topological_sort_dfs(dag))

    # Graph with cycle — should return None
    cyclic = {0: [1], 1: [2], 2: [0]}
    print("\nCyclic graph (Kahn's):", topological_sort_kahn(cyclic))
    print("Cyclic graph (DFS)   :", topological_sort_dfs(cyclic))

    # LeetCode 210: Course Schedule II
    def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(num_courses)}
        for a, b in prerequisites:
            graph[b].append(a)              # b must come before a
        result = topological_sort_kahn(graph)
        return result if result is not None else []

    print("\nCourse order:", find_order(4, [[1,0],[2,0],[3,1],[3,2]]))
