import java.util.*;

public class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) heap.offer(s);
        while (heap.size() > 1) {
            int y = heap.poll();
            int x = heap.poll();
            if (x != y) heap.offer(y - x);
        }
        return heap.isEmpty() ? 0 : heap.peek();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        assert s.lastStoneWeight(new int[]{2,7,4,1,8,1}) == 1;
        assert s.lastStoneWeight(new int[]{1}) == 1;
        assert s.lastStoneWeight(new int[]{2,2}) == 0;
        assert s.lastStoneWeight(new int[]{1,3}) == 2;
        System.out.println("All tests passed.");
    }
}
