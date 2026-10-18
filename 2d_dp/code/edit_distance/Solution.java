import java.util.*;

public class Solution {
    public int minDistance(String word1, String word2) {
        // dp[i][j] = min edits to convert word1[:i] to word2[:j]
        // Match: dp[i-1][j-1]; else 1 + min(replace, delete, insert)
        // Time: O(m*n), Space: O(n)
        int m = word1.length(), n = word2.length();
        int[] dp = new int[n + 1];
        for (int j = 0; j <= n; j++) dp[j] = j;
        for (int i = 1; i <= m; i++) {
            int prev = dp[0];
            dp[0] = i;
            for (int j = 1; j <= n; j++) {
                int temp = dp[j];
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[j] = prev;
                } else {
                    dp[j] = 1 + Math.min(prev, Math.min(dp[j], dp[j - 1]));
                }
                prev = temp;
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.minDistance("horse", "ros") == 3 : "test 1 failed";
        assert sol.minDistance("intention", "execution") == 5 : "test 2 failed";
        assert sol.minDistance("", "") == 0 : "test 3 failed";
        assert sol.minDistance("a", "") == 1 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
