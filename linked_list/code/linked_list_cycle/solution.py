"""
# 141. Linked List Cycle

## Problem
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle if some node can be reached again by continuously following the next pointer.
Return true if there is a cycle, otherwise return false.

## Examples

```text
Input:  head = [3,2,0,-4], pos = 1   (tail connects to node at index 1)
Output: true

Input:  head = [1,2], pos = 0
Output: true

Input:  head = [1], pos = -1
Output: false
```

## Constraints
- The number of nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked list.
"""
from typing import Optional


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


def build_cycle_list(vals, pos):
    """Build a list where tail.next points to node at index pos (-1 = no cycle)."""
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


class Solution:
    def hasCycle_hashset(self, head: Optional[ListNode]) -> bool:
        # O(n) time, O(n) space
        seen = set()
        curr = head
        while curr:
            if id(curr) in seen:
                return True
            seen.add(id(curr))
            curr = curr.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's cycle detection: slow moves 1 step, fast moves 2 steps
        # If they meet, there's a cycle; if fast reaches None, no cycle
        # O(n) time, O(1) space — two pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == '__main__':
    s = Solution()

    assert s.hasCycle_hashset(build_cycle_list([3, 2, 0, -4], 1)) is True
    assert s.hasCycle_hashset(build_cycle_list([1, 2], 0)) is True
    assert s.hasCycle_hashset(build_cycle_list([1], -1)) is False

    assert s.hasCycle(build_cycle_list([3, 2, 0, -4], 1)) is True
    assert s.hasCycle(build_cycle_list([1, 2], 0)) is True
    assert s.hasCycle(build_cycle_list([1], -1)) is False
    assert s.hasCycle(None) is False

    print("All tests passed.")
