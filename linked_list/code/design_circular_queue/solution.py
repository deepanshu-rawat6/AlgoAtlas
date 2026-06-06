"""
# 622. Design Circular Queue

## Problem
Design your implementation of the circular queue. The circular queue is a linear
data structure in which the operations are performed based on FIFO principle, and
the last position is connected back to the first position to make a circle.
It is also called "Ring Buffer".

Implement the MyCircularQueue class:
- MyCircularQueue(k): Initializes the object with the size of the queue to be k.
- int Front(): Gets the front item from the queue. If the queue is empty, return -1.
- int Rear(): Gets the last item from the queue. If the queue is empty, return -1.
- boolean enQueue(int value): Inserts an element into the circular queue. Return true if successful.
- boolean deQueue(): Deletes an element from the circular queue. Return true if successful.
- boolean isEmpty(): Checks whether the circular queue is empty or not.
- boolean isFull(): Checks whether the circular queue is full or not.

## Examples

```text
Input:
  MyCircularQueue(3)
  enQueue(1) -> true
  enQueue(2) -> true
  enQueue(3) -> true
  enQueue(4) -> false  (queue is full)
  Rear()     -> 3
  isFull()   -> true
  deQueue()  -> true
  enQueue(4) -> true
  Rear()     -> 4
```

## Constraints
- 1 <= k <= 1000
- 0 <= value <= 1000
- At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def list_to_arr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


class MyCircularQueue:
    # O(1) time per operation, O(k) space — array with front/rear pointers

    def __init__(self, k: int):
        self.q = [0] * k
        self.front = 0
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        # Add element at rear; advance rear pointer with wrap-around
        if self.isFull():
            return False
        rear = (self.front + self.size) % self.capacity
        self.q[rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        # Remove element at front; advance front pointer with wrap-around
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        # Return element at front without removing it
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self) -> int:
        # Return element at rear without removing it
        if self.isEmpty():
            return -1
        return self.q[(self.front + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        # Queue is empty when size is 0
        return self.size == 0

    def isFull(self) -> bool:
        # Queue is full when size equals capacity
        return self.size == self.capacity


if __name__ == '__main__':
    cq = MyCircularQueue(3)
    assert cq.enQueue(1) is True
    assert cq.enQueue(2) is True
    assert cq.enQueue(3) is True
    assert cq.enQueue(4) is False
    assert cq.Rear() == 3
    assert cq.isFull() is True
    assert cq.deQueue() is True
    assert cq.enQueue(4) is True
    assert cq.Rear() == 4
    assert cq.Front() == 2

    cq2 = MyCircularQueue(1)
    assert cq2.isEmpty() is True
    assert cq2.Front() == -1
    assert cq2.Rear() == -1
    assert cq2.enQueue(5) is True
    assert cq2.isFull() is True
    assert cq2.Front() == 5
    assert cq2.Rear() == 5

    print("All tests passed.")
