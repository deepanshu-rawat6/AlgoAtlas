"""
# LC 126: Word Ladder II

Find all shortest transformation sequences from `beginWord` to `endWord`,
changing one letter at a time, where each intermediate word must exist in
`wordList`.

## Examples
```text
Input: beginWord = "hit", endWord = "cog",
       wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

Input: beginWord = "hit", endWord = "cog",
       wordList = ["hot","dot","dog","lot","log"]
Output: []
```

## Constraints
- If `endWord` is not in `wordList`, return `[]`.
- If no transformation path exists, return `[]`.
- The order of returned paths is not significant.
"""
from typing import List
from collections import defaultdict, deque

class Solution:
    # BFS to find shortest path length + build parent map, then DFS to collect all paths
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        # BFS: build layer-by-layer parent map (child -> set of parents)
        parents = defaultdict(set)
        current_layer = {beginWord}
        found = False

        while current_layer and not found:
            word_set -= current_layer  # remove current layer to prevent revisiting
            next_layer = set()
            for word in current_layer:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nw = word[:i] + c + word[i+1:]
                        if nw in word_set:
                            next_layer.add(nw)
                            parents[nw].add(word)  # record how we reached nw
                            if nw == endWord:
                                found = True
            current_layer = next_layer

        if not found:
            return []

        # DFS backtrack from endWord to beginWord using parent map
        result = []
        def dfs(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                dfs(parent, path)
                path.pop()

        dfs(endWord, [endWord])
        return result


if __name__ == "__main__":
    s = Solution()
    result = s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    expected = [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]
    # path order is non-deterministic; compare as sorted lists of paths
    assert sorted(result) == sorted(expected)
    assert s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]) == []
    print("All tests passed.")
