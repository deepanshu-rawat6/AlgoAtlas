"""
# LC 698: Partition to K Equal Sum Subsets

Given an integer array `nums` and an integer `k`, return true if it is possible to
divide the array into `k` non-empty subsets whose sums are all equal.

## Examples
```text
Input:  nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: true

Input:  nums = [1, 2, 3, 4], k = 3
Output: false
```

## Constraints
- 1 <= k <= nums.length <= 16
- 1 <= nums[i] <= 10^4
- The frequency of each element is in the range [1, 4].
"""
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        ## 698. Partition to K Equal Sum Subsets

        Given an integer array nums and an integer k, return true if it is possible to
        divide this array into k non-empty subsets whose sums are all equal.

        ### Examples

        ```text
        Input:  nums = [4, 3, 2, 3, 5, 2, 1], k = 4
        Output: true
        Explanation: (5), (1,4), (2,3), (2,3)

        Input:  nums = [1, 2, 3, 4], k = 3
        Output: false
        ```

        ### Constraints
        - `1 <= k <= nums.length <= 16`
        - `1 <= nums[i] <= 10^4`
        - The frequency of each element is in the range [1, 4].
        """
        # Try placing each unused number into one of k buckets
        # Skip bucket if it already has the same sum as a previous bucket (pruning)
        # Return True when all k buckets reach target sum
        # O(k * 2^n) time with bitmask memoization, O(2^n) space
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        n = len(nums)
        memo = {}

        def bt(mask, current_sum):
            if mask == (1 << n) - 1:
                return True
            if mask in memo:
                return memo[mask]
            for i in range(n):
                if mask & (1 << i):
                    continue
                next_sum = current_sum + nums[i]
                if next_sum > target:
                    continue
                new_mask = mask | (1 << i)
                if bt(new_mask, next_sum % target):
                    memo[mask] = True
                    return True
            memo[mask] = False
            return False

        return bt(0, 0)


if __name__ == '__main__':
    s = Solution()
    assert s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) is True
    assert s.canPartitionKSubsets([1, 2, 3, 4], 3) is False
    assert s.canPartitionKSubsets([2, 2, 2, 2], 2) is True
    print("All tests passed.")
