import java.util.*;

// LC 214: Shortest Palindrome — KMP on s+'#'+rev(s) O(n)
public class Solution {
    public String shortestPalindrome(String s) {
        if (s.isEmpty()) return s;
        String rev = new StringBuilder(s).reverse().toString();
        String t = s + "#" + rev;
        int[] lps = new int[t.length()];
        int length = 0, i = 1;
        while (i < t.length()) {
            if (t.charAt(i) == t.charAt(length)) {
                lps[i++] = ++length;
            } else if (length != 0) {
                length = lps[length - 1];
            } else {
                i++;
            }
        }
        int palLen = lps[t.length() - 1];
        return rev.substring(0, s.length() - palLen) + s;
    }

    public String shortestPalindromeHash(String s) {
        long BASE = 131, MOD = 1_000_000_007L;
        long fwd = 0, bwd = 0, power = 1;
        int best = 0;
        for (int i = 0; i < s.length(); i++) {
            long v = s.charAt(i);
            fwd = (fwd * BASE + v) % MOD;
            bwd = (bwd + v * power) % MOD;
            power = power * BASE % MOD;
            if (fwd == bwd) best = i + 1;
        }
        String suffix = s.substring(best);
        return new StringBuilder(suffix).reverse() + s;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.shortestPalindrome("aacecaaa").equals("aaacecaaa") : "test 1";
        assert s.shortestPalindrome("abcd").equals("dcbabcd") : "test 2";
        assert s.shortestPalindrome("").equals("") : "test 3";
        assert s.shortestPalindrome("a").equals("a") : "test 4";
        assert s.shortestPalindromeHash("aacecaaa").equals("aaacecaaa") : "hash 1";
        assert s.shortestPalindromeHash("abcd").equals("dcbabcd") : "hash 2";
        System.out.println("All tests passed.");
    }
}
