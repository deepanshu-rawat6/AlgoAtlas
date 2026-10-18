import java.util.*;

public class Solution {
    public int romanToInt(String s) {
        // Subtract current symbol if it's smaller than the next one; otherwise add it
        // O(n) time
        Map<Character, Integer> val = new HashMap<>();
        val.put('I', 1); val.put('V', 5); val.put('X', 10); val.put('L', 50);
        val.put('C', 100); val.put('D', 500); val.put('M', 1000);
        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            int cur = val.get(s.charAt(i));
            int next = (i + 1 < s.length()) ? val.get(s.charAt(i + 1)) : 0;
            result += (cur < next) ? -cur : cur;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.romanToInt("III") == 3;
        assert sol.romanToInt("LVIII") == 58;
        assert sol.romanToInt("MCMXCIV") == 1994;
        assert sol.romanToInt("IV") == 4;
        System.out.println("All tests passed.");
    }
}
