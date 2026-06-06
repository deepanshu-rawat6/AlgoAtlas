"""
# LC 27: Remove Element

Given an integer array `nums` and an integer `val`, remove all occurrences of `val`
in `nums` **in-place**. The order of the elements may be changed. Return the number
of elements in `nums` which are not equal to `val`.

## Examples

```text
Input:  nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input:  nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
```

## Constraints
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100
"""
from typing import List


class Solution:
    def removeElement_brute(self, nums: List[int], val: int) -> int:
        # Shift all elements left when val found — O(n^2) due to shifting
        # O(n^2) time | O(1) space
        i = 0
        while i < len(nums):
            if nums[i] == val:
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
                nums.pop()
            else:
                i += 1
        return len(nums)

    def removeElement(self, nums: List[int], val: int) -> int:
        # k tracks the write position for non-val elements
        # Only advance k when we copy a valid element — O(n) single pass
        # O(n) time | O(1) space
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 2, 3]
    assert s.removeElement(nums, 3) == 2 and nums[:2] == [2, 2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert s.removeElement(nums, 2) == 5 and sorted(nums[:5]) == [0, 0, 1, 3, 4]
    print("All tests passed.")
