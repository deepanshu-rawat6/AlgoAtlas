import java.util.*;

// LC 41: First Missing Positive
public class Solution {
    public int firstMissingPositiveHashset(int[] nums) {
        // Hash set then probe 1,2,3... — O(n) time, O(n) space
        Set<Integer> set = new HashSet<>();
        for (int n : nums) set.add(n);
        int i = 1;
        while (set.contains(i)) i++;
        return i;
    }

    public int firstMissingPositive(int[] nums) {
        // Cyclic sort: place each n at index n-1 if in range [1,n] — O(n) time, O(1) space
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            while (nums[i] >= 1 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {
                int tmp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = tmp;
            }
        }
        for (int i = 0; i < n; i++)
            if (nums[i] != i + 1) return i + 1;
        return n + 1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.firstMissingPositive(new int[]{1,2,0}) == 3 : "test 1";
        assert s.firstMissingPositive(new int[]{3,4,-1,1}) == 2 : "test 2";
        assert s.firstMissingPositive(new int[]{7,8,9,11,12}) == 1 : "test 3";
        assert s.firstMissingPositive(new int[]{1}) == 2 : "test 4";
        assert s.firstMissingPositive(new int[]{1,2,3}) == 4 : "test 5";
        System.out.println("All tests passed.");
    }
}
