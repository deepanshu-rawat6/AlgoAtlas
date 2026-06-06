"""
# 25. Reverse Nodes in k-Group

## Problem
Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

## Examples

```text
Input:  head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input:  head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

## Constraints
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000
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
    def reverseKGroup_iterative(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # O(n) time, O(1) space
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # check if k nodes remain
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next

            # reverse the group
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # reconnect
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if k nodes remain; if not, leave as-is
        # Reverse k nodes, then recursively process the rest
        # Connect reversed segment's tail to the result of the recursive call
        # O(n) time, O(n/k) space (recursion)
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head
        # reverse k nodes
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # head is now the tail of reversed group; recurse for rest
        head.next = self.reverseKGroup(curr, k)
        return prev


if __name__ == '__main__':
    s = Solution()

    assert list_to_arr(s.reverseKGroup_iterative(build_list([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert list_to_arr(s.reverseKGroup_iterative(build_list([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert list_to_arr(s.reverseKGroup_iterative(build_list([1, 2, 3, 4, 5]), 1)) == [1, 2, 3, 4, 5]

    assert list_to_arr(s.reverseKGroup(build_list([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert list_to_arr(s.reverseKGroup(build_list([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert list_to_arr(s.reverseKGroup(build_list([1, 2, 3, 4, 5]), 1)) == [1, 2, 3, 4, 5]

    print("All tests passed.")
