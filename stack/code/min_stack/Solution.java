import java.util.*;

// Design problem: Solution IS the MinStack.
// Two parallel stacks: main stack and a min-tracking stack.
// minStack top always holds the minimum of all current elements.
// All operations are O(1).
public class Solution {
    private Deque<Integer> stack = new ArrayDeque<>();
    private Deque<Integer> minStack = new ArrayDeque<>();

    public void push(int val) {
        // Push value to main stack; also push new running minimum to minStack
        // O(1)
        stack.push(val);
        int curMin = minStack.isEmpty() ? val : Math.min(val, minStack.peek());
        minStack.push(curMin);
    }

    public void pop() {
        // Pop from both stacks to keep them in sync
        // O(1)
        stack.pop();
        minStack.pop();
    }

    public int top() {
        // Peek top of main stack
        // O(1)
        return stack.peek();
    }

    public int getMin() {
        // Peek top of minStack — always holds current minimum
        // O(1)
        return minStack.peek();
    }

    public static void main(String[] args) {
        Solution ms = new Solution();
        ms.push(-2);
        ms.push(0);
        ms.push(-3);
        assert ms.getMin() == -3 : "getMin 1 failed";
        ms.pop();
        assert ms.top() == 0 : "top failed";
        assert ms.getMin() == -2 : "getMin 2 failed";
        System.out.println("All tests passed.");
    }
}
