# Simplify Path (LC 71)

Given an absolute Unix-style file path, return its simplified canonical form — no `.`, `..`, double slashes, or trailing slash.

## Approaches

### 1. Stack with Split
- **Time:** O(n) | **Space:** O(n)
- Split the path on `"/"` to get components. Empty strings and `"."` are skipped.
- `".."` pops the last directory from the stack (go up one level), if the stack is non-empty.
- Any other component is a valid directory name — push it.
- Join the stack with `"/"` and prepend `"/"` for the root.

## Key Insight

Splitting on `"/"` handles multiple consecutive slashes automatically (they produce empty strings, which are filtered out). The stack models the current directory path: `..` undoes the last directory, and any other name extends it. The stack at the end represents the canonical path from root.

## Edge Cases

- `"/../"` → can't go above root → stack stays empty → result is `"/"`.
- Multiple consecutive slashes (`"/home//foo/"`) → empty strings from split are ignored.
- Trailing slash (`"/home/"`) → trailing empty string ignored → `"/home"`.
- `"."` at any position → skip (stay in current directory).
- Path that is just `"/"` → stack empty → result is `"/"`.
