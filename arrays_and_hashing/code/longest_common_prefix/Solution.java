import java.util.*;

// LC 14: Longest Common Prefix
public class Solution {
    public String longestCommonPrefixVertical(String[] strs) {
        // Check each char position across all strings — O(S) time, O(1) space
        if (strs.length == 0) return "";
        for (int i = 0; i < strs[0].length(); i++) {
            char ch = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (i >= strs[j].length() || strs[j].charAt(i) != ch)
                    return strs[0].substring(0, i);
            }
        }
        return strs[0];
    }

    public String longestCommonPrefix(String[] strs) {
        // Sort: only compare first and last — O(n log n * m) time, O(1) space
        Arrays.sort(strs);
        String first = strs[0], last = strs[strs.length - 1];
        int i = 0;
        while (i < first.length() && i < last.length() && first.charAt(i) == last.charAt(i)) i++;
        return first.substring(0, i);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.longestCommonPrefix(new String[]{"flower","flow","flight"}).equals("fl") : "test 1";
        assert s.longestCommonPrefix(new String[]{"dog","racecar","car"}).equals("") : "test 2";
        assert s.longestCommonPrefix(new String[]{"interview","interact","interface"}).equals("inter") : "test 3";
        System.out.println("All tests passed.");
    }
}
