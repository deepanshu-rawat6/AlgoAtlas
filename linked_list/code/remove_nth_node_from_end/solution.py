"""
# 19. Remove Nth Node From End of List

## Problem
Given the head of a linked list, remove the nth node from the end of the list
and return its head.

## Examples

```text
Input:  head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input:  head = [1], n = 1
Output: []

Input:  head = [1,2], n = 1
Output: [1]
```

## Constraints
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
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
    def removeNthFromEnd_twopass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n) time, O(1) space — two passes
        dummy = ListNode(0, head)
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        curr = dummy
        for _ in range(length - n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use two pointers n apart; when fast reaches end, slow is at the target
        # Dummy head handles edge case of removing the first node
        # O(n) time, O(1) space — one pass with two pointers
        dummy = ListNode(0, head)
        fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()

    assert list_to_arr(s.removeNthFromEnd_twopass(build_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert list_to_arr(s.removeNthFromEnd_twopass(build_list([1]), 1)) == []
    assert list_to_arr(s.removeNthFromEnd_twopass(build_list([1, 2]), 1)) == [1]

    assert list_to_arr(s.removeNthFromEnd(build_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert list_to_arr(s.removeNthFromEnd(build_list([1]), 1)) == []
    assert list_to_arr(s.removeNthFromEnd(build_list([1, 2]), 1)) == [1]

    print("All tests passed.")
