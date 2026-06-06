"""
Reverse Stack Using Recursion

Problem: Reverse a stack using only recursion. No extra data structures allowed.

Examples:
    [1, 2, 3] (top=3) -> [3, 2, 1] (top=1)
    [1]               -> [1]

Constraints:
    Only recursion allowed (no auxiliary stack/queue/list).

Approach: O(n^2) time, O(n) space (call stack)
    - Pop top element
    - Recursively reverse the remaining stack
    - Insert the popped element at the bottom
"""

from typing import List


class Solution:
    def reverseStack(self, stack: List[int]) -> List[int]:
        # Base case: empty or single element — already reversed
        if len(stack) <= 1:
            return stack
        # Pop top, reverse the rest, then insert top at the bottom
        top = stack.pop()
        self.reverseStack(stack)
        self._insertAtBottom(stack, top)
        return stack

    def _insertAtBottom(self, stack: List[int], val: int) -> None:
        # Base case: empty stack — just push the value
        if not stack:
            stack.append(val)
            return
        # Hold current top, recurse to reach bottom, then restore top
        top = stack.pop()
        self._insertAtBottom(stack, val)
        stack.append(top)


if __name__ == '__main__':
    sol = Solution()
    assert sol.reverseStack([1, 2, 3]) == [3, 2, 1]
    assert sol.reverseStack([1]) == [1]
    assert sol.reverseStack([]) == []
    assert sol.reverseStack([4, 3, 2, 1]) == [1, 2, 3, 4]
    print("All tests passed.")
