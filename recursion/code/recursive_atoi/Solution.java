import java.util.*;

public class Solution {
    private static final int INT_MIN = Integer.MIN_VALUE;
    private static final int INT_MAX = Integer.MAX_VALUE;

    public int myAtoi(String s) {
        s = s.stripLeading();
        if (s.isEmpty()) return 0;
        int sign = 1, start = 0;
        if (s.charAt(0) == '-') { sign = -1; start = 1; }
        else if (s.charAt(0) == '+') { start = 1; }
        long result = sign * recurse(s, start, 0);
        return (int) Math.max(INT_MIN, Math.min(INT_MAX, result));
    }

    private long recurse(String s, int idx, long current) {
        if (idx == s.length() || !Character.isDigit(s.charAt(idx))) return current;
        return recurse(s, idx + 1, current * 10 + (s.charAt(idx) - '0'));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.myAtoi("   -42") == -42 : "test failed";
        assert sol.myAtoi("4193 with words") == 4193 : "test failed";
        assert sol.myAtoi("words and 987") == 0 : "test failed";
        assert sol.myAtoi("") == 0 : "test failed";
        assert sol.myAtoi("-91283472332") == Integer.MIN_VALUE : "test failed";
        assert sol.myAtoi("91283472332") == Integer.MAX_VALUE : "test failed";
        System.out.println("All tests passed.");
    }
}
