# Encode and Decode Strings (LC 271)

Design an algorithm to encode a list of strings into a single string, then decode it
back to the original list. The strings may contain any ASCII character including delimiters.

## Approaches

### 1. Length-Prefix Encoding — O(n) time, O(n) space
Encode each string as `"<length>#<string>"`. Decode by reading the length prefix up to `#`, then extracting exactly that many characters.

**Why it works:** The length prefix tells the decoder exactly how many characters to consume, so any character (including `#`) inside the string is handled correctly without ambiguity.

## Key Insight
Embed the length of each string before it. This makes the delimiter unambiguous regardless of what characters the string contains.

## Edge Cases
- Empty string `""` → encoded as `"0#"`, decoded back to `""`
- Empty list `[]` → encoded as `""`, decoded back to `[]`
- Strings containing `#` characters
- Strings containing spaces, newlines, or other special characters
- Very long strings (length prefix scales with string length)
