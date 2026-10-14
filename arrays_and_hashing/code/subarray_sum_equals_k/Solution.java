import java.util.*;

// LC 560: Subarray Sum Equals K
public class Solution {
    public int subarraySumBrute(int[] nums, int k) {
        // Try all subarrays — O(n^2) time, O(1) space
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            int total = 0;
            for (int j = i; j < nums.length; j++) {
                total += nums[j];
                if (total == k) count++;
            }
        }
        return count;
    }

    public int subarraySum(int[] nums, int k) {
        // Prefix sum + hash map — O(n) time, O(n) space
        // freq[prefix] counts how many times this prefix sum has appeared
        // prefix[j] - prefix[i] == k  =>  look up freq[prefix[j] - k]
        Map<Integer, Integer> freq = new HashMap<>();
        freq.put(0, 1);
        int count = 0, prefix = 0;
        for (int n : nums) {
            prefix += n;
            count += freq.getOrDefault(prefix - k, 0);
            freq.merge(prefix, 1, Integer::sum);
        }
        return count;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.subarraySum(new int[]{1,1,1}, 2) == 2 : "test 1";
        assert s.subarraySum(new int[]{1,2,3}, 3) == 2 : "test 2";
        assert s.subarraySum(new int[]{1}, 0) == 0 : "test 3";
        assert s.subarraySum(new int[]{-1,-1,1}, 0) == 1 : "test 4";
        System.out.println("All tests passed.");
    }
}
