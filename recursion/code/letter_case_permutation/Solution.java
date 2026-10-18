import java.util.*;

public class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> result = new ArrayList<>();
        backtrack(s.toCharArray(), 0, result);
        return result;
    }

    private void backtrack(char[] chars, int idx, List<String> result) {
        if (idx == chars.length) {
            result.add(new String(chars));
            return;
        }
        if (Character.isDigit(chars[idx])) {
            backtrack(chars, idx + 1, result);
        } else {
            chars[idx] = Character.toLowerCase(chars[idx]);
            backtrack(chars, idx + 1, result);
            chars[idx] = Character.toUpperCase(chars[idx]);
            backtrack(chars, idx + 1, result);
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        List<String> r1 = sol.letterCasePermutation("a1b2");
        assert r1.size() == 4 : "test failed";
        assert r1.contains("a1b2") && r1.contains("A1b2") && r1.contains("a1B2") && r1.contains("A1B2") : "test failed";
        List<String> r2 = sol.letterCasePermutation("3z4");
        assert r2.size() == 2 : "test failed";
        assert r2.contains("3z4") && r2.contains("3Z4") : "test failed";
        System.out.println("All tests passed.");
    }
}
