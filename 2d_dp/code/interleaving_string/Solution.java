import java.util.*;

public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        // dp[i][j] = can s1[:i] and s2[:j] interleave to form s3[:i+j]
        // Time: O(m*n), Space: O(n)
        int m = s1.length(), n = s2.length();
        if (m + n != s3.length()) return false;
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int j = 1; j <= n; j++) dp[j] = dp[j-1] && s2.charAt(j-1) == s3.charAt(j-1);
        for (int i = 1; i <= m; i++) {
            dp[0] = dp[0] && s1.charAt(i-1) == s3.charAt(i-1);
            for (int j = 1; j <= n; j++) {
                dp[j] = (dp[j] && s1.charAt(i-1) == s3.charAt(i+j-1))
                      || (dp[j-1] && s2.charAt(j-1) == s3.charAt(i+j-1));
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.isInterleave("aabcc", "dbbca", "aadbbcbcac") == true : "test 1 failed";
        assert sol.isInterleave("aabcc", "dbbca", "aadbbbaccc") == false : "test 2 failed";
        assert sol.isInterleave("", "", "") == true : "test 3 failed";
        assert sol.isInterleave("a", "b", "ab") == true : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
