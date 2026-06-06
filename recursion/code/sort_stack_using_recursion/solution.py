"""
Sort Stack Using Recursion

Problem: Sort a stack in ascending order (smallest on top) using only recursion.
No extra data structures allowed — only the call stack.

Examples:
    [3, 1, 2] (top=3) -> [1, 2, 3] (top=1)
    [5, 1, 4, 2, 3]   -> [1, 2, 3, 4, 5]

Constraints:
    Stack elements are integers.
    Only recursion allowed (no auxiliary stack/queue/list).

Approach: O(n^2) time, O(n) space (call stack)
    - Pop top element
    - Recursively sort the remaining stack
    - Insert the popped element into its correct sorted position
"""

from typing import List


class Solution:
    def sortStack(self, stack: List[int]) -> List[int]:
        # Base case: empty stack is already sorted
        if not stack:
            return stack
        # Pop top, sort the rest, then insert top in correct position
        top = stack.pop()
        self.sortStack(stack)
        self._insertSorted(stack, top)
        return stack

    def _insertSorted(self, stack: List[int], val: int) -> None:
        # Base case: empty stack or val is smaller than current top -> push
        if not stack or stack[-1] <= val:
            stack.append(val)
            return
        # Current top is greater than val; pop it, recurse, then restore
        top = stack.pop()
        self._insertSorted(stack, val)
        stack.append(top)


if __name__ == '__main__':
    sol = Solution()
    assert sol.sortStack([3, 1, 2]) == [1, 2, 3]
    assert sol.sortStack([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]
    assert sol.sortStack([]) == []
    assert sol.sortStack([1]) == [1]
    print("All tests passed.")
