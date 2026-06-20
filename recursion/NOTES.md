# Recursion

## Core Intuition
Break a problem into a smaller version of itself; trust the recursive call to handle the subproblem, and only write the logic for the current step plus the base case.

## Problems

### Fibonacci Variants — No LC | Easy
- **Learn**: Base case + recurrence; two variants: fib(n)=fib(n-1)+fib(n-2), tribonacci
- **Mistake**: Forgetting memoization (exponential without it)
- **Complexity**: O(2^n) naive, O(n) memo time, O(n) space
- **Edge**: n=0, 1, 2

---

### Check Palindrome Recursive — No LC | Easy
- **Learn**: Compare first and last chars, recurse on middle slice
- **Mistake**: Modifying string instead of passing indices
- **Complexity**: O(n) time, O(n) space
- **Edge**: Empty string, single char

---

### String to Integer Recursive — No LC | Easy
- **Learn**: atoi(s) = atoi(s[:-1]) * 10 + digit(s[-1]); build up from left with digit_value * 10^(n-index-1)
- **Mistake**: Not handling sign
- **Complexity**: O(n) time, O(n) space
- **Edge**: Empty string, negative numbers

---

### Power Set Recursive — No LC | Medium
- **Learn**: Include/exclude each element; 2^n subsets total
- **Mistake**: Sharing mutable lists between branches (use `current[:]` when appending)
- **Complexity**: O(n*2^n) time, O(n) space
- **Edge**: Empty array → [[]]

---

### Sort Stack Using Recursion — No LC | Medium
- **Learn**: Pop top, sort remaining, insert top in correct position via helper
- **Mistake**: Trying to sort without a separate `insert_sorted` helper function
- **Complexity**: O(n^2) time, O(n) space
- **Edge**: Empty stack, single element

---

### Reverse Stack Using Recursion — No LC | Medium
- **Learn**: Pop all elements, push reversed using `insert_at_bottom` helper
- **Mistake**: Using an auxiliary stack (defeats the point of recursive approach)
- **Complexity**: O(n^2) time, O(n) space
- **Edge**: Empty stack

---

### Count Subsequences with Sum K — No LC | Medium
- **Learn**: At each index, branch include (add to sum) or exclude; count paths where sum==K at the end
- **Mistake**: Mutating the sum variable instead of passing it as a parameter
- **Complexity**: O(2^n) time, O(n) space
- **Edge**: K=0 (empty subsequence counts), negative numbers

---

### Check Subsequence with Sum K — No LC | Easy
- **Learn**: Same include/exclude tree, return True as soon as one path reaches K
- **Mistake**: Continuing recursion after finding the answer instead of propagating True
- **Complexity**: O(2^n) worst case, but early return in practice
- **Edge**: K=0 (empty subsequence counts), negative numbers

---

### Generate Binary Strings Without Consecutive Ones — No LC | Medium
- **Learn**: If last char placed is '1', next must be '0'; if '0', next can be '0' or '1'
- **Mistake**: Not tracking the last character placed
- **Complexity**: O(2^n) time, O(n) space
- **Edge**: n=1

---

### Print All Permutations — No LC | Medium
- **Learn**: Swap element at current index with each element from current to end; recurse; swap back
- **Mistake**: Not swapping back (backtracking step) — leaves the array in a mutated state
- **Complexity**: O(n*n!) time, O(n) space
- **Edge**: n=1

---

### Generate All Balanced Parentheses — LC 22 | Medium
- **Learn**: Track open/close counts; add '(' if open<n; add ')' if close<open
- **Mistake**: Using a single depth counter instead of separate open/close counts
- **Complexity**: O(4^n/sqrt(n)) time, O(n) space
- **Edge**: n=0 → [] or [[]]

---

### Word Break Recursive — No LC | Medium
- **Learn**: Try every prefix; if it's in the dictionary, recurse on the suffix
- **Mistake**: Not memoizing — without it, complexity is exponential
- **Complexity**: O(2^n) naive, O(n^2) with memo time, O(n) space
- **Edge**: Empty string → True

---

### Letter Case Permutation — LC 784 | Medium
- **Learn**: At each character, if letter: branch lowercase and uppercase; if digit: single branch forward
- **Mistake**: Trying to enumerate positions first instead of branching per character during traversal
- **Complexity**: O(2^L * n) time where L=letter count, O(n) space
- **Edge**: All digits → exactly one result

---

### Josephus Problem — No LC | Medium
- **Learn**: J(n,k) = (J(n-1,k) + k) % n; base case J(1,k)=0; recurrence eliminates the circular structure
- **Mistake**: Simulating the circle iteratively (works but O(n*k) vs O(n) recursive)
- **Complexity**: O(n) time, O(n) space
- **Edge**: n=1

---

### Tower of Hanoi — No LC | Medium
- **Learn**: Move n-1 disks to aux, move nth disk to dest, move n-1 from aux to dest; exactly 2^n-1 moves
- **Mistake**: Getting the source/dest/aux argument order wrong in the two recursive calls
- **Complexity**: O(2^n) time, O(n) space
- **Edge**: n=1 (single move)

---

### Flood Fill Recursive — LC 733 | Easy
- **Learn**: DFS from start pixel; change color and recurse on 4 neighbors if they match original color
- **Mistake**: Not saving original color before starting — causes infinite loop if newColor == oldColor
- **Complexity**: O(m*n) time, O(m*n) space
- **Edge**: newColor == oldColor (return immediately, no change needed)

---

### Count Good Numbers — LC 1922 | Medium
- **Learn**: Even positions (0-indexed) have 5 choices {0,2,4,6,8}; odd positions have 4 choices {2,3,5,7}; use fast modular exponentiation
- **Mistake**: Iterating n times instead of using fast power (O(n) vs O(log n))
- **Complexity**: O(log n) time, O(log n) space
- **Edge**: n=1

---

### Recursive Atoi — No LC | Medium
- **Learn**: atoi(s, n) = atoi(s, n-1) * 10 + (s[n-1] - '0'); pass length as parameter
- **Mistake**: Not passing length as a parameter — makes it hard to track position
- **Complexity**: O(n) time, O(n) space
- **Edge**: Empty string

---

### K-th Symbol in Grammar — LC 779 | Medium
- **Learn**: k-th element of row n = parent's value XOR (1 if k is right child, else 0); parent is at ceil(k/2)
- **Mistake**: Building entire rows (exponential space) instead of tracing back to parent
- **Complexity**: O(n) time, O(n) space
- **Edge**: k=1 always gives 0

---

### Sum of All Subset XOR Totals — LC 1863 | Easy
- **Learn**: Result = (XOR of all elements) * 2^(n-1); each bit contributes independently across half the subsets
- **Mistake**: Actually enumerating all 2^n subsets instead of using the O(n) formula
- **Complexity**: O(n) time, O(1) space
- **Edge**: n=1
