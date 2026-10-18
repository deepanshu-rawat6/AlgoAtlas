import java.util.*;

public class Solution {
    // Bottom-up DP — O(n^2) time, O(n) space
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.wordBreak("leetcode", Arrays.asList("leet", "code")) : "leetcode";
        assert sol.wordBreak("applepenapple", Arrays.asList("apple", "pen")) : "applepenapple";
        assert !sol.wordBreak("catsandog", Arrays.asList("cats", "dog", "sand", "and", "cat")) : "catsandog";
        assert sol.wordBreak("a", Arrays.asList("a")) : "single";
        System.out.println("All tests passed.");
    }
}
