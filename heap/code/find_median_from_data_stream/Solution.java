import java.util.*;

public class Solution {
    static class MedianFinder {
        private PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder()); // max-heap, lower half
        private PriorityQueue<Integer> large = new PriorityQueue<>(); // min-heap, upper half

        public void addNum(int num) {
            small.offer(num);
            // Ensure all of small <= all of large
            if (!large.isEmpty() && small.peek() > large.peek()) {
                large.offer(small.poll());
            }
            // Balance sizes: small can have at most 1 more than large
            if (small.size() > large.size() + 1) {
                large.offer(small.poll());
            } else if (large.size() > small.size()) {
                small.offer(large.poll());
            }
        }

        public double findMedian() {
            if (small.size() > large.size()) return small.peek();
            return (small.peek() + large.peek()) / 2.0;
        }
    }

    public static void main(String[] args) {
        MedianFinder mf = new MedianFinder();
        mf.addNum(1);
        mf.addNum(2);
        assert mf.findMedian() == 1.5;
        mf.addNum(3);
        assert mf.findMedian() == 2.0;

        MedianFinder mf2 = new MedianFinder();
        mf2.addNum(-1);
        assert mf2.findMedian() == -1.0;
        mf2.addNum(-2);
        assert mf2.findMedian() == -1.5;
        mf2.addNum(-3);
        assert mf2.findMedian() == -2.0;
        mf2.addNum(-4);
        assert mf2.findMedian() == -2.5;
        mf2.addNum(-5);
        assert mf2.findMedian() == -3.0;

        System.out.println("All tests passed.");
    }
}
