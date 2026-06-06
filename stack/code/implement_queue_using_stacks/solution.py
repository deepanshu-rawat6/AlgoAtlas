"""
# 232. Implement Queue using Stacks

## Problem
Implement a first-in-first-out (FIFO) queue using only two stacks. The
implemented queue should support `push`, `pop`, `peek`, and `empty` operations.

You must use **only** standard stack operations: `push to top`, `peek/pop from
top`, `size`, and `is empty`.

## Operations
- `push(x)` — Push element `x` to the back of the queue.
- `pop()` — Removes the element from the front of the queue and returns it.
- `peek()` — Returns the element at the front of the queue.
- `empty()` — Returns `true` if the queue is empty, `false` otherwise.

## Examples
```text
Input:
  ["MyQueue","push","push","peek","pop","empty"]
  [[],[1],[2],[],[],[]]
Output:
  [null,null,null,1,1,false]
```

## Constraints
- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`
- All calls to `pop` and `peek` are valid
"""


class MyQueue:
    """Approach 1: Two stacks, costly push — O(n) push, O(1) pop/peek."""

    def __init__(self):
        self.s1: list = []  # front stack
        self.s2: list = []  # temp stack

    def push(self, x: int) -> None:
        # Move all elements to s2, push new element to bottom of s1, move back
        # O(n) — move all to s2, push x to s1 (bottom), move back
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        # Front element is always at top of s1 after costly push
        # O(1)
        return self.s1.pop()

    def peek(self) -> int:
        # Peek top of s1 which holds the front of the queue
        # O(1)
        return self.s1[-1]

    def empty(self) -> bool:
        # Queue is empty when s1 is empty
        # O(1)
        return not self.s1


class MyQueueAmortized:
    """Approach 2: Two stacks, amortized O(1) — lazy transfer on pop/peek."""

    def __init__(self):
        self.inbox: list = []
        self.outbox: list = []

    def push(self, x: int) -> None:
        # Move all elements to s2, push new element to bottom of s1, move back
        # O(1)
        self.inbox.append(x)

    def _transfer(self) -> None:
        # Lazy transfer: only move inbox to outbox when outbox is empty
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())

    def pop(self) -> int:
        # Front element is always at top of s1 after costly push
        # O(1) amortized
        self._transfer()
        return self.outbox.pop()

    def peek(self) -> int:
        # Peek top of s1 which holds the front of the queue
        # O(1) amortized
        self._transfer()
        return self.outbox[-1]

    def empty(self) -> bool:
        # Queue is empty when s1 is empty
        # O(1)
        return not self.inbox and not self.outbox


if __name__ == "__main__":
    for Cls in (MyQueue, MyQueueAmortized):
        q = Cls()
        q.push(1)
        q.push(2)
        assert q.peek() == 1
        assert q.pop() == 1
        assert q.empty() is False
        assert q.pop() == 2
        assert q.empty() is True
    print("All tests passed.")
