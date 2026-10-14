import java.util.*;

// LC 1021: Remove Outermost Parentheses — depth tracking O(n)
public class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        int depth = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                if (depth > 0) sb.append(ch);
                depth++;
            } else {
                depth--;
                if (depth > 0) sb.append(ch);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.removeOuterParentheses("(()())(())").equals("()()()") : "test 1";
        assert s.removeOuterParentheses("(()())(())(()(()))").equals("()()()()(())") : "test 2";
        assert s.removeOuterParentheses("()()").equals("") : "test 3";
        assert s.removeOuterParentheses("((()))").equals("(())") : "test 4";
        System.out.println("All tests passed.");
    }
}
