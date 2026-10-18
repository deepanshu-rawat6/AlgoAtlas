import java.util.*;

public class Solution {
    static class KthLargest {
        private final int k;
        private final PriorityQueue<Integer> heap = new PriorityQueue<>(); // min-heap of size k

        public KthLargest(int k, int[] nums) {
            this.k = k;
            for (int n : nums) add(n);
        }

        public int add(int val) {
            heap.offer(val);
            if (heap.size() > k) heap.poll();
            return heap.peek();
        }
    }

    public static void main(String[] args) {
        KthLargest obj = new KthLargest(3, new int[]{4, 5, 8, 2});
        assert obj.add(3) == 4;
        assert obj.add(5) == 5;
        assert obj.add(10) == 5;
        assert obj.add(9) == 8;
        assert obj.add(4) == 8;

        KthLargest obj2 = new KthLargest(1, new int[]{});
        assert obj2.add(-3) == -3;
        assert obj2.add(-2) == -2;
        assert obj2.add(-4) == -2;

        System.out.println("All tests passed.");
    }
}
