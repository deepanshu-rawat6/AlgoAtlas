import java.util.*;

public class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (k == 0) return 0;
        Map<Character,Integer> count = new HashMap<>();
        int left = 0, result = 0;
        for (int right = 0; right < s.length(); right++) {
            char rc = s.charAt(right);
            count.merge(rc, 1, Integer::sum);
            while (count.size() > k) {
                char lc = s.charAt(left++);
                if (count.merge(lc, -1, Integer::sum) == 0) count.remove(lc);
            }
            result = Math.max(result, right - left + 1);
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.lengthOfLongestSubstringKDistinct("eceba", 2) == 3;
        assert sol.lengthOfLongestSubstringKDistinct("aa", 1) == 2;
        assert sol.lengthOfLongestSubstringKDistinct("aabbcc", 2) == 4;
        System.out.println("All tests passed.");
    }
}
