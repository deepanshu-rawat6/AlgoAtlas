import java.util.*;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character,Integer> charIdx = new HashMap<>();
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            Integer prev = charIdx.get(ch);
            if (prev != null && prev >= left) left = prev + 1;
            charIdx.put(ch, right);
            best = Math.max(best, right - left + 1);
        }
        return best;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.lengthOfLongestSubstring("abcabcbb") == 3;
        assert sol.lengthOfLongestSubstring("bbbbb") == 1;
        assert sol.lengthOfLongestSubstring("pwwkew") == 3;
        System.out.println("All tests passed.");
    }
}
