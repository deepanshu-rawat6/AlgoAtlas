import java.util.*;

// LC 151: Reverse Words in a String — split + join O(n)
public class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            if (sb.length() > 0) sb.append(' ');
            sb.append(words[i]);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.reverseWords("  hello world  ").equals("world hello") : "test 1";
        assert s.reverseWords("a good   example").equals("example good a") : "test 2";
        assert s.reverseWords("  Bob    Loves  Alice   ").equals("Alice Loves Bob") : "test 3";
        System.out.println("All tests passed.");
    }
}
