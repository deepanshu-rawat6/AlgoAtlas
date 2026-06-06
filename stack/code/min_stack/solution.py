"""
# 155. Min Stack

## Problem
Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum
element — all in **O(1)** time.

## Operations
- `push(val)` — Push element `val` onto the stack.
- `pop()` — Removes the element on top of the stack.
- `top()` — Gets the top element.
- `getMin()` — Retrieves the minimum element in the stack.

## Examples
```text
Input:
  ["MinStack","push","push","push","getMin","pop","top","getMin"]
  [[],[-2],[0],[-3],[],[],[],[]]
Output:
  [null,null,null,null,-3,null,0,-2]
```

## Constraints
- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top`, and `getMin` will always be called on non-empty stacks
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`
"""


class MinStack:
    """Approach 1: Two stacks — main stack + parallel min-tracking stack."""

    def __init__(self):
        self.stack: list = []
        self.min_stack: list = []

    def push(self, val: int) -> None:
        # Push value to main stack; also push new min to min_stack
        # O(1)
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))

    def pop(self) -> None:
        # Pop from both stacks to keep them in sync
        # O(1)
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Peek top of main stack
        # O(1)
        return self.stack[-1]

    def getMin(self) -> int:
        # Peek top of min_stack — always holds current minimum
        # O(1)
        return self.min_stack[-1]


class MinStackTuple:
    """Approach 2: Single stack of (value, current_min) tuples."""

    def __init__(self):
        self.stack: list = []  # each entry: (val, current_min)

    def push(self, val: int) -> None:
        # Push value to main stack; also push new min to min_stack
        # O(1)
        cur_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        # Pop from both stacks to keep them in sync
        # O(1)
        self.stack.pop()

    def top(self) -> int:
        # Peek top of main stack
        # O(1)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Peek top of min_stack — always holds current minimum
        # O(1)
        return self.stack[-1][1]


if __name__ == "__main__":
    for Cls in (MinStack, MinStackTuple):
        ms = Cls()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        assert ms.getMin() == -3
        ms.pop()
        assert ms.top() == 0
        assert ms.getMin() == -2
    print("All tests passed.")
