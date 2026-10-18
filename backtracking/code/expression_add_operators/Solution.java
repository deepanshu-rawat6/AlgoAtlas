import java.util.*;

public class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> result = new ArrayList<>();
        backtrack(result, num, target, 0, "", 0, 0);
        return result;
    }

    private void backtrack(List<String> result, String num, int target,
                           int idx, String expr, long total, long prev) {
        if (idx == num.length()) {
            if (total == target) result.add(expr);
            return;
        }
        for (int i = idx; i < num.length(); i++) {
            // No leading zeros (except "0" itself)
            if (i > idx && num.charAt(idx) == '0') break;
            String currStr = num.substring(idx, i + 1);
            long currVal = Long.parseLong(currStr);
            if (idx == 0) {
                backtrack(result, num, target, i + 1, currStr, currVal, currVal);
            } else {
                backtrack(result, num, target, i + 1, expr + '+' + currStr,
                          total + currVal, currVal);
                backtrack(result, num, target, i + 1, expr + '-' + currStr,
                          total - currVal, -currVal);
                backtrack(result, num, target, i + 1, expr + '*' + currStr,
                          total - prev + prev * currVal, prev * currVal);
            }
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<String> r1 = sol.addOperators("123", 6);
        assert r1.contains("1+2+3") : "missing 1+2+3";
        assert r1.contains("1*2*3") : "missing 1*2*3";

        List<String> r2 = sol.addOperators("232", 8);
        assert r2.size() == 2 : "size wrong: " + r2.size();

        assert sol.addOperators("3456237490", 9191).isEmpty() : "should be empty";

        System.out.println("All tests passed.");
    }
}
