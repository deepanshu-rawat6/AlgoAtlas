import java.util.*;

// Z-Function pattern matching — O(n+m) via Z-array
public class Solution {
    public int[] zFunction(String s) {
        int n = s.length();
        int[] z = new int[n];
        int l = 0, r = 0;
        for (int i = 1; i < n; i++) {
            if (i < r) z[i] = Math.min(z[i - l], r - i);
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) z[i]++;
            if (i + z[i] > r) { l = i; r = i + z[i]; }
        }
        return z;
    }

    public List<Integer> patternSearch(String text, String pattern) {
        int m = pattern.length();
        String combined = pattern + "#" + text;
        int[] z = zFunction(combined);
        List<Integer> result = new ArrayList<>();
        for (int i = m + 1; i < combined.length(); i++)
            if (z[i] == m) result.add(i - m - 1);
        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert Arrays.equals(s.zFunction("aabxaa"), new int[]{0,1,0,0,2,1}) : "z 1";
        assert Arrays.equals(s.zFunction("aaaa"), new int[]{0,3,2,1}) : "z 2";
        assert Arrays.equals(s.zFunction("abcabc"), new int[]{0,0,0,3,0,0}) : "z 3";
        assert s.patternSearch("aabxaa", "aa").equals(Arrays.asList(0, 4)) : "search 1";
        assert s.patternSearch("AABAACAADAABAABA", "AABA").equals(Arrays.asList(0, 9, 12)) : "search 2";
        System.out.println("All tests passed.");
    }
}
