import java.util.*;

public class Solution {
    public String longestDiverseString(int a, int b, int c) {
        // Max-heap by count; greedily pick most frequent char, avoiding 3 in a row
        PriorityQueue<int[]> heap = new PriorityQueue<>((x, y) -> y[0] - x[0]); // [count, char]
        if (a > 0) heap.offer(new int[]{a, 'a'});
        if (b > 0) heap.offer(new int[]{b, 'b'});
        if (c > 0) heap.offer(new int[]{c, 'c'});

        StringBuilder sb = new StringBuilder();
        while (!heap.isEmpty()) {
            int[] top = heap.poll();
            int n = sb.length();
            // If last two chars are same as top, use second most frequent
            if (n >= 2 && sb.charAt(n-1) == top[1] && sb.charAt(n-2) == top[1]) {
                if (heap.isEmpty()) break;
                int[] second = heap.poll();
                sb.append((char) second[1]);
                if (second[0] > 1) heap.offer(new int[]{second[0] - 1, second[1]});
                heap.offer(top);
            } else {
                sb.append((char) top[1]);
                if (top[0] > 1) heap.offer(new int[]{top[0] - 1, top[1]});
            }
        }
        return sb.toString();
    }

    private static boolean isHappy(String res, int a, int b, int c) {
        if (res.contains("aaa") || res.contains("bbb") || res.contains("ccc")) return false;
        long ca = res.chars().filter(ch -> ch == 'a').count();
        long cb = res.chars().filter(ch -> ch == 'b').count();
        long cc = res.chars().filter(ch -> ch == 'c').count();
        return ca <= a && cb <= b && cc <= c;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        String r1 = s.longestDiverseString(1, 1, 7);
        assert isHappy(r1, 1, 1, 7) && r1.length() == 8 : "Got: " + r1;

        String r2 = s.longestDiverseString(7, 1, 0);
        assert isHappy(r2, 7, 1, 0) && r2.length() == 5 : "Got: " + r2;

        String r3 = s.longestDiverseString(2, 2, 1);
        assert isHappy(r3, 2, 2, 1) && r3.length() == 5 : "Got: " + r3;

        String r4 = s.longestDiverseString(0, 0, 1);
        assert r4.equals("c") : "Got: " + r4;

        System.out.println("All tests passed.");
    }
}
