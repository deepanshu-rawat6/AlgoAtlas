import java.util.*;

public class Solution {
    public int largestRectangleArea(int[] heights) {
        // Monotonic increasing stack: when a shorter bar is found, pop taller bars
        // Each popped bar's rectangle extends from its stored start index to current i
        // 'start' tracks how far left the current bar can extend
        // O(n) time, O(n) space — increasing monotonic stack of {start, height} pairs
        Deque<int[]> stack = new ArrayDeque<>();  // each element: {start_index, height}
        int maxArea = 0;
        int n = heights.length;
        for (int i = 0; i < n; i++) {
            int h = heights[i];
            int start = i;
            while (!stack.isEmpty() && stack.peek()[1] > h) {
                int[] top = stack.pop();
                maxArea = Math.max(maxArea, top[1] * (i - top[0]));
                start = top[0];  // current bar can extend as far left as the popped bar
            }
            stack.push(new int[]{start, h});
        }
        // Process remaining bars — they extend to the end of the histogram
        while (!stack.isEmpty()) {
            int[] top = stack.pop();
            maxArea = Math.max(maxArea, top[1] * (n - top[0]));
        }
        return maxArea;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.largestRectangleArea(new int[]{2, 1, 5, 6, 2, 3}) == 10 : "test 1 failed";
        assert sol.largestRectangleArea(new int[]{2, 4}) == 4 : "test 2 failed";
        assert sol.largestRectangleArea(new int[]{1}) == 1 : "test 3 failed";
        assert sol.largestRectangleArea(new int[]{6, 2, 5, 4, 5, 1, 6}) == 12 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
