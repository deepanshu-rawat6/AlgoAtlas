import java.util.*;

// Count substrings with exactly k distinct chars — exactly(k) = atMost(k) - atMost(k-1)
public class Solution {
    private int atMost(String s, int k) {
        int count = 0, left = 0;
        Map<Character, Integer> freq = new HashMap<>();
        for (int right = 0; right < s.length(); right++) {
            freq.merge(s.charAt(right), 1, Integer::sum);
            while (freq.size() > k) {
                char lc = s.charAt(left++);
                if (freq.merge(lc, -1, Integer::sum) == 0) freq.remove(lc);
            }
            count += right - left + 1;
        }
        return count;
    }

    public int countSubstrings(String s, int k) {
        return atMost(s, k) - atMost(s, k - 1);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.countSubstrings("aba", 2) == 3 : "test 1";
        assert s.countSubstrings("aaa", 1) == 6 : "test 2";
        assert s.countSubstrings("abc", 1) == 3 : "test 3";
        assert s.countSubstrings("abc", 2) == 2 : "test 4";
        assert s.countSubstrings("abc", 3) == 1 : "test 5";
        System.out.println("All tests passed.");
    }
}
