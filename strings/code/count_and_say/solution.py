from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Approach 1: Iterative simulation O(n * L) where L = avg term length
        Start with "1", build each term by describing the previous one.
        """
        result = "1"
        for _ in range(n - 1):
            # group consecutive identical digits
            result = "".join(str(len(list(g))) + k for k, g in groupby(result))
        return result

    def countAndSay_manual(self, n: int) -> str:
        """
        Approach 2: Same idea without groupby — explicit two-pointer scan
        """
        result = "1"
        for _ in range(n - 1):
            nxt, i = [], 0
            while i < len(result):
                j = i
                while j < len(result) and result[j] == result[i]:
                    j += 1
                nxt.append(str(j - i) + result[i])
                i = j
            result = "".join(nxt)
        return result


# Tests
if __name__ == "__main__":
    sol = Solution()
    # Sequence: 1 -> 11 -> 21 -> 1211 -> 111221
    assert sol.countAndSay(1) == "1"
    assert sol.countAndSay(2) == "11"
    assert sol.countAndSay(3) == "21"
    assert sol.countAndSay(4) == "1211"
    assert sol.countAndSay(5) == "111221"
    assert sol.countAndSay_manual(4) == "1211"
    print("All tests passed")
