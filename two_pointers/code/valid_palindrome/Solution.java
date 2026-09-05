// LC 125: Valid Palindrome
// Alphanumeric-only check, ignoring case, using two pointers from both ends.
// Time: O(n), Space: O(1)
import java.util.*;

public class Solution {
    // Brute: O(n) build filtered string then compare
    public boolean isPalindromeBrute(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray())
            if (Character.isLetterOrDigit(c)) sb.append(Character.toLowerCase(c));
        String filtered = sb.toString();
        return filtered.equals(sb.reverse().toString());
    }

    // Optimal: O(n) two pointers
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) return false;
            l++; r--;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.isPalindrome("A man, a plan, a canal: Panama") == true : "Test 1 failed";
        assert s.isPalindrome("race a car") == false : "Test 2 failed";
        assert s.isPalindrome(" ") == true : "Test 3 failed";
        assert s.isPalindrome("") == true : "Test 4 failed";
        assert s.isPalindrome("0P") == false : "Test 5 failed";
        System.out.println("All tests passed.");
    }
}
