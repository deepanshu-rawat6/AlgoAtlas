import java.util.*;

public class Solution {
    public int strToInt(String s) {
        if (s.isEmpty()) return 0;
        if (s.length() == 1) return s.charAt(0) - '0';
        return strToInt(s.substring(0, s.length() - 1)) * 10 + (s.charAt(s.length() - 1) - '0');
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.strToInt("1234") == 1234 : "test failed";
        assert sol.strToInt("0") == 0 : "test failed";
        assert sol.strToInt("9") == 9 : "test failed";
        assert sol.strToInt("100") == 100 : "test failed";
        assert sol.strToInt("999") == 999 : "test failed";
        System.out.println("All tests passed.");
    }
}
