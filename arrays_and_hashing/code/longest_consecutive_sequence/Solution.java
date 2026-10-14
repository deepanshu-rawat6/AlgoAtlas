import java.util.*;

// LC 128: Longest Consecutive Sequence
public class Solution {
    public int longestConsecutiveSort(int[] nums) {
        // Sort + scan — O(n log n) time, O(1) extra space
        if (nums.length == 0) return 0;
        Arrays.sort(nums);
        int best = 1, cur = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) continue;
            if (nums[i] == nums[i - 1] + 1) { cur++; best = Math.max(best, cur); }
            else cur = 1;
        }
        return best;
    }

    public int longestConsecutive(int[] nums) {
        // Hash set: only start counting from sequence beginnings — O(n) time
        Set<Integer> set = new HashSet<>();
        for (int n : nums) set.add(n);
        int best = 0;
        for (int n : set) {
            if (!set.contains(n - 1)) {
                int cur = 1;
                while (set.contains(n + cur)) cur++;
                best = Math.max(best, cur);
            }
        }
        return best;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.longestConsecutive(new int[]{100,4,200,1,3,2}) == 4 : "test 1";
        assert s.longestConsecutive(new int[]{0,3,7,2,5,8,4,6,0,1}) == 9 : "test 2";
        assert s.longestConsecutive(new int[]{}) == 0 : "test 3";
        assert s.longestConsecutive(new int[]{1}) == 1 : "test 4";
        System.out.println("All tests passed.");
    }
}
