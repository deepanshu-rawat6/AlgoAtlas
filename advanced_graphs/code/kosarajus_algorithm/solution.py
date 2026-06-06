from typing import List
from collections import defaultdict

class Solution:
    # Kosaraju's: 1) DFS on original, push to stack in finish order
    #             2) Transpose graph  3) DFS in reverse finish order on transposed
    def findSCCs(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        rev_graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            rev_graph[v].append(u)

        visited = [False] * n
        stack = []

        def dfs1(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs1(neighbor)
            stack.append(node)  # push after all descendants processed

        def dfs2(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in rev_graph[node]:
                if not visited[neighbor]:
                    dfs2(neighbor, component)

        # Pass 1: fill stack with finish order
        for i in range(n):
            if not visited[i]:
                dfs1(i)

        # Pass 2: process in reverse finish order on transposed graph
        visited = [False] * n
        sccs = []
        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                dfs2(node, component)
                sccs.append(sorted(component))

        return sccs
