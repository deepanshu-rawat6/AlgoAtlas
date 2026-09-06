public class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i-1]) nums[k++] = nums[i];
        }
        return k;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] a = {1,1,2};
        assert sol.removeDuplicates(a) == 2 && a[0] == 1 && a[1] == 2;
        int[] b = {0,0,1,1,1,2,2,3,3,4};
        assert sol.removeDuplicates(b) == 5;
        int[] c = {1};
        assert sol.removeDuplicates(c) == 1;
        System.out.println("All tests passed.");
    }
}
