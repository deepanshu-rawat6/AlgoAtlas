import java.util.*;

public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        Map<Integer, Boolean> memo = new HashMap<>();
        return dp(s, 0, wordSet, memo);
    }

    private boolean dp(String s, int start, Set<String> wordSet, Map<Integer, Boolean> memo) {
        if (start == s.length()) return true;
        if (memo.containsKey(start)) return memo.get(start);
        for (int end = start + 1; end <= s.length(); end++) {
            if (wordSet.contains(s.substring(start, end)) && dp(s, end, wordSet, memo)) {
                memo.put(start, true);
                return true;
            }
        }
        memo.put(start, false);
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.wordBreak("leetcode", Arrays.asList("leet", "code")) : "test failed";
        assert sol.wordBreak("applepenapple", Arrays.asList("apple", "pen")) : "test failed";
        assert !sol.wordBreak("catsandog", Arrays.asList("cats", "dog", "sand", "and", "cat")) : "test failed";
        assert sol.wordBreak("a", Arrays.asList("a")) : "test failed";
        System.out.println("All tests passed.");
    }
}
