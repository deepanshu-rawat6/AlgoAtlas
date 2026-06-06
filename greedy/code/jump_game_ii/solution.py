from typing import List


class Solution:
    """
    ## 45. Jump Game II

    Given a 0-indexed integer array nums, return the minimum number of jumps to reach
    the last index. You can always reach the last index.

    ### Example
    ```text
    Input:  nums = [2, 3, 1, 1, 4]
    Output: 2  (jump 1 step from index 0 to 1, then 3 steps to last index)

    Input:  nums = [2, 3, 0, 1, 4]
    Output: 2
    ```

    ### Constraints
    - 1 <= nums.length <= 10^4
    - 0 <= nums[i] <= 1000
    - The answer is guaranteed to exist.
    """

    def jump_dp(self, nums: List[int]) -> int:
        # O(n^2) time, O(n) space — DP
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]

    def jump(self, nums: List[int]) -> int:
        # Greedy BFS levels: at each jump, find the farthest reachable position
        # Increment jumps when we exhaust the current level's range
        # O(n) time, O(1) space — BFS-like level tracking
        jumps = cur_end = farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = farthest
        return jumps


if __name__ == '__main__':
    s = Solution()
    assert s.jump([2, 3, 1, 1, 4]) == 2
    assert s.jump([2, 3, 0, 1, 4]) == 2
    assert s.jump([1]) == 0
    assert s.jump_dp([2, 3, 1, 1, 4]) == 2
    print("All tests passed.")
