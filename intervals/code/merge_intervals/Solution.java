import java.util.*;

public class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int[]> result = new ArrayList<>();
        result.add(intervals[0]);
        for (int i = 1; i < intervals.length; i++) {
            int[] last = result.get(result.size() - 1);
            if (intervals[i][0] <= last[1]) {
                last[1] = Math.max(last[1], intervals[i][1]);
            } else {
                result.add(intervals[i]);
            }
        }
        return result.toArray(new int[0][]);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Arrays.deepEquals(sol.merge(new int[][]{{1,3},{2,6},{8,10},{15,18}}), new int[][]{{1,6},{8,10},{15,18}}) : "test 1 failed";
        assert Arrays.deepEquals(sol.merge(new int[][]{{1,4},{4,5}}), new int[][]{{1,5}}) : "test 2 failed";
        assert Arrays.deepEquals(sol.merge(new int[][]{{1,4},{0,4}}), new int[][]{{0,4}}) : "test 3 failed";
        assert Arrays.deepEquals(sol.merge(new int[][]{{1,4},{2,3}}), new int[][]{{1,4}}) : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
