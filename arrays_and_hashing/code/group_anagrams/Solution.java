// LC 49: Group Anagrams
// Group strings that are anagrams of each other.
// Time: O(n * k * log k), Space: O(n * k)
import java.util.*;

public class Solution {
    // Brute: O(n^2 * k * log k) — compare each pair
    public List<List<String>> groupAnagramsBrute(String[] strs) {
        int n = strs.length;
        boolean[] used = new boolean[n];
        List<List<String>> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (used[i]) continue;
            List<String> group = new ArrayList<>();
            group.add(strs[i]);
            char[] ci = strs[i].toCharArray(); Arrays.sort(ci);
            for (int j = i + 1; j < n; j++) {
                if (used[j]) continue;
                char[] cj = strs[j].toCharArray(); Arrays.sort(cj);
                if (Arrays.equals(ci, cj)) { group.add(strs[j]); used[j] = true; }
            }
            res.add(group);
        }
        return res;
    }

    // Optimal: sort each word as key — O(n * k * log k)
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> mp = new HashMap<>();
        for (String w : strs) {
            char[] c = w.toCharArray();
            Arrays.sort(c);
            String key = new String(c);
            mp.computeIfAbsent(key, k -> new ArrayList<>()).add(w);
        }
        return new ArrayList<>(mp.values());
    }

    private static List<List<String>> normalize(List<List<String>> groups) {
        for (List<String> g : groups) Collections.sort(g);
        groups.sort(Comparator.comparing(g -> g.get(0)));
        return groups;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        List<List<String>> res1 = normalize(s.groupAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"}));
        assert res1.get(0).equals(Arrays.asList("ate","eat","tea")) : "Test 1a failed";
        assert res1.get(1).equals(Arrays.asList("bat")) : "Test 1b failed";
        assert res1.get(2).equals(Arrays.asList("nat","tan")) : "Test 1c failed";

        List<List<String>> res2 = s.groupAnagrams(new String[]{""});
        assert res2.size() == 1 && res2.get(0).equals(Arrays.asList("")) : "Test 2 failed";

        List<List<String>> res3 = s.groupAnagrams(new String[]{"a"});
        assert res3.size() == 1 && res3.get(0).equals(Arrays.asList("a")) : "Test 3 failed";

        System.out.println("All tests passed.");
    }
}
