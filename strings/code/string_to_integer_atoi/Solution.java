import java.util.*;

// LC 8: String to Integer (atoi) — whitespace, sign, digits, clamp O(n)
public class Solution {
    public int myAtoi(String s) {
        int i = 0, n = s.length();
        while (i < n && s.charAt(i) == ' ') i++;
        int sign = 1;
        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
            sign = s.charAt(i++) == '-' ? -1 : 1;
        }
        long result = 0;
        while (i < n && Character.isDigit(s.charAt(i))) {
            result = result * 10 + (s.charAt(i++) - '0');
            if (result * sign <= Integer.MIN_VALUE) return Integer.MIN_VALUE;
            if (result * sign >= Integer.MAX_VALUE) return Integer.MAX_VALUE;
        }
        return (int)(result * sign);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.myAtoi("42") == 42 : "test 1";
        assert s.myAtoi("   -42") == -42 : "test 2";
        assert s.myAtoi("4193 with words") == 4193 : "test 3";
        assert s.myAtoi("words and 987") == 0 : "test 4";
        assert s.myAtoi("-91283472332") == Integer.MIN_VALUE : "test 5";
        assert s.myAtoi("91283472332") == Integer.MAX_VALUE : "test 6";
        assert s.myAtoi("  +0 123") == 0 : "test 7";
        System.out.println("All tests passed.");
    }
}
