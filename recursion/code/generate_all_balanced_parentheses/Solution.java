import java.util.*;

public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        recurse("", 0, 0, n, result);
        return result;
    }

    private void recurse(String current, int open, int close, int n, List<String> result) {
        if (current.length() == 2 * n) {
            result.add(current);
            return;
        }
        if (open < n) recurse(current + "(", open + 1, close, n, result);
        if (close < open) recurse(current + ")", open, close + 1, n, result);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        List<String> r = sol.generateParenthesis(3);
        assert r.size() == 5 : "test failed";
        assert !r.contains("(((())))") : "test failed";
        assert r.contains("((()))") : "test failed";
        assert r.contains("(()())") : "test failed";
        List<String> r1 = sol.generateParenthesis(1);
        assert r1.size() == 1 && r1.get(0).equals("()") : "test failed";
        System.out.println("All tests passed.");
    }
}
