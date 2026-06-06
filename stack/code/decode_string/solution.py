"""
# 394. Decode String

## Problem
Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside
the square brackets is repeated exactly `k` times. `k` is guaranteed to be a
positive integer. You may assume the input is always valid — no extra white
spaces, square brackets are well-formed, etc.

Note: The original data does not contain any digits; all digits are only for
repeat counts `k`. For example, there won't be input like `3a` or `2[4]`.

## Examples
```text
Input:  s = "3[a]2[bc]"
Output: "aaabcbc"

Input:  s = "3[a2[c]]"
Output: "accaccacc"

Input:  s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Constraints
- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `[]`
- `s` is guaranteed to be a valid input
- All integers are in the range `[1, 300]`
"""


class Solution:
    def decodeString_stack(self, s: str) -> str:
        # On '[': save current (count, string) to stack, reset both
        # On ']': pop saved state, append current string repeated count times
        # Handles nested brackets because each level is saved/restored on stack
        # O(n) time, O(n) space — iterative stack of (repeat_count, built_string)
        stack = []
        cur_str = ""
        cur_num = 0
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == "[":
                stack.append((cur_num, cur_str))
                cur_str, cur_num = "", 0
            elif ch == "]":
                num, prev_str = stack.pop()
                cur_str = prev_str + cur_str * num
            else:
                cur_str += ch
        return cur_str

    def decodeString(self, s: str) -> str:
        # Recursive descent: parse number, skip '[', recurse for inner, skip ']'
        # Returns (decoded_string, next_index) so caller knows where to continue
        # O(n) time, O(n) space — recursive descent with index pointer
        def decode(i: int):
            result = ""
            while i < len(s) and s[i] != "]":
                if s[i].isdigit():
                    num = 0
                    while s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    i += 1  # skip '['
                    inner, i = decode(i)
                    i += 1  # skip ']'
                    result += inner * num
                else:
                    result += s[i]
                    i += 1
            return result, i

        return decode(0)[0]


if __name__ == "__main__":
    s = Solution()
    assert s.decodeString_stack("3[a]2[bc]") == "aaabcbc"
    assert s.decodeString_stack("3[a2[c]]") == "accaccacc"
    assert s.decodeString_stack("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert s.decodeString("3[a]2[bc]") == "aaabcbc"
    assert s.decodeString("3[a2[c]]") == "accaccacc"
    assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    print("All tests passed.")
