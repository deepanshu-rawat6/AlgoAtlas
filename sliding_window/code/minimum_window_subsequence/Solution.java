import java.util.*;

public class Solution {
    public String minWindow(String s1, String s2) {
        int n = s1.length(), m = s2.length();
        String result = "";
        int i = 0;
        while (i < n) {
            int j = 0;
            while (i < n && j < m) {
                if (s1.charAt(i) == s2.charAt(j)) j++;
                i++;
            }
            if (j < m) break;
            int end = i - 1;
            j = m - 1;
            int k = end;
            while (k >= 0 && j >= 0) {
                if (s1.charAt(k) == s2.charAt(j)) j--;
                k--;
            }
            int start = k + 1;
            if (result.isEmpty() || end - start + 1 < result.length())
                result = s1.substring(start, end + 1);
            i = start + 1;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.minWindow("abcdebdde", "bde").equals("bcde");
        assert sol.minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u").equals("");
        assert sol.minWindow("abcde", "ace").equals("abcde");
        System.out.println("All tests passed.");
    }
}
