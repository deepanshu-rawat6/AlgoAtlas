import java.util.*;

public class Solution {
    // Bottom-up DP — O(amount * n) time, O(amount) space
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE / 2);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
        return dp[amount] >= Integer.MAX_VALUE / 2 ? -1 : dp[amount];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.coinChange(new int[]{1, 2, 5}, 11) == 3 : "11";
        assert sol.coinChange(new int[]{2}, 3) == -1 : "impossible";
        assert sol.coinChange(new int[]{1}, 0) == 0 : "zero amount";
        assert sol.coinChange(new int[]{1, 5, 11}, 11) == 1 : "exact coin";
        System.out.println("All tests passed.");
    }
}
