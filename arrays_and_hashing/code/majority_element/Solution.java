import java.util.*;

// LC 169: Majority Element
public class Solution {
    public int majorityElementMap(int[] nums) {
        // Count frequencies; return max — O(n) time, O(n) space
        Map<Integer, Integer> count = new HashMap<>();
        for (int n : nums) count.merge(n, 1, Integer::sum);
        return Collections.max(count.entrySet(), Map.Entry.comparingByValue()).getKey();
    }

    public int majorityElementSort(int[] nums) {
        // Middle element after sort is always the majority — O(n log n) time
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }

    public int majorityElement(int[] nums) {
        // Boyer-Moore voting — O(n) time, O(1) space
        int candidate = 0, count = 0;
        for (int n : nums) {
            if (count == 0) candidate = n;
            count += (n == candidate) ? 1 : -1;
        }
        return candidate;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.majorityElement(new int[]{3,2,3}) == 3 : "test 1";
        assert s.majorityElement(new int[]{2,2,1,1,1,2,2}) == 2 : "test 2";
        assert s.majorityElement(new int[]{1}) == 1 : "test 3";
        System.out.println("All tests passed.");
    }
}
