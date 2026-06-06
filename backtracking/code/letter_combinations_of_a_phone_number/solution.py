from typing import List
from collections import deque


class Solution:
    PHONE = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    def letterCombinations_bt(self, digits: str) -> List[str]:
        """
        ## 17. Letter Combinations of a Phone Number

        Given a string containing digits from 2-9 inclusive, return all possible letter
        combinations that the number could represent. Return the answer in any order.

        A mapping of digits to letters (just like on the telephone buttons) is given below.
        Note that 1 does not map to any letters.

        ### Examples

        ```text
        Input:  digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

        Input:  digits = ""
        Output: []

        Input:  digits = "2"
        Output: ["a","b","c"]
        ```

        ### Constraints
        - `0 <= digits.length <= 4`
        - `digits[i]` is a digit in the range `['2', '9']`.
        """
        # O(4^n * n) time, O(n) stack space
        if not digits:
            return []
        result = []

        def bt(idx, current):
            if idx == len(digits):
                result.append(current)
                return
            for ch in self.PHONE[digits[idx]]:
                bt(idx + 1, current + ch)

        bt(0, '')
        return result

    def letterCombinations(self, digits: str) -> List[str]:
        """Iterative BFS: expand combinations level by level."""
        # Map each digit to its letters; DFS appending one letter per digit
        # Add to result when path length equals number of digits
        # O(4^n * n) time, O(4^n) space
        if not digits:
            return []
        queue = deque([''])
        for digit in digits:
            for _ in range(len(queue)):
                prefix = queue.popleft()
                for ch in self.PHONE[digit]:
                    queue.append(prefix + ch)
        return list(queue)


if __name__ == '__main__':
    s = Solution()
    expected = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    for fn in (s.letterCombinations_bt, s.letterCombinations):
        assert sorted(fn("23")) == expected
        assert fn("") == []
        assert sorted(fn("2")) == ["a", "b", "c"]
    print("All tests passed.")
