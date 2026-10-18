import java.util.*;

// Design problem: Solution IS the StockSpanner.
// Monotonic decreasing stack of {price, span} pairs.
// When a higher price arrives, collapse all dominated entries into an accumulated span.
// O(1) amortized per next() call — each entry is pushed and popped at most once.
public class Solution {
    private Deque<int[]> stack = new ArrayDeque<>();  // {price, span}

    public int next(int price) {
        // Collapse all previous days with price <= current into one span
        // Stack stores {price, span} pairs; accumulate spans of dominated days
        // O(1) amortized — collapse dominated entries into accumulated span
        int span = 1;
        while (!stack.isEmpty() && stack.peek()[0] <= price) {
            span += stack.pop()[1];
        }
        stack.push(new int[]{price, span});
        return span;
    }

    public static void main(String[] args) {
        Solution sp = new Solution();
        assert sp.next(100) == 1 : "next(100) failed";
        assert sp.next(80) == 1 : "next(80) failed";
        assert sp.next(60) == 1 : "next(60) failed";
        assert sp.next(70) == 2 : "next(70) failed";
        assert sp.next(60) == 1 : "next(60) second failed";
        assert sp.next(75) == 4 : "next(75) failed";
        assert sp.next(85) == 6 : "next(85) failed";
        System.out.println("All tests passed.");
    }
}
