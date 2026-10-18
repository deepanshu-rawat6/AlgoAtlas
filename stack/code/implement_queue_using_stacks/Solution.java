import java.util.*;

// Design problem: Solution IS the queue implemented with two stacks.
// Amortized O(1) push/pop/peek: lazy transfer from inbox to outbox on pop/peek.
public class Solution {
    private Deque<Integer> inbox = new ArrayDeque<>();   // new elements go here
    private Deque<Integer> outbox = new ArrayDeque<>();  // front elements served from here

    public void push(int x) {
        // O(1) — just push to inbox
        inbox.push(x);
    }

    private void transfer() {
        // Lazy transfer: only move inbox -> outbox when outbox is empty
        // Reversal via stack-to-stack gives FIFO order from outbox
        if (outbox.isEmpty()) {
            while (!inbox.isEmpty()) {
                outbox.push(inbox.pop());
            }
        }
    }

    public int pop() {
        // O(1) amortized
        transfer();
        return outbox.pop();
    }

    public int peek() {
        // O(1) amortized
        transfer();
        return outbox.peek();
    }

    public boolean empty() {
        return inbox.isEmpty() && outbox.isEmpty();
    }

    public static void main(String[] args) {
        Solution q = new Solution();
        q.push(1);
        q.push(2);
        assert q.peek() == 1 : "peek failed";
        assert q.pop() == 1 : "pop 1 failed";
        assert !q.empty() : "empty failed";
        assert q.pop() == 2 : "pop 2 failed";
        assert q.empty() : "empty after all pops failed";
        System.out.println("All tests passed.");
    }
}
