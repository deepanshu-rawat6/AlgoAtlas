"""
# LC 217: Contains Duplicate

Given an integer array `nums`, return `true` if any value appears **at least twice**,
and return `false` if every element is distinct.

## Examples

```text
Input:  nums = [1,2,3,1]
Output: true

Input:  nums = [1,2,3,4]
Output: false

Input:  nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## Constraints
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def containsDuplicate_brute(self, nums: List[int]) -> bool:
        # Compare every pair — O(n^2); fine for small inputs
        # O(n^2) time | O(1) space
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicate_sort(self, nums: List[int]) -> bool:
        # After sorting, duplicates are adjacent — one linear scan suffices
        # O(n log n) time | O(1) space
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        # A set collapses duplicates; if lengths differ, a duplicate existed
        # O(n) time | O(n) space
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) == True
    assert s.containsDuplicate([1, 2, 3, 4]) == False
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    print("All tests passed.")
