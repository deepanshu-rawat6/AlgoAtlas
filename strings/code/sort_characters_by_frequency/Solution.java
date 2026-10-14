import java.util.*;

// LC 451: Sort Characters By Frequency — bucket sort O(n)
public class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) freq.merge(c, 1, Integer::sum);
        // bucket sort: index = frequency
        @SuppressWarnings("unchecked")
        List<Character>[] buckets = new List[s.length() + 1];
        for (var e : freq.entrySet()) {
            int cnt = e.getValue();
            if (buckets[cnt] == null) buckets[cnt] = new ArrayList<>();
            buckets[cnt].add(e.getKey());
        }
        StringBuilder sb = new StringBuilder();
        for (int i = s.length(); i >= 1; i--)
            if (buckets[i] != null)
                for (char c : buckets[i])
                    sb.append(String.valueOf(c).repeat(i));
        return sb.toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String res = s.frequencySort("tree");
        assert res.charAt(0) == 'e' && res.charAt(1) == 'e' && res.contains("r") && res.contains("t") : "test 1";
        assert s.frequencySort("cccaaa").equals("cccaaa") || s.frequencySort("cccaaa").equals("aaaccc") : "test 2";
        // "Aabb" → "bbAa" or "bbaA"
        String r3 = s.frequencySort("Aabb");
        assert r3.charAt(0) == 'b' && r3.charAt(1) == 'b' : "test 3";
        System.out.println("All tests passed.");
    }
}
