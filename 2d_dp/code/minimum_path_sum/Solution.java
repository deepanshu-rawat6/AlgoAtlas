import java.util.*;

public class Solution {
    public int minPathSum(int[][] grid) {
        // dp[j] = min path sum to current cell; update in-place left-to-right, top-to-bottom
        // Time: O(m*n), Space: O(n)
        int m = grid.length, n = grid[0].length;
        int[] dp = new int[n];
        dp[0] = 0;
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int i = 0; i < m; i++) {
            dp[0] += grid[i][0];
            for (int j = 1; j < n; j++) {
                dp[j] = Math.min(dp[j], dp[j - 1]) + grid[i][j];
            }
        }
        return dp[n - 1];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.minPathSum(new int[][]{{1,3,1},{1,5,1},{4,2,1}}) == 7 : "test 1 failed";
        assert sol.minPathSum(new int[][]{{1,2,3},{4,5,6}}) == 12 : "test 2 failed";
        assert sol.minPathSum(new int[][]{{1}}) == 1 : "test 3 failed";
        assert sol.minPathSum(new int[][]{{1,2},{1,1}}) == 3 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
