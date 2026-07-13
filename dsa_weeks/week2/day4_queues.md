# Day 4: Queues — First In, First Out

**Time:** ~35 minutes

Today you learn:
1. Queue behavior
2. Why `deque` is better than a list for queues
3. How queues process work in arrival order

**Practice file:** Create `day4_practice.py`

---

## Part 1: A Real Queue

The first person to enter a line is the first person served.

Use `deque`:

```python
from collections import deque

queue = deque()
queue.append("Ana")
queue.append("Ben")
queue.append("Cara")

print(queue.popleft())  # Ana
print(queue.popleft())  # Ben
```

Both `append()` and `popleft()` are `O(1)`.

Using `list.pop(0)` is `O(n)` because remaining values shift left.

### 🧩 Stack vs Queue in one picture

Both hold items; they differ in **which end you take from**:

```
STACK (LIFO — Last In, First Out)      QUEUE (FIFO — First In, First Out)
  push ↓   ↑ pop  (same end)              append →  [ ... ]  → popleft
  like a stack of plates                  like a line at a coffee shop
  newest leaves first                     oldest leaves first
```

Trace the queue: we add Ana, Ben, Cara, then `popleft()` twice.

| Action | Queue contents (front → back) | Returned |
|--------|-------------------------------|----------|
| `append("Ana")` | `Ana` | — |
| `append("Ben")` | `Ana, Ben` | — |
| `append("Cara")` | `Ana, Ben, Cara` | — |
| `popleft()` | `Ben, Cara` | **Ana** (arrived first) |
| `popleft()` | `Cara` | **Ben** |

**Why `deque` and not a list?** `popleft()` removes from the front in `O(1)`. A list's `pop(0)` also removes the front, but then every remaining item must *shift left one spot* to fill the gap — that's `O(n)` work every time. For a queue you take from the front constantly, so `deque` is the right tool.

---

## Part 2: Process Tasks

```python
from collections import deque


def process_tasks(tasks):
    queue = deque(tasks)

    while queue:
        current = queue.popleft()
        print("Processing:", current)
```

---

## Part 3: Stack or Queue?

| Situation | Structure |
|---|---|
| Undo latest action | Stack |
| Serve oldest request | Queue |
| Browser back button | Stack |
| Printer jobs | Queue |

---

## Exercises

1. Simulate customers waiting at a store.
2. Add an urgent customer to the front with `appendleft()`.
3. Process five printer jobs in order.
4. Explain stack versus queue in your own words.

