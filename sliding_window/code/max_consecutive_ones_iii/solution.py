"""
LC 1004 - Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of
consecutive 1s in the array if you can flip at most k 0s.

Examples:
```text
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
```

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
- 0 <= k <= nums.length
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding window: expand right always, shrink left when zeros > k
        left = 0
        zeros = 0
        result = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # Window has more than k zeros — shrink from left
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            result = max(result, right - left + 1)

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
    assert s.longestOnes([1,1,1], 0) == 3
    assert s.longestOnes([0,0,0], 0) == 0
    print("All tests passed.")
