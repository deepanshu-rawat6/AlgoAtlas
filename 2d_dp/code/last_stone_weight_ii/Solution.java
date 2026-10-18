import java.util.*;

public class Solution {
    public int lastStoneWeightII(int[] stones) {
        // Minimize |S1 - S2|; find largest subset sum <= total/2
        // Equivalent to subset-sum boolean DP
        // Time: O(n*sum), Space: O(sum)
        int total = 0;
        for (int s : stones) total += s;
        int target = total / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int s : stones) {
            for (int j = target; j >= s; j--) {
                dp[j] = dp[j] || dp[j - s];
            }
        }
        for (int j = target; j >= 0; j--) {
            if (dp[j]) return total - 2 * j;
        }
        return total;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.lastStoneWeightII(new int[]{2,7,4,1,8,1}) == 1 : "test 1 failed";
        assert sol.lastStoneWeightII(new int[]{31,26,33,21,40}) == 5 : "test 2 failed";
        assert sol.lastStoneWeightII(new int[]{1}) == 1 : "test 3 failed";
        assert sol.lastStoneWeightII(new int[]{1,2}) == 1 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
