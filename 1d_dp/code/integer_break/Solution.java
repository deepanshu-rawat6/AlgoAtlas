import java.util.*;

public class Solution {
    // DP — O(n^2) time, O(n) space
    public int integerBreak(int n) {
        int[] dp = new int[n + 1];
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                dp[i] = Math.max(dp[i], Math.max(j * (i - j), j * dp[i - j]));
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.integerBreak(2) == 1 : "n=2";
        assert sol.integerBreak(3) == 2 : "n=3";
        assert sol.integerBreak(10) == 36 : "n=10";
        assert sol.integerBreak(4) == 4 : "n=4";
        System.out.println("All tests passed.");
    }
}
