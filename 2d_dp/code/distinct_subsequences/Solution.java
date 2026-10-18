import java.util.*;

public class Solution {
    public long numDistinct(String s, String t) {
        // dp[i][j] = ways to form t[:j] from s[:i]
        // If s[i-1]==t[j-1]: dp[i-1][j-1] + dp[i-1][j]; else dp[i-1][j]
        // Time: O(m*n), Space: O(n) — long to avoid overflow on large inputs
        int n = t.length();
        long[] dp = new long[n + 1];
        dp[0] = 1;
        for (char c : s.toCharArray()) {
            for (int j = n; j >= 1; j--) {
                if (c == t.charAt(j - 1)) dp[j] += dp[j - 1];
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.numDistinct("rabbbit", "rabbit") == 3 : "test 1 failed";
        assert sol.numDistinct("babgbag", "bag") == 5 : "test 2 failed";
        assert sol.numDistinct("a", "b") == 0 : "test 3 failed";
        assert sol.numDistinct("aaa", "a") == 3 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
