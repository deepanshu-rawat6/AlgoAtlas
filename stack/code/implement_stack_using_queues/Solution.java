import java.util.*;

// Design problem: Solution IS the stack implemented with two queues.
// Costly push approach: O(n) push, O(1) pop/top.
// On each push, the new element is rotated to the front of q1 via q2.
public class Solution {
    private Deque<Integer> q1 = new ArrayDeque<>();  // main queue; front = stack top
    private Deque<Integer> q2 = new ArrayDeque<>();  // temp queue used during push

    public void push(int x) {
        // Enqueue x to q2, move all of q1 behind it, then swap
        // O(n) — rotate all existing elements through q2 so x ends up at front
        q2.offer(x);
        while (!q1.isEmpty()) q2.offer(q1.poll());
        Deque<Integer> temp = q1;
        q1 = q2;
        q2 = temp;
    }

    public int pop() {
        // Front of q1 is always the most recently pushed element
        // O(1)
        return q1.poll();
    }

    public int top() {
        // Peek front of q1
        // O(1)
        return q1.peek();
    }

    public boolean empty() {
        return q1.isEmpty();
    }

    public static void main(String[] args) {
        Solution st = new Solution();
        st.push(1);
        st.push(2);
        assert st.top() == 2 : "top failed";
        assert st.pop() == 2 : "pop 2 failed";
        assert !st.empty() : "empty failed";
        assert st.pop() == 1 : "pop 1 failed";
        assert st.empty() : "empty after all pops failed";
        System.out.println("All tests passed.");
    }
}
