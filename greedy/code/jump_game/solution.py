from typing import List


class Solution:
    """
    ## 55. Jump Game

    Given an integer array nums where nums[i] is the maximum jump length from index i,
    return true if you can reach the last index starting from index 0.

    ### Example
    ```text
    Input:  nums = [2, 3, 1, 1, 4]
    Output: true

    Input:  nums = [3, 2, 1, 0, 4]
    Output: false
    ```

    ### Constraints
    - 1 <= nums.length <= 10^4
    - 0 <= nums[i] <= 10^5
    """

    def canJump_dp(self, nums: List[int]) -> bool:
        # O(n^2) time, O(n) space — DP
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        return dp[-1]

    def canJump(self, nums: List[int]) -> bool:
        # Track the farthest index reachable; if current index exceeds it, can't proceed
        # Update farthest at each step; return True if we reach or pass last index
        # O(n) time, O(1) space — track farthest reachable index
        farthest = 0
        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + jump)
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4]) == True
    assert s.canJump([3, 2, 1, 0, 4]) == False
    assert s.canJump([0]) == True
    assert s.canJump_dp([2, 3, 1, 1, 4]) == True
    assert s.canJump_dp([3, 2, 1, 0, 4]) == False
    print("All tests passed.")
