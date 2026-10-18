# 2D Dynamic Programming

```mermaid
mindmap
  root((2D DP))
    Grid Path
      Unique Paths LC62
      Unique Paths II LC63
      Minimum Path Sum LC64
      Longest Increasing Path in Matrix LC329
    String Matching
      Longest Common Subsequence LC1143
      Edit Distance LC72
      Distinct Subsequences LC115
      Interleaving String LC97
      Regular Expression Matching LC10
    Interval DP
      Burst Balloons LC312
    Game Theory
      Stone Game LC877
      Stone Game II LC1140
    State Machine
      Best Time Buy/Sell Stock Cooldown LC309
    Knapsack
      Coin Change II LC518
      Target Sum LC494
      Last Stone Weight II LC1049
```

## Problem List

| # | Problem | LC # | Difficulty | Key Technique |
|---|---------|------|------------|---------------|
| 1 | Unique Paths | 62 | Medium | Grid DP |
| 2 | Unique Paths II | 63 | Medium | Grid DP with obstacles |
| 3 | Minimum Path Sum | 64 | Medium | Grid DP |
| 4 | Longest Common Subsequence | 1143 | Medium | String matching DP |
| 5 | Last Stone Weight II | 1049 | Medium | 0/1 Knapsack |
| 6 | Best Time Buy/Sell Stock Cooldown | 309 | Medium | State machine DP |
| 7 | Coin Change II | 518 | Medium | Unbounded knapsack (2D→1D) |
| 8 | Target Sum | 494 | Medium | 0/1 Knapsack |
| 9 | Interleaving String | 97 | Medium | 2D string DP |
| 10 | Stone Game | 877 | Medium | Game theory DP |
| 11 | Stone Game II | 1140 | Medium | Game theory DP |
| 12 | Longest Increasing Path in Matrix | 329 | Hard | DFS + memoization on grid |
| 13 | Distinct Subsequences | 115 | Hard | String matching DP |
| 14 | Edit Distance | 72 | Medium | String matching DP |
| 15 | Burst Balloons | 312 | Hard | Interval DP |
| 16 | Regular Expression Matching | 10 | Hard | String matching DP |

---

## Patterns & Diagrams

### 1. 2D DP Categories

```mermaid
flowchart TD
    A[2D DP Problem] --> B{"What are the two dimensions?"}
    B -->|Row & col of grid| C[Grid DP<br>62 63 64 329]
    B -->|Two string indices| D[String Matching DP<br>1143 72 115 97 10]
    B -->|Left & right bounds of array| E[Interval DP<br>312 Burst Balloons]
    B -->|Index & state/capacity| F[State Machine / Knapsack<br>309 518 494 877 1140]
```

### 2. Grid DP State Transition

```mermaid
flowchart TD
    A["Init dp[0][0] = grid[0][0]"] --> B["Fill first row: dp[0][j] = dp[0][j-1] + cost"]
    B --> C["Fill first col: dp[i][0] = dp[i-1][0] + cost"]
    C --> D["For i=1..m, j=1..n"]
    D --> E{"Obstacle at i,j?"}
    E -->|Yes| F["dp[i][j] = ∞ or 0"]
    E -->|No| G["dp[i][j] = min/+ of<br>dp[i-1][j] and dp[i][j-1]"]
    G --> D
    F --> D
    D --> H["Answer at dp[m-1][n-1]"]
```

### 3. String Matching DP — LCS / Edit Distance Cell Logic

```mermaid
flowchart TD
    A["dp[i][j] = ?"] --> B{"s1[i-1] == s2[j-1]?"}
    B -->|Yes — LCS| C["dp[i][j] = dp[i-1][j-1] + 1"]
    B -->|Yes — Edit Distance| D["dp[i][j] = dp[i-1][j-1]<br>no operation needed"]
    B -->|No — LCS| E["dp[i][j] = max(dp[i-1][j], dp[i][j-1])"]
    B -->|No — Edit Distance| F["dp[i][j] = 1 + min(<br>  dp[i-1][j],   // delete<br>  dp[i][j-1],   // insert<br>  dp[i-1][j-1]  // replace<br>)"]
```

### 4. Interval DP Pattern — Burst Balloons

```mermaid
flowchart TD
    A["Interval DP: dp[l][r]"] --> B[Iterate length = 2 to n]
    B --> C[For each left bound l]
    C --> D[r = l + length - 1]
    D --> E[For each k in l..r<br>k = last balloon to burst]
    E --> F["dp[l][r] = max(<br>  dp[l][k-1] +<br>  nums[l-1]*nums[k]*nums[r+1] +<br>  dp[k+1][r]<br>)"]
    F --> E
    E --> C
    C --> B
    B --> G["Answer: dp[1][n]"]

    style E fill:#69f,color:#000
```

### 5. State Machine DP — Buy/Sell with Cooldown

```mermaid
stateDiagram-v2
    [*] --> Holding: buy (pay price)
    Holding --> Sold: sell (gain price)
    Sold --> Cooldown: automatic
    Cooldown --> [*]: rest
    Cooldown --> Holding: buy next day
    [*] --> [*]: rest (stay idle)

    note right of Holding
        held[i] = max(held[i-1], idle[i-1] - price[i])
    end note
    note right of Sold
        sold[i] = held[i-1] + price[i]
    end note
    note right of Cooldown
        idle[i] = max(idle[i-1], sold[i-1])
    end note
```

---

## Complexity Summary

| Problem | Time | Space | Pattern |
|---------|------|-------|---------|
| unique_paths | O(m×n) | O(n) | Grid DP |
| unique_paths_ii | O(m×n) | O(n) | Grid DP with obstacles |
| minimum_path_sum | O(m×n) | O(n) | Grid DP |
| longest_common_subsequence | O(m×n) | O(n) | String matching DP |
| last_stone_weight_ii | O(n·sum) | O(sum) | 0/1 Knapsack |
| best_time_to_buy_and_sell_stock_with_cooldown | O(n) | O(1) | State machine DP |
| coin_change_ii | O(n·amount) | O(amount) | Unbounded knapsack |
| target_sum | O(n·sum) | O(sum) | 0/1 Knapsack |
| interleaving_string | O(m×n) | O(n) | 2D string DP |
| stone_game | O(n) | O(1) | Game theory DP |
| stone_game_ii | O(n²) | O(n²) | Game theory DP |
| longest_increasing_path_in_a_matrix | O(m×n) | O(m×n) | DFS + memoization |
| distinct_subsequences | O(m×n) | O(n) | String matching DP |
| edit_distance | O(m×n) | O(n) | String matching DP |
| burst_balloons | O(n³) | O(n²) | Interval DP |
| regular_expression_matching | O(m×n) | O(n) | String matching DP |

---

## Study Order

1. **Grid DP basics** — 62, 63, 64 (path counting / min cost)
2. **String matching** — 1143 (LCS), 72 (Edit Distance)
3. **String matching hard** — 115 (Distinct Subseq), 97 (Interleaving), 10 (Regex)
4. **Knapsack in 2D** — 518 (Coin Change II), 494 (Target Sum), 1049 (Last Stone)
5. **State machine** — 309 (Stock Cooldown)
6. **Game theory** — 877, 1140 (Stone Game I & II)
7. **Grid DFS + memo** — 329 (Longest Increasing Path)
8. **Interval DP** — 312 (Burst Balloons — hardest)
