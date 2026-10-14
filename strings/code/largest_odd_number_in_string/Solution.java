import java.util.*;

// LC 1903: Largest Odd Number in String — scan right to left O(n)
public class Solution {
    public String largestOddNumber(String num) {
        for (int i = num.length() - 1; i >= 0; i--) {
            if ((num.charAt(i) - '0') % 2 == 1)
                return num.substring(0, i + 1);
        }
        return "";
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.largestOddNumber("52").equals("5") : "test 1";
        assert s.largestOddNumber("4206").equals("") : "test 2";
        assert s.largestOddNumber("35427").equals("35427") : "test 3";
        assert s.largestOddNumber("2").equals("") : "test 4";
        assert s.largestOddNumber("1").equals("1") : "test 5";
        System.out.println("All tests passed.");
    }
}
