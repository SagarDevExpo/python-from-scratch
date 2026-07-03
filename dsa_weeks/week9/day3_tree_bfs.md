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

