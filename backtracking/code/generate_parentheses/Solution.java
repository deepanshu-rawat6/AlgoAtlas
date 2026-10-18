import java.util.*;

public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, "", 0, 0, n);
        return result;
    }

    private void backtrack(List<String> result, String current, int open, int close, int n) {
        if (current.length() == 2 * n) {
            result.add(current);
            return;
        }
        if (open < n) backtrack(result, current + '(', open + 1, close, n);
        if (close < open) backtrack(result, current + ')', open, close + 1, n);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<String> r3 = sol.generateParenthesis(3);
        assert r3.size() == 5 : "size wrong: " + r3.size();
        assert r3.contains("((()))");
        assert r3.contains("()()()");

        List<String> r1 = sol.generateParenthesis(1);
        assert r1.equals(Collections.singletonList("()"));

        System.out.println("All tests passed.");
    }
}
