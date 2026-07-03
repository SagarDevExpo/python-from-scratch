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

---

## Exercises

1. Implement all three DFS orders.
2. Return traversal values in a list instead of printing.
3. Count all nodes recursively.
4. Find the sum of all node values.

