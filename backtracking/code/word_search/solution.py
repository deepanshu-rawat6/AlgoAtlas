from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        ## 79. Word Search

        Given an m x n grid of characters board and a string word, return true if word
        exists in the grid. The word can be constructed from letters of sequentially
        adjacent cells, where adjacent cells are horizontally or vertically neighboring.
        The same letter cell may not be used more than once.

        ### Examples

        ```text
        Input:  board = [["A","B","C","E"],
                          ["S","F","C","S"],
                          ["A","D","E","E"]], word = "ABCCED"
        Output: true

        Input:  board = [["A","B","C","E"],
                          ["S","F","C","S"],
                          ["A","D","E","E"]], word = "SEE"
        Output: true

        Input:  board = [["A","B","C","E"],
                          ["S","F","C","S"],
                          ["A","D","E","E"]], word = "ABCB"
        Output: false
        ```

        ### Constraints
        - `m == board.length`, `n = board[i].length`
        - `1 <= m, n <= 6`
        - `1 <= word.length <= 15`
        - board and word consist of only lowercase and uppercase English letters.
        """
        # DFS from each cell matching word[0]; mark cell visited by modifying grid
        # Backtrack by restoring the cell after recursion
        # O(m * n * 4^L) time where L = len(word), O(L) stack space
        m, n = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
                return False
            tmp, board[r][c] = board[r][c], '#'
            found = (dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1))
            board[r][c] = tmp
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    import copy
    assert s.exist(copy.deepcopy(board), "ABCCED") is True
    assert s.exist(copy.deepcopy(board), "SEE") is True
    assert s.exist(copy.deepcopy(board), "ABCB") is False
    print("All tests passed.")
