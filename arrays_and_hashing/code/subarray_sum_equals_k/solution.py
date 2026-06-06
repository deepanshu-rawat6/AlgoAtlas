"""
# LC 560: Subarray Sum Equals K

Given an array of integers `nums` and an integer `k`, return the total number
of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

```text
Input:  nums = [1,1,1], k = 2
Output: 2

Input:  nums = [1,2,3], k = 3
Output: 2
```

## Constraints
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
"""
from typing import List
from collections import defaultdict


class Solution:
    def subarraySum_brute(self, nums: List[int], k: int) -> int:
        """Brute force — O(n^2) time, O(1) space."""
        # Try all subarrays starting at i — O(n^2)
        count = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1
        return count

    def subarraySum(self, nums: List[int], k: int) -> int:
        """Prefix sum with hash map — O(n) time, O(n) space."""
        # prefix[j] - prefix[i] == k  =>  prefix[i] == prefix[j] - k
        # Store how many times each prefix sum has occurred
        # freq[0]=1 handles subarrays starting from index 0
        count = 0
        prefix = 0
        freq: dict = defaultdict(int)
        freq[0] = 1
        for n in nums:
            prefix += n
            count += freq[prefix - k]
            freq[prefix] += 1
        return count


if __name__ == "__main__":
    s = Solution()

    assert s.subarraySum([1, 1, 1], 2) == 2
    assert s.subarraySum([1, 2, 3], 3) == 2
    assert s.subarraySum([1], 0) == 0
    assert s.subarraySum([-1, -1, 1], 0) == 1

    print("All tests passed.")
