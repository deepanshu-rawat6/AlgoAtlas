import java.util.*;

public class Solution {
    public List<Integer> reverseStack(List<Integer> stack) {
        if (stack.size() <= 1) return stack;
        int top = stack.remove(stack.size() - 1);
        reverseStack(stack);
        insertAtBottom(stack, top);
        return stack;
    }

    private void insertAtBottom(List<Integer> stack, int val) {
        if (stack.isEmpty()) { stack.add(val); return; }
        int top = stack.remove(stack.size() - 1);
        insertAtBottom(stack, val);
        stack.add(top);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.reverseStack(new ArrayList<>(Arrays.asList(1, 2, 3))).equals(Arrays.asList(3, 2, 1)) : "test failed";
        assert sol.reverseStack(new ArrayList<>(Arrays.asList(1))).equals(Arrays.asList(1)) : "test failed";
        assert sol.reverseStack(new ArrayList<>()).equals(new ArrayList<>()) : "test failed";
        assert sol.reverseStack(new ArrayList<>(Arrays.asList(4, 3, 2, 1))).equals(Arrays.asList(1, 2, 3, 4)) : "test failed";
        System.out.println("All tests passed.");
    }
}
