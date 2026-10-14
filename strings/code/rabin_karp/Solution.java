import java.util.*;

// Rabin-Karp rolling hash substring search — O(n+m) average
public class Solution {
    public int strStr(String haystack, String needle) {
        int n = haystack.length(), m = needle.length();
        if (m == 0) return 0;
        if (m > n) return -1;
        long BASE = 31, MOD = 1_000_000_007L;
        long power = 1;
        for (int i = 0; i < m - 1; i++) power = power * BASE % MOD;

        long needleHash = 0, windowHash = 0;
        for (int i = 0; i < m; i++) {
            needleHash = (needleHash * BASE + (needle.charAt(i) - 'a' + 1)) % MOD;
            windowHash = (windowHash * BASE + (haystack.charAt(i) - 'a' + 1)) % MOD;
        }
        if (windowHash == needleHash && haystack.substring(0, m).equals(needle)) return 0;

        for (int i = 1; i <= n - m; i++) {
            windowHash = (windowHash - (haystack.charAt(i - 1) - 'a' + 1) * power % MOD + MOD) % MOD;
            windowHash = (windowHash * BASE + (haystack.charAt(i + m - 1) - 'a' + 1)) % MOD;
            if (windowHash == needleHash && haystack.substring(i, i + m).equals(needle)) return i;
        }
        return -1;
    }

    public int strStrNaive(String haystack, String needle) {
        int n = haystack.length(), m = needle.length();
        for (int i = 0; i <= n - m; i++)
            if (haystack.substring(i, i + m).equals(needle)) return i;
        return -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.strStr("hello", "ll") == 2 : "test 1";
        assert s.strStr("aaaaa", "bba") == -1 : "test 2";
        assert s.strStr("", "") == 0 : "test 3";
        assert s.strStr("mississippi", "issip") == 4 : "test 4";
        assert s.strStrNaive("hello", "ll") == 2 : "naive";
        System.out.println("All tests passed.");
    }
}
