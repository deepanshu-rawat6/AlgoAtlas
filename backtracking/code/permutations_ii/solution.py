from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        ## 47. Permutations II

        Given a collection of numbers, nums, that might contain duplicates, return all
        possible unique permutations in any order.

        ### Examples

        ```text
        Input:  nums = [1, 1, 2]
        Output: [[1,1,2],[1,2,1],[2,1,1]]

        Input:  nums = [1, 2, 3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        ```

        ### Constraints
        - `1 <= nums.length <= 8`
        - `-10 <= nums[i] <= 10`
        """
        # Sort to group duplicates; use a 'used' array to track which elements are in current path
        # Skip duplicate: if nums[i]==nums[i-1] and nums[i-1] not used, skip to avoid duplicate permutations
        # O(n!) time, O(n) stack space
        nums.sort()
        result = []
        used = [False] * len(nums)

        def bt(current):
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # skip duplicate: same value as previous, and previous not used in this path
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                current.append(nums[i])
                bt(current)
                current.pop()
                used[i] = False

        bt([])
        return result


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.permuteUnique([1, 1, 2])) == sorted([[1, 1, 2], [1, 2, 1], [2, 1, 1]])
    assert len(s.permuteUnique([1, 2, 3])) == 6
    print("All tests passed.")
