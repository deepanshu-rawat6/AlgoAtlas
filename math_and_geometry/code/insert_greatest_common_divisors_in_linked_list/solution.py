"""
# 2807. Insert Greatest Common Divisors in Linked List

Given the head of a linked list, for every pair of adjacent nodes, insert a new node
with value equal to the greatest common divisor of those two nodes' values.

Return the linked list after insertion.

## Examples

```text
Input: head = [18, 6, 10, 3]
Output: [18, 6, 6, 2, 10, 1, 3]

Input: head = [7]
Output: [7]
```

## Constraints
- The number of nodes in the list is in the range [1, 5000].
- 1 <= Node.val <= 1000
"""

from __future__ import annotations
from math import gcd
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Between each pair of adjacent nodes, insert a node with gcd(a, b)
        # O(n) time, O(1) space — single pass inserting GCD nodes between each pair
        cur = head
        while cur and cur.next:
            g = gcd(cur.val, cur.next.val)
            cur.next = ListNode(g, cur.next)
            cur = cur.next.next
        return head


def to_list(head: Optional[ListNode]) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def from_list(vals: list) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


if __name__ == '__main__':
    s = Solution()
    assert to_list(s.insertGreatestCommonDivisors(from_list([18, 6, 10, 3]))) == [18, 6, 6, 2, 10, 1, 3]
    assert to_list(s.insertGreatestCommonDivisors(from_list([7]))) == [7]
    print("All tests passed.")
