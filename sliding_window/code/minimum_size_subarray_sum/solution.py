from typing import List


class Solution:
    """
    ## 209. Minimum Size Subarray Sum

    Given an array of positive integers `nums` and a positive integer `target`, return
    the minimal length of a subarray whose sum is greater than or equal to `target`.
    If there is no such subarray, return `0` instead.

    ### Examples

    ```text
    Input:  target = 7, nums = [2, 3, 1, 2, 4, 3]
    Output: 2
    Explanation: [4, 3] has the minimal length under the problem constraint.

    Input:  target = 4, nums = [1, 4, 4]
    Output: 1

    Input:  target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
    Output: 0
    ```

    ### Constraints

    - `1 <= target <= 10^9`
    - `1 <= nums.length <= 10^5`
    - `1 <= nums[i] <= 10^4`
    """

    def minSubArrayLen_brute(self, target: int, nums: List[int]) -> int:
        # Expand from each start until sum >= target — O(n^2)
        # O(n^2) time, O(1) space
        best = float("inf")
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total >= target:
                    best = min(best, j - i + 1)
                    break
        return 0 if best == float("inf") else best

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Expand right to grow sum; shrink left while sum still >= target
        # Each element is added and removed at most once — O(n) total
        # O(n) time, O(1) space
        left = total = 0
        best = float("inf")
        for right, num in enumerate(nums):
            total += num
            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if best == float("inf") else best


if __name__ == "__main__":
    sol = Solution()
    assert sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert sol.minSubArrayLen(4, [1, 4, 4]) == 1
    assert sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert sol.minSubArrayLen_brute(7, [2, 3, 1, 2, 4, 3]) == 2
    assert sol.minSubArrayLen_brute(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    print("All tests passed.")
