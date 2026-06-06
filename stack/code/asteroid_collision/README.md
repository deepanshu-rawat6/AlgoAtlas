# Asteroid Collision (LC 735)

Given asteroids moving left (negative) or right (positive), simulate collisions. Smaller asteroids explode; equal sizes both explode. Same-direction asteroids never collide. Return the final state.

## Approaches

### 1. Stack Simulation
- **Time:** O(n) | **Space:** O(n)
- Push asteroids onto a stack. A collision only occurs when the incoming asteroid is **negative** and the stack top is **positive** (moving toward each other).
- While collision conditions hold: if stack top is smaller, pop it (right asteroid destroyed); if equal, pop and mark incoming as dead; if stack top is larger, mark incoming as dead.
- If the incoming asteroid survives, push it.

## Key Insight

Only right-moving asteroids on the stack can collide with an incoming left-mover. The stack naturally holds the "surviving" asteroids in order. The `alive` flag avoids pushing a destroyed asteroid. Each asteroid is pushed and popped at most once → O(n) total.

The condition `a < 0 and stack and stack[-1] > 0` precisely captures the only collision scenario: left-mover meeting a right-mover.

## Edge Cases

- `[-2, -1, 1, 2]` → no collisions (left-movers never meet right-movers ahead of them).
- `[8, -8]` → both destroyed → `[]`.
- `[10, 2, -5]` → 2 and -5 collide first (-5 wins), then 10 and -5 collide (10 wins) → `[10]`.
- All same direction → no collisions, return as-is.
- Asteroid 0 is excluded by constraints.
