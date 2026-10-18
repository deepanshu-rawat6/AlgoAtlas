import java.util.*;

public class Solution {
    public String simplifyPath(String path) {
        // Split on '/' to get path components; skip empty strings and '.'
        // '..' pops the last directory from stack (go up one level)
        // Join remaining stack with '/' and prepend root '/'
        // O(n) time, O(n) space — split on '/', process with stack
        Deque<String> stack = new ArrayDeque<>();
        for (String part : path.split("/")) {
            if (part.equals("..")) {
                if (!stack.isEmpty()) stack.pop();
            } else if (!part.isEmpty() && !part.equals(".")) {
                stack.push(part);
            }
        }
        // stack.push() adds to HEAD (top); descendingIterator goes TAIL->HEAD = bottom->top = insertion order
        List<String> parts = new ArrayList<>();
        Iterator<String> iter = stack.descendingIterator();
        while (iter.hasNext()) parts.add(iter.next());
        return "/" + String.join("/", parts);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.simplifyPath("/home/").equals("/home") : "test 1 failed";
        assert sol.simplifyPath("/../").equals("/") : "test 2 failed";
        assert sol.simplifyPath("/home//foo/").equals("/home/foo") : "test 3 failed";
        assert sol.simplifyPath("/a/./b/../../c/").equals("/c") : "test 4 failed";
        assert sol.simplifyPath("/").equals("/") : "test 5 failed";
        System.out.println("All tests passed.");
    }
}
