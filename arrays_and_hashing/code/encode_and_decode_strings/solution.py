"""
# LC 271: Encode and Decode Strings

Design an algorithm to encode a list of strings to a single string. The encoded
string is then sent over the network and is decoded back to the original list of
strings.

## Examples

```text
Input:  strs = ["Hello","World"]
Encoded: "5#Hello5#World"
Output: ["Hello","World"]

Input:  strs = [""]
Output: [""]
```

## Constraints
- 0 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] contains any possible characters out of 256 valid ASCII characters
"""
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Delimiter with escaping — O(n) time."""
        # Prefix each string with its length and '#' as delimiter
        # This handles strings containing any character including '#'
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Length-prefix decoding — O(n) time."""
        # Read length prefix up to '#', then extract exactly that many chars
        # Advance i past the extracted string to process the next one
        result, i = [], 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return result


if __name__ == "__main__":
    codec = Codec()

    for strs in [
        ["Hello", "World"],
        [""],
        [],
        ["a#b", "c#d"],
        ["with spaces", "and\nnewlines"],
    ]:
        assert codec.decode(codec.encode(strs)) == strs, strs

    print("All tests passed.")
