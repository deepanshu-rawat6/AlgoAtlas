import java.util.*;

// LC 1781: Sum of Beauty of All Substrings — O(n^2 * 26) brute force
public class Solution {
    public int beautySum(String s) {
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            int[] freq = new int[26];
            for (int j = i; j < s.length(); j++) {
                freq[s.charAt(j) - 'a']++;
                int maxF = 0, minF = Integer.MAX_VALUE;
                for (int f : freq) {
                    if (f > 0) {
                        maxF = Math.max(maxF, f);
                        minF = Math.min(minF, f);
                    }
                }
                total += maxF - minF;
            }
        }
        return total;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.beautySum("aabcb") == 5 : "test 1";
        assert s.beautySum("aabcbaa") == 17 : "test 2";
        assert s.beautySum("a") == 0 : "test 3";
        assert s.beautySum("aa") == 0 : "test 4";
        System.out.println("All tests passed.");
    }
}
