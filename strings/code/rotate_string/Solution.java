import java.util.*;

// LC 796: Rotate String — s+s contains every rotation O(n)
public class Solution {
    public boolean rotateStringBrute(String s, String goal) {
        if (s.length() != goal.length()) return false;
        for (int i = 0; i < s.length(); i++)
            if ((s.substring(i) + s.substring(0, i)).equals(goal)) return true;
        return false;
    }

    public boolean rotateString(String s, String goal) {
        return s.length() == goal.length() && (s + s).contains(goal);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.rotateString("abcde", "cdeab") : "test 1";
        assert !s.rotateString("abcde", "abced") : "test 2";
        assert s.rotateString("", "") : "test 3";
        assert s.rotateString("a", "a") : "test 4";
        assert !s.rotateString("aa", "a") : "test 5";
        assert s.rotateStringBrute("abcde", "cdeab") : "brute";
        System.out.println("All tests passed.");
    }
}
