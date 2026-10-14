import java.util.*;

// LC 38: Count and Say — run-length encoding, iterative O(n*L)
public class Solution {
    public String countAndSay(int n) {
        String result = "1";
        for (int k = 1; k < n; k++) {
            StringBuilder sb = new StringBuilder();
            int i = 0;
            while (i < result.length()) {
                char ch = result.charAt(i);
                int j = i;
                while (j < result.length() && result.charAt(j) == ch) j++;
                sb.append(j - i).append(ch);
                i = j;
            }
            result = sb.toString();
        }
        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.countAndSay(1).equals("1") : "test 1";
        assert s.countAndSay(2).equals("11") : "test 2";
        assert s.countAndSay(3).equals("21") : "test 3";
        assert s.countAndSay(4).equals("1211") : "test 4";
        assert s.countAndSay(5).equals("111221") : "test 5";
        System.out.println("All tests passed.");
    }
}
