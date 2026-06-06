# Design Circular Queue (LC 622)

Implement a circular queue (ring buffer) with fixed capacity supporting enQueue, deQueue, Front, Rear, isEmpty, and isFull — all in O(1).

## Approaches

### 1. Array with Front Pointer and Size
- **Time:** O(1) all ops | **Space:** O(k)
- Use a fixed-size array of length k, a `front` index, and a `size` counter.
- `rear = (front + size) % capacity` — computed on the fly, no separate rear pointer needed.
- `enQueue`: write to rear, increment size.
- `deQueue`: advance front with wrap-around, decrement size.

## Key Insight

Using `size` instead of a separate `rear` pointer avoids the ambiguity of distinguishing a full queue from an empty one (both would have `front == rear` with a naive two-pointer approach). The rear index is always derivable as `(front + size - 1) % capacity`. Modular arithmetic handles the wrap-around automatically.

## Edge Cases

- `enQueue` when full → return False.
- `deQueue` when empty → return False.
- `Front`/`Rear` when empty → return -1.
- Wrap-around: after filling and partially draining, new elements correctly wrap to the beginning of the array.
- Capacity of 1: enQueue then deQueue then enQueue should work correctly.
