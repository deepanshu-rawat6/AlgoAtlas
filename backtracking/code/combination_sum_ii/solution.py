from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        ## 40. Combination Sum II

        Given a collection of candidate numbers (candidates) and a target number (target),
        find all unique combinations in candidates where the candidate numbers sum to target.

        Each number in candidates may only be used once in the combination.
        Note: The solution set must not contain duplicate combinations.

        ### Examples

        ```text
        Input:  candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
        Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

        Input:  candidates = [2, 5, 2, 1, 2], target = 5
        Output: [[1, 2, 2], [5]]
        ```

        ### Constraints
        - `1 <= candidates.length <= 100`
        - `1 <= candidates[i] <= 50`
        - `1 <= target <= 30`
        """
        # Sort so duplicates are adjacent; skip duplicate values at same level
        # Each candidate used at most once: recurse with i+1
        # O(2^n) time, O(n) stack space
        candidates.sort()
        result = []

        def bt(start, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                bt(i + 1, remaining - candidates[i], current)
                current.pop()

        bt(0, target, [])
        return result


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
    assert sorted(s.combinationSum2([2, 5, 2, 1, 2], 5)) == sorted([[1, 2, 2], [5]])
    print("All tests passed.")
