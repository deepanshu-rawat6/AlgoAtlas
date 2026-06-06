from typing import List


class Solution:
    """
    ## 763. Partition Labels

    You are given a string s. Partition it into as many parts as possible so that each letter
    appears in at most one part. Return a list of integers representing the size of each part.

    ### Example
    ```text
    Input:  s = "ababcbacadefegdehijhklij"
    Output: [9, 7, 8]
    (parts: "ababcbaca", "defegde", "hijhklij")

    Input:  s = "eccbbbbdec"
    Output: [10]
    ```

    ### Constraints
    - 1 <= s.length <= 500
    - s consists of lowercase English letters
    """

    def partitionLabels(self, s: str) -> List[int]:
        # Record last occurrence of each character
        # Extend current partition end to the last occurrence of each char seen
        # When current index reaches partition end, record partition size and start new one
        # O(n) time, O(1) space — record last occurrence of each character
        last = {c: i for i, c in enumerate(s)}
        result = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert s.partitionLabels("eccbbbbdec") == [10]
    assert s.partitionLabels("a") == [1]
    print("All tests passed.")
