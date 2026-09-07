import java.util.*;

public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> window = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (!window.add(nums[i])) return true;
            if (window.size() > k) window.remove(nums[i - k]);
        }
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.containsNearbyDuplicate(new int[]{1,2,3,1}, 3) == true;
        assert sol.containsNearbyDuplicate(new int[]{1,0,1,1}, 1) == true;
        assert sol.containsNearbyDuplicate(new int[]{1,2,3,1,2,3}, 2) == false;
        System.out.println("All tests passed.");
    }
}
