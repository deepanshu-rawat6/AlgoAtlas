import java.util.*;

// LC 27: Remove Element
public class Solution {
    public int removeElementBrute(int[] nums, int val) {
        // Shift left when val found — O(n^2) time, O(1) space
        int len = nums.length;
        int i = 0;
        while (i < len) {
            if (nums[i] == val) {
                for (int j = i; j < len - 1; j++) nums[j] = nums[j + 1];
                len--;
            } else i++;
        }
        return len;
    }

    public int removeElement(int[] nums, int val) {
        // k = write pointer for non-val elements — O(n) time, O(1) space
        int k = 0;
        for (int n : nums)
            if (n != val) nums[k++] = n;
        return k;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums;

        nums = new int[]{3,2,2,3};
        assert s.removeElement(nums, 3) == 2 && nums[0] == 2 && nums[1] == 2 : "test 1";

        nums = new int[]{0,1,2,2,3,0,4,2};
        int k = s.removeElement(nums, 2);
        assert k == 5 : "test 2";
        int[] head = Arrays.copyOf(nums, k);
        Arrays.sort(head);
        assert Arrays.equals(head, new int[]{0,0,1,3,4}) : "test 2b";

        System.out.println("All tests passed.");
    }
}
