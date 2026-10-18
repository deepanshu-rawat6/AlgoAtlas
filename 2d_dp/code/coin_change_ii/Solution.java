import java.util.*;

public class Solution {
    public int change(int amount, int[] coins) {
        // dp[j] = ways to make amount j; for each coin update forward (unbounded)
        // Time: O(n*amount), Space: O(amount)
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins) {
            for (int j = coin; j <= amount; j++) {
                dp[j] += dp[j - coin];
            }
        }
        return dp[amount];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.change(5, new int[]{1,2,5}) == 4 : "test 1 failed";
        assert sol.change(3, new int[]{2}) == 0 : "test 2 failed";
        assert sol.change(10, new int[]{10}) == 1 : "test 3 failed";
        assert sol.change(0, new int[]{1,2,5}) == 1 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
