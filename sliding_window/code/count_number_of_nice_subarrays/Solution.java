import java.util.*;

public class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        Map<Integer,Integer> count = new HashMap<>();
        count.put(0, 1);
        int prefix = 0, result = 0;
        for (int n : nums) {
            prefix += n % 2;
            result += count.getOrDefault(prefix - k, 0);
            count.merge(prefix, 1, Integer::sum);
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.numberOfSubarrays(new int[]{1,1,2,1,1}, 3) == 2;
        assert sol.numberOfSubarrays(new int[]{2,4,6}, 1) == 0;
        assert sol.numberOfSubarrays(new int[]{2,2,2,1,2,2,1,2,2,2}, 2) == 16;
        System.out.println("All tests passed.");
    }
}
