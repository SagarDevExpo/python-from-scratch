# Day 3: Tree Breadth-First Search

**Time:** ~40 minutes

Today you learn:
1. Level-by-level traversal
2. Why BFS uses a queue
3. How to group values by level

**Practice file:** Create `day3_practice.py`

---

## Part 1: BFS Order

```text
        10
       /  \
      5    15
     / \
    2   7
```

BFS visits:

```text
10, 5, 15, 2, 7
```

---

## Part 2: BFS with a Queue

```python
from collections import deque


def bfs(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
```

Each node enters and leaves the queue once.

Time: `O(n)`  
Space: `O(n)`

### 🧩 Why a queue gives level-by-level order

DFS (recursion) plunges deep down one branch first. BFS instead visits **level by level** — and a queue (First In, First Out) is exactly what makes that happen: you process nodes in the *same order you discovered them*, so a whole level is handled before its children.

Trace `bfs(root)` on this tree:
```text
        10
       /  \
      5    15
     / \
    2   7
```

`queue` starts as `[10]`, `result` starts empty. Each loop: pop the front, record it, then push its children to the back.

| Step | pop (front) | add to `result` | push children | `queue` after (front→back) |
|------|-------------|------------------|----------------|-----------------------------|
| 1 | 10 | `[10]` | 5, 15 | `[5, 15]` |
| 2 | 5  | `[10, 5]` | 2, 7 | `[15, 2, 7]` |
| 3 | 15 | `[10, 5, 15]` | (none) | `[2, 7]` |
| 4 | 2  | `[10, 5, 15, 2]` | (none) | `[7]` |
| 5 | 7  | `[10, 5, 15, 2, 7]` | (none) | `[]` → loop ends |

Result: `[10, 5, 15, 2, 7]` — top level, then next level, then the bottom. Because 5 and 15 were queued before 2 and 7, they're processed first. That FIFO ordering *is* the level-by-level behaviour. (Swap the queue for a stack and you'd get DFS instead.)

---

## Part 3: Values by Level

At the start of each loop, `len(queue)` tells you how many nodes belong to the
current level. Process exactly that many before starting the next level.

Expected result:

```python
[[10], [5, 15], [2, 7]]
```

---

## Exercises

1. Type BFS from memory.
2. Return the rightmost value on each level.
3. Return values grouped by level.
4. Compare the queue used by BFS with recursion used by DFS.

