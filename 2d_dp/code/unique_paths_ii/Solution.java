import java.util.*;

public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // Same as unique paths but zero out any cell with an obstacle
        // Time: O(m*n), Space: O(n)
        int n = obstacleGrid[0].length;
        int[] dp = new int[n];
        dp[0] = 1;
        for (int[] row : obstacleGrid) {
            for (int j = 0; j < n; j++) {
                if (row[j] == 1) {
                    dp[j] = 0;
                } else if (j > 0) {
                    dp[j] += dp[j - 1];
                }
            }
        }
        return dp[n - 1];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.uniquePathsWithObstacles(new int[][]{{0,0,0},{0,1,0},{0,0,0}}) == 2 : "test 1 failed";
        assert sol.uniquePathsWithObstacles(new int[][]{{0,1},{0,0}}) == 1 : "test 2 failed";
        assert sol.uniquePathsWithObstacles(new int[][]{{1}}) == 0 : "test 3 failed";
        assert sol.uniquePathsWithObstacles(new int[][]{{0,0},{0,0}}) == 2 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
