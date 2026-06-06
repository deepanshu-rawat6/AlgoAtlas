from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        ## 22. Generate Parentheses

        Given n pairs of parentheses, write a function to generate all combinations
        of well-formed parentheses.

        ### Examples

        ```text
        Input:  n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]

        Input:  n = 1
        Output: ["()"]
        ```

        ### Constraints
        - `1 <= n <= 8`
        """
        # Add '(' if open count < n; add ')' if close count < open count
        # Valid string when both counts reach n
        # O(4^n / sqrt(n)) time (Catalan number), O(n) stack space
        result = []

        def bt(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                bt(current + '(', open_count + 1, close_count)
            if close_count < open_count:
                bt(current + ')', open_count, close_count + 1)

        bt('', 0, 0)
        return result


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.generateParenthesis(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert s.generateParenthesis(1) == ["()"]
    print("All tests passed.")
