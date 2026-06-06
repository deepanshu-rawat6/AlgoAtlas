from typing import List
from collections import deque

class Solution:
    # Approach 1: BFS coloring - try to 2-color the graph
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 = unvisited, 0 and 1 are the two colors

        for start in range(n):  # handle disconnected components
            if color[start] != -1:
                continue
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]  # assign opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False  # same color on both ends = odd cycle
        return True

    # Approach 2: DFS coloring
    def isBipartite_dfs(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == c:
                    return False  # conflict
            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
