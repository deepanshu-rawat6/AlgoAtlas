"""
# LC 41: First Missing Positive

Given an unsorted integer array `nums`, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

## Examples

```text
Input:  nums = [1,2,0]
Output: 3

Input:  nums = [3,4,-1,1]
Output: 2

Input:  nums = [7,8,9,11,12]
Output: 1
```

## Constraints
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List


class Solution:
    def firstMissingPositive_hashset(self, nums: List[int]) -> int:
        """Hash set — O(n) time, O(n) space."""
        # Store all numbers in a set, then probe 1, 2, 3... for the first gap
        s = set(nums)
        i = 1
        while i in s:
            i += 1
        return i

    def firstMissingPositive(self, nums: List[int]) -> int:
        """Index marking (cyclic sort idea) — O(n) time, O(1) space."""
        # Cyclic sort: place each number at index nums[i]-1 if in range [1,n]
        # After rearranging, the first index where nums[i] != i+1 is the answer
        # If all positions are correct, the answer is n+1
        n = len(nums)
        # Place each number in its correct index position (nums[i] == i+1)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == "__main__":
    s = Solution()

    assert s.firstMissingPositive([1, 2, 0]) == 3
    assert s.firstMissingPositive([3, 4, -1, 1]) == 2
    assert s.firstMissingPositive([7, 8, 9, 11, 12]) == 1
    assert s.firstMissingPositive([1]) == 2
    assert s.firstMissingPositive([1, 2, 3]) == 4

    print("All tests passed.")
