from collections import defaultdict

class Solution:
    def countSubstrings(self, s: str, k: int) -> int:
        # exactly(k) = atMost(k) - atMost(k-1)
        def at_most(k: int) -> int:
            count = left = 0
            freq = defaultdict(int)
            for right, ch in enumerate(s):
                freq[ch] += 1
                # Shrink window until distinct chars <= k
                while len(freq) > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1
                # All substrings ending at `right` with left..right are valid
                count += right - left + 1
            return count

        return at_most(k) - at_most(k - 1)


# Tests
if __name__ == '__main__':
    sol = Solution()
    assert sol.countSubstrings("aba", 2) == 3   # "ab","ba","aba"
    assert sol.countSubstrings("aaa", 1) == 6   # all substrings
    assert sol.countSubstrings("abc", 1) == 3   # "a","b","c"
    assert sol.countSubstrings("abc", 2) == 2   # "ab","bc"
    assert sol.countSubstrings("abc", 3) == 1   # "abc"
    print("All tests passed.")
