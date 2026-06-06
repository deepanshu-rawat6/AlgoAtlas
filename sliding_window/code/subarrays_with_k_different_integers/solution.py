"""
LC 992 - Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of
good subarrays. A good subarray has exactly k different integers.

Examples:
```text
Input: nums = [1,2,1,2,3], k = 2
Output: 7

Input: nums = [1,2,1,3,4], k = 3
Output: 3
```

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i] <= nums.length
- 1 <= k <= nums.length
"""

from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # exactly(k) = atMost(k) - atMost(k-1)
        # Each atMost is a standard sliding window counting subarrays
        def atMost(limit: int) -> int:
            count = defaultdict(int)
            left = res = 0
            for right in range(len(nums)):
                count[nums[right]] += 1
                # shrink until distinct count <= limit
                while len(count) > limit:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                # all subarrays ending at right with at most `limit` distinct
                res += right - left + 1
            return res

        return atMost(k) - atMost(k - 1)


if __name__ == '__main__':
    s = Solution()
    assert s.subarraysWithKDistinct([1,2,1,2,3], 2) == 7
    assert s.subarraysWithKDistinct([1,2,1,3,4], 3) == 3
    assert s.subarraysWithKDistinct([1,1,1,1], 1) == 10
    print("All tests passed.")
