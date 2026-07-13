# Day 2: Tree Depth-First Search

**Time:** ~45 minutes

Today you learn:
1. Preorder, inorder, and postorder
2. Recursive tree traversal
3. Maximum tree depth

**Practice file:** Create `day2_practice.py`

---

## Part 1: Three DFS Orders

```text
        10
       /  \
      5    15
```

- Preorder: node, left, right → `10, 5, 15`
- Inorder: left, node, right → `5, 10, 15`
- Postorder: left, right, node → `5, 15, 10`

---

## Part 2: Preorder

```python
def preorder(node):
    if node is None:
        return

    print(node.value)
    preorder(node.left)
    preorder(node.right)
```

The `None` check is the base case.

### 🧩 First, what is recursion? (read this before the code)

Recursion = **a function that calls itself** on a smaller piece of the problem. Two parts are mandatory:

1. **Base case** — the "stop" condition so it doesn't call forever. Here: `if node is None: return`. An empty branch has nothing to do, so we back out.
2. **Recursive case** — the function calls itself on smaller sub-problems. Here: `preorder(node.left)` and `preorder(node.right)`.

Mental model: to explore a tree, you say *"visit me, then let a helper explore my left branch the exact same way, then my right branch the exact same way."* That helper is just the same function again. Each call handles one node and delegates the rest.

For the tree:
```text
        10
       /  \
      5    15
```
`preorder(10)` runs: print 10 → call `preorder(5)` (prints 5, its children are None so they stop) → call `preorder(15)` (prints 15). Output: `10, 5, 15`. The order of the three lines inside the function is *literally* the visit order — that's the only difference between preorder/inorder/postorder.

---

## Part 3: Inorder

```python
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.value)
    inorder(node.right)
```

Inorder traversal of a Binary Search Tree prints values in sorted order.

---

## Part 4: Maximum Depth

```python
def max_depth(node):
    if node is None:
        return 0

    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)

    return 1 + max(left_depth, right_depth)
```

### 🧩 Tracing recursion: how the answers bubble back up

This is the part that bends everyone's brain: the function calls itself, waits, and the small answers **combine on the way back up**. Read `max_depth` as: *"my depth = 1 (for me) + the depth of my taller child."*

Use this tree:
```text
        10
       /  \
      5    15
```

Calls go **down** (asking children), answers come **back up**. Watch the flow:

```
max_depth(10)
  │  needs its children's depths first, so it pauses and asks...
  ├─ max_depth(5)
  │     ├─ max_depth(5.left = None) → base case → returns 0
  │     ├─ max_depth(5.right = None) → base case → returns 0
  │     └─ returns 1 + max(0, 0) = 1
  ├─ max_depth(15)
  │     ├─ max_depth(None) → 0
  │     ├─ max_depth(None) → 0
  │     └─ returns 1 + max(0, 0) = 1
  └─ returns 1 + max(1, 1) = 2
```

Step by step in words:
1. `max_depth(10)` can't answer yet — it needs both children's depths. It **pauses** and calls `max_depth(5)`.
2. `max_depth(5)` also pauses, calls its two `None` children → each hits the base case and returns `0`.
3. Now `max_depth(5)` has its pieces: `1 + max(0, 0) = 1`. It returns `1` back up to node 10.
4. Same story for `max_depth(15)` → returns `1`.
5. Finally `max_depth(10)` has both pieces: `1 + max(1, 1) = 2`. Total depth = **2**.

The key insight: **each call waits for its sub-calls to finish, then builds its own answer from theirs.** The `+ 1` is "count myself," and the base case `return 0` is the floor that stops the descent and starts the answers flowing back up.

---

## Exercises

1. Implement all three DFS orders.
2. Return traversal values in a list instead of printing.
3. Count all nodes recursively.
4. Find the sum of all node values.

