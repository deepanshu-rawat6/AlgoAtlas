import java.util.*;

public class Solution {
    public boolean isMatch(String s, String p) {
        // dp[i][j] = does s[:i] match p[:j]
        // '*': zero occurrences dp[i][j-2], or more dp[i-1][j] if p[j-2] matches s[i-1]
        // Time: O(m*n), Space: O(m*n)
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;
        for (int j = 1; j <= n; j++) {
            if (p.charAt(j - 1) == '*' && j >= 2) dp[0][j] = dp[0][j - 2];
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                char pc = p.charAt(j - 1);
                if (pc == '*') {
                    dp[i][j] = dp[i][j - 2]; // zero occurrences
                    if (p.charAt(j - 2) == s.charAt(i - 1) || p.charAt(j - 2) == '.') {
                        dp[i][j] = dp[i][j] || dp[i - 1][j];
                    }
                } else if (pc == s.charAt(i - 1) || pc == '.') {
                    dp[i][j] = dp[i - 1][j - 1];
                }
            }
        }
        return dp[m][n];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.isMatch("aa", "a*") == true : "test 1 failed";
        assert sol.isMatch("ab", ".*") == true : "test 2 failed";
        assert sol.isMatch("aa", "a") == false : "test 3 failed";
        assert sol.isMatch("aab", "c*a*b") == true : "test 4 failed";
        assert sol.isMatch("mississippi", "mis*is*p*.") == false : "test 5 failed";
        System.out.println("All tests passed.");
    }
}
