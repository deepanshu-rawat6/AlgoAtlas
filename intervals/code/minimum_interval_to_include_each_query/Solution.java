import java.util.*;

public class Solution {
    public int[] minInterval(int[][] intervals, int[] queries) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        int q = queries.length;
        Integer[] order = new Integer[q];
        for (int i = 0; i < q; i++) order[i] = i;
        Arrays.sort(order, (a, b) -> queries[a] - queries[b]);

        int[] result = new int[q];
        // min-heap by (size, end)
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int i = 0;

        for (int idx : order) {
            int qv = queries[idx];
            while (i < intervals.length && intervals[i][0] <= qv) {
                int size = intervals[i][1] - intervals[i][0] + 1;
                heap.offer(new int[]{size, intervals[i][1]});
                i++;
            }
            while (!heap.isEmpty() && heap.peek()[1] < qv) heap.poll();
            result[idx] = heap.isEmpty() ? -1 : heap.peek()[0];
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Arrays.equals(sol.minInterval(new int[][]{{1,4},{2,4},{3,6},{4,4}}, new int[]{2,3,4,5}), new int[]{3,3,1,4}) : "test 1 failed";
        assert Arrays.equals(sol.minInterval(new int[][]{{2,3},{2,5},{1,8},{20,25}}, new int[]{2,19,5,22}), new int[]{2,-1,4,6}) : "test 2 failed";
        System.out.println("All tests passed.");
    }
}
