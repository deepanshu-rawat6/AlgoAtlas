import java.util.*;

public class Solution {
    public int characterReplacement(String s, int k) {
        int[] freq = new int[26];
        int left = 0, maxFreq = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            maxFreq = Math.max(maxFreq, ++freq[s.charAt(right) - 'A']);
            if (right - left + 1 - maxFreq > k) freq[s.charAt(left++) - 'A']--;
            best = Math.max(best, right - left + 1);
        }
        return best;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.characterReplacement("ABAB", 2) == 4;
        assert sol.characterReplacement("AABABBA", 1) == 4;
        assert sol.characterReplacement("A", 0) == 1;
        System.out.println("All tests passed.");
    }
}
