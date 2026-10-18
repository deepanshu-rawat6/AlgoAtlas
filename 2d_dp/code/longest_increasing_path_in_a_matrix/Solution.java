import java.util.*;

public class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        // DFS + memoization: dp[r][c] = longest increasing path starting at (r,c)
        // Time: O(m*n), Space: O(m*n)
        int m = matrix.length, n = matrix[0].length;
        int[][] memo = new int[m][n];
        int res = 0;
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                res = Math.max(res, dfs(matrix, memo, r, c, m, n));
        return res;
    }

    private int dfs(int[][] matrix, int[][] memo, int r, int c, int m, int n) {
        if (memo[r][c] != 0) return memo[r][c];
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        int best = 1;
        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && matrix[nr][nc] > matrix[r][c])
                best = Math.max(best, 1 + dfs(matrix, memo, nr, nc, m, n));
        }
        memo[r][c] = best;
        return best;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.longestIncreasingPath(new int[][]{{9,9,4},{6,6,8},{2,1,1}}) == 4 : "test 1 failed";
        assert sol.longestIncreasingPath(new int[][]{{3,4,5},{3,2,6},{2,2,1}}) == 4 : "test 2 failed";
        assert sol.longestIncreasingPath(new int[][]{{1}}) == 1 : "test 3 failed";
        assert sol.longestIncreasingPath(new int[][]{{1,2},{3,4}}) == 3 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
