import java.util.*;

public class Solution {
    // LC 2707: Extra Characters in a String
    public int minExtraChar(String s, String[] dictionary) {
        // Build trie from dictionary
        TrieNode root = new TrieNode();
        for (String w : dictionary) {
            TrieNode node = root;
            for (char c : w.toCharArray()) {
                if (node.children[c - 'a'] == null)
                    node.children[c - 'a'] = new TrieNode();
                node = node.children[c - 'a'];
            }
            node.isEnd = true;
        }

        int n = s.length();
        int[] dp = new int[n + 1]; // dp[i] = min extra in s[0..i-1]
        // dp[0] = 0 by default
        for (int i = 0; i < n; i++) {
            dp[i + 1] = dp[i] + 1; // skip s[i] as extra char
            // try all substrings s[j..i] in trie
            TrieNode node = root;
            for (int j = i; j >= 0; j--) {
                int c = s.charAt(j) - 'a';
                if (node.children[c] == null) break;
                node = node.children[c];
                if (node.isEnd)
                    dp[i + 1] = Math.min(dp[i + 1], dp[j]);
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.minExtraChar("leetscode", new String[]{"leet","code","leetcode"}) == 1;
        assert sol.minExtraChar("sayhelloworld", new String[]{"hello","world"}) == 3;
        System.out.println("All tests passed.");
    }
}

class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd;
}
