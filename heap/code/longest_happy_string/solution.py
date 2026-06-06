import heapq


class Solution:
    """
    ## 1405. Longest Happy String

    A string `s` is called **happy** if it satisfies all of the following conditions:
    - `s` only contains the letters `'a'`, `'b'`, and `'c'`.
    - `s` does not contain `"aaa"`, `"bbb"`, or `"ccc"` as a substring.
    - `s` contains **at most** `a` occurrences of the letter `'a'`.
    - `s` contains **at most** `b` occurrences of the letter `'b'`.
    - `s` contains **at most** `c` occurrences of the letter `'c'`.

    Given three integers `a`, `b`, and `c`, return the **longest possible happy string**.
    If there are multiple longest happy strings, return any of them. If there is no such string,
    return the empty string `""`.

    ### Examples

    ```text
    Input: a = 1, b = 1, c = 7
    Output: "ccbccacc"
    ```

    ```text
    Input: a = 2, b = 2, c = 1
    Output: "aabbc" (or any valid)
    ```

    ```text
    Input: a = 7, b = 1, c = 0
    Output: "aabaa"
    ```

    ### Constraints
    - `0 <= a, b, c <= 100`
    - `a + b + c > 0`
    """

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Greedily pick the most frequent character that doesn't create 3 consecutive
        # If top char would create 3 in a row, use second most frequent instead
        # Re-add characters to heap after use if count > 0
        # O(a+b+c) — greedy: always pick most frequent char, limited to 2 consecutive
        heap = []
        for cnt, ch in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt < 0:
                heapq.heappush(heap, (cnt, ch))

        result = []
        while heap:
            cnt, ch = heapq.heappop(heap)
            # If last two chars are same as current, use second most frequent
            if len(result) >= 2 and result[-1] == result[-2] == ch:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                result.append(ch2)
                if cnt2 + 1 < 0:
                    heapq.heappush(heap, (cnt2 + 1, ch2))
                heapq.heappush(heap, (cnt, ch))
            else:
                result.append(ch)
                if cnt + 1 < 0:
                    heapq.heappush(heap, (cnt + 1, ch))

        return ''.join(result)


if __name__ == '__main__':
    s = Solution()

    def is_happy(res, a, b, c):
        if 'aaa' in res or 'bbb' in res or 'ccc' in res:
            return False
        if res.count('a') > a or res.count('b') > b or res.count('c') > c:
            return False
        return True

    res = s.longestDiverseString(1, 1, 7)
    assert is_happy(res, 1, 1, 7) and len(res) == 8, f"Got '{res}'"

    res = s.longestDiverseString(7, 1, 0)
    assert is_happy(res, 7, 1, 0) and len(res) == 5, f"Got '{res}'"

    res = s.longestDiverseString(2, 2, 1)
    assert is_happy(res, 2, 2, 1) and len(res) == 5, f"Got '{res}'"

    print("All tests passed.")
