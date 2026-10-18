import java.util.*;

public class Solution {
    static class MyCircularQueue {
        private int[] q;
        private int front, size, capacity;

        MyCircularQueue(int k) { q = new int[k]; capacity = k; }

        boolean enQueue(int value) {
            if (isFull()) return false;
            q[(front + size) % capacity] = value;
            size++;
            return true;
        }

        boolean deQueue() {
            if (isEmpty()) return false;
            front = (front + 1) % capacity;
            size--;
            return true;
        }

        int Front() { return isEmpty() ? -1 : q[front]; }

        int Rear() { return isEmpty() ? -1 : q[(front + size - 1) % capacity]; }

        boolean isEmpty() { return size == 0; }

        boolean isFull() { return size == capacity; }
    }

    public static void main(String[] args) {
        MyCircularQueue cq = new MyCircularQueue(3);
        assert cq.enQueue(1);
        assert cq.enQueue(2);
        assert cq.enQueue(3);
        assert !cq.enQueue(4);
        assert cq.Rear() == 3;
        assert cq.isFull();
        assert cq.deQueue();
        assert cq.enQueue(4);
        assert cq.Rear() == 4;
        assert cq.Front() == 2;

        MyCircularQueue cq2 = new MyCircularQueue(1);
        assert cq2.isEmpty();
        assert cq2.Front() == -1;
        assert cq2.Rear() == -1;
        assert cq2.enQueue(5);
        assert cq2.isFull();
        assert cq2.Front() == 5;
        assert cq2.Rear() == 5;

        System.out.println("All tests passed.");
    }
}

class ListNode {
    int val; ListNode next; ListNode random;
    ListNode(int v) { val = v; }
}
