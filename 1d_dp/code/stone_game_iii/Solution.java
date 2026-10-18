import java.util.*;

public class Solution {
    // Bottom-up DP — O(n) time, O(n) space
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        // dp[i] = max score advantage current player can get from index i
        int[] dp = new int[n + 1];
        // dp[n] = 0 (no stones left)
        for (int i = n - 1; i >= 0; i--) {
            dp[i] = Integer.MIN_VALUE / 2;
            int total = 0;
            for (int k = 1; k <= 3 && i + k <= n; k++) {
                total += stoneValue[i + k - 1];
                dp[i] = Math.max(dp[i], total - dp[i + k]);
            }
        }
        if (dp[0] > 0) return "Alice";
        if (dp[0] < 0) return "Bob";
        return "Tie";
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.stoneGameIII(new int[]{1, 2, 3, 7}).equals("Bob") : "[1,2,3,7]";
        assert sol.stoneGameIII(new int[]{1, 2, 3, -9}).equals("Alice") : "[1,2,3,-9]";
        assert sol.stoneGameIII(new int[]{1, 2, 3, 6}).equals("Tie") : "[1,2,3,6]";
        assert sol.stoneGameIII(new int[]{1}).equals("Alice") : "single";
        System.out.println("All tests passed.");
    }
}
