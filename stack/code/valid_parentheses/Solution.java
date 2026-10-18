import java.util.*;

public class Solution {
    public boolean isValid(String s) {
        // Push opening brackets; on closing bracket, check top matches
        // Stack empty at end means all brackets were properly closed
        // O(n) time, O(n) space — stack-based bracket matching
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> match = new HashMap<>();
        match.put(')', '(');
        match.put('}', '{');
        match.put(']', '[');
        for (char ch : s.toCharArray()) {
            if (match.containsKey(ch)) {
                if (stack.isEmpty() || !stack.peek().equals(match.get(ch))) return false;
                stack.pop();
            } else {
                stack.push(ch);
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.isValid("()") : "test 1 failed";
        assert sol.isValid("()[]{}") : "test 2 failed";
        assert !sol.isValid("(]") : "test 3 failed";
        assert !sol.isValid("([)]") : "test 4 failed";
        assert sol.isValid("{[]}") : "test 5 failed";
        assert sol.isValid("") : "test 6 failed";
        System.out.println("All tests passed.");
    }
}
