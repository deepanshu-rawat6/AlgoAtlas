import java.util.*;

// Minimum Bracket Reversals — stack to cancel pairs, then ceil(close/2)+ceil(open/2)
public class Solution {
    public int countRev(String s) {
        if (s.length() % 2 != 0) return -1;
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch == '{') {
                stack.push(ch);
            } else {
                if (!stack.isEmpty() && stack.peek() == '{') stack.pop();
                else stack.push(ch);
            }
        }
        int close = 0, open = 0;
        for (char c : stack) {
            if (c == '}') close++;
            else open++;
        }
        return (close + 1) / 2 + (open + 1) / 2;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.countRev("}{") == 2 : "test 1";
        assert s.countRev("{{}}") == 0 : "test 2";
        assert s.countRev("{{{") == -1 : "test 3";
        assert s.countRev("}}{{") == 2 : "test 4";
        assert s.countRev("}{{}}{") == 2 : "test 5";
        System.out.println("All tests passed.");
    }
}
