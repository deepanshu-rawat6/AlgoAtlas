import java.util.*;

public class Solution {
    public List<Integer> partitionLabels(String s) {
        int[] last = new int[26];
        for (int i = 0; i < s.length(); i++) {
            last[s.charAt(i) - 'a'] = i;
        }
        List<Integer> result = new ArrayList<>();
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            end = Math.max(end, last[s.charAt(i) - 'a']);
            if (i == end) {
                result.add(end - start + 1);
                start = i + 1;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.partitionLabels("ababcbacadefegdehijhklij").equals(Arrays.asList(9, 7, 8));
        assert sol.partitionLabels("eccbbbbdec").equals(Arrays.asList(10));
        assert sol.partitionLabels("a").equals(Arrays.asList(1));
        assert sol.partitionLabels("ab").equals(Arrays.asList(1, 1));
        System.out.println("All tests passed.");
    }
}
