import java.util.*;

public class Solution {
    public boolean isPalindrome(String s) {
        if (s.length() <= 1) return true;
        if (s.charAt(0) != s.charAt(s.length() - 1)) return false;
        return isPalindrome(s.substring(1, s.length() - 1));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.isPalindrome("racecar") : "test failed";
        assert sol.isPalindrome("abba") : "test failed";
        assert sol.isPalindrome("a") : "test failed";
        assert sol.isPalindrome("") : "test failed";
        assert !sol.isPalindrome("abc") : "test failed";
        assert sol.isPalindrome("abcba") : "test failed";
        System.out.println("All tests passed.");
    }
}
