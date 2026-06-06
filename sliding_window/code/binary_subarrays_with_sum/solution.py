"""
LC 930 - Binary Subarrays With Sum

Given a binary array nums and an integer goal, return the number of
non-empty subarrays with a sum equal to goal.

Examples:
```text
Input: nums = [1,0,1,0,1], goal = 2
Output: 4

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
```

Constraints:
- 1 <= nums.length <= 3 * 10^4
- nums[i] is either 0 or 1
- 0 <= goal <= nums.length
"""

from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Approach 1: prefix sum + hash map
        # count[prefix] = how many times this prefix sum has appeared
        count = defaultdict(int)
        count[0] = 1
        prefix = 0
        result = 0

        for num in nums:
            prefix += num
            # subarrays ending here with sum == goal
            result += count[prefix - goal]
            count[prefix] += 1

        return result

    def numSubarraysWithSum_atmost(self, nums: List[int], goal: int) -> int:
        # Approach 2: atMost(goal) - atMost(goal-1)
        # The atMost trick converts exact-count to two atMost calls
        def atMost(g: int) -> int:
            if g < 0:
                return 0
            left = curr_sum = res = 0
            for right in range(len(nums)):
                curr_sum += nums[right]
                # shrink window until sum <= g
                while curr_sum > g:
                    curr_sum -= nums[left]
                    left += 1
                # all subarrays ending at right with sum <= g
                res += right - left + 1
            return res

        return atMost(goal) - atMost(goal - 1)


if __name__ == '__main__':
    s = Solution()
    assert s.numSubarraysWithSum([1,0,1,0,1], 2) == 4
    assert s.numSubarraysWithSum([0,0,0,0,0], 0) == 15
    assert s.numSubarraysWithSum_atmost([1,0,1,0,1], 2) == 4
    assert s.numSubarraysWithSum_atmost([0,0,0,0,0], 0) == 15
    print("All tests passed.")
