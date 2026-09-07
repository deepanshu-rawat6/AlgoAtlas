import java.util.*;

public class Solution {
    public String minWindow(String s, String t) {
        if (t.isEmpty()) return "";
        Map<Character,Integer> need = new HashMap<>(), have = new HashMap<>();
        for (char c : t.toCharArray()) need.merge(c, 1, Integer::sum);
        int formed = 0, required = need.size();
        int left = 0, bestLen = Integer.MAX_VALUE, bestL = 0;
        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            have.merge(ch, 1, Integer::sum);
            if (need.containsKey(ch) && have.get(ch).equals(need.get(ch))) formed++;
            while (formed == required) {
                if (right - left + 1 < bestLen) { bestLen = right - left + 1; bestL = left; }
                char lch = s.charAt(left);
                have.merge(lch, -1, Integer::sum);
                if (need.containsKey(lch) && have.get(lch) < need.get(lch)) formed--;
                left++;
            }
        }
        return bestLen == Integer.MAX_VALUE ? "" : s.substring(bestL, bestL + bestLen);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.minWindow("ADOBECODEBANC", "ABC").equals("BANC");
        assert sol.minWindow("a", "a").equals("a");
        assert sol.minWindow("a", "aa").equals("");
        System.out.println("All tests passed.");
    }
}
