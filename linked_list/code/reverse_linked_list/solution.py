"""
# 206. Reverse Linked List

## Problem
Given the head of a singly linked list, reverse the list, and return the reversed list.

## Examples

```text
Input:  head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input:  head = [1,2]
Output: [2,1]

Input:  head = []
Output: []
```

## Constraints
- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000
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
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Keep track of prev; for each node, point its next to prev, then advance
        # O(n) time, O(1) space
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time, O(n) space (call stack)
        if not head or not head.next:
            return head
        new_head = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive: reverse the rest of the list, then attach current node at end
        return self.reverseList_iterative(head)


if __name__ == '__main__':
    s = Solution()

    head = build_list([1, 2, 3, 4, 5])
    assert list_to_arr(s.reverseList_iterative(head)) == [5, 4, 3, 2, 1]

    head = build_list([1, 2, 3, 4, 5])
    assert list_to_arr(s.reverseList_recursive(head)) == [5, 4, 3, 2, 1]

    assert s.reverseList(None) is None

    head = build_list([1])
    assert list_to_arr(s.reverseList(head)) == [1]

    print("All tests passed.")
