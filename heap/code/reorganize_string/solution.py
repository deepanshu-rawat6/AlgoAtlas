import heapq
from collections import Counter


class Solution:
    """
    ## 767. Reorganize String

    Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are
    not the same. Return any possible rearrangement of `s` or return `""` if not possible.

    ### Examples

    ```text
    Input: s = "aab"
    Output: "aba"
    ```

    ```text
    Input: s = "aaab"
    Output: ""
    ```

    ```text
    Input: s = "vvvlo"
    Output: "vlvov" (or any valid rearrangement)
    ```

    ### Constraints
    - `1 <= s.length <= 500`
    - `s` consists of lowercase English letters.
    """

    def reorganizeString(self, s: str) -> str:
        # Always place the most frequent remaining character
        # Use max-heap; after placing, cool down for one step before re-adding
        # O(n log k) where k=26 — greedy: always place most frequent char not equal to last placed
        counts = Counter(s)
        heap = [(-cnt, ch) for ch, cnt in counts.items()]
        heapq.heapify(heap)

        result = []
        prev_cnt, prev_ch = 0, ''

        while heap:
            cnt, ch = heapq.heappop(heap)
            result.append(ch)
            # Re-push previous character now that it's no longer adjacent
            if prev_cnt < 0:
                heapq.heappush(heap, (prev_cnt, prev_ch))
            prev_cnt, prev_ch = cnt + 1, ch  # cnt is negative, so +1 decrements

        return ''.join(result) if len(result) == len(s) else ''


if __name__ == '__main__':
    s = Solution()

    res = s.reorganizeString("aab")
    assert res == "aba", f"Got {res}"

    res = s.reorganizeString("aaab")
    assert res == ""

    res = s.reorganizeString("a")
    assert res == "a"

    # Validate no two adjacent chars are same for longer inputs
    res = s.reorganizeString("vvvlo")
    assert res and all(res[i] != res[i + 1] for i in range(len(res) - 1))

    res = s.reorganizeString("aabbcc")
    assert res and all(res[i] != res[i + 1] for i in range(len(res) - 1))

    print("All tests passed.")
