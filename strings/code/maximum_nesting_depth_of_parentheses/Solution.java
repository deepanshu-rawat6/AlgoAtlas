import java.util.*;

// LC 1614: Maximum Nesting Depth of Parentheses — track depth O(n)
public class Solution {
    public int maxDepth(String s) {
        int depth = 0, max = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '(') max = Math.max(max, ++depth);
            else if (ch == ')') depth--;
        }
        return max;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.maxDepth("(1+(2*3)+((8)/4))+1") == 3 : "test 1";
        assert s.maxDepth("(1)+((2))+(((3)))") == 3 : "test 2";
        assert s.maxDepth("1+(2*3)/(2-1)") == 1 : "test 3";
        assert s.maxDepth("1") == 0 : "test 4";
        assert s.maxDepth("()") == 1 : "test 5";
        System.out.println("All tests passed.");
    }
}
