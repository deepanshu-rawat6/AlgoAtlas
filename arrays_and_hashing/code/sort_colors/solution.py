"""
# LC 75: Sort Colors

Given an array `nums` with `n` objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue. Use integers 0, 1, and 2 to represent red, white,
and blue respectively.

You must solve this without using the library's sort function.

## Examples

```text
Input:  nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input:  nums = [2,0,1]
Output: [0,1,2]
```

## Constraints
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2
"""
from typing import List


class Solution:
    def sortColors_counting(self, nums: List[int]) -> None:
        """Counting sort — O(n) time, O(1) space, two-pass."""
        # Count 0s, 1s, 2s then overwrite array in order — two passes
        count = [0, 0, 0]
        for n in nums:
            count[n] += 1
        i = 0
        for val, cnt in enumerate(count):
            for _ in range(cnt):
                nums[i] = val
                i += 1

    def sortColors(self, nums: List[int]) -> None:
        """Dutch National Flag — O(n) time, O(1) space, one-pass."""
        # Dutch National Flag: three regions — [0..lo-1]=0, [lo..mid-1]=1, [hi+1..n-1]=2
        # If mid is 0: swap with lo (both advance), if 1: advance mid, if 2: swap with hi
        # hi shrinks but mid doesn't advance after swap with hi (unknown value)
        lo, mid, hi = 0, 0, len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1


if __name__ == "__main__":
    s = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    s.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2], nums

    nums = [2, 0, 1]
    s.sortColors(nums)
    assert nums == [0, 1, 2], nums

    nums = [0]
    s.sortColors(nums)
    assert nums == [0], nums

    print("All tests passed.")
