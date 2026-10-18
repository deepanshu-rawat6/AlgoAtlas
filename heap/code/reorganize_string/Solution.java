import java.util.*;

public class Solution {
    public String reorganizeString(String s) {
        // Count chars, max-heap by count; place greedily with one-step cooldown
        int[] counts = new int[26];
        for (char c : s.toCharArray()) counts[c - 'a']++;

        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> b[0] - a[0]); // [count, char]
        for (int i = 0; i < 26; i++) {
            if (counts[i] > 0) heap.offer(new int[]{counts[i], i + 'a'});
        }

        StringBuilder sb = new StringBuilder();
        int[] prev = {0, -1}; // previous [count, char] held back for cooldown

        while (!heap.isEmpty()) {
            int[] top = heap.poll();
            sb.append((char) top[1]);
            if (prev[0] > 0) heap.offer(prev);
            prev = new int[]{top[0] - 1, top[1]};
        }

        return sb.length() == s.length() ? sb.toString() : "";
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        assert s.reorganizeString("aab").equals("aba");
        assert s.reorganizeString("aaab").equals("");
        assert s.reorganizeString("a").equals("a");

        String r = s.reorganizeString("vvvlo");
        assert !r.isEmpty();
        for (int i = 0; i < r.length() - 1; i++) assert r.charAt(i) != r.charAt(i+1);

        System.out.println("All tests passed.");
    }
}
