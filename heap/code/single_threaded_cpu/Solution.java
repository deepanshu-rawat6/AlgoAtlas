import java.util.*;

public class Solution {
    public int[] getOrder(int[][] tasks) {
        // Sort by enqueue time; min-heap of (processingTime, originalIndex) for available tasks
        int n = tasks.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, (a, b) -> tasks[a][0] != tasks[b][0] ? tasks[a][0] - tasks[b][0] : a - b);

        // min-heap: [processingTime, originalIndex]
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

        int[] result = new int[n];
        long time = 0;
        int i = 0, ri = 0;

        while (ri < n) {
            // Enqueue all tasks available at current time
            while (i < n && tasks[order[i]][0] <= time) {
                heap.offer(new int[]{tasks[order[i]][1], order[i]});
                i++;
            }
            if (heap.isEmpty()) {
                // CPU idle: jump to next task's enqueue time
                time = tasks[order[i]][0];
            } else {
                int[] top = heap.poll();
                result[ri++] = top[1];
                time += top[0];
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert Arrays.equals(s.getOrder(new int[][]{{1,2},{2,4},{3,2},{4,1}}), new int[]{0,2,3,1});
        assert Arrays.equals(s.getOrder(new int[][]{{7,10},{7,12},{7,5},{7,4},{7,2}}), new int[]{4,3,2,0,1});
        assert Arrays.equals(s.getOrder(new int[][]{{1,1},{1,1}}), new int[]{0,1});
        System.out.println("All tests passed.");
    }
}
