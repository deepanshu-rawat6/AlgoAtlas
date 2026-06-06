"""
# 92. Reverse Linked List II

## Problem
Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position right,
and return the reversed list.

## Examples

```text
Input:  head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input:  head = [5], left = 1, right = 1
Output: [5]
```

## Constraints
- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n
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


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Advance to the node just before position left
        # Reverse the sublist from left to right in-place
        # Reconnect the reversed segment back into the list
        # O(n) time, O(1) space — single pass with prev tracking
        dummy = ListNode(0, head)
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        curr = pre.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        return dummy.next


if __name__ == '__main__':
    s = Solution()

    assert list_to_arr(s.reverseBetween(build_list([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
    assert list_to_arr(s.reverseBetween(build_list([5]), 1, 1)) == [5]
    assert list_to_arr(s.reverseBetween(build_list([1, 2, 3, 4, 5]), 1, 5)) == [5, 4, 3, 2, 1]
    assert list_to_arr(s.reverseBetween(build_list([3, 5]), 1, 2)) == [5, 3]

    print("All tests passed.")
