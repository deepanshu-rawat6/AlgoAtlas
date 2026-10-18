# Backtracking

```mermaid
mindmap
  root((Backtracking))
    Subsets
      Sum of All Subsets XOR Total LC1863
      Subsets LC78
      Subsets II LC90
    Combinations
      Combination Sum LC39
      Combination Sum II LC40
      Combination Sum III LC216
      Combinations LC77
      Letter Combinations of Phone Number LC17
    Permutations
      Permutations LC46
      Permutations II LC47
    Grid Search
      Word Search LC79
      Rat in a Maze
      Sudoku Solver LC37
    Constraint Satisfaction
      N Queens LC51
      N Queens II LC52
      Generate Parentheses LC22
      M Coloring Problem
    Partitioning
      Palindrome Partitioning LC131
      Matchsticks to Square LC473
      Partition to K Equal Sum Subsets LC698
      Word Break II LC140
    Expression Building
      Expression Add Operators LC282
```

## Problem List

| # | Problem | LC | Difficulty |
|---|---------|-----|------------|
| 1 | Sum of All Subsets XOR Total | [1863](https://leetcode.com/problems/sum-of-all-subset-xor-totals/) | 🟢 Easy |
| 2 | Subsets | [78](https://leetcode.com/problems/subsets/) | 🟡 Medium |
| 3 | Combination Sum | [39](https://leetcode.com/problems/combination-sum/) | 🟡 Medium |
| 4 | Combination Sum II | [40](https://leetcode.com/problems/combination-sum-ii/) | 🟡 Medium |
| 5 | Combinations | [77](https://leetcode.com/problems/combinations/) | 🟡 Medium |
| 6 | Permutations | [46](https://leetcode.com/problems/permutations/) | 🟡 Medium |
| 7 | Subsets II | [90](https://leetcode.com/problems/subsets-ii/) | 🟡 Medium |
| 8 | Permutations II | [47](https://leetcode.com/problems/permutations-ii/) | 🟡 Medium |
| 9 | Generate Parentheses | [22](https://leetcode.com/problems/generate-parentheses/) | 🟡 Medium |
| 10 | Word Search | [79](https://leetcode.com/problems/word-search/) | 🟡 Medium |
| 11 | Palindrome Partitioning | [131](https://leetcode.com/problems/palindrome-partitioning/) | 🟡 Medium |
| 12 | Letter Combinations of Phone Number | [17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | 🟡 Medium |
| 13 | Matchsticks to Square | [473](https://leetcode.com/problems/matchsticks-to-square/) | 🟡 Medium |
| 14 | Partition to K Equal Sum Subsets | [698](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | 🟡 Medium |
| 15 | N Queens | [51](https://leetcode.com/problems/n-queens/) | 🔴 Hard |
| 16 | N Queens II | [52](https://leetcode.com/problems/n-queens-ii/) | 🔴 Hard |
| 17 | Word Break II | [140](https://leetcode.com/problems/word-break-ii/) | 🔴 Hard |
| 18 | Combination Sum III | [216](https://leetcode.com/problems/combination-sum-iii/) | 🟡 Medium |
| 19 | Rat in a Maze | — | 🟡 Medium |
| 20 | M Coloring Problem | — | 🟡 Medium |
| 21 | Sudoku Solver | [37](https://leetcode.com/problems/sudoku-solver/) | 🔴 Hard |
| 22 | Expression Add Operators | [282](https://leetcode.com/problems/expression-add-operators/) | 🔴 Hard |

---

## Approach Diagrams

### Backtracking Template

```mermaid
flowchart TD
    A[backtrack state] --> B{"Base case met?"}
    B -- Yes --> C[Add to results<br>or count]
    B -- No --> D[Loop over choices]
    D --> E[CHOOSE:<br>add choice to state]
    E --> F[EXPLORE:<br>backtrack next state]
    F --> G[UNCHOOSE:<br>remove choice from state]
    G --> D
    C --> H[Return]
```

### Subsets vs Combinations vs Permutations

```mermaid
flowchart TD
    A[What are you building?] --> B{"Order matters?"}
    B -- No --> C{"Repetition allowed?"}
    B -- Yes --> D{"Duplicates in input?"}
    C -- No, pick any subset --> E[Subsets<br>LC 78, 90<br>start index moves forward]
    C -- Yes, reuse elements --> F[Combination Sum<br>LC 39<br>start index stays]
    C -- No, pick exactly k --> G[Combinations<br>LC 77<br>start index moves forward]
    D -- No --> H[Permutations<br>LC 46<br>use visited array]
    D -- Yes --> I[Permutations II<br>LC 47<br>sort + skip duplicates]
```

### Duplicate Handling Pattern

```mermaid
flowchart TD
    A[Input has duplicates] --> B[Sort the array first]
    B --> C[In the loop at each level]
    C --> D{"i > start AND nums i == nums i-1?"}
    D -- Yes --> E[Skip: continue<br>avoids duplicate branches]
    D -- No --> F[Choose nums i]
    F --> G[Recurse with i+1<br>or i for reuse]
    G --> H[Unchoose]
    H --> C
    E --> C
    C --> I[LC 40 Combo Sum II<br>LC 90 Subsets II<br>LC 47 Permutations II]
```

### Constraint Satisfaction — N-Queens Flow

```mermaid
flowchart TD
    A[Place queen in row r] --> B{"row == n?"}
    B -- Yes --> C[Valid solution found]
    B -- No --> D[Try each column c in row r]
    D --> E{"Is c safe? check col, diag, anti-diag"}
    E -- No --> F[Try next column]
    E -- Yes --> G[Place queen at r,c<br>mark col, diag, anti-diag]
    G --> H[Recurse row r+1]
    H --> I[Remove queen<br>unmark sets]
    I --> F
    F --> D
```

### Pruning Strategies

```mermaid
flowchart TD
    A[Pruning Type] --> B{"When to prune?"}
    B -- Sum exceeds target --> C[Combination Sum<br>if curr_sum > target: return]
    B -- Remaining elements<br>not enough --> D[Combinations<br>if n-i+1 < k-len: return]
    B -- Partition impossible --> E[Matchsticks / K Subsets<br>if bucket_sum > target: skip<br>sort descending first]
    B -- Invalid constraint --> F[N-Queens<br>if col or diag used: skip]
    B -- Word mismatch --> G[Word Search<br>if board char != word char: return]
    B -- Parentheses invalid --> H[Generate Parens<br>if close > open: return<br>if open > n: return]
```

---

## Complexity Summary

| Problem | Time | Space | Pattern |
|---------|------|-------|---------|
| sum_of_all_subset_xor_totals | O(2ⁿ) | O(n) | Include/exclude |
| subsets | O(n·2ⁿ) | O(n) | Include/exclude |
| combination_sum | O(2^(t/min)) | O(t/min) | Unbounded pick |
| combination_sum_ii | O(2ⁿ) | O(n) | Sort + skip dups |
| combinations | O(k·C(n,k)) | O(k) | Fixed-size pick |
| permutations | O(n·n!) | O(n) | Visited array |
| subsets_ii | O(n·2ⁿ) | O(n) | Sort + skip dups |
| permutations_ii | O(n·n!) | O(n) | Sort + skip dups |
| generate_parentheses | O(4ⁿ/√n) | O(n) | Open/close count |
| word_search | O(m·n·4^L) | O(L) | Grid DFS + backtrack |
| palindrome_partitioning | O(n·2ⁿ) | O(n²) | Palindrome check + split |
| letter_combinations_of_a_phone_number | O(4^n·n) | O(n) | Digit-to-letters map |
| matchsticks_to_square | O(k·2ⁿ) | O(n) | Partition into k buckets |
| partition_to_k_equal_sum_subsets | O(k·2ⁿ) | O(n) | Partition into k buckets |
| n_queens | O(n!) | O(n) | Constraint satisfaction |
| n_queens_ii | O(n!) | O(n) | Constraint satisfaction |
| word_break_ii | O(2ⁿ) | O(n) | Prefix match + memo |
| combination_sum_iii | O(k·C(9,k)) | O(k) | Fixed-size pick with sum |
| rat_in_a_maze | O(4^(m·n)) | O(m·n) | Grid DFS + backtrack |
| m_coloring_problem | O(m^V) | O(V) | Constraint coloring |
| sudoku_solver | O(9^m) | O(1) | Constraint satisfaction |
| expression_add_operators | O(4^n·n) | O(n) | Expression building |

---

## Study Order

```mermaid
flowchart LR
    subgraph W1["Week 1: Subsets + Permutations"]
        b1["sum_xor_totals(1863) → subsets(78) → subsets_ii(90)"]
        b2["permutations(46) → permutations_ii(47)"]
    end

    subgraph W2["Week 2: Combinations"]
        b3["combination_sum(39) → combination_sum_ii(40) → combination_sum_iii(216)"]
        b4["combinations(77) → letter_combinations(17)"]
    end

    subgraph W3["Week 3: String + Grid Backtracking"]
        b5["generate_parentheses(22) → word_search(79)"]
        b6["palindrome_partitioning(131) → word_break_ii(140)"]
    end

    subgraph W4["Week 4: Partitioning"]
        b7["matchsticks_to_square(473) → partition_k_subsets(698)"]
    end

    subgraph W5["Week 5: Hard Constraint Satisfaction"]
        b8["n_queens(51) → n_queens_ii(52) → rat_in_a_maze"]
        b9["m_coloring_problem → sudoku_solver(37) → expression_add_operators(282)"]
    end

    W1 --> W2 --> W3 --> W4 --> W5
```

**Key insight:** Every backtracking problem follows choose → explore → unchoose. The difference is *what* you choose (index vs element), *when* you record a result (at every node vs only at leaves), and *how* you prune (sum, length, constraint checks).
