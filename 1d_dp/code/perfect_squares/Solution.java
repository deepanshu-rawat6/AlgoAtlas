import java.util.*;

public class Solution {
    // DP — O(n * sqrt(n)) time, O(n) space
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE / 2);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.numSquares(12) == 3 : "12";
        assert sol.numSquares(13) == 2 : "13";
        assert sol.numSquares(1) == 1 : "1";
        assert sol.numSquares(4) == 1 : "4";
        System.out.println("All tests passed.");
    }
}
