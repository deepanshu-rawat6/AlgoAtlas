import java.util.*;

public class Solution {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, (a, b) -> a[0] - b[0]);
        PriorityQueue<Integer> available = new PriorityQueue<>();
        for (int i = 0; i < n; i++) available.offer(i);
        // min-heap by (endTime, roomIndex)
        PriorityQueue<long[]> ongoing = new PriorityQueue<>((a, b) -> a[0] != b[0] ? Long.compare(a[0], b[0]) : Long.compare(a[1], b[1]));
        int[] count = new int[n];

        for (int[] meeting : meetings) {
            long start = meeting[0], end = meeting[1];
            while (!ongoing.isEmpty() && ongoing.peek()[0] <= start) {
                available.offer((int) ongoing.poll()[1]);
            }
            int room;
            if (!available.isEmpty()) {
                room = available.poll();
                ongoing.offer(new long[]{end, room});
            } else {
                long[] earliest = ongoing.poll();
                room = (int) earliest[1];
                ongoing.offer(new long[]{earliest[0] + (end - start), room});
            }
            count[room]++;
        }

        int best = 0;
        for (int i = 1; i < n; i++) if (count[i] > count[best]) best = i;
        return best;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.mostBooked(2, new int[][]{{0,10},{1,5},{2,7},{3,4}}) == 0 : "test 1 failed";
        assert sol.mostBooked(3, new int[][]{{1,20},{2,10},{3,5},{4,9},{6,8}}) == 1 : "test 2 failed";
        assert sol.mostBooked(1, new int[][]{{0,1},{1,2},{2,3}}) == 0 : "test 3 failed";
        System.out.println("All tests passed.");
    }
}
