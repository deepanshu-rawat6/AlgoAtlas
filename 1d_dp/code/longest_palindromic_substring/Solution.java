import java.util.*;

public class Solution {
    // Expand around center — O(n^2) time, O(1) space
    public String longestPalindrome(String s) {
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            int[] odd  = expand(s, i, i);
            int[] even = expand(s, i, i + 1);
            if (odd[1]  - odd[0]  > end - start) { start = odd[0];  end = odd[1]; }
            if (even[1] - even[0] > end - start) { start = even[0]; end = even[1]; }
        }
        return s.substring(start, end + 1);
    }

    private int[] expand(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) { l--; r++; }
        return new int[]{l + 1, r - 1};
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String r1 = sol.longestPalindrome("babad");
        assert r1.equals("bab") || r1.equals("aba") : "babad";
        assert sol.longestPalindrome("cbbd").equals("bb") : "cbbd";
        assert sol.longestPalindrome("a").equals("a") : "single char";
        assert sol.longestPalindrome("racecar").equals("racecar") : "full palindrome";
        System.out.println("All tests passed.");
    }
}
