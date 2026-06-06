"""
# 138. Copy List with Random Pointer

## Problem
A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n
brand new nodes, where each new node has its value set to the value of its
corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the
original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

## Examples

```text
Input:  head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Input:  head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Input:  head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

## Constraints
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random is null or pointing to some node in the linked list.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


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


def build_random_list(data):
    """data: list of [val, random_index] where random_index is None or int."""
    if not data:
        return None
    nodes = [Node(d[0]) for d in data]
    for i, d in enumerate(data):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if d[1] is not None:
            nodes[i].random = nodes[d[1]]
    return nodes[0]


class Solution:
    def copyRandomList_hashmap(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # O(n) time, O(n) space
        if not head:
            return None
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        return old_to_new[head]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # First pass: create all new nodes and map old->new
        # Second pass: wire up next and random pointers using the map
        # O(n) time, O(1) space — interleave cloned nodes
        if not head:
            return None
        # Step 1: interleave clones
        curr = head
        while curr:
            clone = Node(curr.val, curr.next)
            curr.next = clone
            curr = clone.next
        # Step 2: assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        # Step 3: separate lists
        dummy = Node(0)
        clone_curr = dummy
        curr = head
        while curr:
            clone_curr.next = curr.next
            curr.next = curr.next.next
            clone_curr = clone_curr.next
            curr = curr.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()

    original = build_random_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    copy1 = s.copyRandomList_hashmap(original)
    assert copy1 is not original
    assert copy1.val == 7
    assert copy1.next.val == 13
    assert copy1.next.random.val == 7

    original2 = build_random_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    copy2 = s.copyRandomList(original2)
    assert copy2 is not original2
    assert copy2.val == 7
    assert copy2.next.random.val == 7

    assert s.copyRandomList(None) is None

    print("All tests passed.")
