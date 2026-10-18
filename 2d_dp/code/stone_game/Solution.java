import java.util.*;

public class Solution {
    public boolean stoneGame(int[] piles) {
        // Alice always wins: even piles, odd total means Alice can always pick the
        // optimal parity group. Math shortcut: return true.
        // Time: O(1), Space: O(1)
        return true;
    }

    // DP version: dp[i][j] = score difference (current player - other) for piles[i..j]
    public boolean stoneGameDP(int[] piles) {
        int n = piles.length;
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) dp[i][i] = piles[i];
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                dp[i][j] = Math.max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1]);
            }
        }
        return dp[0][n-1] > 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.stoneGame(new int[]{5,3,4,5}) == true : "test 1 failed";
        assert sol.stoneGame(new int[]{3,7,2,3}) == true : "test 2 failed";
        assert sol.stoneGameDP(new int[]{5,3,4,5}) == true : "test 3 failed";
        assert sol.stoneGameDP(new int[]{3,7,2,3}) == true : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
