from typing import List


class Solution:
    def permute_used(self, nums: List[int]) -> List[List[int]]:
        """
        ## 46. Permutations

        Given an array nums of distinct integers, return all the possible permutations.
        You can return the answer in any order.

        ### Examples

        ```text
        Input:  nums = [1, 2, 3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        Input:  nums = [0, 1]
        Output: [[0,1],[1,0]]

        Input:  nums = [1]
        Output: [[1]]
        ```

        ### Constraints
        - `1 <= nums.length <= 6`
        - `-10 <= nums[i] <= 10`
        - All integers of nums are unique.
        """
        # O(n!) time, O(n) extra space for used set
        result = []
        used = [False] * len(nums)

        def bt(current):
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current.append(nums[i])
                    bt(current)
                    current.pop()
                    used[i] = False

        bt([])
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        """Swap-based backtracking: swap element into current position."""
        # Swap current index with each subsequent index to generate permutations
        # Backtrack by swapping back after recursion
        # O(n!) time, O(1) extra space (in-place swaps)
        result = []

        def bt(start):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                bt(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        bt(0)
        return result


if __name__ == '__main__':
    s = Solution()
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    for fn in (s.permute_used, s.permute):
        assert sorted(fn([1, 2, 3])) == sorted(expected)
        assert sorted(fn([0, 1])) == sorted([[0, 1], [1, 0]])
    print("All tests passed.")
