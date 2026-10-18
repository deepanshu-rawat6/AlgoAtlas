import java.util.*;

public class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), s, 0);
        return result;
    }

    private void backtrack(List<List<String>> result, List<String> current, String s, int start) {
        if (start == s.length()) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (int end = start + 1; end <= s.length(); end++) {
            String sub = s.substring(start, end);
            if (isPalindrome(sub)) {
                current.add(sub);
                backtrack(result, current, s, end);
                current.remove(current.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--)) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<List<String>> r = sol.partition("aab");
        assert r.size() == 2 : "size wrong: " + r.size();
        assert r.contains(Arrays.asList("a", "a", "b"));
        assert r.contains(Arrays.asList("aa", "b"));

        List<List<String>> r2 = sol.partition("a");
        assert r2.equals(Collections.singletonList(Collections.singletonList("a")));

        System.out.println("All tests passed.");
    }
}
