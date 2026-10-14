import java.util.*;

// LC 730: Count Different Palindromic Subsequences — interval DP O(n^2)
public class Solution {
    public int countPalindromicSubsequences(String s) {
        int MOD = 1_000_000_007;
        int n = s.length();
        String chars = "abcd";

        // next[i][c] = next occurrence of char c at or after index i
        // prev[i][c] = prev occurrence of char c at or before index i
        int[][] next = new int[n + 1][4];
        int[][] prev = new int[n + 1][4];

        Arrays.fill(next[n], n);
        for (int i = n - 1; i >= 0; i--) {
            for (int ci = 0; ci < 4; ci++) {
                next[i][ci] = (s.charAt(i) == chars.charAt(ci)) ? i : next[i + 1][ci];
            }
        }
        Arrays.fill(prev[0], -1);
        for (int i = 0; i < n; i++) {
            for (int ci = 0; ci < 4; ci++) {
                prev[i][ci] = (s.charAt(i) == chars.charAt(ci)) ? i : (i > 0 ? prev[i - 1][ci] : -1);
            }
        }

        int[][] dp = new int[n][n];

        for (int len = 1; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                for (int ci = 0; ci < 4; ci++) {
                    int lo = next[i][ci];
                    int hi = (j < n) ? prev[j][ci] : prev[n - 1][ci];
                    // recompute hi correctly: prev up to j
                    hi = prev[j][ci];
                    if (lo > j) continue;
                    else if (lo == hi) dp[i][j] = (dp[i][j] + 1) % MOD;
                    else if (lo + 1 == hi) dp[i][j] = (dp[i][j] + 2) % MOD;
                    else dp[i][j] = (dp[i][j] + dp[lo + 1][hi - 1] + 2) % MOD;
                }
            }
        }
        return dp[0][n - 1];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.countPalindromicSubsequences("bccb") == 6 : "test 1";
        assert s.countPalindromicSubsequences("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba") == 104860361 : "test 2";
        System.out.println("All tests passed.");
    }
}
