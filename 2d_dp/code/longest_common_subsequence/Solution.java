import java.util.*;

public class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        // dp[j] = LCS of current text1 prefix and text2[:j]
        // Track prev (diagonal) to update correctly in-place
        // Time: O(m*n), Space: O(min(m,n))
        if (text1.length() < text2.length()) { String t = text1; text1 = text2; text2 = t; }
        int n = text2.length();
        int[] dp = new int[n + 1];
        for (char c1 : text1.toCharArray()) {
            int prev = 0;
            for (int j = 0; j < n; j++) {
                int temp = dp[j + 1];
                dp[j + 1] = c1 == text2.charAt(j) ? prev + 1 : Math.max(dp[j + 1], dp[j]);
                prev = temp;
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.longestCommonSubsequence("abcde", "ace") == 3 : "test 1 failed";
        assert sol.longestCommonSubsequence("abc", "abc") == 3 : "test 2 failed";
        assert sol.longestCommonSubsequence("abc", "def") == 0 : "test 3 failed";
        assert sol.longestCommonSubsequence("bl", "yby") == 1 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
