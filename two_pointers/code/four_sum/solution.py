"""
## LC 18 — 4Sum

Given an array `nums` of `n` integers and an integer `target`, return all unique
quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that all indices are distinct
and `nums[a] + nums[b] + nums[c] + nums[d] == target`.

### Examples

```text
Input:  nums = [1, 0, -1, 0, -2, 2], target = 0
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

Input:  nums = [2, 2, 2, 2, 2], target = 8
Output: [[2, 2, 2, 2]]
```

### Constraints

- 1 <= nums.length <= 200
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def method_brute_force(self, nums: List[int], target: int) -> List[List[int]]:
        """O(n^4) time | O(n) space (result)"""
        # Try all quadruplets — O(n^4); use set to deduplicate
        n = len(nums)
        result = set()
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            result.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))
        return [list(t) for t in result]

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """O(n^3) time | O(1) extra space"""
        # Sort, fix two outer indices i and j, then use two pointers for the rest
        # Skip duplicate values at each level to avoid duplicate quadruplets
        # Inner two-pointer converges: move lo right if sum too small, hi left if too large
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo, hi = j + 1, n - 1
                while lo < hi:
                    s = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if s == target:
                        result.append([nums[i], nums[j], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif s < target:
                        lo += 1
                    else:
                        hi -= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(sol.fourSum([2, 2, 2, 2, 2], 8))        # [[2,2,2,2]]
