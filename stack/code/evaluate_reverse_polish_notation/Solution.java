import java.util.*;

public class Solution {
    public int evalRPN(String[] tokens) {
        // Push numbers; on operator, pop two operands and push result
        // Java integer division already truncates toward zero (no special handling needed)
        // O(n) time, O(n) space — single stack evaluation
        Deque<Integer> stack = new ArrayDeque<>();
        for (String t : tokens) {
            if (t.equals("+") || t.equals("-") || t.equals("*") || t.equals("/")) {
                int b = stack.pop();
                int a = stack.pop();
                int result;
                switch (t) {
                    case "+":  result = a + b; break;
                    case "-":  result = a - b; break;
                    case "*":  result = a * b; break;
                    default:   result = a / b; break;  // Java int division truncates toward zero
                }
                stack.push(result);
            } else {
                stack.push(Integer.parseInt(t));
            }
        }
        return stack.peek();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.evalRPN(new String[]{"2", "1", "+", "3", "*"}) == 9 : "test 1 failed";
        assert sol.evalRPN(new String[]{"4", "13", "5", "/", "+"}) == 6 : "test 2 failed";
        assert sol.evalRPN(new String[]{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}) == 22 : "test 3 failed";
        assert sol.evalRPN(new String[]{"3", "-4", "/"}) == 0 : "test 4 failed";  // -0.75 truncates toward zero -> 0
        System.out.println("All tests passed.");
    }
}
