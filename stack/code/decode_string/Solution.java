import java.util.*;

public class Solution {
    public String decodeString(String s) {
        // On '[': save current (count, string) to stacks, reset both
        // On ']': pop saved state, append current string repeated count times
        // Handles nested brackets because each level is saved/restored on stack
        // O(n) time, O(n) space — iterative stack of (repeat_count, built_string)
        Deque<Integer> countStack = new ArrayDeque<>();
        Deque<String> strStack = new ArrayDeque<>();
        String curStr = "";
        int curNum = 0;
        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch)) {
                curNum = curNum * 10 + (ch - '0');
            } else if (ch == '[') {
                countStack.push(curNum);
                strStack.push(curStr);
                curStr = "";
                curNum = 0;
            } else if (ch == ']') {
                int num = countStack.pop();
                String prev = strStack.pop();
                StringBuilder sb = new StringBuilder(prev);
                for (int i = 0; i < num; i++) sb.append(curStr);
                curStr = sb.toString();
            } else {
                curStr += ch;
            }
        }
        return curStr;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.decodeString("3[a]2[bc]").equals("aaabcbc") : "test 1 failed";
        assert sol.decodeString("3[a2[c]]").equals("accaccacc") : "test 2 failed";
        assert sol.decodeString("2[abc]3[cd]ef").equals("abcabccdcdcdef") : "test 3 failed";
        System.out.println("All tests passed.");
    }
}
