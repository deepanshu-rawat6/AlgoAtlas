import java.util.*;

public class Solution {
    public int calPoints(String[] operations) {
        // Simulate the record: C removes last, D doubles last, + sums last two
        // O(n) time, O(n) space — stack as mutable record
        Deque<Integer> stack = new ArrayDeque<>();
        for (String op : operations) {
            if (op.equals("C")) {
                stack.pop();
            } else if (op.equals("D")) {
                stack.push(stack.peek() * 2);
            } else if (op.equals("+")) {
                int top = stack.pop();
                int second = stack.peek();
                stack.push(top);
                stack.push(top + second);
            } else {
                stack.push(Integer.parseInt(op));
            }
        }
        int sum = 0;
        for (int v : stack) sum += v;
        return sum;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.calPoints(new String[]{"5", "2", "C", "D", "+"}) == 30 : "test 1 failed";
        assert sol.calPoints(new String[]{"5", "-2", "4", "C", "D", "9", "+", "+"}) == 27 : "test 2 failed";
        assert sol.calPoints(new String[]{"1"}) == 1 : "test 3 failed";
        System.out.println("All tests passed.");
    }
}
