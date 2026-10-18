import java.util.*;

public class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        // Sort projects by capital; max-heap for available profits
        int n = profits.length;
        int[][] projects = new int[n][2];
        for (int i = 0; i < n; i++) {
            projects[i][0] = capital[i];
            projects[i][1] = profits[i];
        }
        Arrays.sort(projects, (a, b) -> a[0] - b[0]);

        PriorityQueue<Integer> available = new PriorityQueue<>(Collections.reverseOrder());
        int i = 0;
        for (int round = 0; round < k; round++) {
            while (i < n && projects[i][0] <= w) {
                available.offer(projects[i][1]);
                i++;
            }
            if (available.isEmpty()) break;
            w += available.poll();
        }
        return w;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.findMaximizedCapital(2, 0, new int[]{1,2,3}, new int[]{0,1,1}) == 4;
        assert s.findMaximizedCapital(3, 0, new int[]{1,2,3}, new int[]{0,1,2}) == 6;
        assert s.findMaximizedCapital(1, 0, new int[]{1,2,3}, new int[]{1,1,2}) == 0;
        assert s.findMaximizedCapital(2, 1, new int[]{1,2,3}, new int[]{1,1,2}) == 6;
        System.out.println("All tests passed.");
    }
}
