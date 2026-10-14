import java.util.*;

// KMP pattern matching — O(n+m) via LPS array
public class Solution {
    private int[] computeLPS(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int length = 0, i = 1;
        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(length)) {
                lps[i++] = ++length;
            } else if (length != 0) {
                length = lps[length - 1];
            } else {
                i++;
            }
        }
        return lps;
    }

    public int kmpSearch(String text, String pattern) {
        int n = text.length(), m = pattern.length();
        if (m == 0) return 0;
        int[] lps = computeLPS(pattern);
        int i = 0, j = 0;
        while (i < n) {
            if (text.charAt(i) == pattern.charAt(j)) { i++; j++; }
            if (j == m) return i - j;
            else if (i < n && text.charAt(i) != pattern.charAt(j)) {
                if (j != 0) j = lps[j - 1];
                else i++;
            }
        }
        return -1;
    }

    public List<Integer> kmpSearchAll(String text, String pattern) {
        int n = text.length(), m = pattern.length();
        List<Integer> results = new ArrayList<>();
        if (m == 0) return results;
        int[] lps = computeLPS(pattern);
        int i = 0, j = 0;
        while (i < n) {
            if (text.charAt(i) == pattern.charAt(j)) { i++; j++; }
            if (j == m) {
                results.add(i - j);
                j = lps[j - 1];
            } else if (i < n && text.charAt(i) != pattern.charAt(j)) {
                if (j != 0) j = lps[j - 1];
                else i++;
            }
        }
        return results;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert Arrays.equals(s.computeLPS("AABAACAABAA"), new int[]{0,1,0,1,2,0,1,2,3,4,5}) : "lps";
        assert s.kmpSearch("AABAACAADAABAABA", "AABA") == 0 : "test 1";
        assert s.kmpSearch("hello", "ll") == 2 : "test 2";
        assert s.kmpSearch("aaaaa", "bba") == -1 : "test 3";
        assert s.kmpSearchAll("AABAACAADAABAABA", "AABA").equals(Arrays.asList(0, 9, 12)) : "all";
        System.out.println("All tests passed.");
    }
}
