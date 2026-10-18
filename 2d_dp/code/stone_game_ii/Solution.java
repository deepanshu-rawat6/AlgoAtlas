import java.util.*;

public class Solution {
    public int stoneGameII(int[] piles) {
        // dp[i][m] = max stones current player can get from piles[i:] with M=m
        // suffix sums; try all x in [1, 2M]: take suffix[i] - dp(i+x, max(M,x))
        // Time: O(n^3), Space: O(n^2)
        int n = piles.length;
        int[] suffix = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) suffix[i] = suffix[i+1] + piles[i];
        // dp[i][m]: max stones from index i with current M=m
        int[][] dp = new int[n + 1][n + 1];
        for (int i = n - 1; i >= 0; i--) {
            for (int m = 1; m <= n; m++) {
                if (i + 2 * m >= n) {
                    dp[i][m] = suffix[i];
                } else {
                    for (int x = 1; x <= 2 * m; x++) {
                        dp[i][m] = Math.max(dp[i][m], suffix[i] - dp[i + x][Math.max(m, x)]);
                    }
                }
            }
        }
        return dp[0][1];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.stoneGameII(new int[]{2,7,9,4,4}) == 10 : "test 1 failed";
        assert sol.stoneGameII(new int[]{1,2,3,4,5,100}) == 104 : "test 2 failed";
        assert sol.stoneGameII(new int[]{1}) == 1 : "test 3 failed";
        assert sol.stoneGameII(new int[]{1,2}) == 3 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
