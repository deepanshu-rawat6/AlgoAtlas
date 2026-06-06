"""
# 225. Implement Stack using Queues

## Problem
Implement a last-in-first-out (LIFO) stack using only two queues. The
implemented stack should support `push`, `pop`, `top`, and `empty` operations.

You must use **only** standard queue operations: `push to back`, `peek/pop from
front`, `size`, and `is empty`.

## Operations
- `push(x)` — Push element `x` onto stack.
- `pop()` — Removes the element on top of the stack and returns it.
- `top()` — Get the top element.
- `empty()` — Returns `true` if the stack is empty, `false` otherwise.

## Examples
```text
Input:
  ["MyStack","push","push","top","pop","empty"]
  [[],[1],[2],[],[],[]]
Output:
  [null,null,null,2,2,false]
```

## Constraints
- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `top`, and `empty`
- All calls to `pop` and `top` are valid
"""

from collections import deque


class MyStack:
    """Approach 1: Two queues, costly push — O(n) push, O(1) pop/top."""

    def __init__(self):
        self.q1: deque = deque()
        self.q2: deque = deque()

    def push(self, x: int) -> None:
        # Rotate all existing elements behind the new one so it's at front
        # O(n) — rotate all existing elements through q2 so x ends up at front
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # Front of q1 is always the most recently pushed element
        # O(1)
        return self.q1.popleft()

    def top(self) -> int:
        # Peek front of q1
        # O(1)
        return self.q1[0]

    def empty(self) -> bool:
        # Stack is empty when q1 is empty
        # O(1)
        return not self.q1


class MyStackCostlyPop:
    """Approach 2: Two queues, costly pop — O(1) push, O(n) pop/top."""

    def __init__(self):
        self.q1: deque = deque()
        self.q2: deque = deque()

    def push(self, x: int) -> None:
        # Rotate all existing elements behind the new one so it's at front
        # O(1)
        self.q1.append(x)

    def pop(self) -> int:
        # Front of q1 is always the most recently pushed element
        # O(n) — drain q1 into q2 leaving last element
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return val

    def top(self) -> int:
        # Peek front of q1
        # O(n)
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        return val

    def empty(self) -> bool:
        # Stack is empty when q1 is empty
        # O(1)
        return not self.q1


if __name__ == "__main__":
    for Cls in (MyStack, MyStackCostlyPop):
        st = Cls()
        st.push(1)
        st.push(2)
        assert st.top() == 2
        assert st.pop() == 2
        assert st.empty() is False
        assert st.pop() == 1
        assert st.empty() is True
    print("All tests passed.")
