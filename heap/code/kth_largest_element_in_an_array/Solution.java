import java.util.*;

public class Solution {
    public int findKthLargest(int[] nums, int k) {
        // Min-heap of size k; top is the k-th largest
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int n : nums) {
            heap.offer(n);
            if (heap.size() > k) heap.poll();
        }
        return heap.peek();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.findKthLargest(new int[]{3,2,1,5,6,4}, 2) == 5;
        assert s.findKthLargest(new int[]{3,2,3,1,2,4,5,5,6}, 4) == 4;
        assert s.findKthLargest(new int[]{1}, 1) == 1;
        assert s.findKthLargest(new int[]{-1,-2,-3,-4,-5}, 2) == -2;
        System.out.println("All tests passed.");
    }
}
