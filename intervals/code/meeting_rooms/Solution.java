import java.util.*;

public class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < intervals[i-1][1]) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert !sol.canAttendMeetings(new int[][]{{0,30},{5,10},{15,20}}) : "test 1 failed";
        assert sol.canAttendMeetings(new int[][]{{7,10},{2,4}}) : "test 2 failed";
        assert sol.canAttendMeetings(new int[][]{}) : "test 3 failed";
        assert sol.canAttendMeetings(new int[][]{{1,5},{5,10}}) : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
