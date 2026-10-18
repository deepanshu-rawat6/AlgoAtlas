import java.util.*;

public class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, word, i, j, 0, m, n)) return true;
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int r, int c, int idx, int m, int n) {
        if (idx == word.length()) return true;
        if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != word.charAt(idx)) return false;
        char orig = board[r][c];
        board[r][c] = '#';
        boolean found = dfs(board, word, r + 1, c, idx + 1, m, n)
                     || dfs(board, word, r - 1, c, idx + 1, m, n)
                     || dfs(board, word, r, c + 1, idx + 1, m, n)
                     || dfs(board, word, r, c - 1, idx + 1, m, n);
        board[r][c] = orig;
        return found;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        char[][] board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        // deep copy helper
        char[][] b1 = new char[][]{ {'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'} };
        char[][] b2 = new char[][]{ {'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'} };
        char[][] b3 = new char[][]{ {'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'} };

        assert sol.exist(b1, "ABCCED") : "ABCCED should exist";
        assert sol.exist(b2, "SEE") : "SEE should exist";
        assert !sol.exist(b3, "ABCB") : "ABCB should not exist";

        System.out.println("All tests passed.");
    }
}
