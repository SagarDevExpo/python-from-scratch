# Day 1: Trees — Parent and Child Data

**Time:** ~40 minutes

Today you learn:
1. Tree vocabulary
2. Binary trees
3. How to build a tree with nodes

**Practice file:** Create `day1_practice.py`

---

## Part 1: Vocabulary

```text
        10          root
       /  \
      5    15       children of 10
     / \
    2   7           leaves
```

- **Root:** top node
- **Parent:** node directly above another node
- **Child:** node directly below another node
- **Leaf:** node without children
- **Depth:** distance from the root
- **Subtree:** a node and everything below it

---

## Part 2: Tree Node

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

Build the pictured tree:

```python
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
```

---

## Part 3: Binary Search Tree Rule

In a Binary Search Tree:

- Smaller values go left
- Larger values go right

This ordering can make searching faster when the tree remains balanced.

---

## Exercises

1. Draw a tree with seven values.
2. Build it with `TreeNode`.
3. Print the root's two children.
4. Count the leaves by looking at your drawing.

