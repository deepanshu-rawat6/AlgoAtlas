"""
# 287. Find the Duplicate Number

## Problem
Given an array of integers nums containing n + 1 integers where each integer is
in the range [1, n] inclusive, there is only one repeated number in nums.
Return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

## Examples

```text
Input:  nums = [1,3,4,2,2]
Output: 2

Input:  nums = [3,1,3,4,2]
Output: 3

Input:  nums = [3,3,3,3,3]
Output: 3
```

## Constraints
- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n
- All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""
from typing import List


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
    def findDuplicate_hashset(self, nums: List[int]) -> int:
        # O(n) time, O(n) space
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        return -1

    def findDuplicate(self, nums: List[int]) -> int:
        # Treat array as a linked list: index -> nums[index]
        # Floyd's cycle detection finds the entry point of the cycle = duplicate
        # O(n) time, O(1) space — treat array as linked list, find cycle entry
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == '__main__':
    s = Solution()

    assert s.findDuplicate_hashset([1, 3, 4, 2, 2]) == 2
    assert s.findDuplicate_hashset([3, 1, 3, 4, 2]) == 3

    assert s.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert s.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert s.findDuplicate([3, 3, 3, 3, 3]) == 3

    print("All tests passed.")
