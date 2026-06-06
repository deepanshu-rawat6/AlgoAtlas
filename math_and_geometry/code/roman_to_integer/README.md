# LC 13 — Roman to Integer

Convert a Roman numeral string to an integer. Roman numerals use subtraction when a smaller value precedes a larger one (e.g., IV = 4, IX = 9).

## Approaches

### 1. Left-to-Right Scan with Subtraction Rule
- **Time:** O(n) | **Space:** O(1)
- Map each symbol to its value. For each character, if the current value is less than the next value, subtract it; otherwise add it.

## Key Insight

The subtraction rule is the only special case in Roman numerals. A symbol is subtracted when it's followed by a larger symbol. Scanning left to right and comparing each symbol to the next handles all six subtraction cases (IV, IX, XL, XC, CD, CM) without needing to enumerate them explicitly.

## Edge Cases

- Single character: Just return its value.
- All additive (e.g., `"VIII"`): Sum all values.
- All subtractive (e.g., `"MCMXCIV"`): Multiple subtractions in sequence.
- Input is guaranteed valid (1–3999), so no need to validate.
