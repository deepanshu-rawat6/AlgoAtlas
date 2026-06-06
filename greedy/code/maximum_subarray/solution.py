from typing import List


class Solution:
    """
    ## 53. Maximum Subarray

    Given an integer array nums, find the subarray with the largest sum and return its sum.

    ### Example
    ```text
    Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6  (subarray [4, -1, 2, 1])

    Input:  nums = [1]
    Output: 1

    Input:  nums = [5, 4, -1, 7, 8]
    Output: 23
    ```

    ### Constraints
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    """

    def maxSubArray_brute(self, nums: List[int]) -> int:
        # O(n^2) time, O(1) space
        n, best = len(nums), nums[0]
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                best = max(best, curr)
        return best

    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's: extend current subarray or start fresh if current sum goes negative
        # Track global max throughout
        # O(n) time, O(1) space — Kadane's algorithm
        best = curr = nums[0]
        for x in nums[1:]:
            curr = max(x, curr + x)
            best = max(best, curr)
        return best


if __name__ == '__main__':
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert s.maxSubArray_brute([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print("All tests passed.")
