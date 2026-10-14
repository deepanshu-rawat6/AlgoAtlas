import java.util.*;

// LC 1392: Longest Happy Prefix — KMP LPS array O(n)
public class Solution {
    public String longestPrefix(String s) {
        int n = s.length();
        int[] lps = new int[n];
        int length = 0, i = 1;
        while (i < n) {
            if (s.charAt(i) == s.charAt(length)) {
                lps[i++] = ++length;
            } else if (length != 0) {
                length = lps[length - 1];
            } else {
                i++;
            }
        }
        return s.substring(0, lps[n - 1]);
    }

    public String longestPrefixHash(String s) {
        long BASE = 131, MOD = 1_000_000_007L;
        int n = s.length();
        long prefix = 0, suffix = 0, power = 1;
        int best = 0;
        for (int i = 0; i < n - 1; i++) {
            prefix = (prefix * BASE + s.charAt(i)) % MOD;
            suffix = (s.charAt(n - 1 - i) * power + suffix) % MOD;
            power = power * BASE % MOD;
            if (prefix == suffix) best = i + 1;
        }
        return s.substring(0, best);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.longestPrefix("level").equals("l") : "test 1";
        assert s.longestPrefix("ababab").equals("abab") : "test 2";
        assert s.longestPrefix("leetcodeleet").equals("leet") : "test 3";
        assert s.longestPrefix("a").equals("") : "test 4";
        assert s.longestPrefixHash("level").equals("l") : "hash 1";
        assert s.longestPrefixHash("ababab").equals("abab") : "hash 2";
        System.out.println("All tests passed.");
    }
}
