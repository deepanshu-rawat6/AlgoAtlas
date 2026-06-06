from typing import List
from collections import defaultdict, deque


class Solution:
    """
    ## 269. Alien Dictionary

    There is a new alien language that uses the English alphabet. However, the order among the
    letters is unknown to you.

    You are given a list of strings `words` from the alien language's dictionary, where the
    strings in `words` are **sorted lexicographically** by the rules of this new language.

    Return a string of the unique letters in the new alien language sorted in the order they
    appear in the alien language. If there is no solution, return `""`. If there are multiple
    solutions, return **any of them**.

    ---

    ### Examples

    ```text
    Input:  words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"

    Input:  words = ["z","x"]
    Output: "zx"

    Input:  words = ["z","x","z"]
    Output: ""
    Explanation: The order is invalid, so return "".
    ```

    ---

    ### Constraints

    - `1 <= words.length <= 100`
    - `1 <= words[i].length <= 100`
    - `words[i]` consists of only lowercase English letters.
    """

    def alienOrder(self, words: List[str]) -> str:
        # Compare adjacent words to extract character ordering constraints
        # Build directed graph of char dependencies; topological sort gives the order
        # Return '' if cycle detected (contradictory ordering)
        # O(C) — Kahn's BFS topological sort, C = total characters across all words
        adj = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        q = deque([c for c in in_degree if in_degree[c] == 0])
        result = []
        while q:
            c = q.popleft()
            result.append(c)
            for nb in adj[c]:
                in_degree[nb] -= 1
                if in_degree[nb] == 0:
                    q.append(nb)

        return "".join(result) if len(result) == len(in_degree) else ""

    def alienOrder_dfs(self, words: List[str]) -> str:
        # DFS topological sort with 3-state coloring: unvisited/in-progress/done
        # Cycle = revisiting an in-progress node; append to result in post-order
        # O(C) — DFS topological sort with cycle detection
        adj = defaultdict(set)
        chars = {c for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # 0=unvisited, 1=visiting, 2=visited
        state = {c: 0 for c in chars}
        result = []

        def dfs(c: str) -> bool:
            if state[c] == 1:
                return False  # cycle
            if state[c] == 2:
                return True
            state[c] = 1
            for nb in adj[c]:
                if not dfs(nb):
                    return False
            state[c] = 2
            result.append(c)
            return True

        for c in chars:
            if state[c] == 0:
                if not dfs(c):
                    return ""

        return "".join(reversed(result))


if __name__ == '__main__':
    s = Solution()
    # BFS
    assert s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    assert s.alienOrder(["z", "x"]) == "zx"
    assert s.alienOrder(["z", "x", "z"]) == ""

    # DFS (multiple valid orderings possible; check length and no cycle)
    res = s.alienOrder_dfs(["wrt", "wrf", "er", "ett", "rftt"])
    assert len(res) == 5
    assert s.alienOrder_dfs(["z", "x", "z"]) == ""

    print("All tests passed.")
