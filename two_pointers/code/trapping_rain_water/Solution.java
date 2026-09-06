public class Solution {
    public int trap(int[] height) {
        int lo = 0, hi = height.length - 1;
        int leftMax = 0, rightMax = 0, water = 0;
        while (lo <= hi) {
            if (height[lo] <= height[hi]) {
                if (height[lo] >= leftMax) leftMax = height[lo];
                else water += leftMax - height[lo];
                lo++;
            } else {
                if (height[hi] >= rightMax) rightMax = height[hi];
                else water += rightMax - height[hi];
                hi--;
            }
        }
        return water;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        assert sol.trap(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}) == 6;
        assert sol.trap(new int[]{4,2,0,3,2,5}) == 9;
        assert sol.trap(new int[]{3,0,3}) == 3;
        System.out.println("All tests passed.");
    }
}
