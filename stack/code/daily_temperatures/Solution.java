import java.util.*;

public class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        // Monotonic decreasing stack stores indices of unresolved days
        // When a warmer day arrives, resolve all cooler days on the stack
        // O(n) time, O(n) space — decreasing monotonic stack of indices
        int n = temperatures.length;
        int[] answer = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();  // stores indices with unresolved warmer day
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int idx = stack.pop();
                answer[idx] = i - idx;
            }
            stack.push(i);
        }
        return answer;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert Arrays.equals(
            sol.dailyTemperatures(new int[]{73, 74, 75, 71, 69, 72, 76, 73}),
            new int[]{1, 1, 4, 2, 1, 1, 0, 0}) : "test 1 failed";
        assert Arrays.equals(
            sol.dailyTemperatures(new int[]{30, 40, 50, 60}),
            new int[]{1, 1, 1, 0}) : "test 2 failed";
        assert Arrays.equals(
            sol.dailyTemperatures(new int[]{30, 60, 90}),
            new int[]{1, 1, 0}) : "test 3 failed";
        System.out.println("All tests passed.");
    }
}
