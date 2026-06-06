"""
# 71. Simplify Path

## Problem
Given an absolute path for a Unix-style file system, which begins with a
slash `'/'`, transform this path into its simplified canonical path.

Rules:
- A single period `'.'` refers to the current directory.
- A double period `'..'` refers to the parent directory.
- Multiple consecutive slashes are treated as a single slash.
- Any other string is a valid directory or file name.

The canonical path must:
- Start with a single slash `'/'`
- Not end with a trailing slash (unless it is the root)
- Not have consecutive slashes
- Not contain `.` or `..`

## Examples
```text
Input:  path = "/home/"
Output: "/home"

Input:  path = "/../"
Output: "/"

Input:  path = "/home//foo/"
Output: "/home/foo"

Input:  path = "/a/./b/../../c/"
Output: "/c"
```

## Constraints
- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, period `'.'`, slash `'/'`, or
  underscore `'_'`
- `path` is a valid absolute Unix path
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split on '/' to get path components; skip empty strings and '.'
        # '..' pops the last directory from stack (go up one level)
        # Join remaining stack with '/' and prepend root '/'
        # O(n) time, O(n) space — split on '/', process with stack
        stack = []
        for part in path.split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != ".":
                stack.append(part)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    s = Solution()
    assert s.simplifyPath("/home/") == "/home"
    assert s.simplifyPath("/../") == "/"
    assert s.simplifyPath("/home//foo/") == "/home/foo"
    assert s.simplifyPath("/a/./b/../../c/") == "/c"
    assert s.simplifyPath("/") == "/"
    print("All tests passed.")
