public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;
        while (l < r) {
            int s = numbers[l] + numbers[r];
            if (s == target) return new int[]{l+1, r+1};
            else if (s < target) l++;
            else r--;
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] r1 = sol.twoSum(new int[]{2,7,11,15}, 9);
        assert r1[0]==1 && r1[1]==2;
        int[] r2 = sol.twoSum(new int[]{2,3,4}, 6);
        assert r2[0]==1 && r2[1]==3;
        int[] r3 = sol.twoSum(new int[]{-1,0}, -1);
        assert r3[0]==1 && r3[1]==2;
        System.out.println("All tests passed.");
    }
}
