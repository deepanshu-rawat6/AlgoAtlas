"""
# 212: Word Search II

Given an `m x n` board of characters and a list of `words`, return all words
that can be constructed from sequentially adjacent (horizontal/vertical) cells,
using each cell at most once per word.

## Examples
```text
Input:  board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Input:  board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

## Constraints
- m == board.length, n == board[i].length
- 1 <= m, n <= 12
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- All strings in words are unique.
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    """
    **LC 212: Word Search II**

    Given an `m x n` board of characters and a list of strings `words`, return
    all words on the board. Each word must be constructed from letters of
    sequentially adjacent cells (horizontally or vertically neighboring). The
    same cell may not be used more than once in a word.

    Example 1:
    ```text
    Input:  board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
            words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]
    ```

    Example 2:
    ```text
    Input:  board = [["a","b"],["c","d"]]
            words = ["abcb"]
    Output: []
    ```

    **Constraints:**
    * `m == board.length`, `n == board[i].length`
    * `1 <= m, n <= 12`
    * `board[i][j]` is a lowercase English letter
    * `1 <= words.length <= 3 * 10^4`
    * `1 <= words[i].length <= 10`
    * All strings in `words` are unique
    """

    def findWords_brute(self, board: List[List[str]], words: List[str]) -> List[str]:
        # O(w * m * n * 4^L) — DFS per word independently
        pass

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build a trie from all words for efficient prefix pruning
        # DFS from each cell; prune when current path is not a trie prefix
        # When a word is found in trie, add to result and remove from trie to avoid duplicates
        # O(m * n * 4^L) — Trie + backtracking DFS (prune branches)
        pass


if __name__ == "__main__":
    sol = Solution()

    # Example 1: expected ["eat", "oath"]
    board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    print(sol.findWords(board1, ["oath","pea","eat","rain"]))

    # Example 2: expected []
    board2 = [["a","b"],["c","d"]]
    print(sol.findWords(board2, ["abcb"]))
