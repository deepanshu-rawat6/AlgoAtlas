import java.util.*;

public class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        // Sort cars by position descending (closest to target first)
        // Compute arrival time for each car; if it arrives before the car ahead, it joins that fleet
        // A new fleet forms only when a car arrives strictly later than the current top
        // O(n log n) time, O(n) space — sort by position, stack of arrival times
        int n = position.length;
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i][0] = position[i];
            pairs[i][1] = speed[i];
        }
        Arrays.sort(pairs, (a, b) -> b[0] - a[0]);  // sort by position descending
        Deque<Double> stack = new ArrayDeque<>();
        for (int[] pair : pairs) {
            double time = (double)(target - pair[0]) / pair[1];
            if (stack.isEmpty() || time > stack.peek()) {
                stack.push(time);
            }
            // if time <= stack.peek(), this car catches the fleet ahead -> same fleet
        }
        return stack.size();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.carFleet(12, new int[]{10, 8, 0, 5, 3}, new int[]{2, 4, 1, 1, 3}) == 3 : "test 1 failed";
        assert sol.carFleet(10, new int[]{3}, new int[]{3}) == 1 : "test 2 failed";
        assert sol.carFleet(100, new int[]{0, 2, 4}, new int[]{4, 2, 1}) == 1 : "test 3 failed";
        assert sol.carFleet(10, new int[]{6, 8}, new int[]{3, 2}) == 2 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
