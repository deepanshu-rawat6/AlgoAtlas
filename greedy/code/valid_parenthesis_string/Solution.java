import java.util.*;

public class Solution {
    public boolean checkValidString(String s) {
        int lo = 0, hi = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                lo++;
                hi++;
            } else if (c == ')') {
                lo--;
                hi--;
            } else { // '*'
                lo--;
                hi++;
            }
            if (hi < 0) return false;
            lo = Math.max(lo, 0);
        }
        return lo == 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.checkValidString("(*)") == true;
        assert sol.checkValidString("(*))") == true;
        assert sol.checkValidString("(*()") == true;
        assert sol.checkValidString(")(") == false;
        System.out.println("All tests passed.");
    }
}
