import java.util.*;

public class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        // dp map: sum -> count of ways; each num adds or subtracts
        // Time: O(n*sum), Space: O(sum)
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 1);
        for (int n : nums) {
            Map<Integer, Integer> next = new HashMap<>();
            for (Map.Entry<Integer, Integer> e : dp.entrySet()) {
                int s = e.getKey(), cnt = e.getValue();
                next.merge(s + n, cnt, Integer::sum);
                next.merge(s - n, cnt, Integer::sum);
            }
            dp = next;
        }
        return dp.getOrDefault(target, 0);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.findTargetSumWays(new int[]{1,1,1,1,1}, 3) == 5 : "test 1 failed";
        assert sol.findTargetSumWays(new int[]{1}, 1) == 1 : "test 2 failed";
        assert sol.findTargetSumWays(new int[]{1}, -1) == 1 : "test 3 failed";
        assert sol.findTargetSumWays(new int[]{1,0}, 1) == 2 : "test 4 failed";
        System.out.println("All tests passed.");
    }
}
