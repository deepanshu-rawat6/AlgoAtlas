import java.util.*;

public class Solution {
    // Build rank map; compare adjacent words character by character
    public boolean isAlienSorted(String[] words, String order) {
        int[] rank = new int[26];
        for (int i = 0; i < order.length(); i++) rank[order.charAt(i) - 'a'] = i;
        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i], w2 = words[i+1];
            boolean found = false;
            for (int j = 0; j < w1.length(); j++) {
                if (j == w2.length()) return false; // w2 is prefix of w1
                if (w1.charAt(j) != w2.charAt(j)) {
                    if (rank[w1.charAt(j)-'a'] > rank[w2.charAt(j)-'a']) return false;
                    found = true; break;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.isAlienSorted(new String[]{"hello","leetcode"}, "hlabcdefgijkmnopqrstuvwxyz") : "test 1";
        assert !s.isAlienSorted(new String[]{"word","world","row"}, "worldabcefghijkmnpqstuvxyz") : "test 2";
        assert !s.isAlienSorted(new String[]{"apple","app"}, "abcdefghijklmnopqrstuvwxyz") : "test 3";
        assert s.isAlienSorted(new String[]{"z","z"}, "abcdefghijklmnopqrstuvwxyz") : "test 4";
        System.out.println("All tests passed.");
    }
}
