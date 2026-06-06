"""
# 143. Reorder List

## Problem
You are given the head of a singly linked-list:
  L0 → L1 → … → Ln-1 → Ln
Reorder it to:
  L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Examples

```text
Input:  head = [1,2,3,4]
Output: [1,4,2,3]

Input:  head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## Constraints
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000
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
    def reorderList_array(self, head: Optional[ListNode]) -> None:
        # O(n) time, O(n) space
        if not head:
            return
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        lo, hi = 0, len(nodes) - 1
        while lo < hi:
            nodes[lo].next = nodes[hi]
            lo += 1
            if lo == hi:
                break
            nodes[hi].next = nodes[lo]
            hi -= 1
        nodes[lo].next = None

    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find middle using slow/fast pointers
        # Step 2: reverse the second half in-place
        # Step 3: merge first half and reversed second half alternately
        # O(n) time, O(1) space — find middle, reverse second half, merge
        if not head or not head.next:
            return
        # find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second half
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


if __name__ == '__main__':
    s = Solution()

    head = build_list([1, 2, 3, 4])
    s.reorderList_array(head)
    assert list_to_arr(head) == [1, 4, 2, 3]

    head = build_list([1, 2, 3, 4, 5])
    s.reorderList_array(head)
    assert list_to_arr(head) == [1, 5, 2, 4, 3]

    head = build_list([1, 2, 3, 4])
    s.reorderList(head)
    assert list_to_arr(head) == [1, 4, 2, 3]

    head = build_list([1, 2, 3, 4, 5])
    s.reorderList(head)
    assert list_to_arr(head) == [1, 5, 2, 4, 3]

    print("All tests passed.")
