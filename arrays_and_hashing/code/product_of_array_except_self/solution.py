"""
# LC 238: Product of Array Except Self

Given an integer array `nums`, return an array `answer` such that `answer[i]`
is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit
integer. You must write an algorithm that runs in O(n) time and without using
the division operation.

## Examples

```text
Input:  nums = [1,2,3,4]
Output: [24,12,8,6]

Input:  nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Constraints
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer
"""
from typing import List


class Solution:
    def productExceptSelf_brute(self, nums: List[int]) -> List[int]:
        """Brute force — O(n^2) time, O(1) extra space."""
        # For each position, multiply all other elements — O(n^2)
        n = len(nums)
        answer = []
        for i in range(n):
            p = 1
            for j in range(n):
                if j != i:
                    p *= nums[j]
            answer.append(p)
        return answer

    def productExceptSelf_prefix_suffix(self, nums: List[int]) -> List[int]:
        """Prefix and suffix arrays — O(n) time, O(n) space."""
        # prefix[i] = product of all elements to the LEFT of i
        # suffix[i] = product of all elements to the RIGHT of i
        # answer[i] = prefix[i] * suffix[i] — no division needed
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        return [prefix[i] * suffix[i] for i in range(n)]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Single output array — O(n) time, O(1) extra space."""
        # First pass: fill answer[i] with running left-product up to i-1
        # Second pass: multiply in running right-product from i+1 onward
        # This avoids the O(n) extra arrays by reusing the output array
        n = len(nums)
        answer = [1] * n
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer


if __name__ == "__main__":
    s = Solution()

    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert s.productExceptSelf([1, 1]) == [1, 1]

    print("All tests passed.")
