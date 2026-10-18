import java.util.*;

public class Solution {
    public List<Integer> sortStack(List<Integer> stack) {
        if (stack.isEmpty()) return stack;
        int top = stack.remove(stack.size() - 1);
        sortStack(stack);
        insertSorted(stack, top);
        return stack;
    }

    private void insertSorted(List<Integer> stack, int val) {
        if (stack.isEmpty() || stack.get(stack.size() - 1) <= val) {
            stack.add(val);
            return;
        }
        int top = stack.remove(stack.size() - 1);
        insertSorted(stack, val);
        stack.add(top);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.sortStack(new ArrayList<>(Arrays.asList(3, 1, 2))).equals(Arrays.asList(1, 2, 3)) : "test failed";
        assert sol.sortStack(new ArrayList<>(Arrays.asList(5, 1, 4, 2, 3))).equals(Arrays.asList(1, 2, 3, 4, 5)) : "test failed";
        assert sol.sortStack(new ArrayList<>()).equals(new ArrayList<>()) : "test failed";
        assert sol.sortStack(new ArrayList<>(Arrays.asList(1))).equals(Arrays.asList(1)) : "test failed";
        System.out.println("All tests passed.");
    }
}
