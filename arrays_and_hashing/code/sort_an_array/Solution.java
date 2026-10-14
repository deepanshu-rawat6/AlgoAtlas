import java.util.*;

// LC 912: Sort an Array — heap sort O(n log n) time, O(1) space
public class Solution {
    public int[] sortArrayMerge(int[] nums) {
        // Merge sort — O(n log n) time, O(n) space
        if (nums.length <= 1) return nums;
        int mid = nums.length / 2;
        int[] left  = sortArrayMerge(Arrays.copyOfRange(nums, 0, mid));
        int[] right = sortArrayMerge(Arrays.copyOfRange(nums, mid, nums.length));
        return merge(left, right);
    }

    private int[] merge(int[] l, int[] r) {
        int[] res = new int[l.length + r.length];
        int i = 0, j = 0, k = 0;
        while (i < l.length && j < r.length)
            res[k++] = (l[i] <= r[j]) ? l[i++] : r[j++];
        while (i < l.length) res[k++] = l[i++];
        while (j < r.length) res[k++] = r[j++];
        return res;
    }

    public int[] sortArray(int[] nums) {
        // Heap sort — O(n log n) time, O(1) space
        int n = nums.length;
        for (int i = n / 2 - 1; i >= 0; i--) heapify(nums, n, i);
        for (int i = n - 1; i > 0; i--) {
            int tmp = nums[0]; nums[0] = nums[i]; nums[i] = tmp;
            heapify(nums, i, 0);
        }
        return nums;
    }

    private void heapify(int[] nums, int n, int i) {
        int largest = i, l = 2*i+1, r = 2*i+2;
        if (l < n && nums[l] > nums[largest]) largest = l;
        if (r < n && nums[r] > nums[largest]) largest = r;
        if (largest != i) {
            int tmp = nums[i]; nums[i] = nums[largest]; nums[largest] = tmp;
            heapify(nums, n, largest);
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert Arrays.equals(s.sortArray(new int[]{5,2,3,1}), new int[]{1,2,3,5}) : "test 1";
        assert Arrays.equals(s.sortArray(new int[]{5,1,1,2,0,0}), new int[]{0,0,1,1,2,5}) : "test 2";
        int[] arr = {-4,0,7,4,9,-5,-1,0,-7,-1};
        int[] exp = arr.clone(); Arrays.sort(exp);
        assert Arrays.equals(s.sortArray(arr), exp) : "test 3";
        System.out.println("All tests passed.");
    }
}
