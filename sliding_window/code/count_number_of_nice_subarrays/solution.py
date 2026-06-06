"""
LC 1248 - Count Number of Nice Subarrays

Given an array of integers nums and an integer k, return the number of
nice sub-arrays. A subarray is nice if there are k odd numbers in it.

Examples:
```text
Input: nums = [1,1,2,1,1], k = 3
Output: 2

Input: nums = [2,4,6], k = 1
Output: 0

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
```

Constraints:
- 1 <= nums.length <= 5 * 10^4
- 1 <= nums[i] <= 10^5
- 1 <= k <= nums.length
"""

from typing import List
from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Approach 1: prefix sum
        # Treat odd as 1, even as 0 — same as binary subarrays with sum k
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        result = 0

        for num in nums:
            prefix += num % 2          # 1 if odd, 0 if even
            result += count[prefix - k]
            count[prefix] += 1

        return result

    def numberOfSubarrays_atmost(self, nums: List[int], k: int) -> int:
        # Approach 2: atMost(k) - atMost(k-1)
        # exactly(k) = atMost(k) - atMost(k-1)
        def atMost(limit: int) -> int:
            left = odds = res = 0
            for right in range(len(nums)):
                odds += nums[right] % 2
                while odds > limit:
                    odds -= nums[left] % 2
                    left += 1
                res += right - left + 1
            return res

        return atMost(k) - atMost(k - 1)


if __name__ == '__main__':
    s = Solution()
    assert s.numberOfSubarrays([1,1,2,1,1], 3) == 2
    assert s.numberOfSubarrays([2,4,6], 1) == 0
    assert s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2) == 16
    assert s.numberOfSubarrays_atmost([1,1,2,1,1], 3) == 2
    assert s.numberOfSubarrays_atmost([2,2,2,1,2,2,1,2,2,2], 2) == 16
    print("All tests passed.")
