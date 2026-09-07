import java.util.*;

public class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        Map<Integer,Integer> count = new HashMap<>();
        count.put(0, 1);
        int prefix = 0, result = 0;
        for (int n : nums) {
            prefix += n;
            result += count.getOrDefault(prefix - goal, 0);
            count.merge(prefix, 1, Integer::sum);
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.numSubarraysWithSum(new int[]{1,0,1,0,1}, 2) == 4;
        assert sol.numSubarraysWithSum(new int[]{0,0,0,0,0}, 0) == 15;
        assert sol.numSubarraysWithSum(new int[]{1,0,1}, 1) == 4;
        System.out.println("All tests passed.");
    }
}
