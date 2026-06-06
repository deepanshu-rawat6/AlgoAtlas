"""
# 23. Merge K Sorted Lists

## Problem
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

## Examples

```text
Input:  lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Input:  lists = []
Output: []

Input:  lists = [[]]
Output: []
```

## Constraints
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.
"""
from typing import List, Optional
import heapq


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
    def mergeKLists_sequential(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(kN) time, O(1) space — merge one by one
        def merge_two(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1; l1 = l1.next
                else:
                    curr.next = l2; l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        result = None
        for lst in lists:
            result = merge_two(result, lst)
        return result

    def mergeKLists_divide(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(N log k) time, O(log k) space — divide and conquer
        def merge_two(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1; l1 = l1.next
                else:
                    curr.next = l2; l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(merge_two(l1, l2))
            lists = merged
        return lists[0]

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Use a min-heap to always extract the globally smallest node
        # Push each list's head; after popping, push that node's next
        # O(N log k) time, O(k) space — min heap
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next


if __name__ == '__main__':
    s = Solution()

    def make(lists_vals):
        return [build_list(v) for v in lists_vals]

    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    assert list_to_arr(s.mergeKLists_sequential(make([[1, 4, 5], [1, 3, 4], [2, 6]]))) == expected
    assert list_to_arr(s.mergeKLists_divide(make([[1, 4, 5], [1, 3, 4], [2, 6]]))) == expected
    assert list_to_arr(s.mergeKLists(make([[1, 4, 5], [1, 3, 4], [2, 6]]))) == expected

    assert s.mergeKLists([]) is None
    assert s.mergeKLists([None]) is None

    print("All tests passed.")
