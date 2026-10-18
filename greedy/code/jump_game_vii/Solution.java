import java.util.*;

public class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        int n = s.length();
        boolean[] reach = new boolean[n];
        reach[0] = true;
        int prefix = 0;
        for (int i = 1; i < n; i++) {
            if (i >= minJump) prefix += reach[i - minJump] ? 1 : 0;
            if (i > maxJump) prefix -= reach[i - maxJump - 1] ? 1 : 0;
            reach[i] = prefix > 0 && s.charAt(i) == '0';
        }
        return reach[n - 1];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.canReach("011010", 2, 3) == true;
        assert sol.canReach("01101110", 2, 3) == false;
        assert sol.canReach("00", 1, 1) == true;
        assert sol.canReach("011", 1, 2) == false; // both reachable positions are '1'
        System.out.println("All tests passed.");
    }
}
