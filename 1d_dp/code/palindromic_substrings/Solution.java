import java.util.*;

public class Solution {
    // Expand around center — O(n^2) time, O(1) space
    public int countSubstrings(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            count += expand(s, i, i);     // odd length
            count += expand(s, i, i + 1); // even length
        }
        return count;
    }

    private int expand(String s, int l, int r) {
        int cnt = 0;
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            cnt++; l--; r++;
        }
        return cnt;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.countSubstrings("abc") == 3 : "abc";
        assert sol.countSubstrings("aaa") == 6 : "aaa";
        assert sol.countSubstrings("a") == 1 : "single";
        assert sol.countSubstrings("aa") == 3 : "aa";
        System.out.println("All tests passed.");
    }
}
