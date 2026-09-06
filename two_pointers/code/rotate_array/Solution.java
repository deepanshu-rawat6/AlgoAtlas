public class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;
        reverse(nums, 0, n-1);
        reverse(nums, 0, k-1);
        reverse(nums, k, n-1);
    }

    private void reverse(int[] nums, int l, int r) {
        while (l < r) {
            int tmp = nums[l]; nums[l] = nums[r]; nums[r] = tmp;
            l++; r--;
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] a = {1,2,3,4,5,6,7};
        sol.rotate(a, 3);
        assert a[0]==5 && a[1]==6 && a[2]==7 && a[3]==1;
        int[] b = {-1,-100,3,99};
        sol.rotate(b, 2);
        assert b[0]==3 && b[1]==99 && b[2]==-1 && b[3]==-100;
        int[] c = {1,2};
        sol.rotate(c, 3);
        assert c[0]==2 && c[1]==1;
        System.out.println("All tests passed.");
    }
}
