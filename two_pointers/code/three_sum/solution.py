from typing import List


class Solution:
    """
    ## LC 15 — 3Sum

    Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]`
    such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
    The solution set must not contain duplicate triplets.

    ### Examples

    ```text
    Input:  nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

    Input:  nums = [0, 1, 1]
    Output: []

    Input:  nums = [0, 0, 0]
    Output: [[0, 0, 0]]
    ```

    ### Constraints

    - 3 <= nums.length <= 3000
    - -10^5 <= nums[i] <= 10^5
    """

    def method_brute_force(self, nums: List[int]) -> List[List[int]]:
        """O(n^3) time | O(n) space (result)"""
        # Try all triplets — O(n^3); use a set to avoid duplicate triplets
        n = len(nums)
        result = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return [list(t) for t in result]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """O(n^2) time | O(1) extra space"""
        # Sort first so we can use two pointers and skip duplicates easily
        # Fix one element i, then use two pointers lo/hi for the remaining pair
        # Skip duplicate values of i, lo, hi to avoid duplicate triplets
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s == 0:
                    result.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif s < 0:
                    lo += 1
                else:
                    hi -= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    print(sol.threeSum([0, 1, 1]))               # []
    print(sol.threeSum([0, 0, 0]))               # [[0,0,0]]
